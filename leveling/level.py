import groups
import config
import discord
import db.databace
import log.logging
from discord import Option
from discord.ext import commands


class Level(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.leveling.command()
    async def level(
        ctx: commands.Context,
        user: Option(
            discord.User,
            description="The user to lookup",  # noqa: F722
            required=True
        )
    ):
        """Display your current message level and experience"""
        await log.logging.Info(
            f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})"
            " executed Level in Leveling"
        )

        if user.bot:
            await ctx.respond(
                "Cannot lookup level of bot accounts",
                ephemeral=True
            )
            return

        exp = await db.databace.ReadKey(
            f"leveling.{user.id}.{ctx.guild.id}"
        )
        if not exp:
            exp = 0

        emb = discord.Embed(
            color=config.embed_color
        )
        emb.set_author(
            name=user.name,
            icon_url=user.avatar.url
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
