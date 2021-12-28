import groups
import db.sets
import db.databace
from discord.ext import commands
from discord.commands.commands import Option


class Set(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.settings.command()
    async def set(
        ctx: commands.Context,
        type: Option(
            str,
            description="Config type User or Guild",  # noqa: F722
            required=True,
            choices=["User", "Guild"]  # noqa: F821
        ),
        setting: Option(
            str,
            description="The setting you wish to change",  # noqa: F722
            required=True
        ),
        value: Option(
            str,
            description="The new value of the setting",  # noqa: F722
            required=True
        )
    ):
        """Configure User and Guild settings"""

        match type:
            case "User":
                if setting not in db.sets.user_settings:
                    await ctx.respond(
                        f"Invalid user setting `{setting}`",
                        ephemeral=True
                    )
                    return
                await db.databace.WriteKey(
                    f"settings.{ctx.author.id}.{setting}",
                    value
                )
            case "Guild":
                if setting not in db.sets.guild_settings:
                    await ctx.respond(
                        f"Invalid guild setting `{setting}`",
                        ephemeral=True
                    )
                    return
                await db.databace.WriteKey(
                    f"settings.{ctx.guild.id}.{setting}",
                    value
                )

        await ctx.respond(
            ":white_check_mark: Updated your settings successfully",
            ephemeral=True
        )


def setup(bot):
    bot.add_cog(Set(bot))
