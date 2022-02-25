import groups
import config
import db.sets
import db.databace
import log.logging
from discord import Option
from discord.ext import commands


class View(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.settings.command()
    async def view(
        ctx: commands.Context,
        type: Option(
            str,
            description="Config type User or Guild",  # noqa: F722
            required=True,
            choices=["User", "Guild"]  # noqa: F821
        ),
        setting: Option(
            str,
            description="The setting you wish to view",  # noqa: F722
            required=True
        )
    ):
        """View a configuration value"""
        await log.logging.Info(
            f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})"
            " executed View in Settings"
        )

        match type:
            case "User":
                if setting not in db.sets.user_settings:
                    await ctx.respond(
                        f"Invalid user setting `{setting}`",
                        ephemeral=True
                    )
                    return
                value = await db.databace.ReadKey(
                    f"settings.{ctx.author.id}.{setting}"
                )
            case "Guild":
                if not ctx.author.guild_permissions.administrator:
                    await ctx.respond(
                        config.bot_permission_errormsg,
                        ephemeral=True
                    )
                    return

                if setting not in db.sets.guild_settings:
                    await ctx.respond(
                        f"Invalid guild setting `{setting}`",
                        ephemeral=True
                    )
                    return
                value = await db.databace.ReadKey(
                    f"settings.{ctx.guild.id}.{setting}"
                )

        if not value:
            await ctx.respond(
                "That setting is not currently "
                "defined and is using default values",
                ephemeral=True
            )
            return

        await ctx.respond(
            f"The value of {setting} is ```{value}```",
            ephemeral=True
        )


def setup(bot):
    bot.add_cog(View(bot))
