"""YouTube API client for fetching channel videos."""

from googleapiclient.discovery import build
from datetime import datetime
from typing import List, Optional


class YouTubeClient:
    def __init__(self, api_key: str):
        self.youtube = build("youtube", "v3", developerKey=api_key)

    def get_channel_info(self, channel_id: str) -> dict:
        """Get channel name and uploads playlist ID."""
        response = self.youtube.channels().list(
            part="snippet,contentDetails",
            id=channel_id
        ).execute()

        if not response.get("items"):
            raise ValueError(f"Channel not found: {channel_id}")

        item = response["items"][0]
        return {
            "id": channel_id,
            "name": item["snippet"]["title"],
            "uploads_playlist": item["contentDetails"]["relatedPlaylists"]["uploads"]
        }

    def get_latest_videos(
        self,
        channel_id: str,
        max_results: int = 5,
        after: Optional[datetime] = None
    ) -> List[dict]:
        """Get latest videos from a channel's uploads playlist."""
        # First get the uploads playlist ID
        channel_info = self.get_channel_info(channel_id)
        playlist_id = channel_info["uploads_playlist"]

        # Fetch videos from uploads playlist (costs 1 unit vs 100 for search)
        response = self.youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist_id,
            maxResults=max_results
        ).execute()

        videos = []
        for item in response.get("items", []):
            snippet = item["snippet"]
            published_at = datetime.fromisoformat(
                snippet["publishedAt"].replace("Z", "+00:00")
            )

            # Filter by date if specified
            if after and published_at <= after:
                continue

            videos.append({
                "video_id": snippet["resourceId"]["videoId"],
                "title": snippet["title"],
                "channel_id": channel_id,
                "channel_name": channel_info["name"],
                "published_at": snippet["publishedAt"],
                "thumbnail": snippet["thumbnails"].get("medium", {}).get("url", ""),
                "description": snippet["description"][:200] if snippet["description"] else ""
            })

        return videos
