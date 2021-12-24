import json

global queue
queue = {}

async def WriteKey(key, value):
    global queue
    queue[key] = value

async def ReadKey(key):
    global queue
    return queue.get(key)

def Load():
    global queue
    with open("bot.db", "r") as f:
        queue = json.loads(f.read())

def Flush():
    global queue
    print("[Databace] Starting flush operation (DO NOT FORCE KILL THE PROCESS)...")
    with open("bot.db", "w") as f:
        f.write(json.dumps(queue, indent=4))
    print("[Databace] Flush operation completed, exiting...")