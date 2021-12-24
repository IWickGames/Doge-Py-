import os

import groups
import config
import discord
import db.databace

from sys import path
path.append(os.path.realpath("."))

bot = discord.Bot()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="fetch"))
    print(f"{bot.user.name}#{bot.user.discriminator} is now online")

config.PassBot(bot)
groups.MakeGroups(bot)

for directory in config.cog_directorys:
    for cog in os.listdir(directory):
        if cog.endswith(".py"):
            print("Loading " + cog)
            bot.load_extension(f'{directory}.{cog[:-3]}')

db.databace.Load()
loop = bot.loop
try:
    loop.run_until_complete(bot.start(config.token, reconnect=True))
except:
    loop.run_until_complete(bot.close())
finally:
    db.databace.Flush()
