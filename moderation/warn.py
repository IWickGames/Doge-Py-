import groups
import config
import discord
from discord.ext import commands
from utility import CheckHigharchy

class Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.moderation.command()
    async def warn(self, ctx: commands.Context, user: discord.User, reason: str):
        """Warns a user on your server via a direct message"""
        higharchy: bool = await CheckHigharchy(user, ctx.author)
        if not ctx.author.guild_permissions.ban_members or higharchy:
            await ctx.respond(config.bot_permission_errormsg, ephemeral=True)
            return
        emb = discord.Embed(
            title=f"Warning from `{ctx.guild.name}` ({ctx.guild.id})",
            color=config.embed_color,
        )

        if ctx.guild.icon:
            emb.set_thumbnail(ctx.guild.icon.url)

        emb.add_field(name="Reason", value=reason, inline=True)
        emb.add_field(name="Issuer", value=f"{ctx.author.name}", inline=True)
        try:
            await user.send(embed=emb)
        except discord.Forbidden:
            await ctx.respond(config.bot_permission_boterrormsg, ephemeral=True)
            return
        except discord.HTTPException:
            await ctx.respond(config.bot_discorderror, ephemeral=True)
            return

        await ctx.respond(f":white_check_mark: Warned {user.name}#{user.discriminator} successfully")

def setup(bot):
    bot.add_cog(Warn(bot))