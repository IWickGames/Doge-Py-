import groups
import base64
import binascii
import log.logging
from discord import Option
from discord.ext import commands


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
        await log.logging.Info(
            f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})"
            " executed Base64 in Utilities"
        )

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
