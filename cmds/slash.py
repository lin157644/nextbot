import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash import SlashCommand
from discord_slash import SlashContext
from discord_slash import http
from discord_slash import utils



load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')
BOT_ID=os.getenv('PUBLIC_KEY')
GUILD_ID=os.getenv('GUILD_ID')

class Slash(commands.Cog):
    def __init__(self, bot):
        if not hasattr(bot, "slash"):
            # Creates new SlashCommand instance to bot if bot doesn't have.
            bot.slash = SlashCommand(bot, override_type=True)
        self.bot = bot
        self.bot.slash.get_cog_commands(self)
        

    def cog_unload(self):
        self.bot.slash.remove_cog_commands(self)

    # resp = {
    #     "name": "test",
    #     "description": "Send a embed test",
    #     "options": []
    # }
    # await http.SlashCommandRequest.post(resp, bot_id, interaction_id, token, initial=True)
    # await http.SlashCommandRequest.post(resp, bot_id, interaction_id, token, initial=True)
    # @commands.command()
    # async def add_slash(self, ctx):
    #     await 

    @commands.command()
    async def add_commands(self, ctx):
        await utils.manage_commands.add_slash_command(770143431770505238, TOKEN, GUILD_ID, 'say', 'say')
        await utils.manage_commands.add_slash_command(770143431770505238, TOKEN, GUILD_ID, 'test', 'test')
        await utils.manage_commands.add_slash_command(770143431770505238, TOKEN, GUILD_ID, 'ping', 'ping')


    @cog_ext.cog_slash(name="test")
    async def _test(self, ctx: SlashContext):
        embed = discord.Embed(title="embed test")
        await ctx.send(content="test", embeds=[embed])
    
    @cog_ext.cog_slash(name="ping")
    async def ping(self, ctx: SlashContext):
        await ctx.send(content="Pong!")
    
    # @cog_ext.cog_slash(name="say")
    # async def say(self, ctx: SlashContext):
    #     #這裡傳入的msg是str
    #     await ctx.message.delete()
    #     await SlashContext.send(contents='say')
    
    @cog_ext.cog_slash(name="say")
    async def say(self, ctx: SlashContext, text: str):
        await ctx.send(content=text)


def setup(bot):
    bot.add_cog(Slash(bot))