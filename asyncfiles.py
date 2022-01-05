import os
import config


async def read(file: str) -> bytes:
    return await config.bot.loop.run_in_executor(
        None, __read, file
    )


def __read(file: str) -> bytes:
    if not os.path.exists(file):
        return None
    with open(file, "rb") as f:
        return f.read()


async def write(file: str, data: bytes):
    return await config.bot.loop.run_in_executor(
        None, __write, file, data
    )


def __write(file: str, data: bytes):
    with open(file, "wb") as f:
        f.write(data)
