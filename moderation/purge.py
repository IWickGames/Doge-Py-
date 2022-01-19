import groups
import config
import discord
import asyncio
import log.logging
from typing import List
from discord.ext import commands
from discord.commands.commands import Option


class Purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.moderation.command()
    async def purge(
        ctx: commands.Context,
        amount: Option(
            int,
            description="The amount of messages to purge",  # noqa: F722
            required=True
        )
    ):
        """Removes a spesified amount of messages"""
        await log.logging.Info(
            f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})"
            " executed Purge in Moderation"
        )

        if not ctx.author.guild_permissions.manage_messages:
            await ctx.respond(config.bot_permission_errormsg, ephemeral=True)
            return

        if amount > 1000:
            await ctx.respond(
                ":no_entry: Whoa! Purge has a "
                "maximum of 1000 messages per command.",
                ephemeral=True
            )
            return

        await ctx.respond(
            ":satellite: Starting message deletion...",
            ephemeral=True
        )

        if amount < 25:
            await ctx.channel.purge(limit=amount)
            await ctx.edit(
                content=":white_check_mark: Successfully purged"
                f" {amount} messages from `{ctx.channel.name}`"
            )
            return

        try:
            chunks: List[str] = int(str((amount/25)).split(".")[0])
            rmNum: List[str] = int(str((amount/25)).split(".")[1])
            for n in range(chunks):
                await ctx.edit(
                    content=f":satellite: Purging cunk {n+1} of {chunks}"
                    " ... | Deleteing"
                )
                await ctx.channel.purge(limit=25)
                await ctx.edit(
                    content=f":satellite: Purging cunk {n+1} of {chunks} ..."
                    " | Idle (Cooldown)"
                )
                await asyncio.sleep(30)
            if rmNum != 0:
                await ctx.channel.purge(limit=rmNum)
        except discord.Forbidden:
            await ctx.edit(
                content=config.bot_permission_boterrormsg,
                ephemeral=True
            )
            return
        except discord.HTTPException:
            await ctx.edit(content=config.bot_discorderror, ephemeral=True)
            return

        await ctx.edit(
            content=":white_check_mark: Successfully purged "
            f"{amount} messages from `{ctx.channel.name}`"
        )


def setup(bot):
    bot.add_cog(Purge(bot))
