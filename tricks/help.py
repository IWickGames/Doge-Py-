import config
import groups
import discord
from discord.ext import commands
from discord.commands.commands import Option

async def HelpTrics():
    emb = discord.Embed(
        title="Tricks",
        color=config.embed_color,
    )
    emb.add_field(name="help", value="Display help page", inline=True)
    emb.add_field(name="ping", value="Get the bots ping to Discord API", inline=True)
    emb.add_field(name="pet", value="Tell me I am doing a good job :yum:", inline=True)
    emb.add_field(name="fetch", value="Fetch this bone -> :bone:", inline=True)
    emb.add_field(name="emote {emoji:Emoji}", value="Give you information on a emote", inline=True)
    return emb

async def HelpTasks():
    emb = discord.Embed(
        title="Tasks",
        color=config.embed_color,
    )
    emb.add_field(name="OnJoin", value="Greets new users in the default channel", inline=True)
    emb.add_field(name="OnLeave", value="Says goodbye to users in the default channel", inline=True)
    return emb

async def HelpModeration():
    emb = discord.Embed(
        title="Moderation",
        color=config.embed_color,
    )
    emb.add_field(name="purge {amount:Number<1000}", value="Purges amount messages from a channel (requires ManageMessages permission)", inline=True);
    emb.add_field(name="warn {user:Mention} {reason:String}", value="Warns a user for an infraction (requires KickMemebers permission)", inline=True);
    emb.add_field(name="ban {user:Mention} {reason:String}", value="Bans a user from the guild (requires BanMembers permission)", inline=True);
    emb.add_field(name="kick {user:Mention} {reason:String}", value="Kicks a user from the guild (requires KickMembers permission)", inline=True);
    return emb

async def HelpUtilities():
    emb = discord.Embed(
        title="Utilities",
        color=config.embed_color
    )
    emb.add_field(name="afk", value="Toggles your afk status", inline=True);
    emb.add_field(name="poll {message:String}", value="Creates a poll message and adds reactions", inline=True);
    emb.add_field(name="star {messageID:String}", value="Adds the message to the servers star channel (requires ManageMessages permission)", inline=True);
    emb.add_field(name="userinfo {(Optional) user:Mention}", value="Sends information about a user", inline=True);
    return emb

async def HelpFun():
    emb = discord.Embed(
        title="Fun",
        color=config.embed_color
    )
    emb.add_field(name="coinflip", value="Flip a coin", inline=True)
    emb.add_field(name="meme", value="Get a dank meme", inline=True)
    return emb

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @groups.tricks.command()
    async def help(
        ctx: commands.Context, 
        category: Option(
            str, 
            description="Select a category to get help on", 
            choices=["tricks", "tasks", "moderation", "utilities", "fun"]
        )
    ):
        """Display a help message"""
        
        if category:
            if category == "tricks":
                await ctx.respond(embed=await HelpTrics())
                return
            
            if category == "tasks":
                await ctx.respond(embed=await HelpTasks())
                return

            if category == "moderation":
                await ctx.respond(embed=await HelpModeration())
                return
            
            if category == "utilities":
                await ctx.respond(embed=await HelpUtilities())
                return
            
            if category == "fun":
                await ctx.respond(embed=await HelpFun())
                return
            
            await ctx.respond(f":anger: Grrrr, invalid category `{category}`", ephemeral=True)
            return

        hEmb = discord.Embed(
            title=f"Hello {ctx.author.name} :wave:",
            color=config.embed_color,
            description=f":guide_dog: I am your friendly Discord server doge to help you out on `{ctx.guild.name}` :smiley:\n"
                + "( I also like being pet :wink: )\n\n"

                + ":mega: Wolf! Here are the different catigories of things I can do,\n"
                + "`tricks`, `tasks`, `moderation`, `utilities`, `fun`\n\n"
                + "You can select one by doing `/help catigoryName`\n"
                + "Example: `/help tricks`"
        )
        hEmb.set_footer(text="Created with ❤️ by IWick Development")
        await ctx.respond(embed=hEmb)

def setup(bot):
    bot.add_cog(Help(bot))