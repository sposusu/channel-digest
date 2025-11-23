"""AI summarization using local CLI tools (Gemini or Claude)."""

import subprocess
import tempfile
import os
from typing import Dict, Optional


SUMMARY_PROMPT_BASE = """Summarize this YouTube video. This summary will replace watching the video, so preserve the storyline and narrative flow.

Provide:

1. **TL;DR** (2-3 sentences max - the core message/outcome)

2. **Story/Content Flow** (summarize what happens in order, like a condensed version of watching the video)
   - Beginning: How the video starts, what's introduced
   - Middle: Key developments, main content, turning points
   - End: How it concludes, final results or takeaways

3. **Key Insights** (3-5 most valuable points or lessons)

4. **Notable Moments** (memorable quotes, funny moments, or highlights worth knowing)

Keep the summary engaging and capture the video's tone/style. The reader should feel like they watched it."""

# Bilingual prompt template - generates full summary in each language sequentially
BILINGUAL_SUMMARY_PROMPT_BASE = """Summarize this YouTube video. This summary will replace watching the video, so preserve the storyline and narrative flow.

Provide the summary in TWO languages, SEQUENTIALLY (full zh-TW first, then full English, separated by ---).

FORMAT:

# [Video Title in Chinese]

## 重點摘要
(2-3 sentences max - the core message/outcome)

## 故事大綱
(summarize what happens in order, like a condensed version of watching the video)
- 開場：影片如何開始，介紹了什麼
- 中段：主要發展、核心內容、轉折點
- 結尾：如何收尾、最終結果或重點

## 關鍵見解
(3-5 most valuable points or lessons)

## 精彩時刻
(memorable quotes, funny moments, or highlights worth knowing)

---

# [Video Title in English]

## TL;DR
(2-3 sentences max - the core message/outcome)

## Story Flow
(summarize what happens in order)
- Beginning: How the video starts, what's introduced
- Middle: Key developments, main content, turning points
- End: How it concludes, final results or takeaways

## Key Insights
(3-5 most valuable points or lessons)

## Notable Moments
(memorable quotes, funny moments, or highlights worth knowing)

Keep the summary engaging and capture the video's tone/style. The reader should feel like they watched it."""

SUMMARY_PROMPT = SUMMARY_PROMPT_BASE + """

TRANSCRIPT:
{transcript}
"""

BILINGUAL_SUMMARY_PROMPT = BILINGUAL_SUMMARY_PROMPT_BASE + """

TRANSCRIPT:
{transcript}
"""

SHORTS_PROMPT = """This is a YouTube Shorts transcript (short video < 60 seconds).

Summarize briefly:

1. **What happens**: Describe what occurs in 1-2 sentences
2. **The point**: What's the joke, insight, or takeaway?
3. **Vibe**: Is it funny, informative, dramatic, etc?

Keep it short - match the video's quick format.

TRANSCRIPT:
{transcript}
"""

# Threshold: if transcript is under this many characters, treat as Shorts
SHORTS_TRANSCRIPT_THRESHOLD = 400


def is_shorts(transcript: str) -> bool:
    """Detect if this is likely a YouTube Shorts based on transcript length."""
    return len(transcript) < SHORTS_TRANSCRIPT_THRESHOLD


def summarize_with_gemini(transcript: str, video_title: str, bilingual: bool = False) -> Optional[Dict]:
    """Summarize transcript using Gemini CLI."""
    # Use shorter prompt for Shorts
    if is_shorts(transcript):
        prompt = SHORTS_PROMPT.format(transcript=transcript)
    elif bilingual:
        prompt = BILINGUAL_SUMMARY_PROMPT.format(transcript=transcript[:50000])
    else:
        prompt = SUMMARY_PROMPT.format(transcript=transcript[:50000])

    try:
        # Call gemini CLI with stdin input and text output
        result = subprocess.run(
            ["gemini", "-m", "gemini-2.5-pro", "-o", "text"],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=180
        )

        if result.returncode != 0:
            print(f"  Gemini error: {result.stderr[:200]}")
            return None

        return parse_summary(result.stdout, video_title, bilingual=bilingual)

    except FileNotFoundError:
        print("  Error: 'gemini' CLI not found. Install it or use 'claude' provider.")
        return None
    except subprocess.TimeoutExpired:
        print("  Error: Gemini CLI timed out")
        return None
    except Exception as e:
        print(f"  Error running Gemini: {e}")
        return None


