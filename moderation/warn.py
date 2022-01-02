import groups
import config
import discord
import db.databace
import log.logging
from discord.ext import commands
from utility import CheckHigharchy
from discord.commands.commands import Option


class Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.moderation.command()
    async def warn(
        ctx: commands.Context,
        user: Option(
            discord.User,
            description="The user to warn",  # noqa: F722
            required=True
        ),
        reason: Option(
            str,
            description="The reasion to warn the user",  # noqa: F722
            required=True
        )
    ):
        """Warns a user on your server via a direct message"""
        await log.logging.Info(
            f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})"
            " executed Warn in Moderation"
        )

        higharchy: bool = await CheckHigharchy(user, ctx.author)
        if not ctx.author.guild_permissions.ban_members or higharchy:
            await ctx.respond(config.bot_permission_errormsg, ephemeral=True)
            return

        if user.bot:
            await ctx.respond(config.bot_interaction_boterror, ephemeral=True)
            return

        emb = discord.Embed(
            title=f"Warning from `{ctx.guild.name}` ({ctx.guild.id})",
            color=config.embed_color,
        )

        if ctx.guild.icon:
            emb.set_thumbnail(ctx.guild.icon.url)

        emb.add_field(name="Reason", value=reason, inline=True)
        emb.add_field(name="Issuer", value=f"{ctx.author.name}", inline=True)

        await db.databace.AppendKey(
            f"punishments.{user.id}.{ctx.guild.id}",
            {
                "type": "Warning",
                "reason": reason,
                "issuer": f"{ctx.author.name}#{ctx.author.discriminator}"
            }
        )

        try:
            await user.send(embed=emb)
        except discord.Forbidden:
            await ctx.respond(
                ":mailbox_with_mail: The spesified user "
                "has direct messaging disabled",
                ephemeral=True
            )
            return
        except discord.HTTPException:
            await ctx.respond(config.bot_discorderror, ephemeral=True)
            return

        await ctx.respond(
            f":white_check_mark: Warned {user.name}#{user.discriminator} "
            "successfully"
        )


def setup(bot):
    bot.add_cog(Warn(bot))
