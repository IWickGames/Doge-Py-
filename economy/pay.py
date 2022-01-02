import groups
import config
import discord
import db.databace
import log.logging
from discord.ext import commands
from discord.commands.commands import Option


class Pay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.economy.command()
    async def pay(
        ctx: commands.Context,
        user: Option(
            discord.User,
            description="The user to pay",  # noqa: F722
            required=True
        ),
        amount: Option(
            int,
            description="The amount to give",  # noqa: F722
            required=True
        )
    ):
        """Pay another user"""
        await log.logging.Info(
            f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})"
            " executed Pay in Economy"
        )

        if amount == 0:
            await ctx.respond(
                "You cannot pay someone 0 funds",
                ephemeral=True
            )
            return

        if user.bot:
            await ctx.respond(
                "You cannot pay a bot",
                ephemeral=True
            )
            return

        authorBal = await db.databace.ReadKey(
            f"economy.{ctx.author.id}.balance"
        )
        authorBal = authorBal or 0
        userBal = await db.databace.ReadKey(
            f"economy.{user.id}.balance"
        )
        userBal = userBal or 0

        if amount > authorBal:
            await ctx.respond(
                "You do not have the required funds",
                ephemeral=True
            )
            return

        await db.databace.WriteKey(
            f"economy.{ctx.author.id}.balance",
            authorBal-amount
        )
        await db.databace.WriteKey(
            f"economy.{user.id}.balance",
            userBal+amount
        )

        emb = discord.Embed(
            title="Payment successfull",
            description=f"You paid `{user.name}#{user.discriminator}` {amount}",  # noqa: E501
            color=config.embed_color
        )
        emb.add_field(
            name="Your balance",
            value=f"`{authorBal-amount}`"
        )
        emb.add_field(
            name=f"{user.name}'s balance",
            value=f"`{userBal+amount}`"
        )

        await ctx.respond(
            content=f"{user.mention}, you have "
            f"been paid by {ctx.author.mention}",
            embed=emb
        )


def setup(bot):
    bot.add_cog(Pay(bot))
