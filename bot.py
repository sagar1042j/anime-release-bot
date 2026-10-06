import requests
import os

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]

message = """
🎌 Anime Release Bot Working!

If you're seeing this message,
the bot is successfully connected.
"""

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    json={
        "chat_id": CHANNEL_ID,
        "text": message
    }
)
