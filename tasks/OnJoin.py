import discord
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
            message = f":inbox_tray: Welcome `{member.name}#"
            f"{member.discriminator} ({member.id})` to `{member.guild.name}`"

        await member.guild.system_channel.send(
            message
        )


def setup(bot):
    bot.add_cog(OnJoin(bot))
