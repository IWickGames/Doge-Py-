import os
import groups
import config
import discord
import db.databace

from sys import path
path.append(os.path.realpath("."))

bot = discord.Bot()

config.PassBot(bot)
groups.MakeGroups(bot)

for directory in config.cog_directorys:
    for cog in os.listdir(directory):
        if cog.endswith(".py"):
            print("Loading " + cog)
            bot.load_extension(f'{directory}.{cog[:-3]}')

try:
    bot.loop.create_task(db.databace.databace_flush())
    bot.loop.run_until_complete(bot.start(config.token, reconnect=True))
except:  # noqa: E722
    bot.loop.run_until_complete(bot.close())
finally:
    db.databace.Flush()
