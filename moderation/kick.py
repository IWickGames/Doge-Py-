import groups
import config
import discord
from typing import Optional
from discord.ext import commands
from utility import CheckHigharchy

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.moderation.command(guild_ids=config.test_servers)
    async def kick(self, ctx: commands.Context, user: discord.User, reason=Optional[str]):
        """Kicks a user from the server"""
        higharchy: bool = await CheckHigharchy(user, ctx.author)
        if not ctx.author.guild_permissions.ban_members or higharchy:
            await ctx.respond(config.bot_permission_errormsg, ephemeral=True)
            return
        
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