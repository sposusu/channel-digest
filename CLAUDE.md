# Claude Code Instructions

This is a YouTube channel digest project. Use the built-in CLI commands instead of writing custom scripts.

## CLI Commands

```bash
# Add channels (use URL, not channel ID)
python3 -m src.main add https://www.youtube.com/@ChannelName

# Import multiple channels
python3 -m src.main import channels.txt

# Run digest (fetch videos, summarize, generate HTML)
python3 -m src.main run

# Run and push to GitHub Pages
python3 -m src.main run --push

# List channels
python3 -m src.main list

# Preview locally
python3 -m src.main serve
```

## Key Files

- `config.yaml` - Configuration (API key, channels, AI provider, languages)
- `data.json` - Video data and summaries
- `docs/` - Generated static site (index.html, summaries/)
- `src/main.py` - CLI entry point
- `src/summarizer.py` - AI summarization logic
- `src/publisher.py` - HTML generation

## Configuration

```yaml
ai_provider: gemini          # or claude
summary_languages:           # Bilingual summaries
  - zh-TW
  - en
channels:                    # Channel IDs (auto-added via CLI)
  - UCxxxxx
max_videos_per_channel: 5
```

## Deployment

- Main branch: source code
- gh-pages branch: static site for GitHub Pages
- Use `python3 -m src.main run --push` to deploy

## Important

- Always use CLI commands, don't write custom scripts for adding channels or running digests
- Videos without transcripts will use Whisper fallback (slower)
- Bilingual mode generates zh-TW summary first, then English
