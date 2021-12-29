import groups
import config
import db.databace
from discord.ext import commands
from discord.commands.commands import Option


class Disable(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.settings.command()
    async def disable(
        ctx: commands.Context,
        type: Option(
            str,
            description="Config type User or Guild",  # noqa: F722
            required=True,
            choices=["User", "Guild"]  # noqa: F821
        ),
        setting: Option(
            str,
            description="The setting you wish to disable",  # noqa: F722
            required=True
        )
    ):
        """Set a setting to disabled"""
        match type:
            case "User":
                if setting not in db.sets.user_settings:
                    await ctx.respond(
                        f"Invalid user setting `{setting}`",
                        ephemeral=True
                    )
                    return

                await db.databace.RemoveKey(
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
                await db.databace.RemoveKey(
                    f"settings.{ctx.guild.id}.{setting}"
                )

        await ctx.respond(
            ":white_check_mark: Updated settings successfully",
            ephemeral=True
        )


def setup(bot):
    bot.add_cog(Disable(bot))
