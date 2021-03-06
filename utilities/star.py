import config
import groups
import discord
import log.logging
from discord import Option
from discord.ext import commands


class Star(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.utilities.command()
    async def star(
        ctx: commands.Context,
        message_id: Option(
            str,
            description="The ID of the message you would like to star",  # noqa: F722, E501
            required=True
        )
    ):
        """Add a message to the servers star board"""
        await ctx.defer()

        await log.logging.Info(
            f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})"
            " executed Star in Utilities"
        )

        if not ctx.author.guild_permissions.manage_messages:
            await ctx.respond(config.bot_permission_errormsg, ephemeral=True)
            return

        try:
            msg: discord.Message = await ctx.fetch_message(int(message_id))
        except discord.NotFound:
            await ctx.respond(
                ":mag: Unable to locate the spesified message ID",
                ephemeral=True
            )
            return
        except discord.Forbidden:
            await ctx.respond(
                config.bot_permission_boterrormsg,
                ephemeral=True
            )
            return
        except discord.HTTPException:
            await ctx.respond(config.bot_discorderror, ephemeral=True)
            return

        channel = None
        for chl in ctx.guild.text_channels:
            if "star" in chl.name.lower() and "board" in chl.name.lower():
                channel = chl
                break
        if not channel:
            await ctx.respond(
                ":mag: Unable to locate a star-board channel",
                ephemeral=True
            )
            return

        emb = discord.Embed(
            description=f"[Jump to message]({msg.jump_url})",
            color=config.embed_color
        )
        emb.set_author(name=msg.author.name, icon_url=msg.author.avatar.url)
        emb.set_footer(
            text=f"#{msg.channel.name} ??? "
            f"{discord.utils.format_dt(msg.created_at)}"
        )

        await channel.send(embed=emb)

        await ctx.respond(
            ":white_check_mark: Added message "
            f"id `{message_id}` to {channel.mention}"
        )


def setup(bot):
    bot.add_cog(Star(bot))
