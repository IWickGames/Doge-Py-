import discord


class AboutBtn(discord.ui.View):
    def __init__(self):
        super().__init__()

        self.add_item(
            discord.ui.Button(
                label="Invite Bot",
                url="https://discord.com/api/oauth2/authorize?client_id=869706426975670312&permissions=8&scope=applications.commands%20bot"  # noqa: E501
            )
        )

        self.add_item(
            discord.ui.Button(
                label="GitHub",
                url="https://github.com/IWickGames/Doge-Py-"
            )
        )
