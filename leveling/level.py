import groups
import config
import discord
import db.databace
from discord.ext import commands


class Level(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.leveling.command()
    async def level(ctx: commands.Context):
        """Display your current message level and experience"""

        exp = await db.databace.ReadKey(
            f"leveling.{ctx.author.id}.{ctx.guild.id}"
        )
        if not exp:
            exp = 0

        emb = discord.Embed(
            color=config.embed_color
        )
        emb.set_author(
            name=ctx.author.name,
            icon_url=ctx.author.avatar.url
        )
        emb.add_field(
            name="Level",
            value=str(int(exp/100))
        )
        emb.add_field(
            name="Experience",
            value=f"{exp % 100}/100 • `{exp}` total"
        )
        await ctx.respond(embed=emb)


def setup(bot):
    bot.add_cog(Level(bot))
