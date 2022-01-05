import groups
import config
import random
import log.logging
from discord.ext import commands


class Coinflip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.fun.command(guild_ids=config.test_servers)
    async def coinflip(ctx: commands.Context):
        """Flip a coin"""
        await log.logging.Info(
            f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})"
            " executed Coinflip in Fun"
        )

        side: str = ["Head", "Tails"][random.randint(0, 1)]
        await ctx.respond(f":coin: {ctx.author.mention} you got: `{side}`")


def setup(bot):
    bot.add_cog(Coinflip(bot))
