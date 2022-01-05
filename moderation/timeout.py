import groups
import config
import discord
import datetime
import db.databace
import log.logging
from discord.ext import commands
from utility import CheckHigharchy
from discord.commands.commands import Option


class Timeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.moderation.command(guild_ids=config.test_servers)
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
        await log.logging.Info(
            f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})"
            " executed Timeout in Moderation"
        )

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

        match time:
            case "1 Minute":
                util = datetime.timedelta(seconds=60)
            case "5 Minutes":
                util = datetime.timedelta(minutes=5)
            case "10 Minutes":
                util = datetime.timedelta(minutes=10)
            case "1 Hour":
                util = datetime.timedelta(hours=1)
            case "1 Day":
                util = datetime.timedelta(days=1)
            case "1 Week":
                util = datetime.timedelta(weeks=1)
            case _:
                util = datetime.timedelta(minutes=5)

        await db.databace.AppendKey(
            f"punishments.{user.id}.{ctx.guild.id}",
            {
                "type": "Timeout",
                "reason": reason,
                "issuer": f"{ctx.author.name}#{ctx.author.discriminator}",
                "timestamp": str(datetime.datetime.utcnow())
            }
        )

        try:
            await user.timeout_for(duration=util, reason=reason)
        except discord.Forbidden:
            await ctx.respond(
                config.bot_permission_boterrormsg,
                ephemeral=True
            )
            return

        await ctx.respond(
            f":white_check_mark: The user `{user.name}#{user.discriminator}` "
            f"was successfully timeouted for {time}"
        )


def setup(bot):
    bot.add_cog(Timeout(bot))
