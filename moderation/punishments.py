import groups
import config
import discord
import log.logging
from discord import Option
from db.databace import ReadKey
from discord.ext import commands


class Punishments(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.moderation.command()
    async def punishments(
        ctx: commands.Context,
        user: Option(
            discord.User,
            description="The user you want to lookup",  # noqa: F722
            required=True
        )
    ):
        """List a users past punishments"""
        await log.logging.Info(
            f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})"
            " executed Punishments in Moderation"
        )

        if user.bot:
            await ctx.respond(config.bot_interaction_boterror, ephemeral=True)
            return

        db = await ReadKey(f"punishments.{user.id}.{ctx.guild.id}")
        if not db:
            await ctx.respond(
                ":pencil: This user has no record of any punishments",
                ephemeral=True
            )
            return

        emb = discord.Embed(
            title=f"{user.name}#{user.discriminator} Punishment History",
            description="\n".join(
                ["`{}` (`{}`) `{}` | Issued `{}`".format(
                    value["type"],
                    value["issuer"],
                    value["reason"],
                    value["timestamp"]) for value in db]
            ),
            color=config.embed_color
        )
        await ctx.respond(embed=emb, ephemeral=True)


def setup(bot):
    bot.add_cog(Punishments(bot))
