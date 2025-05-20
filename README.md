# Kids Story Video Bot (Hugging Face Edition)

This bot generates a fun AI-powered kids story using Hugging Face's `distilgpt2`, converts it to speech, creates a video, and uploads it to YouTube. It's fully automated with GitHub Actions.

## Setup

1. Place a background image at `assets/background.jpg`.
2. Store your `token.pickle` from YouTube OAuth in `secrets/token.pickle`.
3. Run `python main.py` to test locally.

## GitHub Actions

To automate daily uploads, use the `.github/workflows/daily_upload.yml` file.

## License

MIT
