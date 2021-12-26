import config
import groups
import random
import discord
from typing import List
from utility import GetImages
from utility import Image as ResponceImages
from discord.ext import commands


class Image(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.fun.command()
    async def image(ctx: commands.Context, query: str):
        """Lookup an image from the internet"""
        await ctx.respond(":satellite: Looking up images...")

        try:
            img: List[ResponceImages] = await GetImages(query)
        except Exception as err:
            print("Failed to grab images online")
            print(err)
            await ctx.edit(
                content=":no_enry: Failed to pull image from API (try again)"
            )
            return

        emb = discord.Embed(
            title=f"Image of {query}",
            color=config.embed_color
        )
        emb.set_footer(
            text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
        emb.set_image(url=random.choice(img).image)

        await ctx.edit(content="", embed=emb)


def setup(bot):
    bot.add_cog(Image(bot))
