# flake8: noqa: E501
import os
import json
import config
import asyncio
import log.logging

global queue
queue = {}

global updated
updated = False


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
    global updated
    queue[key] = value
    updated = True


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
    global updated
    db = await ReadKey(key)
    if not db:
        db = []
    db.append(value)
    await WriteKey(key, db)
    updated = True


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
    global updated
    if key in queue.keys():
        queue.pop(key)
    updated = True


async def databace_flush():
    """
    The databace flush task

    /!\ IF YOU ARE CALLING THIS ANYWHERE YOU ARE USING IT WRONG /!\ 
    """
    global updated
    Load()
    while True:
        await asyncio.sleep(30)
        if updated:
            Flush()
            updated = False


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
    with open(config.databace_file, "w") as f:
        f.write(json.dumps(queue, indent=4))
    log.logging.Databace("Flush operation completed")
