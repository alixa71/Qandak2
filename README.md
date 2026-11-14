# Qandak2

A small helper for downloading selected media posts from a public Telegram channel and preparing the files for review in ChatGPT.

## First test

The first test target is Ali's public channel post:

- Channel: [@deklamehayeali](https://t.me/deklamehayeali)
- Post: [158](https://t.me/deklamehayeali/158)

The current script downloads one post by its Telegram link. It uses a user-authorized Telethon session so it can request a specific post from channel history.

## Setup

1. Install Python 3.8.10 (64-bit) on Windows 7. Python 3.9+ does not support Windows 7.
2. Open Command Prompt in this folder.
3. Install the dependency:

   ```bat
   python -m pip install -r requirements.txt
   ```

4. Copy `config.example.ini` to `config.ini`.
5. Create your own Telegram API application at [my.telegram.org](https://my.telegram.org), then put its `api_id` and `api_hash` in `config.ini`.
6. Run:

   ```bat
   python download_post.py
   ```

7. On first run, sign in with your Telegram phone number and the login code Telegram sends you. If your account uses two-step verification, Telethon will also ask for that password.
8. The downloaded media will be placed in the `downloads` folder.

You can also provide a different post link:

```bat
python download_post.py https://t.me/deklamehayeali/158
```

## Security

- Never send your API hash, login code, two-step password, or `qandak_telegram.session` file to anyone.
- Never commit `config.ini` or session files. They are excluded by `.gitignore`.
- The example config contains placeholders only.
- Downloaded media stays local in the `downloads` folder, which is also ignored by Git.

## Current limitations

- This is an initial command-line test, not the finished Windows interface.
- It has not yet been run against post 158. Telegram login and download must be completed on the user's computer.
- Windows 7 compatibility is a best-effort target. Python 3.8 is the last Python series supporting Windows 7, and the operating system itself is obsolete.
- Downloading a file does not automatically make it playable inside ChatGPT. The selected audio will still need to be uploaded to the conversation.

See [PROJECT_PLAN.md](PROJECT_PLAN.md) for milestones.
