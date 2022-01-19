import groups
import db.databace
import log.logging
from discord.ext import commands
from discord.commands.commands import Option


class Credit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.economy.command()
    async def credit(
        ctx: commands.Context,
        amount: Option(
            int,
            description="The amount of experience to credit to currency",  # noqa: F722, E501
            required=True
        )
    ):
        """Converts your guild experience into global currency"""
        await log.logging.Info(
            f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})"
            " executed Credit in Economy"
        )

        if amount == 0:
            await ctx.respond(
                "You cannot credit 0 experience",
                ephemeral=True
            )
            return

        experience = await db.databace.ReadKey(
            f"leveling.{ctx.author.id}.{ctx.guild.id}"
        )

        if not experience or amount > experience:
            await ctx.respond(
                "You do not have enough experience",
                ephemeral=True
            )
            return

        balance = await db.databace.ReadKey(
            f"economy.{ctx.author.id}.balance"
        )
        if not balance:
            balance = 0
        await db.databace.WriteKey(
            f"economy.{ctx.author.id}.balance",
            balance+amount
        )

        await db.databace.WriteKey(
            f"leveling.{ctx.author.id}.{ctx.guild.id}",
            experience-amount
        )

        await ctx.respond(
            ":white_check_mark: Credit successfull!"
            f" You are now at a balance of `{balance+amount}`",
            ephemeral=True
        )


def setup(bot):
    bot.add_cog(Credit(bot))
