import config
import discord
import utility


async def RunLinkScanning(message: discord.Message):
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
                        "\n`Do not enter any personal or login "
                        "information into "
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
