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
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing,
            name="fetch"
        )
    )
    print(f"{bot.user.name}#{bot.user.discriminator} is now online")


@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    value = await db.databace.ReadKey(
        f"leveling.{message.author.id}.{message.guild.id}"
    )
    if not value:
        value = 0

    await db.databace.WriteKey(
        f"leveling.{message.author.id}.{message.guild.id}",
        value+1
    )

    if (value+1) % 100 == 0:
        await message.reply(
            content=":confetti_ball: Congrats "
            f"`{message.author.name}` you reached "
            f"level `{int((value+1)/100)}` with `{value+1}` total experience"
        )


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
