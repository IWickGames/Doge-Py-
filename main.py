import os

import groups
import config
import discord

from sys import path
path.append(os.path.realpath("."))

bot = discord.Bot()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="fetch"))
    print(f"{bot.user.name}#{bot.user.discriminator} is now online")

groups.MakeGroups(bot)

for directory in config.cog_directorys:
    for cog in os.listdir(directory):
        if cog.endswith(".py"):
            print("Loading " + cog)
            bot.load_extension(f'{directory}.{cog[:-3]}')

bot.run(config.token)