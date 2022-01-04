def MakeGroups(bot):
    global tricks
    global moderation
    global utilities
    global fun
    global leveling
    global settings
    global tickets
    global economy

    tricks = bot.create_group(
        name="tricks",
        description="My trick set"
    )

    moderation = bot.create_group(
        name="moderation",
        description="Only authorized people here"
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

    tickets = bot.create_group(
        name="tickets",
        description="Ticketing feature for users "
        "to create tickets on your guild"
    )

    economy = bot.create_group(
        name="economy",
        description="Show me the moneeeeeeeey"
    )
