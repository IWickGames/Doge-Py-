import discord
import db.databace
from discord.ext import commands


class OnMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        value = await db.databace.ReadKey(
            f"leveling.{message.author.id}.{message.guild.id}"
        )
        if not value:
            value = 0

        await db.databace.WriteKey(
            f"leveling.{message.author.id}.{message.guild.id}",
            value+1
        )

        if (value+1) % 100 == 0:
            await message.reply(
                content=":confetti_ball: Congrats "
                f"`{message.author.name}` you reached "
                f"level `{int((value+1)/100)}` with `{value+1}` "
                "total experience"
            )


def setup(bot):
    bot.add_cog(OnMessage(bot))
