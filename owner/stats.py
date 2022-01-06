import psutil
import config
import groups
import discord
import platform
from discord.ext import commands


async def ScaleBytes(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.owner.command(guild_ids=config.test_servers)
    async def stats(ctx: commands.Context):
        """Display system and usage information"""
        if ctx.author.id not in config.authorized_users:
            await ctx.respond(config.bot_permission_errormsg, ephemeral=True)
            return

        emb = discord.Embed(
            title=f"Bot Statistics "
            f"({config.bot.user.name}#{config.bot.user.discriminator})",
            description=f"Running `{len(config.bot.cogs)}` "
            f"cogs in `{len(config.bot.guilds)}` guilds",
            color=config.embed_color
        )

        uname = platform.uname()
        emb.add_field(
            name="General",
            value=f"""OS         : {uname.system or "Unknown"}"""
            + f"""\nRelease  : {uname.release or "Unknown"}"""
            + f"""\nVersion  : {uname.version or "Unknown"}"""
            + f"""\nMachine  : {uname.machine or "Unknown"}"""
            + f"""\nProcessor: {uname.processor or "Unknown"}"""
        )
        emb.add_field(
            name="CPU",
            value=f"""Usage: {psutil.cpu_percent()}%"""
            + f"""\nTotal Cores: {psutil.cpu_count(logical=True)}"""
            + f"""\nPhysical Cores: {psutil.cpu_count(logical=False)}"""
        )
        svem = psutil.virtual_memory()
        swap = psutil.swap_memory()
        emb.add_field(
            name="Memory",
            value=f"""Total: {await ScaleBytes(svem.total)}"""
            + f"""\nUsed: {await ScaleBytes(svem.used)} / {svem.percent}%"""
            + f"""\nSwap: {await ScaleBytes(swap.total)}"""
            + f"""\nSwap Used: {await ScaleBytes(swap.used)} """
            f"""/ {swap.percent}%"""
        )
        await ctx.respond(embed=emb, ephemeral=True)


def setup(bot):
    bot.add_cog(Stats(bot))
