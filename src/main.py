#!/usr/bin/env python3
"""YouTube Digest - CLI entry point."""

import argparse
import csv
import os
import subprocess
import sys
from pathlib import Path
from typing import Optional, Tuple

import yaml

from .youtube_client import YouTubeClient
from .transcript import get_transcript
from .summarizer import summarize
from .publisher import (
    load_data,
    save_data,
    save_summary_markdown,
    generate_index_html,
    generate_summary_viewer,
    git_push
)


def resolve_channel_id(url_or_id: str) -> Optional[Tuple[str, str]]:
    """
    Resolve a YouTube URL or handle to channel ID using yt-dlp.

    Returns: (channel_id, channel_name) or None on failure
    """
    # If it's already a channel ID (starts with UC and is 24 chars)
    if url_or_id.startswith("UC") and len(url_or_id) == 24:
        return (url_or_id, "")

    # Normalize URL
    url = url_or_id
    if not url.startswith("http"):
        if url.startswith("@"):
            url = f"https://youtube.com/{url}"
        else:
            url = f"https://youtube.com/@{url}"

    try:
        import json
        # Use --flat-playlist to get channel info without downloading
        result = subprocess.run(
            ["yt-dlp", "-j", "--flat-playlist", "--playlist-items", "1", url],
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode == 0 and result.stdout.strip():
            data = json.loads(result.stdout.strip().split('\n')[0])
            channel_id = data.get("playlist_channel_id") or data.get("channel_id")
            channel_name = data.get("playlist_channel") or data.get("channel") or ""
            if channel_id and channel_id.startswith("UC"):
                return (channel_id, channel_name)

        # Check for actual errors (not just warnings)
        if "ERROR" in result.stderr:
            print(f"  yt-dlp error: {result.stderr.split('ERROR')[-1][:100]}")
        return None

    except FileNotFoundError:
        print("Error: yt-dlp not found. Install with: brew install yt-dlp")
        return None
    except subprocess.TimeoutExpired:
        print("  Timeout resolving channel")
        return None
    except json.JSONDecodeError:
        print("  Failed to parse yt-dlp output")
        return None
    except Exception as e:
        print(f"  Error: {e}")
        return None


# Paths
ROOT_DIR = Path(__file__).parent.parent
CONFIG_PATH = ROOT_DIR / "config.yaml"
DATA_PATH = ROOT_DIR / "data.json"
DOCS_DIR = ROOT_DIR / "docs"
SUMMARIES_DIR = DOCS_DIR / "summaries"


def load_config() -> dict:
    """Load configuration from config.yaml."""
    if not CONFIG_PATH.exists():
        print(f"Error: Config file not found at {CONFIG_PATH}")
        print("Create config.yaml with your settings.")
        sys.exit(1)

    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


def cmd_run(args):
    """Fetch new videos, summarize, and publish."""
    config = load_config()

    if not config.get("youtube_api_key"):
        print("Error: youtube_api_key not set in config.yaml")
        sys.exit(1)

    if not config.get("channels"):
        print("No channels configured. Add channels to config.yaml")
        sys.exit(1)

    # Initialize
    yt = YouTubeClient(config["youtube_api_key"])
    data = load_data(str(DATA_PATH))
    existing_ids = {v["video_id"] for v in data["videos"]}
    ai_provider = config.get("ai_provider", "gemini")
    max_videos = config.get("max_videos_per_channel", 5)

    print(f"Using AI provider: {ai_provider}")
    print(f"Checking {len(config['channels'])} channels...")

    new_videos = []

    # Initialize channels dict if not present
    if "channels" not in data:
        data["channels"] = {}

    for channel_id in config["channels"]:
        print(f"\nChannel: {channel_id}")
        try:
            videos = yt.get_latest_videos(channel_id, max_results=max_videos)

            # Cache channel name
            if videos and videos[0].get("channel_name"):
                data["channels"][channel_id] = videos[0]["channel_name"]
            for video in videos:
                if video["video_id"] in existing_ids:
                    continue

                print(f"  New: {video['title'][:50]}...")

                # Get transcript
                print(f"    Fetching transcript...")
                transcript = get_transcript(video["video_id"])

                # Summarize (will fallback to video URL if no transcript and using Gemini)
                print(f"    Summarizing with {ai_provider}...")
                summary = summarize(transcript, video["title"], ai_provider, video["video_id"])
                if not summary:
                    print(f"    Skipping (summarization failed)")
                    continue

                video["short_summary"] = summary["short_summary"]
                video["full_summary"] = summary["full_summary"]
                new_videos.append(video)

                # Save markdown
                save_summary_markdown(video, str(SUMMARIES_DIR))
                print(f"    Done!")

        except Exception as e:
            print(f"  Error: {e}")

    # Always save data (to update channel names even if no new videos)
    save_data(data, str(DATA_PATH))

    # Get channel names for display
    channel_names = list(data.get("channels", {}).values())

    if new_videos:
        # Update data
        data["videos"].extend(new_videos)
        save_data(data, str(DATA_PATH))

        # Generate HTML
        generate_index_html(data, str(DOCS_DIR / "index.html"), channel_names)
        generate_summary_viewer(str(DOCS_DIR / "summary.html"))

        print(f"\nAdded {len(new_videos)} new video(s)")

        # Push to GitHub if configured
        if args.push:
            git_push(str(ROOT_DIR), f"Add {len(new_videos)} video summary(ies)")
    else:
        print("\nNo new videos found.")


def add_channel_to_config(channel_id: str, channel_name: str, config: dict) -> bool:
    """Add a channel to config if not already present. Returns True if added."""
    if "channels" not in config:
        config["channels"] = []

    if channel_id in config["channels"]:
        print(f"  Already exists: {channel_name or channel_id}")
        return False

    config["channels"].append(channel_id)
    print(f"  Added: {channel_name or channel_id}")
    return True


def save_config(config: dict):
    """Save config to yaml file."""
    with open(CONFIG_PATH, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)


def cmd_add(args):
    """Add a channel by URL, handle, or ID."""
    config = load_config()

    print(f"Resolving: {args.channel}")
    result = resolve_channel_id(args.channel)

    if not result:
        print("Failed to resolve channel")
        return

    channel_id, channel_name = result

    if add_channel_to_config(channel_id, channel_name, config):
        save_config(config)


def cmd_import(args):
    """Import channels from a text file (one URL per line)."""
    config = load_config()

    if not os.path.exists(args.file):
        print(f"File not found: {args.file}")
        return

    with open(args.file, 'r') as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith('#')]

    print(f"Found {len(lines)} channels to import...")
    added = 0

    for line in lines:
        print(f"\nResolving: {line}")
        result = resolve_channel_id(line)
        if result:
            channel_id, channel_name = result
            if add_channel_to_config(channel_id, channel_name, config):
                added += 1

    save_config(config)
    print(f"\nImported {added} new channel(s)")


