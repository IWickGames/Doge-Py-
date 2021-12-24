import os
import json
import asyncio

global queue
queue = {}

async def WriteKey(key, value):
    global queue
    queue[key] = value

async def AppendKey(key, value):
    global queue
    db = await ReadKey(key)
    if not db:
        db = []
    db.append(value)
    await WriteKey(key, db)

async def ReadKey(key):
    global queue
    return queue.get(key)


async def databace_flush():
    Load()
    while True:
        await asyncio.sleep(30)
        Flush()

def Load():
    global queue
    if os.path.exists("db/bot.db"):
        with open("bot.db", "r") as f:
            queue = json.loads(f.read())
    else:
        queue = {}

def Flush():
    global queue
    print("[Databace] Starting flush operation...")
    with open("db/bot.db", "w") as f:
        f.write(json.dumps(queue, indent=4))
    print("[Databace] Flush operation completed")