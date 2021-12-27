import discord
from discord.ext import commands


class OnLeave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(member: discord.Member):
        return


def setup(bot):
    bot.add_cog(OnLeave(bot))
