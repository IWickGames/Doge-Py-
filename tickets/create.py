import groups
import config
import random
import discord
import db.databace
import log.logging
from datetime import datetime
from discord.ext import commands


class Create(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.tickets.command()
    async def create(ctx: commands.Context):
        """Create a new ticket"""
        await log.logging.Info(
            f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})"
            " executed Create in Tickets"
        )

        enabled = await db.databace.ReadKey(
            f"settings.{ctx.guild.id}.enable_tickets"
        )

        if not enabled or enabled != "True":
            await ctx.respond(
                "Ticketing is disable on this guild",
                ephemeral=True
            )
            return

        overwrites = {
            ctx.author: discord.PermissionOverwrite(
                view_channel=True, send_messages=True
            ),
            ctx.guild.me: discord.PermissionOverwrite(
                view_channel=True, send_messages=True
            ),
            ctx.guild.default_role: discord.PermissionOverwrite(
                view_channel=False, send_messages=False
            )
        }

        try:
            channel: discord.TextChannel = await ctx.guild.create_text_channel(
                f"ticket-{random.randint(100000, 999999)}",
                overwrites=overwrites
            )
        except discord.Forbidden:
            await ctx.respond(
                "Could not create new ticket due to permissions",
                ephemeral=True
            )
            return

        emb = discord.Embed(
            description="Support is on its way! Just sit tight."
            "\nIf you want to close this ticket run the `close` "
            "command in this channel",
            color=config.embed_color
        )
        emb.timestamp = datetime.now()

        try:
            await channel.send(
                content=f"{ctx.author.mention} your ticket has been created",
                embed=emb
            )
        except discord.Forbidden:
            await ctx.respond(
                "Failed to send message to ticket channel",
                ephemeral=True
            )
            return

        await ctx.respond(
            ":white_check_mark: Ticket created successfully",
            ephemeral=True
        )


def setup(bot):
    bot.add_cog(Create(bot))
