import config
import groups
import discord
import db.databace
from discord.ext import commands
from utility import CheckHigharchy
from discord.commands.commands import Option


class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.moderation.command()
    async def ban(
        ctx: commands.Context,
        user: Option(
            discord.User,
            description="User to ban",  # noqa: F722
            required=True
        ),
        reason: Option(
            str,
            description="The reason for the ban",  # noqa: F722
            required=False
        )
    ):
        """Ban a user from the server"""
        higharchy: bool = await CheckHigharchy(user, ctx.author)
        if not ctx.author.guild_permissions.ban_members or higharchy:
            await ctx.respond(config.bot_permission_errormsg, ephemeral=True)
            return

        await db.databace.AppendKey(
            f"punishments.{user.id}.{ctx.guild.id}",
            {
                "type": "Ban",
                "reason": reason,
                "issuer": f"{ctx.author.name}#{ctx.author.discriminator}"
            }
        )

        try:
            await ctx.guild.ban(user, reason=reason)
        except discord.Forbidden:
            await ctx.respond(
                config.bot_permission_boterrormsg,
                ephemeral=True
            )
            return
        except discord.HTTPException:
            await ctx.respond(config.bot_discorderror, ephemeral=True)
            return

        await ctx.respond(
            f":hammer: Successfully banned {user.name}#{user.discriminator}",
            ephemeral=True
        )


def setup(bot):
    bot.add_cog(Ban(bot))
