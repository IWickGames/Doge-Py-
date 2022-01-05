import groups
import config
import log.logging
from discord.ext import commands


class Pet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.tricks.command(guild_ids=config.test_servers)
    async def pet(ctx: commands.Context):
        """Tell me I am doing a good job!"""
        await log.logging.Info(
            f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})"
            " executed Pet in Tricks"
        )

        await ctx.respond(f":dog2: Awww! Thanks {ctx.author.mention} :yum:")


def setup(bot):
    bot.add_cog(Pet(bot))
