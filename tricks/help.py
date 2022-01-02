import config
import groups
import db.sets
import discord
import log.logging
from discord.ext import commands
from discord.commands.commands import Option


async def HelpTrics():
    emb = discord.Embed(
        title="Tricks",
        color=config.embed_color,
    )
    emb.add_field(
        name="help",
        value="Display help page",
        inline=True
    )
    emb.add_field(
        name="about",
        value="Displays information about the bot",
        inline=True
    )
    emb.add_field(
        name="ping",
        value="Get the bots ping to Discord API",
        inline=True
    )
    emb.add_field(
        name="pet",
        value="Tell me I am doing a good job :yum:",
        inline=True
    )
    emb.add_field(
        name="fetch",
        value="Fetch this bone -> :bone:",
        inline=True
    )
    emb.add_field(
        name="emote {emoji:Emoji}",
        value="Give you information on a emote",
        inline=True
    )
    return emb


async def HelpTasks():
    emb = discord.Embed(
        title="Tasks",
        color=config.embed_color,
    )
    emb.add_field(
        name="OnJoin",
        value="Greets new users in the default channel",
        inline=True
    )
    emb.add_field(
        name="OnLeave",
        value="Says goodbye to users in the default channel",
        inline=True
    )
    return emb


async def HelpModeration():
    emb = discord.Embed(
        title="Moderation",
        color=config.embed_color,
    )
    emb.add_field(
        name="purge {amount:Number<1000}",
        value="Purges amount messages from a channel"
        " (requires ManageMessages permission)",
        inline=True
    )
    emb.add_field(
        name="warn {user:Mention} {reason:String}",
        value="Warns a user for an infraction "
        "(requires KickMemebers permission)",
        inline=True
    )
    emb.add_field(
        name="timeout {user:Mention} {time:Choice} {reason:String}",
        value="Timeouts a user for a certain amount of time "
        "(required ModerateMembers permission)",
        inline=True
    )
    emb.add_field(
        name="kick {user:Mention} {reason:String}",
        value="Kicks a user from the guild (requires KickMembers permission)",
        inline=True
    )
    emb.add_field(
        name="ban {user:Mention} {reason:String}",
        value="Bans a user from the guild (requires BanMembers permission)",
        inline=True
    )
    emb.add_field(
        name="punishments {user:Mention}",
        value="List a users past punishments",
        inline=True
    )
    return emb


async def HelpUtilities():
    emb = discord.Embed(
        title="Utilities",
        color=config.embed_color
    )
    emb.add_field(
        name="afk",
        value="Toggles your afk status",
        inline=True
    )
    emb.add_field(
        name="poll {message:String}",
        value="Creates a poll message and adds reactions",
        inline=True
    )
    emb.add_field(
        name="star {messageID:String}",
        value="Adds the message to the servers star channel "
        "(requires ManageMessages permission)",
        inline=True
    )
    emb.add_field(
        name="userinfo {(Optional) user:Mention}",
        value="Sends information about a user",
        inline=True
    )
    emb.add_field(
        name="hash {algorithm:Choice} {text:String}",
        value="Hashes the given text using the selected algorithm",
        inline=True
    )
    emb.add_field(
        name="base64 {operation:Chocie} {text:String}",
        value="Encodes and decodes a string using base64",
        inline=True
    )
    return emb


async def HelpFun():
    emb = discord.Embed(
        title="Fun",
        color=config.embed_color
    )
    emb.add_field(
        name="draw {code:String}",
        value="Draws the code onto the screen using emotes",
        inline=True
    )
    emb.add_field(
        name="image {query:String}",
        value="Lookup a image online",
        inline=True
    )
    emb.add_field(
        name="coinflip",
        value="Flip a coin",
        inline=True
    )
    emb.add_field(
        name="meme",
        value="Get a dank meme",
        inline=True
    )
    return emb


async def HelpLeveling():
    emb = discord.Embed(
        title="Leveling",
        color=config.embed_color
    )
    emb.add_field(
        name="level",
        value="Display your level and experience",
        inline=True
    )
    return emb


