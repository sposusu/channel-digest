"""Publisher for generating GitHub Pages content."""

import json
import os
import subprocess
from datetime import datetime
from pathlib import Path


def load_data(data_path: str) -> dict:
    """Load existing data.json or create empty structure."""
    if os.path.exists(data_path):
        with open(data_path, 'r') as f:
            return json.load(f)
    return {"videos": [], "channels": {}, "last_updated": None}


def save_data(data: dict, data_path: str):
    """Save data to data.json."""
    data["last_updated"] = datetime.now().isoformat()
    with open(data_path, 'w') as f:
        json.dump(data, f, indent=2)


def save_summary_markdown(video: dict, summaries_dir: str) -> str:
    """Save full summary as markdown file."""
    # Ensure directory exists
    os.makedirs(summaries_dir, exist_ok=True)

    date_str = video["published_at"][:10]
    filename = f"{date_str}-{video['video_id']}.md"
    filepath = os.path.join(summaries_dir, filename)

    content = f"""# {video['title']}

**Channel:** {video['channel_name']}
**Published:** {video['published_at'][:10]}
**Video:** [Watch on YouTube](https://youtube.com/watch?v={video['video_id']})

---

{video.get('full_summary', 'No summary available.')}
"""

    with open(filepath, 'w') as f:
        f.write(content)

    return filename


