import groups
import config
import discord
import datetime
import db.databace
from discord.ext import commands
from utility import CheckHigharchy
from discord.commands.commands import Option


class Timeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.moderation.command()
    async def timeout(
        ctx: commands.Context,
        user: Option(
            discord.Member,
            description="The user to timeout",  # noqa: F722
            required=True
        ),
        time: Option(
            str,
            description="The amount of time to mute the user for",  # noqa: F722, E501
            choices=["1 Minute", "5 Minutes",                       # noqa: F722, E501
                     "10 Minutes", "1 Hour", "1 Day", "1 Week"],    # noqa: F722, E501
            required=True
        ),
        reason: Option(
            str,
            description="The reason for the timeout",  # noqa: F722
            default="No reason spesified",             # noqa: F722
            required=False
        )
    ):
        """Timeout a user for a certain amount of time"""
        higharchy: bool = await CheckHigharchy(user, ctx.author)
        if not ctx.author.guild_permissions.ban_members or higharchy:
            await ctx.respond(config.bot_permission_errormsg, ephemeral=True)
            return

        if user.timed_out:
            await ctx.respond(
                ":hourglass_flowing_sand: The user "
                f"`{user.name}#{user.discriminator}` is already in timeout",
                ephemeral=True
            )
            return

        now = datetime.datetime.now()

        match time:
            case "1 Minute":
                util = now + datetime.timedelta(seconds=60)
            case "5 Minutes":
                util = now + datetime.timedelta(minutes=5)
            case "10 Minutes":
                util = now + datetime.timedelta(minutes=10)
            case "1 Hour":
                util = now + datetime.timedelta(hours=1)
            case "1 Day":
                util = now + datetime.timedelta(days=1)
            case "1 Week":
                util = now + datetime.timedelta(weeks=1)
            case _:
                util = now + datetime.timedelta(minutes=5)

        await db.databace.AppendKey(
            f"punishments.{user.id}.{ctx.guild.id}",
            {
                "type": "Timeout",
                "reason": reason,
                "issuer": f"{ctx.author.name}#{ctx.author.discriminator}"
            }
        )

        try:
            await user.timeout(until=util, reason=reason)
        except discord.Forbidden:
            await ctx.respond(
                config.bot_permission_boterrormsg,
                ephemeral=True
            )
            return

        await ctx.respond(
            f":white_check_mark: The user `{user.name}#{user.discriminator}` "
            f"was successfully timeouted until {discord.utils.format_dt(util)}"
        )


def setup(bot):
    bot.add_cog(Timeout(bot))
