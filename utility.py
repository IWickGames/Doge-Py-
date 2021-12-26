# flake8: noqa: E501
import discord
import aiohttp
from typing import List


class Image:
    def __init__(self, jdata):
        self.height = jdata["height"]
        self.width = jdata["width"]
        self.image = jdata["image"]
        self.source = jdata["source"]
        self.thumbnail = jdata["thumbnail"]
        self.title = jdata["title"]
        self.url = jdata["url"]


async def CheckHigharchy(target: discord.User, author: discord.User):
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


async def EncodeDrawCode(codeRaw):
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
