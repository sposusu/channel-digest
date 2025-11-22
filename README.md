# Channel Digest

AI-powered YouTube channel summaries. Follow channels, get daily digests without watching videos.

## Features

- Fetch latest videos from YouTube channels
- Extract transcripts automatically
- Summarize with local AI (Gemini CLI or Claude Code)
- Generate static site for GitHub Pages
- Import channels from URLs or YouTube Takeout

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install AI CLI (choose one):
   - [Gemini CLI](https://github.com/google-gemini/gemini-cli)
   - [Claude Code](https://docs.anthropic.com/en/docs/claude-code)

3. Install [yt-dlp](https://github.com/yt-dlp/yt-dlp) (for adding channels by URL)

4. Get a [YouTube Data API key](https://console.cloud.google.com/apis/credentials)

5. Copy and configure:
```bash
cp config.yaml.example config.yaml
# Edit config.yaml with your API key
```

## Usage

```bash
# Add channels
python3 -m src.main add https://www.youtube.com/@ChannelName
python3 -m src.main import channels.txt
python3 -m src.main import-subscriptions subscriptions.csv  # YouTube Takeout

# Run digest
python3 -m src.main run          # Fetch, summarize, generate HTML
python3 -m src.main run --push   # Also push to gh-pages

# Preview locally
python3 -m src.main preview      # Generate HTML
python3 -m src.main serve        # Start local server

# List channels
python3 -m src.main list
```

## GitHub Pages

1. Push to GitHub
2. Settings → Pages → Source: `gh-pages` branch, `/docs` folder
3. Your digest will be at `https://username.github.io/channel-digest/`

## How It Works

1. Fetches latest videos via YouTube Data API (free 10k units/day)
2. Extracts transcripts using `youtube-transcript-api` (free)
3. Summarizes with local AI CLI (free)
4. Generates static HTML with video cards and markdown summaries
