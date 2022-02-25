import groups
import config
import discord
import log.logging
from discord import Option
from discord.ext import commands


async def GetEmoteName(em):
    return em.split(':')[1]


async def GetEmoteID(em):
    return em.split(':')[2].split('>')[0]


class Emote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.tricks.command()
    async def emote(
        ctx: commands.Context,
        emoji: Option(
            str,
            description="The emoji send in a string",  # noqa: F722
            required=True
        )
    ):
        """Gives you information about an custom emote"""
        await log.logging.Info(
            f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})"
            " executed Emote in Tricks"
        )

        if not emoji.startswith("<"):
            await ctx.respond(
                ":compass: That emoji does not have a discord identifier",
                emphyrical=True
            )
            return

        emb = discord.Embed(
            title=await GetEmoteName(emoji),
            color=config.embed_color
        )
        emb.add_field(name="ID", value=await GetEmoteID(emoji))
        emb.add_field(
            name="Identifier",
            value=f"\\<:{await GetEmoteName(emoji)}:{await GetEmoteID(emoji)}\\>"  # noqa: E501
        )
        await ctx.respond(
            content=":compass: Here is what I know about that emoji",
            embed=emb
        )


def setup(bot):
    bot.add_cog(Emote(bot))
