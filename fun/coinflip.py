import groups
import random
from discord.ext import commands

class Coinflip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @groups.fun.command()
    async def coinflip(self, ctx: commands.Context):
        """Flip a coin"""
        side: str = ["Head", "Tails"][random.randint(0, 1)]
        await ctx.respond(f":coin: {ctx.author.mention} you got: `{side}`")

def setup(bot):
    bot.add_cog(Coinflip(bot))