def generate_index_html(data: dict, output_path: str, channel_names: list = None, profile_channels: set = None, page_title: str = None):
    """Generate index.html for GitHub Pages."""
    # Filter videos by profile channels if specified
    videos = data["videos"]
    if profile_channels:
        videos = [v for v in videos if v.get("channel_id") in profile_channels]

    # Sort videos by published date (newest first)
    videos = sorted(
        videos,
        key=lambda v: v["published_at"],
        reverse=True
    )

    # Use provided channel names, or fall back to extracting from videos
    if not channel_names:
        channel_names = set()
        for v in videos:
            channel_names.add(v.get("channel_name", ""))
        channel_names = sorted([c for c in channel_names if c])
    else:
        channel_names = sorted(channel_names)

    # Use provided page title or default
    title = page_title if page_title else "YouTube Digest"

    video_cards = []
    for v in videos:
        date_str = v["published_at"][:10]
        summary_link = f"summaries/{date_str}-{v['video_id']}.md"
        short_summary = v.get("short_summary", "No summary available.")

        card = f"""
        <article class="video-card">
            <img src="{v.get('thumbnail', '')}" alt="{v['title']}" class="thumbnail">
            <div class="content">
                <h2><a href="summary.html?v={date_str}-{v['video_id']}">{v['title']}</a></h2>
                <p class="meta">{v['channel_name']} &bull; {date_str}</p>
                <p class="summary">{short_summary}</p>
                <div class="links">
                    <a href="summary.html?v={date_str}-{v['video_id']}">Full Summary</a>
                    <a href="https://youtube.com/watch?v={v['video_id']}" target="_blank">Watch Video</a>
                </div>
            </div>
        </article>"""
        video_cards.append(card)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{ box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
            color: #333;
        }}
        h1 {{
            text-align: center;
            color: #c00;
        }}
        .last-updated {{
            text-align: center;
            color: #666;
            font-size: 0.9em;
            margin-bottom: 30px;
        }}
        .video-card {{
            background: white;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 16px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            display: flex;
            gap: 16px;
        }}
        .thumbnail {{
            width: 160px;
            height: 90px;
            object-fit: cover;
            border-radius: 4px;
            flex-shrink: 0;
        }}
        .content {{ flex: 1; }}
        .content h2 {{
            margin: 0 0 8px 0;
            font-size: 1.1em;
        }}
        .content h2 a {{
            color: #333;
            text-decoration: none;
        }}
        .content h2 a:hover {{
            color: #c00;
        }}
        .meta {{
            color: #666;
            font-size: 0.85em;
            margin: 0 0 8px 0;
        }}
        .summary {{
            font-size: 0.95em;
            line-height: 1.5;
            margin: 0 0 12px 0;
        }}
        .links {{
            display: flex;
            gap: 16px;
        }}
        .links a {{
            color: #c00;
            text-decoration: none;
            font-size: 0.9em;
        }}
        .links a:hover {{
            text-decoration: underline;
        }}
        .channels {{
            text-align: center;
            margin-bottom: 24px;
            padding: 12px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .channels-title {{
            font-size: 0.85em;
            color: #666;
            margin-bottom: 8px;
        }}
        .channel-tag {{
            display: inline-block;
            background: #f0f0f0;
            padding: 4px 10px;
            border-radius: 16px;
            font-size: 0.85em;
            margin: 4px;
            color: #333;
        }}
        @media (max-width: 600px) {{
            .video-card {{
                flex-direction: column;
            }}
            .thumbnail {{
                width: 100%;
                height: auto;
            }}
        }}
    </style>
</head>
<body>
    <h1>{title}</h1>
    <p class="last-updated">Last updated: {data.get('last_updated', 'Never')[:16].replace('T', ' ')}</p>

    <div class="channels">
        <div class="channels-title">Following {len(channel_names)} channel(s)</div>
        {''.join(f'<span class="channel-tag">{name}</span>' for name in channel_names) if channel_names else '<span class="channel-tag">No channels yet</span>'}
    </div>

    {''.join(video_cards) if video_cards else '<p style="text-align:center">No videos yet. Run the digest to fetch summaries.</p>'}
</body>
</html>
"""

    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w') as f:
        f.write(html)


def generate_summary_viewer(output_path: str):
    """Generate summary.html - a markdown viewer page."""
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Summary - YouTube Digest</title>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <style>
        * { box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }
        .back-link {
            display: inline-block;
            margin-bottom: 20px;
            color: #c00;
            text-decoration: none;
        }
        .back-link:hover { text-decoration: underline; }
        #content {
            background: white;
            padding: 24px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        #content h1 { color: #c00; margin-top: 0; }
        #content h2, #content h3 { color: #333; margin-top: 24px; }
        #content a { color: #c00; }
        #content ul, #content ol { padding-left: 24px; }
        #content li { margin-bottom: 8px; }
        #content blockquote {
            border-left: 4px solid #c00;
            margin: 16px 0;
            padding-left: 16px;
            color: #666;
        }
        #content hr { border: none; border-top: 1px solid #ddd; margin: 24px 0; }
        #content code {
            background: #f0f0f0;
            padding: 2px 6px;
            border-radius: 3px;
            font-size: 0.9em;
        }
        .loading { text-align: center; padding: 40px; color: #666; }
        .error { color: #c00; text-align: center; padding: 40px; }
    </style>
</head>
<body>
    <a href="index.html" class="back-link">&larr; Back to Digest</a>
    <div id="content">
        <p class="loading">Loading summary...</p>
    </div>
    <script>
        async function loadSummary() {
            const params = new URLSearchParams(window.location.search);
            const videoId = params.get('v');

            if (!videoId) {
                document.getElementById('content').innerHTML = '<p class="error">No video specified</p>';
                return;
            }

            try {
                const response = await fetch(`summaries/${videoId}.md`);
                if (!response.ok) throw new Error('Summary not found');

                const markdown = await response.text();
                document.getElementById('content').innerHTML = marked.parse(markdown);

                // Update page title
                const h1 = document.querySelector('#content h1');
                if (h1) document.title = h1.textContent + ' - YouTube Digest';
            } catch (error) {
                document.getElementById('content').innerHTML =
                    '<p class="error">Failed to load summary. <a href="index.html">Return to digest</a></p>';
            }
        }

        loadSummary();
    </script>
</body>
</html>
"""
    with open(output_path, 'w') as f:
        f.write(html)


def git_push(repo_path: str, message: str = "Update digest"):
    """Commit data.json to main and docs/ to gh-pages, then push both.

    Note: data.json is tracked on main (metadata), docs/ is gitignored on main
    but committed to gh-pages (generated HTML/markdown content).
    """
    import tempfile
    import shutil

    try:
        # First, commit and push data.json to main
        subprocess.run(["git", "add", "data.json"], cwd=repo_path, check=True)

        # Check if there are changes to commit
        result = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            cwd=repo_path,
            capture_output=True
        )

        if result.returncode != 0:  # There are changes
            subprocess.run(
                ["git", "commit", "-m", message],
                cwd=repo_path,
                check=True
            )
            subprocess.run(["git", "push", "origin", "main"], cwd=repo_path, check=True)
            print("Pushed data.json to main")

        # Save uncommitted docs/ to temp location
        temp_dir = tempfile.mkdtemp()
        docs_src = os.path.join(repo_path, "docs")
        docs_temp = os.path.join(temp_dir, "docs")

        if os.path.exists(docs_src):
            shutil.copytree(docs_src, docs_temp)
        else:
            print("Warning: docs/ directory not found")
            return

        # Switch to gh-pages branch
        subprocess.run(["git", "checkout", "gh-pages"], cwd=repo_path, check=True)

        # Copy docs from temp to gh-pages
        docs_dest = os.path.join(repo_path, "docs")
        if os.path.exists(docs_dest):
            shutil.rmtree(docs_dest)
        shutil.copytree(docs_temp, docs_dest)

        # Commit and push
        subprocess.run(["git", "add", "docs/"], cwd=repo_path, check=True)

        # Check if there are changes to commit
        result = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            cwd=repo_path,
            capture_output=True
        )

        if result.returncode != 0:  # There are changes
            subprocess.run(
                ["git", "commit", "-m", message],
                cwd=repo_path,
                check=True
            )
            subprocess.run(["git", "push", "--force"], cwd=repo_path, check=True)
            print("Pushed docs/ to gh-pages")
        else:
            print("No changes to push to gh-pages")

        # Cleanup temp
        shutil.rmtree(temp_dir)

    except subprocess.CalledProcessError as e:
        print(f"Git error: {e}")
    finally:
        # Always return to main branch
        subprocess.run(["git", "checkout", "main"], cwd=repo_path)
