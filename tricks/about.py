import groups
import config
import discord
import log.logging
from discord.ext import commands
from tricks.views.aboutbtn import AboutBtn


class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.tricks.command(guild_ids=config.test_servers)
    async def about(ctx: commands.Context):
        """Display information about this bot"""
        await log.logging.Info(
            f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})"
            " executed About in Tricks"
        )

        emb = discord.Embed(
            title="About Doge",
            description="""
            Thank you for using Doge bot by IWick Development,
            Doge is a common usage discord bot to attempt to
             fill all your needs.
            We attempt to fit as many features as possibe into
             one single bot to hopefully
            cut down on the large amount of bots that people
             have to add to get a functional
            Discord server
            """.replace("\n", " "),
            color=config.embed_color
        )
        emb.set_thumbnail(url=config.bot.user.avatar.url)

        await ctx.respond(embed=emb, view=AboutBtn())


def setup(bot):
    bot.add_cog(About(bot))
