import discord


class HelpDropDown(discord.ui.Select):
    def __init__(self, user: discord.Member):
        options = [
            discord.SelectOption(
                label="Tricks",
                description="My trick set"
            ),
            discord.SelectOption(
                label="Moderation",
                description="Only authorized people here"
            ),
            discord.SelectOption(
                label="Utilities",
                description="Some usefull things"
            ),
            discord.SelectOption(
                label="Fun",
                description="The fun things"
            ),
            discord.SelectOption(
                label="Leveling",
                description="Leveling system"
            ),
            discord.SelectOption(
                label="Settings",
                description="Manage user and guild settings"
            ),
            discord.SelectOption(
                label="Tickets",
                description="Ticketing feature for users "
                "to create tickets on your guild"
            ),
            discord.SelectOption(
                label="Economy",
                description="Show me the moneeeeeeeey"
            ),
            discord.SelectOption(
                label="Tasks",
                description="Automated tasks"
            )
        ]

        self.user: discord.Member = user
        super().__init__(
            placeholder="Pick a help section",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        if self.user != interaction.user:
            interaction.response.send_message(
                content="You are not part of this interaction",
                ephemeral=True
            )
            return

        from tricks.help import (
            HelpTrics,
            HelpModeration,
            HelpUtilities,
            HelpFun,
            HelpLeveling,
            HelpSettings,
            HelpTickets,
            HelpEconomy,
            HelpTasks
        )

        match self.values[0]:
            case "Tricks":
                embed = await HelpTrics()

            case "Tasks":
                embed = await HelpTasks()

            case "Moderation":
                embed = await HelpModeration()

            case "Utilities":
                embed = await HelpUtilities()

            case "Fun":
                embed = await HelpFun()

            case "Leveling":
                embed = await HelpLeveling()

            case "Settings":
                embed = await HelpSettings()

            case "Tickets":
                embed = await HelpTickets()

            case "Economy":
                embed = await HelpEconomy()

        await interaction.message.edit(
            embed=embed
        )
