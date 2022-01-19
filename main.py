import os
import shutil
import groups
import config
import discord
import db.databace
from sys import path

print("==== Starting bot initialization... ====")

path.append(os.path.realpath("."))

ints = discord.Intents.default()
ints.members = True
ints.messages = True
bot = discord.Bot(
    intents=ints,
    debug_guilds=config.test_servers
)

config.PassBot(bot)

maxlength = len(
    max(
        [f"Initalizing {i} " for i in config.cog_directorys],
        key=len
    )
)

for directory in config.cog_directorys:
    length = len(f"Initalizing {directory} ")
    print(f"Initalizing {directory} " + " "*(maxlength-length) + "|  ", end="")
    for cog in os.listdir(directory):
        if cog.endswith(".py"):
            print(cog, end="  ")
            bot.load_extension(f'{directory}.{cog[:-3]}')
    print("")

print("====    Initialization complete     ====")

try:
    print("Starting Discord websocket...")
    bot.loop.create_task(db.databace.databace_flush())
    bot.loop.run_until_complete(bot.start(config.token, reconnect=True))
except:  # noqa: E722
    bot.loop.run_until_complete(db.databace.Flush())
    bot.loop.run_until_complete(bot.close())
finally:
    if os.path.exists("__pycache__"):
        print("Cleaning up...")
        shutil.rmtree("__pycache__")
        for folder in config.cog_directorys:
            shutil.rmtree(folder + "/__pycache__")
            if os.path.exists(folder + "/views/__pycache__"):
                shutil.rmtree(folder + "/views/__pycache__")
        shutil.rmtree("db/__pycache__")
        shutil.rmtree("log/__pycache__")
