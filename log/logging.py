from datetime import datetime


async def Info(message):
    print(f"[{datetime.now()}] [Info] : " + message)


async def Warning(message):
    print(f"[{datetime.now()}] [Warn] : " + message)


async def Error(message):
    print(f"[{datetime.now()}] [Erro] : " + message)


def Databace(message):
    print(f"[{datetime.now()}] [DBac] : " + message)
