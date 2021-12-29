# flake8: noqa: E501
import os
import json
import config
import asyncio

global queue
queue = {}


async def WriteKey(key, value):
    """
    Writes a key and value to the databace (can also replace or overwrite an existing value)
    
    Arguments:
        key: The access key value to use
        value: The value of the access key stored
    
    Returns:
        None / Nothing
    """
    global queue
    queue[key] = value


async def AppendKey(key, value):
    """
    Appends a value to an existant key, used if the key is a List of values and you want to quickly append a value to said list

    Arguments:
        key: The access key to append the value to
        value: The data to append

    Returns:
        None / Nothing
    """
    global queue
    db = await ReadKey(key)
    if not db:
        db = []
    db.append(value)
    await WriteKey(key, db)


async def ReadKey(key):
    """
    Reads a key value from the databace file and retuns it

    Arguments:
        key: The access key to read

    Returns:
        Anything or None / Nothing
        Will return None if the key does not exist
    """
    global queue
    return queue.get(key)

async def RemoveKey(key):
    """
    Deletes a key from the databace

    Arguments:
        key: The access key to delete
    
    Returns:
        None / Nothing
    """
    global queue
    if key in queue.keys():
        queue.pop(key)


async def databace_flush():
    """
    The databace flush task

    /!\ IF YOU ARE CALLING THIS ANYWHERE YOU ARE USING IT WRONG /!\ 
    """
    Load()
    while True:
        await asyncio.sleep(30)
        Flush()


def Load():
    """
    Loads the databace into the queue global
    
    This should only be run once
    """
    global queue
    if os.path.exists(config.databace_file):
        with open(config.databace_file, "r") as f:
            queue = json.loads(f.read())
    else:
        queue = {}


def Flush():
    """
    Flush operation aka Dumps the queue variable onto disk

    /!\ THIS FUNCTION SHOULD ONLY BE CALLED BY THE databace_flush TASK /!\ 
    """
    global queue
    print("[Databace] Starting flush operation...")
    with open(config.databace_file, "w") as f:
        f.write(json.dumps(queue, indent=4))
    print("[Databace] Flush operation completed")
