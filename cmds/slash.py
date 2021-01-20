import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash import SlashCommand
from discord_slash import SlashContext
from discord_slash import http
from discord_slash import utils


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
    @commands.command()
    async def add_slash(self, ctx):
        bot_id = 770143431770505238
        bot_token = 'NzcwMTQzNDMxNzcwNTA1MjM4.X5ZR9g.9C_R182qfRJ3FMLUhWrOoS458ms'
        guild_id = 231851662761918464
        print("1")
        await utils.manage_commands.add_slash_command(bot_id, bot_token, guild_id, 'test', 'test')
        print("2")
    
    @cog_ext.cog_slash(name="test")
    async def _test(self, ctx: SlashContext):
        embed = discord.Embed(title="embed test")
        await ctx.send(content="test", embeds=[embed])


def setup(bot):
    bot.add_cog(Slash(bot))