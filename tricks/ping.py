import groups
import config
import log.logging
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.tricks.command(guild_ids=config.test_servers)
    async def ping(ctx: commands.Context):
        """Get bots latency to Discord API"""
        await log.logging.Info(
            f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})"
            " executed Ping in Tricks"
        )

        await ctx.respond(
            f":ping_pong: Pong! `{round(config.bot.latency*1000, 2)}ms`"
        )


def setup(bot):
    bot.add_cog(Ping(bot))
