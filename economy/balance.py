import groups
import config
import discord
import db.databace
import log.logging
from discord.ext import commands
from discord.commands.commands import Option


class Balance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.economy.command(guild_ids=config.test_servers)
    async def balance(
        ctx: commands.Context,
        user: Option(
            discord.User,
            description="The user to lookup",  # noqa: F722
            required=True
        )
    ):
        """Get the balance of a user"""
        await log.logging.Info(
            f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})"
            " executed Balance in Economy"
        )

        balance = await db.databace.ReadKey(
            f"economy.{user.id}.balance"
        )

        emb = discord.Embed(
            description=f":coin: Balance: `{balance or 0}`",
            color=config.embed_color
        )
        emb.set_author(
            name=user.name,
            icon_url=user.avatar.url
        )

        await ctx.respond(embed=emb)


def setup(bot):
    bot.add_cog(Balance(bot))
