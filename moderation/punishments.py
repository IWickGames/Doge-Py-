import groups
import config
import discord
from db.databace import ReadKey
from discord.ext import commands
from discord.commands.commands import Option

class Punishments(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.moderation.command()
    async def punishments(
        ctx: commands.Context,
        user: Option(discord.User)
    ):
        """List a users past punishments"""

        db = await ReadKey(f"punishments.{user.id}.{ctx.guild.id}")
        if not db:
            await ctx.respond(":pencil: This user has no record of any punishments", ephemeral=True)
            return

        emb = discord.Embed(
            title=f"{user.name}#{user.discriminator} Punishment History",
            description="\n".join(["`{}` (`{}`) `{}`".format(value["type"], value["issuer"], value["reason"]) for value in db]),
            color=config.embed_color
        )
        await ctx.respond(embed=emb, ephemeral=True)

def setup(bot):
    bot.add_cog(Punishments(bot))