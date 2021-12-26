import groups
import config
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.tricks.command()
    async def ping(ctx: commands.Context):
        """Get bots latency to Discord API"""
        await ctx.respond(f":ping_pong: Pong! `{round(config.bot.latency*1000, 2)}ms`")


def setup(bot):
    bot.add_cog(Ping(bot))
