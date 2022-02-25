import groups
import config
import discord
import log.logging
from discord import Option
from discord.ext import commands


class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.utilities.command()
    async def poll(
        ctx: commands.Context,
        message: Option(
            str,
            description="The poll message",  # noqa: F722
            required=True
        )
    ):
        """Create a simple thumbs up or down poll"""
        await log.logging.Info(
            f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})"
            " executed Poll in Utilities"
        )

        emb = discord.Embed(
            title=message,
            color=config.embed_color,
            description="Place your vote below with :thumbsup: or :thumbsdown:"
        )
        emb.set_footer(
            text="Poll started by"
            f" {ctx.author.name}#{ctx.author.discriminator}"
        )
        msg: discord.Message = await ctx.send(embed=emb)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")
        await ctx.respond(
            ":white_check_mark: Poll created successfully",
            ephemeral=True
        )


def setup(bot):
    bot.add_cog(Poll(bot))
