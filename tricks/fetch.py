import groups
from discord.ext import commands


class Fetch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.tricks.command()
    async def fetch(ctx: commands.Context):
        """Let me fetch a bone for you"""
        await ctx.respond(f":grin: Found it! Here {ctx.author.mention} :bone:")


def setup(bot):
    bot.add_cog(Fetch(bot))
