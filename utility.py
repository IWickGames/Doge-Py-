# flake8: noqa: E501
import re
import discord
import aiohttp
from log import logging
from typing import List, Tuple


class Image:
    def __init__(self, jdata):
        self.height = jdata["height"]
        self.width = jdata["width"]
        self.image = jdata["image"]
        self.source = jdata["source"]
        self.thumbnail = jdata["thumbnail"]
        self.title = jdata["title"]
        self.url = jdata["url"]


async def CheckHigharchy(target: discord.User, author: discord.User) -> bool:
    """Returns True if the target has a higher role than the author else false"""
    return target.top_role >= author.top_role


async def GetImages(search) -> List[Image]:
    async with aiohttp.ClientSession() as s:
        query: str = search.replace(" ", "+")

        vqdReq = await s.get(
            f"https://duckduckgo.com/?q={query}&iax=images&ia=images",
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"}
        )
        vqdText: str = await vqdReq.text()
        vqd: str = vqdText.split("vqd='", 1)[1].split("';", 1)[0]

        jReq = await s.get(
            f"https://duckduckgo.com/i.js?l=us-en&o=json&q={query}&vqd={vqd}&f=,,,,,&p=1",
        )
        j = await jReq.json(content_type="application/x-javascript")

        await s.close()

    images = []
    for image in j["results"]:
        im = Image(image)
        images.append(im)

    return images


async def EncodeDrawCode(codeRaw) -> str | None:
    length, width = codeRaw.split(":", 1)[0].lower().split("x")
    code = codeRaw.split(":", 1)[1]

    if len(list(code)) > 2040:
        return None

    message = ""
    addLen = 0
    addLines = 0
    for num in list(code):
        if num == "1":
            message += ":blue_square:"
        elif num == "0":
            message += ":black_large_square:"
        else:
            return None

        if addLen == int(length) - 1:
            message += "\n"
            addLen = 0
            addLines += 1
        else:
            addLen += 1

        if addLines > int(width):
            return None

    return message

async def InputMessageArguments(member: discord.Member, message: str) -> str:
    message = message.replace("{username}", member.name)
    message = message.replace("{discriminator}", member.discriminator)
    message = message.replace("{id}", member.id)
    message = message.replace("{mention}", member.mention)
    message = message.replace("{created}", discord.utils.format_dt(member.created_at))
    return message


async def GetMessageUrls(message: str) -> List[str]:
    matches = re.findall(
        r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
        message
    )
    return matches


async def ScanUrl(url: str) -> Tuple[int, str]:
    """
    Does a saftey check on a given url

    0 = Safe
    1 = Warning
    2 = Danger

    Returns:
        Status Code - int
        Reason (Check) - str
    """
    headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 14324.62.0) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/97.0.4692.77 Safari/537.36"}

    if url.lower().endswith(".exe") or url.lower().endswith(".py"):
        return 2, "File - Executable file"

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as s:
        try:
            req = await s.get(url, allow_redirects=True, headers=headers)
            data = await req.text()
        except UnicodeDecodeError:
            await logging.Error("Failed to parce scanned: " + url)
            return 1, "Content is not parciable (could be a file such as a PDF)"
        except aiohttp.ClientConnectorError:
            await logging.Error("Scan connection failed: "+ url)
            return 1, "Failed to resolve website"
        data = data.lower()

        # Potential Discord Nitro scam check
        if "free" in data and "discord" in data and "nitro" in data:
            if "worth it" in data or "don't fall for" in data:
                pass
            else:
                return 2, "Advert - Free Nitro (Potential Scam)"
        
        # Cash App Hack scam check
        if "cash" in data and "app" in data and "hack" in data:
            return 2, "Advert - Cash App Hack scam"
        
        return 0, "No issues found"
