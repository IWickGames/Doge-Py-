import groups
import config
import discord
import db.databace
from discord.ext import commands
from utility import CheckHigharchy
from discord.commands.commands import Option


class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.moderation.command()
    async def kick(
        ctx: commands.Context,
        user: Option(discord.User, description="User to kick", required=True),
        reason: Option(
            str, description="The reason for the kick", required=False)
    ):
        """Kicks a user from the server"""
        higharchy: bool = await CheckHigharchy(user, ctx.author)
        if not ctx.author.guild_permissions.ban_members or higharchy:
            await ctx.respond(config.bot_permission_errormsg, ephemeral=True)
            return

        await db.databace.AppendKey(
            f"punishments.{user.id}.{ctx.guild.id}",
            {
                "type": "Kick",
                "reason": reason,
                "issuer": f"{ctx.author.name}#{ctx.author.discriminator}"
            }
        )

        try:
            await ctx.guild.kick(user, reason=reason)
        except discord.Forbidden:
            await ctx.respond(config.bot_permission_boterrormsg, ephemeral=True)
            return
        except discord.HTTPException:
            await ctx.respond(config.bot_discorderror, ephemeral=True)
            return

        await ctx.respond(f":hammer: Successfully kicked {user.name}#{user.discriminator}")


def setup(bot):
    bot.add_cog(Kick(bot))
