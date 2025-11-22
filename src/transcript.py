"""Transcript extraction using youtube-transcript-api."""

from typing import List, Optional
from youtube_transcript_api import YouTubeTranscriptApi


def get_transcript(video_id: str, languages: Optional[List[str]] = None) -> Optional[str]:
    """
    Fetch transcript for a YouTube video.

    Args:
        video_id: YouTube video ID
        languages: Preferred languages in order (default: ['en'])

    Returns:
        Full transcript as string, or None if unavailable
    """
    if languages is None:
        languages = ["en"]

    try:
        # New API requires instantiation
        api = YouTubeTranscriptApi()
        transcript_data = api.fetch(video_id, languages=languages)

        # Combine all text
        full_text = " ".join(entry.text for entry in transcript_data)
        return full_text

    except Exception as e:
        error_msg = str(e).lower()
        if "disabled" in error_msg:
            print(f"  Transcripts disabled for video: {video_id}")
        elif "no transcript" in error_msg or "not found" in error_msg:
            print(f"  No transcript found for video: {video_id}")
        elif "unavailable" in error_msg:
            print(f"  Video unavailable: {video_id}")
        else:
            print(f"  Error fetching transcript for {video_id}: {e}")
        return None
