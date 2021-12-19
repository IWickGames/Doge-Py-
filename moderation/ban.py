import config
import groups
import discord
from typing import Optional
from discord.ext import commands
from utility import CheckHigharchy

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @groups.moderation.command(guild_ids=config.test_servers)
    async def ban(self, ctx: commands.Context, user: discord.User, reason: Optional[str]):
        """Ban a user from the server"""
        higharchy: bool = await CheckHigharchy(user, ctx.author)
        if not ctx.author.guild_permissions.ban_members or higharchy:
            await ctx.respond(config.bot_permission_errormsg, ephemeral=True)
            return

        try:
            await ctx.guild.ban(user, reason=reason)
        except discord.Forbidden:
            await ctx.respond(config.bot_permission_boterrormsg, ephemeral=True)
            return
        except discord.HTTPException:
            await ctx.respond(config.bot_discorderror, ephemeral=True)
            return
        
        await ctx.respond(f":hammer: Successfully banned {user.name}#{user.discriminator}", ephemeral=True)

def setup(bot):
    bot.add_cog(Ban(bot))