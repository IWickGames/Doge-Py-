from discord.ext import commands
import discord
import config
import groups

class Afk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @groups.utilities.command(guild_ids=config.test_servers)
    async def afk(self, ctx: commands.Context):
        """Toggle your AFK status"""
        try:
            member: discord.Member = await ctx.guild.fetch_member(ctx.author.id)

            if member.nick == None or not member.nick.startswith("[AFK]"):
                await member.edit(nick=f"[AFK] {ctx.author.name}")
            else:
                await member.edit(nick=f"{ctx.author.name}")
        except discord.Forbidden:
            await ctx.respond(config.bot_permission_boterrormsg, ephemeral=True)
            return
        except discord.HTTPException:
            await ctx.respond(config.bot_discorderror, ephemeral=True)
            return

        await ctx.respond(":white_check_mark: Changed your AFK status", ephemeral=True)

def setup(bot):
    bot.add_cog(Afk(bot))