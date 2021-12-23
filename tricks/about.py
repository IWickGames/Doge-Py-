import groups
import config
import discord
from discord.ext import commands

class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @groups.tricks.command()
    async def about(ctx: commands.Context):
        """Display information about this bot"""
        emb = discord.Embed(
            title="About Doge",
            description="""Thank you for using Doge bot by IWick Development, 
            Doge is a common useage discord bot to attempt to fill all your needs.
            We attempt to fit as many features as possibe into one single bot to hopefully 
            cut down on the large amount of bots that people have to add to get a functional 
            Discord server""".replace("\n", " "),
            color=config.embed_color
        )
        emb.set_thumbnail(url=config.bot.user.avatar.url)

        emb.add_field(
            name="Add Me!", 
            value="[Click here to add me to your server](https://discord.com/api/oauth2/authorize?client_id=869706426975670312&permissions=8&scope=applications.commands%20bot)", 
            inline=True
        )
        emb.add_field(
            name="GitHub", 
            value="[Click here for my GitHub page](https://github.com/IWickGames/Doge-Py-)", 
            inline=True
        )
        await ctx.respond(embed=emb)

def setup(bot):
    bot.add_cog(About(bot))