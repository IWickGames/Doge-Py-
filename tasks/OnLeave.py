import discord
import utility
import db.databace
from discord.ext import commands


class OnLeave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        message = await db.databace.ReadKey(
            f"settings.{member.guild}.leave_message"
        )
        if not message:
            message = ":outbox_tray: Goodbye `{username}#"
            "{discriminator} ({id})`"

        if message == "None":
            return

        try:
            await member.guild.system_channel.send(
                await utility.InputMessageArguments(member, message)
            )
        except discord.Forbidden:
            return


def setup(bot):
    bot.add_cog(OnLeave(bot))
