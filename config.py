# flake8: noqa: E501
import os
import sys
import discord
import log.logging
from typing import List


def PassBot(b: discord.Bot):
    global bot
    bot = b


if os.getenv("token"):
    token: str = os.getenv("token")
else:
    if not os.path.exists("token.env"):
        log.logging.SyncError("Unable to locate environment token or token file")
        sys.exit(1)
    try:
        token: str = open("token.env").read()
    except OSError:
        log.logging.SyncError("Unable to read token file")
        sys.exit(1)

authorized_users: List[int] = [
    320699339645124608
]

test_servers: List[int] = [
    735935481950503043,
    673399675818213385,
    717736350727798785
]

# test_servers = None
databace_file = "db/bot.db"
cog_directorys: List[str] = [
    "tickets",
    "settings",
    "tasks",
    "tricks",
    "fun",
    "moderation",
    "utilities",
    "leveling",
    "economy",
    "owner"
]
embed_color: int = int("fcd111", 16)
meme_api: str = "https://meme-api.herokuapp.com/gimme"


bot_interaction_boterror: str = ":robot: This action cannot be performed on a bot account"
bot_permission_errormsg: str = ":closed_lock_with_key: You do not hold the correct permissions to perform this action"
bot_permission_boterrormsg: str = ":closed_lock_with_key: Bot does not have the correct permissions to perform this action"
bot_discorderror: str = ":anger: Grrrr, Discord returned an error"
