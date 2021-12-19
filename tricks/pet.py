from discord.ext import commands
import config
import groups

class Pet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @groups.tricks.command(guild_ids=config.test_servers)
    async def pet(self, ctx: commands.Context):
        """Tell me I am doing a good job!"""
        await ctx.respond(f":dog2: Awww! Thanks {ctx.author.mention} :yum:")

def setup(bot):
    bot.add_cog(Pet(bot))