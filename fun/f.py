import groups
from discord import Option
from discord.ext import commands
from fun.views.fbtn import FButtons


class F(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.fun.command()
    async def f(
        ctx: commands.Context,
        message: Option(
            str,
            description="Message to add the F interation to",  # noqa: F722
            required=True
        )
    ):
        """Post a interactable F in the chat message"""
        await ctx.respond(
            message,
            view=FButtons()
        )


def setup(bot):
    bot.add_cog(F(bot))
