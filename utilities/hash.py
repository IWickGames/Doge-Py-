import groups
import hashlib
from discord.ext import commands
from discord.commands.commands import Option


class Hash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.utilities.command()
    async def hash(
        ctx: commands.Context,
        algorithm: Option(
            str,
            description="The algorithm to use",  # noqa: F722
            required=True,
            choices=[
                "md5",  # noqa: F821
                "sha1",  # noqa: F821
                "sha224",  # noqa: F821
                "sha256",  # noqa: F821
                "sha384",  # noqa: F821
                "sha512"  # noqa: F821
            ]
        ),
        text: Option(
            str,
            description="The text to hash",  # noqa: F722
            required=True
        )
    ):
        """Hash a string using a bunch of algorithms"""

        match algorithm:
            case "md5":
                h = hashlib.md5(text.encode("UTF-8"))
            case "sha1":
                h = hashlib.sha1(text.encode("UTF-8"))
            case "sha224":
                h = hashlib.sha224(text.encode("UTF-8"))
            case "sha256":
                h = hashlib.sha256(text.encode("UTF-8"))
            case "sha384":
                h = hashlib.sha384(text.encode("UTF-8"))
            case "sha512":
                h = hashlib.sha512(text.encode("UTF-8"))

        await ctx.respond(
            f"`{text}`\nInput -> {algorithm} = `{h.hexdigest()}`"
        )


def setup(bot):
    bot.add_cog(Hash(bot))
