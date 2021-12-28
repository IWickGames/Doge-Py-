import groups
import base64
import binascii
from discord.ext import commands
from discord.commands.commands import Option


class Base64(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.utilities.command()
    async def base64(
        ctx: commands.Context,
        operation: Option(
            str,
            description="The operation to perform",  # noqa: F722
            required=True,
            choices=[
                "Encode",  # noqa: F821
                "Decode"  # noqa: F821
            ]
        ),
        text: Option(
            str,
            description="The text to encode",  # noqa: F722
            required=True
        )
    ):
        """Encodes and decodes text into and out of base64"""

        try:
            match operation:
                case "Encode":
                    code = base64.b64encode(
                        text.encode("UTF-8")
                    ).decode("UTF-8")
                case "Decode":
                    code = base64.b64decode(
                        text.encode("UTF-8")
                    ).decode("UTF-8")
        except binascii.Error:
            await ctx.respond("Invalid Base64 data", ephemeral=True)
            return

        await ctx.respond(
            f"`{text}`\nInput -> Base64({operation}) = `{code}`"
        )


def setup(bot):
    bot.add_cog(Base64(bot))
