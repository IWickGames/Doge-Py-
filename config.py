# flake8: noqa: E501
import os
import sys
import log.logging

def PassBot(b):
    global bot
    bot = b

if os.getenv("token"):
    token = os.getenv("token")
else:
    try:
        token = open("token.env").read()
    except OSError:
        log.logging.SyncError("Unable to locate token file or token environment entry")
        sys.exit(1)

test_servers = [735935481950503043, 673399675818213385]
# test_servers = None
databace_file = "db/bot.db"
cog_directorys = [
    "tickets",
    "settings",
    "tasks",
    "tricks",
    "fun",
    "moderation",
    "utilities",
    "leveling",
    "economy"
]
embed_color = int("fcd111", 16)
meme_api = "https://meme-api.herokuapp.com/gimme"


bot_interaction_boterror = ":robot: This action cannot be performed on a bot account"
bot_permission_errormsg = ":closed_lock_with_key: You do not hold the correct permissions to perform this action"
bot_permission_boterrormsg = ":closed_lock_with_key: Bot does not have the correct permissions to perform this action"
bot_discorderror = ":anger: Grrrr, Discord returned an error"
