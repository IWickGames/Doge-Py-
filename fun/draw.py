import groups
import config
import discord
import log.logging
from discord.ext import commands
from utility import EncodeDrawCode
from discord.commands.commands import Option


class Draw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.fun.command()
    async def draw(
        ctx: commands.Context,
        code: Option(
            str,
            description="Width x Hight : 1 = Blue | 0 = Black",  # noqa: F722
            required=True
        )
    ):
        """Draws the spesified code to the screen using emotes"""
        await log.logging.Info(
            f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})"
            " executed Draw in Fun"
        )

        if "x" not in code.lower() or ":" not in code:
            await ctx.respond(
                ":anger: Grrrr, invalid draw code format",
                ephemeral=True
            )
            return

        message = await EncodeDrawCode(code)
        if not message:
            await ctx.respond(
                ":anger: Grrrr, Failed to encode message, it may be out of "
                "bounds of your dimensions or has invalid characters",
                ephemeral=True
            )
            return

        emb = discord.Embed(
            title="Drawing",
            description=message,
            color=config.embed_color
        )
        emb.add_field(name="Code", value=code)
        await ctx.respond(embed=emb)


def setup(bot):
    bot.add_cog(Draw(bot))