def cmd_import_subscriptions(args):
    """Import channels from Google Takeout subscriptions.csv."""
    config = load_config()

    if not os.path.exists(args.file):
        print(f"File not found: {args.file}")
        return

    added = 0

    with open(args.file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"Found {len(rows)} subscriptions...")

    for row in rows:
        # Google Takeout CSV has "Channel ID" or "Channel Id" column
        channel_id = row.get("Channel ID") or row.get("Channel Id") or row.get("channel_id")
        channel_name = row.get("Channel title") or row.get("Channel Title") or ""

        if channel_id:
            if add_channel_to_config(channel_id, channel_name, config):
                added += 1

    save_config(config)
    print(f"\nImported {added} new channel(s)")


def cmd_list(args):
    """List configured channels and recent videos."""
    config = load_config()
    data = load_data(str(DATA_PATH))

    print("Configured channels:")
    for ch in config.get("channels", []):
        name = data.get("channels", {}).get(ch, {}).get("name", "Unknown")
        print(f"  - {ch} ({name})")

    print(f"\nTotal videos in digest: {len(data.get('videos', []))}")

    if data.get("videos"):
        print("\nRecent summaries:")
        for v in sorted(data["videos"], key=lambda x: x["published_at"], reverse=True)[:5]:
            print(f"  - {v['published_at'][:10]} | {v['title'][:50]}")


def cmd_preview(args):
    """Generate HTML without pushing."""
    data = load_data(str(DATA_PATH))
    channel_names = list(data.get("channels", {}).values())
    generate_index_html(data, str(DOCS_DIR / "index.html"), channel_names)
    generate_summary_viewer(str(DOCS_DIR / "summary.html"))
    print(f"Generated: {DOCS_DIR / 'index.html'}")
    print(f"Run 'python3 -m src.main serve' to view locally")


def cmd_serve(args):
    """Start local server to preview digest."""
    import http.server
    import socketserver
    import webbrowser

    port = args.port
    os.chdir(DOCS_DIR)

    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        url = f"http://localhost:{port}"
        print(f"Serving at {url}")
        print("Press Ctrl+C to stop")
        webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped")


def main():
    parser = argparse.ArgumentParser(
        description="YouTube Digest - Summarize videos from your favorite channels"
    )
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # run command
    run_parser = subparsers.add_parser("run", help="Fetch, summarize, and publish")
    run_parser.add_argument("--push", action="store_true", help="Push to GitHub after")
    run_parser.set_defaults(func=cmd_run)

    # add command
    add_parser = subparsers.add_parser("add", help="Add a channel by URL, handle, or ID")
    add_parser.add_argument("channel", help="YouTube URL, @handle, or channel ID")
    add_parser.set_defaults(func=cmd_add)

    # import command
    import_parser = subparsers.add_parser("import", help="Import channels from text file")
    import_parser.add_argument("file", help="Text file with one URL per line")
    import_parser.set_defaults(func=cmd_import)

    # import-subscriptions command
    subs_parser = subparsers.add_parser("import-subscriptions", help="Import from Google Takeout CSV")
    subs_parser.add_argument("file", help="subscriptions.csv from Google Takeout")
    subs_parser.set_defaults(func=cmd_import_subscriptions)

    # list command
    list_parser = subparsers.add_parser("list", help="List channels and videos")
    list_parser.set_defaults(func=cmd_list)

    # preview command
    preview_parser = subparsers.add_parser("preview", help="Generate HTML locally")
    preview_parser.set_defaults(func=cmd_preview)

    # serve command
    serve_parser = subparsers.add_parser("serve", help="Start local server to view digest")
    serve_parser.add_argument("--port", "-p", type=int, default=8000, help="Port (default: 8000)")
    serve_parser.set_defaults(func=cmd_serve)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    args.func(args)


if __name__ == "__main__":
    main()
