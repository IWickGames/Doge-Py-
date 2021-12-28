import discord
import db.databace
from discord.ext import commands


class OnLeave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(member: discord.Member):
        message = await db.databace.ReadKey(
            f"settings.{member.guild}.leave_message"
        )
        if not message:
            message = f":outbox_tray: Goodbye `{member.name}#"
            f"{member.discriminator} ({member.id})`"

        await member.guild.system_channel.send(
            message
        )


def setup(bot):
    bot.add_cog(OnLeave(bot))
