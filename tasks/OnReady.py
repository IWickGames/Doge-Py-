import config
import discord
import log.logging
from discord.ext import commands


class OnReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await config.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.playing,
                name="fetch"
            )
        )
        await log.logging.Info(
            f"{config.bot.user.name}#{config.bot.user.discriminator} "
            "is now online"
        )


def setup(bot):
    bot.add_cog(OnReady(bot))
