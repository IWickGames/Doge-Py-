import groups
import config
import discord
from discord.ext import commands

class Userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @groups.utilities.command()
    async def userinfo(self, ctx: commands.Context, user: discord.Member):
        """Get information about a user"""
        member: discord.Member = await ctx.guild.fetch_member(ctx.author.id)
        emb = discord.Embed(
            title=f"{user.name}#{user.discriminator} ({user.id})",
            color=config.embed_color
        )
        emb.set_thumbnail(url=user.avatar.url)
        
        if member.nick != None:
            emb.add_field(name="Nickname", value=member.nick, inline=True)

        emb.add_field(name="Created", value=discord.utils.format_dt(user.created_at), inline=True)
        emb.add_field(name="Joined", value=discord.utils.format_dt(user.joined_at), inline=True)
        emb.add_field(name="Roles", value=" ".join([i.mention for i in user.roles]), inline=True)

        await ctx.respond(embed=emb)

def setup(bot):
    bot.add_cog(Userinfo(bot))