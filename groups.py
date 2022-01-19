import config

tricks = config.bot.create_group(
    name="tricks",
    description="My trick set"
)

moderation = config.bot.create_group(
    name="moderation",
    description="Only authorized people here"
)

utilities = config.bot.create_group(
    name="utilities",
    description="Some usefull things"
)

fun = config.bot.create_group(
    name="fun",
    description="The fun things"
)

leveling = config.bot.create_group(
    name="leveling",
    description="Leveling system"
)

settings = config.bot.create_group(
    name="settings",
    description="Manage user and guild settings"
)

tickets = config.bot.create_group(
    name="tickets",
    description="Ticketing feature for users "
    "to create tickets on your guild"
)

economy = config.bot.create_group(
    name="economy",
    description="Show me the moneeeeeeeey"
)

owner = config.bot.create_group(
    name="owner",
    description="Bot owner commands"
)
