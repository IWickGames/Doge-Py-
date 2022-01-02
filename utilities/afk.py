import groups
import config
import discord
import log.logging
from discord.ext import commands


class Afk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.utilities.command()
    async def afk(ctx: commands.Context):
        """Toggle your AFK status"""
        await log.logging.Info(
            f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})"
            " executed AFK in Utilities"
        )

        try:
            member: discord.Member = await ctx.guild.fetch_member(
                ctx.author.id
            )

            if member.nick is None or not member.nick.startswith("[AFK]"):
                await member.edit(nick=f"[AFK] {ctx.author.name}")
            else:
                await member.edit(nick=f"{ctx.author.name}")
        except discord.Forbidden:
            await ctx.respond(
                config.bot_permission_boterrormsg,
                ephemeral=True
            )
            return
        except discord.HTTPException:
            await ctx.respond(
                config.bot_discorderror,
                ephemeral=True
            )
            return

        await ctx.respond(
            ":white_check_mark: Changed your AFK status",
            ephemeral=True
        )


def setup(bot):
    bot.add_cog(Afk(bot))