def download_audio_with_ytdlp(video_id: str, max_duration: int = 3600) -> Optional[str]:
    """Download audio from YouTube video using yt-dlp. Returns path to audio file."""
    video_url = f"https://youtube.com/watch?v={video_id}"
    output_path = f"/tmp/yt_audio_{video_id}.%(ext)s"

    try:
        # Check duration first to skip very long videos
        duration_result = subprocess.run(
            ["yt-dlp", "--print", "duration", video_url],
            capture_output=True, text=True, timeout=30
        )
        if duration_result.returncode == 0:
            try:
                duration = int(duration_result.stdout.strip())
                if duration > max_duration:
                    print(f"    Skipping: video too long ({duration//60} min > {max_duration//60} min limit)")
                    return None
            except ValueError:
                pass  # Can't parse duration, continue anyway

        # Download video (not -x audio) to avoid 403 errors - same as sign_youtube
        result = subprocess.run(
            ["yt-dlp", "--format", "best[height<=720]", "-o", output_path, video_url],
            capture_output=True,
            text=True,
            timeout=600  # Longer timeout for large files
        )

        # Check if file exists (returncode may be non-zero due to warnings)
        import glob
        matches = glob.glob(f"/tmp/yt_audio_{video_id}.*")
        if matches:
            return matches[0]

        # If no file found, log the actual error (skip warnings)
        stderr_lines = [l for l in result.stderr.split('\n') if 'ERROR' in l]
        if stderr_lines:
            print(f"    yt-dlp error: {stderr_lines[0][:200]}")

        return None

    except subprocess.TimeoutExpired:
        print("    yt-dlp download timed out")
        return None
    except Exception as e:
        print(f"    yt-dlp error: {e}")
        return None


def transcribe_with_whisper(audio_path: str) -> Optional[str]:
    """Transcribe audio file using Whisper CLI. Returns transcript text."""
    try:
        # Find imageio_ffmpeg binary and create symlink if needed
        ffmpeg_dir = "/opt/homebrew/lib/python3.13/site-packages/imageio_ffmpeg/binaries"
        ffmpeg_binary = os.path.join(ffmpeg_dir, "ffmpeg-macos-aarch64-v7.1")
        ffmpeg_link = os.path.join(ffmpeg_dir, "ffmpeg")

        # Create symlink to ffmpeg if it doesn't exist
        if os.path.exists(ffmpeg_binary) and not os.path.exists(ffmpeg_link):
            try:
                os.symlink(ffmpeg_binary, ffmpeg_link)
            except:
                pass  # May fail if no permissions

        env = os.environ.copy()
        if os.path.exists(ffmpeg_dir):
            env["PATH"] = ffmpeg_dir + ":" + env.get("PATH", "")

        # Use whisper CLI to transcribe (no --language flag = auto-detect)
        result = subprocess.run(
            ["whisper", audio_path, "--model", "base",
             "--output_format", "txt", "--output_dir", "/tmp"],
            capture_output=True,
            text=True,
            timeout=600,  # 10 min timeout for long videos
            env=env
        )

        if result.returncode != 0:
            print(f"    Whisper error: {result.stderr[:200]}")
            return None

        # Read the transcript file
        txt_path = audio_path.rsplit('.', 1)[0] + '.txt'
        if os.path.exists(txt_path):
            with open(txt_path, 'r') as f:
                return f.read().strip()

        return None

    except FileNotFoundError:
        print("    Whisper not installed. Install with: pip install openai-whisper")
        return None
    except subprocess.TimeoutExpired:
        print("    Whisper transcription timed out")
        return None
    except Exception as e:
        print(f"    Whisper error: {e}")
        return None


def transcribe_video_fallback(video_id: str) -> Optional[str]:
    """Download video audio and transcribe with Whisper as fallback."""
    print(f"    Downloading audio with yt-dlp...")
    audio_path = download_audio_with_ytdlp(video_id)

    if not audio_path:
        print(f"    Failed to download audio")
        return None

    print(f"    Transcribing with Whisper...")
    transcript = transcribe_with_whisper(audio_path)

    # Cleanup audio file
    try:
        os.remove(audio_path)
        # Also remove whisper output files
        for ext in ['txt', 'srt', 'vtt', 'json']:
            cleanup_path = audio_path.rsplit('.', 1)[0] + '.' + ext
            if os.path.exists(cleanup_path):
                os.remove(cleanup_path)
    except:
        pass

    return transcript


