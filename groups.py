from discord.commands import SlashCommandGroup

tricks = SlashCommandGroup(
    "tricks", "My trick set"
)

tasks = SlashCommandGroup(
    "tasks", "Some automated tasks"
)

moderation = SlashCommandGroup(
    "moderation", "Only autherised people here"
)

utilities = SlashCommandGroup(
    "utilities", "Some usefull things"
)

fun = SlashCommandGroup(
    "fun", "The fun things"
)