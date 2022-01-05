import groups
import config
import discord
import aiohttp
import log.logging
from discord.ext import commands


class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.fun.command(guild_ids=config.test_servers)
    async def meme(ctx: commands.Context):
        """Get an extra dank meme from the interwebs"""
        await log.logging.Info(
            f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})"
            " executed Meme in Fun"
        )

        async with aiohttp.ClientSession() as sess:
            async with sess.get(config.meme_api) as req:
                memeAPI = await req.json()

        emb = discord.Embed(
            title=memeAPI["title"],
            color=config.embed_color,
            url=memeAPI["postLink"]
        )
        emb.set_image(url=memeAPI["url"])
        emb.set_footer(
            text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
        await ctx.respond(embed=emb)


def setup(bot):
    bot.add_cog(Meme(bot))
