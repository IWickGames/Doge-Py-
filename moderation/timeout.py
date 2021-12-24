import groups
import config
import discord
import datetime
from discord.ext import commands
from utility import CheckHigharchy
from discord.commands.commands import Option

class Timeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @groups.moderation.command()
    async def timeout(
        ctx: commands.Context,
        user: Option(discord.Member, description="The user to timeout", required=True),
        time: Option(
            str, 
            description="The amount of time to mute the user for", 
            required=True,
            choices=["1 Minute", "5 Minutes", "10 Minutes", "1 Hour", "1 Day", "1 Week"]),
        reason: Option(str, description="The reason for the timeout", default="No reason spesified")
    ):
        """Timeout a user for a certain amount of time"""
        higharchy: bool = await CheckHigharchy(user, ctx.author)
        if not ctx.author.guild_permissions.ban_members or higharchy:
            await ctx.respond(config.bot_permission_errormsg, ephemeral=True)
            return

        now = datetime.datetime.now()

        if time == "1 Minute":
            util = now + datetime.timedelta(minutes=1)
        elif time == "5 Minutes":
            util = now + datetime.timedelta(minutes=5)
        elif time == "10 Minutes":
            util = now + datetime.timedelta(minutes=10)
        elif time == "1 Hour":
            util = now + datetime.timedelta(hours=1)
        elif time == "1 Day":
            util = now + datetime.timedelta(days=1)
        elif time == "1 Week":
            util = now + datetime.timedelta(weeks=1)
        else:
            util = now + datetime.timedelta(minutes=5)

        await user.timeout(until=util, reason=reason)
        await ctx.respond(
            f":white_check_mark: The user {user.name}#{user.discriminator} was successfully timeouted until {discord.utils.format_dt(util)}"
        )

def setup(bot):
    bot.add_cog(Timeout(bot))