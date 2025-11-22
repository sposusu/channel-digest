"""AI summarization using local CLI tools (Gemini or Claude)."""

import subprocess
import tempfile
import os
from typing import Dict, Optional


SUMMARY_PROMPT = """Summarize this YouTube video transcript. This summary will replace watching the video, so preserve the storyline and narrative flow.

Provide:

1. **TL;DR** (2-3 sentences max - the core message/outcome)

2. **Story/Content Flow** (summarize what happens in order, like a condensed version of watching the video)
   - Beginning: How the video starts, what's introduced
   - Middle: Key developments, main content, turning points
   - End: How it concludes, final results or takeaways

3. **Key Insights** (3-5 most valuable points or lessons)

4. **Notable Moments** (memorable quotes, funny moments, or highlights worth knowing)

Keep the summary engaging and capture the video's tone/style. The reader should feel like they watched it.

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


def summarize_with_gemini(transcript: str, video_title: str) -> Optional[Dict]:
    """Summarize transcript using Gemini CLI."""
    # Use shorter prompt for Shorts
    if is_shorts(transcript):
        prompt = SHORTS_PROMPT.format(transcript=transcript)
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

        return parse_summary(result.stdout, video_title)

    except FileNotFoundError:
        print("  Error: 'gemini' CLI not found. Install it or use 'claude' provider.")
        return None
    except subprocess.TimeoutExpired:
        print("  Error: Gemini CLI timed out")
        return None
    except Exception as e:
        print(f"  Error running Gemini: {e}")
        return None


def summarize_with_claude(transcript: str, video_title: str) -> Optional[Dict]:
    """Summarize transcript using Claude CLI."""
    # Use shorter prompt for Shorts
    if is_shorts(transcript):
        prompt = SHORTS_PROMPT.format(transcript=transcript)
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

        return parse_summary(result.stdout, video_title)

    except FileNotFoundError:
        print("  Error: 'claude' CLI not found. Install Claude Code or use 'gemini' provider.")
        return None
    except subprocess.TimeoutExpired:
        print("  Error: Claude CLI timed out")
        return None
    except Exception as e:
        print(f"  Error running Claude: {e}")
        return None


def parse_summary(raw_output: str, video_title: str) -> dict:
    """Parse AI output into structured summary."""
    lines = raw_output.strip().split('\n')

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


def summarize(transcript: str, video_title: str, provider: str = "gemini") -> Optional[Dict]:
    """
    Summarize transcript using specified AI provider.

    Args:
        transcript: Video transcript text
        video_title: Title of the video
        provider: 'gemini' or 'claude'

    Returns:
        Dict with 'short_summary' and 'full_summary', or None on error
    """
    if not transcript:
        return None

    if provider == "gemini":
        return summarize_with_gemini(transcript, video_title)
    elif provider == "claude":
        return summarize_with_claude(transcript, video_title)
    else:
        print(f"  Unknown AI provider: {provider}")
        return None
