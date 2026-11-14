# Qandak2

Qandak2 is a small, Windows-friendly helper project for collecting audio posts from a Telegram channel and preparing them for review in ChatGPT.

## First milestone

1. Connect to a Telegram channel using a safe, user-controlled method.
2. Find audio posts and download MP3/audio files.
3. Save files locally in an organized folder, with useful filenames and a simple index.
4. Let the user choose which audio files to share in ChatGPT for listening, transcription, and analysis.

## Important constraints

- Never commit Telegram bot tokens, API hashes, phone numbers, session files, or other credentials to GitHub.
- Keep credentials in a local configuration file that is excluded from version control.
- Do not make private channel audio publicly accessible by default.
- GitHub is for source code and project documentation, not a guaranteed audio streaming bridge into ChatGPT.
- Prefer a simple interface and dependencies that can run on older Windows systems where practical.

## Telegram access options

- Public channel: a bot or supported Telegram client integration may be possible, subject to Telegram API limits and channel access.
- Private channel: the user must authorize access. A bot generally needs to be added with suitable permissions; access to older posts may require a user-authorized Telegram client session.

## Current status

- Repository connection verified.
- Read and write access verified.
- Source channel confirmed public: `@deklamehayeali`.
- First test post selected: `https://t.me/deklamehayeali/158`.
- Initial single-post downloader added. It uses a user-authorized Telethon session so it can request a specific older channel post.
- Credentials and session files are excluded from Git.
- Download has not yet been run: the user must provide their own Telegram API ID/hash locally and complete Telegram login.

## Planned milestones

- M1: Public channel and first test post confirmed.
- M2: Run the downloader against post 158 and verify the downloaded media.
- M3: Add a simple Windows interface and local configuration.
- M4: Test a small batch and prepare selected audio for ChatGPT upload.
