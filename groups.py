def MakeGroups(bot):
    global tricks
    global tasks
    global moderation
    global utilities
    global fun
    global leveling
    global settings

    tricks = bot.create_group(
        name="tricks",
        description="My trick set"
    )

    """
    tasks = bot.create_group(
        name="tasks",
        description="Some automated tasks"
    )
    """

    moderation = bot.create_group(
        name="moderation",
        description="Only autherised people here"
    )

    utilities = bot.create_group(
        name="utilities",
        description="Some usefull things"
    )

    fun = bot.create_group(
        name="fun",
        description="The fun things"
    )

    leveling = bot.create_group(
        name="leveling",
        description="Leveling system"
    )

    settings = bot.create_group(
        name="settings",
        description="Manage user and guild settings"
    )
