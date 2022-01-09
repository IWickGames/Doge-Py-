import config
import groups
import discord
from discord.ext import commands


class Guilds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.owner.command()
    async def guilds(ctx: commands.Context):
        """List the bots guilds"""
        if ctx.author.id not in config.authorized_users:
            await ctx.respond(config.bot_permission_errormsg, ephemeral=True)
            return

        lines = [f"""{g.name} ({g.id})""" for g in config.bot.guilds]

        emb = discord.Embed(
            title="Joined guilds",
            description="\n".join(lines),
            color=config.embed_color
        )
        await ctx.respond(embed=emb, ephemeral=True)


def setup(bot):
    bot.add_cog(Guilds(bot))
