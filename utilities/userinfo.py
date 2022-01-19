import groups
import config
import discord
import log.logging
from discord.ext import commands
from discord.commands.commands import Option


class Userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.utilities.command()
    async def userinfo(
        ctx: commands.Context,
        user: Option(
            discord.Member,
            description="The user to view information on",  # noqa: F722
            default=None
        )
    ):
        """Get information about a user"""
        await log.logging.Info(
            f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})"
            " executed UserInfo in Utilities"
        )

        if not user:
            user = ctx.author

        member: discord.Member = await ctx.guild.fetch_member(ctx.author.id)
        emb = discord.Embed(
            title=f"{user.name}#{user.discriminator} ({user.id})",
            color=config.embed_color
        )
        emb.set_thumbnail(url=user.avatar.url)

        if member.nick is not None:
            emb.add_field(name="Nickname", value=member.nick, inline=True)

        emb.add_field(name="Created", value=discord.utils.format_dt(
            user.created_at), inline=True)
        emb.add_field(name="Joined", value=discord.utils.format_dt(
            user.joined_at), inline=True)
        emb.add_field(name="Roles", value=" ".join(
            [i.mention for i in user.roles]), inline=True)

        await ctx.respond(embed=emb)


def setup(bot):
    bot.add_cog(Userinfo(bot))
