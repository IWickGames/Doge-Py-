import os
import json
import asyncio

global queue
queue = {}

async def WriteKey(key, value):
    global queue
    queue[key] = value

async def ReadKey(key):
    global queue
    return queue.get(key)

async def databace_flush():
    while True:
        await asyncio.sleep(30)
        Flush()

def Load():
    global queue
    if os.path.exists("bot.db"):
        with open("bot.db", "r") as f:
            queue = json.loads(f.read())
    else:
        queue = {}

def Flush():
    global queue
    print("[Databace] Starting flush operation...")
    with open("bot.db", "w") as f:
        f.write(json.dumps(queue, indent=4))
    print("[Databace] Flush operation completed")