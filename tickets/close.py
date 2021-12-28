import groups
import discord
from discord.ext import commands


class Close(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.tickets.command()
    async def close(ctx: commands.Context):
        """Run this inside a open ticket to close it"""
        if not ctx.channel.name.startswith("ticket-"):
            await ctx.respond(
                "This is not a ticket channel",
                ephemeral=True
            )
            return

        tnum = ctx.channel.name.split("-")[-1]

        try:
            await ctx.channel.edit(
                name=f"closed-{tnum}"
            )
        except discord.Forbidden:
            await ctx.respond(
                ":closed_lock_with_key: Bot does not"
                " have permissions to edit this channel",
                ephemeral=True
            )
            return

        await ctx.respond(
            ":lock: Ticket closed by "
            f"`{ctx.author.name}#{ctx.author.discriminator}`"
        )


def setup(bot):
    bot.add_cog(Close(bot))
