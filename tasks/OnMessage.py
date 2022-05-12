import discord
from discord.ext import commands

import events.leveling
import events.linkscanning


class OnMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        await events.leveling.RunLeveling(message)
        await events.linkscanning.RunLinkScanning(message)


def setup(bot):
    bot.add_cog(OnMessage(bot))
