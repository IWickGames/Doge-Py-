from datetime import datetime


async def Info(message):
    print(f"[{datetime.now()}] [Info] : " + message)


def SyncInfo(message):
    print(f"[{datetime.now()}] [Info] : " + message)


async def Warning(message):
    print(f"[{datetime.now()}] [Warn] : " + message)


def SyncWarning(message):
    print(f"[{datetime.now()}] [Warn] : " + message)


async def Error(message):
    print(f"[{datetime.now()}] [Erro] : " + message)


def SyncError(message):
    print(f"[{datetime.now()}] [Erro] : " + message)


def Databace(message):
    print(f"[{datetime.now()}] [DBac] : " + message)