def summarize_with_claude(transcript: str, video_title: str, bilingual: bool = False) -> Optional[Dict]:
    """Summarize transcript using Claude CLI."""
    # Use shorter prompt for Shorts
    if is_shorts(transcript):
        prompt = SHORTS_PROMPT.format(transcript=transcript)
    elif bilingual:
        prompt = BILINGUAL_SUMMARY_PROMPT.format(transcript=transcript[:50000])
    else:
        prompt = SUMMARY_PROMPT.format(transcript=transcript[:50000])

    try:
        # Use claude CLI with piped input
        result = subprocess.run(
            ["claude", "-p", prompt],
            capture_output=True,
            text=True,
            timeout=120
        )

        if result.returncode != 0:
            print(f"  Claude error: {result.stderr}")
            return None

        return parse_summary(result.stdout, video_title, bilingual=bilingual)

    except FileNotFoundError:
        print("  Error: 'claude' CLI not found. Install Claude Code or use 'gemini' provider.")
        return None
    except subprocess.TimeoutExpired:
        print("  Error: Claude CLI timed out")
        return None
    except Exception as e:
        print(f"  Error running Claude: {e}")
        return None


def parse_summary(raw_output: str, video_title: str, bilingual: bool = False) -> dict:
    """Parse AI output into structured summary."""
    lines = raw_output.strip().split('\n')

    # For bilingual mode, extract zh-TW summary (重點摘要) as short_summary
    if bilingual:
        tldr = ""
        for i, line in enumerate(lines):
            if "重點摘要" in line:
                # Get the next non-empty line(s)
                for j in range(i + 1, min(i + 6, len(lines))):
                    if lines[j].strip() and not lines[j].startswith('#') and not lines[j].startswith('##'):
                        tldr = lines[j].strip().lstrip('- ')
                        break
                break

        # Fallback to first meaningful paragraph if 重點摘要 not found
        if not tldr:
            for line in lines:
                stripped = line.strip()
                if stripped and not stripped.startswith('#') and len(stripped) > 20:
                    tldr = stripped[:200]
                    break
    else:
        # Extract TL;DR (first meaningful paragraph after the header)
        tldr = ""
        for i, line in enumerate(lines):
            if "tl;dr" in line.lower() or "tldr" in line.lower():
                # Get the next non-empty line(s)
                for j in range(i + 1, min(i + 4, len(lines))):
                    if lines[j].strip() and not lines[j].startswith('#'):
                        tldr = lines[j].strip().lstrip('- ')
                        break
                break

        # If no TL;DR found, use first paragraph
        if not tldr:
            for line in lines:
                stripped = line.strip()
                if stripped and not stripped.startswith('#') and len(stripped) > 20:
                    tldr = stripped[:200]
                    break

    return {
        "short_summary": tldr,
        "full_summary": raw_output.strip()
    }


def summarize(transcript: str, video_title: str, provider: str = "gemini", video_id: str = None, bilingual: bool = False) -> Optional[Dict]:
    """
    Summarize transcript using specified AI provider.

    Args:
        transcript: Video transcript text (can be None if video_id provided)
        video_title: Title of the video
        provider: 'gemini' or 'claude'
        video_id: YouTube video ID (for fallback when no transcript)
        bilingual: If True, generate summary in multiple languages (zh-TW + en)

    Returns:
        Dict with 'short_summary' and 'full_summary', or None on error
    """
    # If no transcript but have video_id, try Whisper fallback
    if not transcript and video_id:
        print(f"    No transcript available, trying Whisper fallback...")
        transcript = transcribe_video_fallback(video_id)
        if not transcript:
            print(f"    Whisper fallback failed")
            return None
        print(f"    Whisper transcription successful ({len(transcript)} chars)")

    if not transcript:
        return None

    if provider == "gemini":
        return summarize_with_gemini(transcript, video_title, bilingual=bilingual)
    elif provider == "claude":
        return summarize_with_claude(transcript, video_title, bilingual=bilingual)
    else:
        print(f"  Unknown AI provider: {provider}")
        return None
