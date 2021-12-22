import groups
import config
import discord
from discord.ext import commands

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @groups.utilities.command()
    async def poll(self, ctx: commands.Context, message: str):
        """Create a simple thumbs up or down poll"""
        emb = discord.Embed(
            title=message,
            color=config.embed_color,
            description="Place your vote below with :thumbsup: or :thumbsdown:"
        )
        emb.set_footer(text=f"Poll started by {ctx.author.name}#{ctx.author.discriminator}")
        msg: discord.Message = await ctx.send(embed=emb)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")
        await ctx.respond(":white_check_mark: Poll created successfully", ephemeral=True)

def setup(bot):
    bot.add_cog(Poll(bot))