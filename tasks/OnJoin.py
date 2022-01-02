import discord
import utility
import db.databace
from discord.ext import commands


class OnJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        message = await db.databace.ReadKey(
            f"settings.{member.guild}.join_message"
        )
        if not message or message == "None":
            return

        try:
            await member.guild.system_channel.send(
                await utility.InputMessageArguments(member, message)
            )
        except discord.Forbidden:
            return


def setup(bot):
    bot.add_cog(OnJoin(bot))