async def HelpSettings():
    emb = discord.Embed(
        title="Settings",
        description="Message settings can have spesial arguments that will be"
        " replaced when sent by the bot\n`{username}`: Username of the user"
        "\n`{discriminator}`: The 4 numbers in a users profile"
        "\n`{id}`: The ID of the user"
        "\n`{mention}`: Mentions the user"
        "\n`{created}`: The date the user was created"
        "\nYou can also put `None` in as the message to disable said setting",
        color=config.embed_color
    )
    emb.add_field(
        name="set",
        value="Set a configuration value for both user and guild",
        inline=True
    )
    emb.add_field(
        name="User Settings",
        value=", ".join(db.sets.user_settings) or "None"
    )
    emb.add_field(
        name="Guild Settings",
        value=", ".join(db.sets.guild_settings) or "None"
    )
    return emb


async def HelpTickets():
    emb = discord.Embed(
        title="Tickets",
        description="Create and close tickets in your guild easially\n"
        "(Note you must enable this feature in the settings before use)",
        color=config.embed_color
    )
    emb.add_field(
        name="create",
        value="Creates a new ticket",
        inline=True
    )
    emb.add_field(
        name="close",
        value="Closes a ticket channel when executed",
        inline=True
    )
    return emb


async def HelpEconomy():
    emb = discord.Embed(
        title="Economy",
        description="Show me the moneeeeeeeeeeey",
        color=config.embed_color
    )
    emb.add_field(
        name="credit {amount:Int}",
        value="Converts leveling experience into economy",
        inline=True
    )
    emb.add_field(
        name="balance {user:User}",
        value="Get the balance of a user",
        inline=True
    )
    emb.add_field(
        name="pay {user:User} {amount:Int}",
        value="Pays a user",
        inline=True
    )
    return emb


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @groups.tricks.command()
    async def help(
        ctx: commands.Context,
        category: Option(
            str,
            description="Select a category to get help on",  # noqa: F722
            choices=[
                "fun",          # noqa: F821
                "leveling",     # noqa: F821
                "economy",      # noqa: F821
                "moderation",   # noqa: F821
                "settings",     # noqa: F821
                "tasks",        # noqa: F821
                "tricks",       # noqa: F821
                "utilities",    # noqa: F821
            ],
            default=""  # noqa: F722
        )
    ):
        """Display a help message"""
        await log.logging.Info(
            f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})"
            " executed Help in Tricks"
        )

        match category:
            case "tricks":
                await ctx.respond(embed=await HelpTrics())
                return

            case "tasks":
                await ctx.respond(embed=await HelpTasks())
                return

            case "moderation":
                await ctx.respond(embed=await HelpModeration())
                return

            case "utilities":
                await ctx.respond(embed=await HelpUtilities())
                return

            case "fun":
                await ctx.respond(embed=await HelpFun())
                return

            case "leveling":
                await ctx.respond(embed=await HelpLeveling())
                return

            case "settings":
                await ctx.respond(embed=await HelpSettings())
                return

            case "tickets":
                await ctx.respond(embed=await HelpTickets())
                return

            case "economy":
                await ctx.respond(embed=await HelpEconomy())
                return

            case "":
                pass

            case _:
                await ctx.respond(
                    f":anger: Grrrr, invalid category `{category}`",
                    ephemeral=True
                )
                return

        hEmb = discord.Embed(
            title=f"Hello {ctx.author.name} :wave:",
            color=config.embed_color,
            description=":guide_dog: I am your friendly Discord server "
            f"doge to help you out on `{ctx.guild.name}` :smiley:\n"
            + "( I also like being pet :wink: )\n\n"

            + ":mega: Wolf! Here are the different "
            "catigories of things I can do,\n"
            + "`tricks`, `tasks`, `moderation`, `utilities`, `fun`\n\n"
            + "You can select one by doing `/help catigoryName`\n"
            + "Example: `/help tricks`"
        )
        hEmb.set_footer(text="Created with ❤️ by IWick Development")
        await ctx.respond(embed=hEmb)


def setup(bot):
    bot.add_cog(Help(bot))
