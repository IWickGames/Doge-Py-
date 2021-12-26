import groups
import config
import discord
from discord.ext import commands
from discord.commands.commands import Option


def GetEmoteName(em):
    return em.split(':')[1]


def GetEmoteID(em):
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
        if not emoji.startswith("<"):
            await ctx.respond(
                ":compass: That emoji does not have a discord identifier",
                emphyrical=True
            )
            return

        emb = discord.Embed(
            title=GetEmoteName(emoji),
            color=config.embed_color
        )
        emb.add_field(name="ID", value=GetEmoteID(emoji))
        emb.add_field(
            name="Identifier",
            value=f"\\<:{GetEmoteName(emoji)}:{GetEmoteID(emoji)}\\>"
        )
        await ctx.respond(
            content=":compass: Here is what I know about that emoji",
            embed=emb
        )


def setup(bot):
    bot.add_cog(Emote(bot))
