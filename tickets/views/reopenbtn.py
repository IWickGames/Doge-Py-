import discord


class ReopenBtn(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(
        label="🔓 Reopen Ticket",
        style=discord.ButtonStyle.red
    )
    async def close(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        tnum = interaction.channel.name.split("-")[-1]

        try:
            await interaction.channel.edit(
                name=f"ticket-{tnum}"
            )
        except discord.Forbidden:
            await interaction.response.send_message(
                ":closed_lock_with_key: Bot does not"
                " have permissions to edit this channel",
                ephemeral=True
            )
            return

        await interaction.response.send_message(
            "🔓 Ticket reopend by "
            f"`{interaction.user.name}#{interaction.user.discriminator}`"
        )

        self.stop()
