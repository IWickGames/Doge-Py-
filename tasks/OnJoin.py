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
        if not message:
            message = ":inbox_tray: Welcome `{username}#"
            "{discriminator} ({id})`, we are glad to have you!"

        if message == "None":
            return

        await member.guild.system_channel.send(
            await utility.InputMessageArguments(member, message)
        )


def setup(bot):
    bot.add_cog(OnJoin(bot))
