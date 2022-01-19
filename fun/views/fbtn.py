import discord


class FButtons(discord.ui.View):
    def __init__(self):
        super().__init__(
            timeout=60*2
        )

    @discord.ui.button(
        label="Pay respects",
        style=discord.ButtonStyle.blurple,
        emoji="🇫"
    )
    async def fbutton(
        self,
        button: discord.ui.Button,
        interaction: discord.Integration
    ):
        await interaction.response.send_message(
            f"{interaction.user.mention} pays their respects"
        )
