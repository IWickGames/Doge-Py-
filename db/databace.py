# flake8: noqa: E501
import os
import json
import config
import asyncio
import log.logging
import db.asyncfiles as asyncfiles

global cache
cache = {}

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
    global cache
    global updated
    cache[key] = value
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
    global cache
    if cache.get(key):
        return cache.get(key)
    else:
        j = await asyncfiles.read(config.databace_file)
        if not j:
            return None
        return json.loads(j).get(key)

async def RemoveKey(key):
    """
    Deletes a key from the databace

    Arguments:
        key: The access key to delete
    
    Returns:
        None / Nothing
    """
    global cache
    global updated
    if key in cache.keys():
        cache.pop(key)
    
    j = await asyncfiles.read(config.databace_file)
    if not j:
        return None
    j = json.loads(j)
    if key in j.keys():
        j.pop(key)
        await asyncfiles.write(
            config.databace_file,
            json.dumps(j).encode("utf-8")
        )


async def databace_flush():
    """
    The databace flush task

    /!\ IF YOU ARE CALLING THIS ANYWHERE YOU ARE USING IT WRONG /!\ 
    """
    global cache
    global updated
    while True:
        await asyncio.sleep(30)
        if updated:
            await Flush()
            log.logging.Databace("Flushed databace successfully")


async def Flush():
    global cache
    global updated

    if updated:
        j = await asyncfiles.read(
            config.databace_file
        )
        if j:
            j = json.loads(j)
            for key in cache.keys():
                j[key] = cache[key]
        else:
            j = cache

        await asyncfiles.write(
            config.databace_file,
            json.dumps(j).encode("utf-8")
        )
        cache = {}
        updated = False
        log.logging.Databace("Flushed databace successfully")
