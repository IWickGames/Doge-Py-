import config
import discord
import utility
import db.databace
from discord.ext import commands


class OnMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        value = await db.databace.ReadKey(
            f"leveling.{message.author.id}.{message.guild.id}"
        )
        if not value:
            value = 0

        await db.databace.WriteKey(
            f"leveling.{message.author.id}.{message.guild.id}",
            value+1
        )

        if (value+1) % 100 == 0:
            await message.reply(
                content=":confetti_ball: Congrats "
                f"`{message.author.name}` you reached "
                f"level `{int((value+1)/100)}` with `{value+1}` "
                "total experience"
            )

        urls = await utility.GetMessageUrls(
            message.content
        )
        if len(urls) != 0:
            await message.add_reaction("🔗")
            for url in urls:
                status, reason = await utility.ScanUrl(url)

                match status:
                    case 0:
                        await message.add_reaction("🟩")
                    case 1:
                        await message.add_reaction("🟨")
                    case 2:
                        await message.add_reaction("🟥")

                        emb = discord.Embed(
                            title="Potentially dangerous content",
                            description="This message has been flaged to "
                            "contain links to potentially malicious "
                            "or phishing content. Proceed with caution. "
                            "\n`Do not enter any personal or login information into "
                            "any website you don't trust.`",
                            color=config.embed_color
                        )
                        emb.add_field(
                            name="Url",
                            value=f"`{url}`"
                        )
                        emb.add_field(
                            name="Check",
                            value=reason
                        )
                        emb.add_field(
                            name="Author",
                            value=f"{message.author.mention} "
                            f"{message.author.name}#"
                            f"{message.author.discriminator} "
                            f"({message.author.id})"
                        )
                        emb.set_thumbnail(
                            url="https://image.flaticon.com/icons/"
                            "png/512/868/868647.png"
                        )
                        await message.reply(embed=emb)


def setup(bot):
    bot.add_cog(OnMessage(bot))
