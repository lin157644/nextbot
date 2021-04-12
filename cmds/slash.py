import os, json
import discord
from discord.ext import commands
from core.classes import Cog_Extension
from dotenv import load_dotenv
from discord_slash import cog_ext
from discord_slash.model import SlashCommandOptionType
from discord_slash.utils.manage_commands import create_option

load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')
BOT_ID=os.getenv('PUBLIC_KEY')
GUILD_ID=os.getenv('GUILD_ID')

class Slash(Cog_Extension):

    guild_ids = [231851662761918464]
    
    @cog_ext.cog_slash(name="ping", description="This is just a test command, nothing more.", guild_ids=guild_ids)
    async def ping(self, ctx):
        await ctx.respond()
        await ctx.send(f"Pong! ({self.bot.latency*1000}ms)")
    
    @cog_ext.cog_slash(name="test",
                description="This is just a test command, nothing more.",
                options=[
                create_option(
                    name="optone",
                    description="This is the first option we have.",
                    option_type=3,
                    required=False
                )
                ],
                guild_ids=guild_ids)
    async def test(self, ctx, optone: str='Nothing'):
        await ctx.respond()
        await ctx.send(content=f"I got you, you said {optone}!")
    
    @cog_ext.cog_slash(name="say",
                description="讓機器人為你說什麼",
                options=[
                create_option(
                    name="context",
                    description="要說的內容",
                    option_type=3,
                    required=True
                )
                ],
                guild_ids=guild_ids)
    async def say(self, ctx, context: str='什麼都沒有'):
        await ctx.respond()
        await ctx.send(content=f" {context}")

def setup(bot):
    bot.add_cog(Slash(bot))