# -*- coding: utf-8 -*-
"""
Download one Telegram channel post by its public t.me link.
Test target: https://t.me/deklamehayeali/158
Compatible design target: Python 3.8 on Windows 7 (best-effort; OS/TLS limitations may apply).
"""
from __future__ import print_function

import argparse
import asyncio
import configparser
import os
import re
import sys

from telethon import TelegramClient


def parse_post_link(value):
    match = re.search(r"(?:https?://)?t\.me/([A-Za-z0-9_]+)/([0-9]+)", value.strip())
    if not match:
        raise ValueError("Link format must look like https://t.me/channelname/123")
    return match.group(1), int(match.group(2))


def load_settings():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.ini")
    if not os.path.isfile(config_path):
        raise IOError("config.ini is missing. Copy config.example.ini to config.ini and fill in your API credentials.")
    config = configparser.ConfigParser()
    config.read(config_path, encoding="utf-8")
    try:
        api_id = config.getint("telegram", "api_id")
        api_hash = config.get("telegram", "api_hash").strip()
    except (configparser.Error, ValueError) as exc:
        raise ValueError("Check [telegram] api_id and api_hash in config.ini: {0}".format(exc))
    if not api_id or not api_hash or api_hash == "PASTE_API_HASH_HERE":
        raise ValueError("Add your own Telegram api_id and api_hash to config.ini.")
    return api_id, api_hash


async def download_post(channel_name, message_id, output_dir):
    api_id, api_hash = load_settings()
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    session_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "qandak_telegram")
    client = TelegramClient(session_path, api_id, api_hash)

    await client.start()
    try:
        print("Looking up @{0}, post {1} ...".format(channel_name, message_id))
        channel = await client.get_entity(channel_name)
        message = await client.get_messages(channel, ids=message_id)
        if message is None:
            print("Post not found or not accessible.")
            return 2
        if not message.media:
            print("This post has no downloadable media.")
            if message.message:
                print("Text: {0}".format(message.message))
            return 3

        path = await client.download_media(message, file=output_dir)
        if not path:
            print("Telegram did not return a downloadable file.")
            return 4

        print("Downloaded successfully:")
        print(path)
        if message.message:
            print("Caption: {0}".format(message.message))
        return 0
    finally:
        await client.disconnect()


def main():
    parser = argparse.ArgumentParser(description="Download a single Telegram channel post by link.")
    parser.add_argument("link", nargs="?", default="https://t.me/deklamehayeali/158",
                        help="Public Telegram post link (defaults to the first test post).")
    parser.add_argument("--output", default="downloads", help="Output folder (default: downloads)")
    args = parser.parse_args()

    try:
        channel_name, message_id = parse_post_link(args.link)
        result = asyncio.run(download_post(channel_name, message_id, args.output))
        sys.exit(result)
    except (ValueError, IOError) as exc:
        print("Error: {0}".format(exc))
        sys.exit(1)
    except KeyboardInterrupt:
        print("Cancelled.")
        sys.exit(130)


if __name__ == "__main__":
    main()
