from os import getenv
from discord.ext import commands
from core.classes import Cog_Extension
from dotenv import load_dotenv
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option, create_choice

class ReactionRole(Cog_Extension):

    GUILD_ID=[int(getenv('GUILD_ID'))]

    @cog_ext.cog_slash(name="reactionroletest", description="This is just a test command, nothing more.", guild_ids=GUILD_ID)
    async def ping(self, ctx):
        await ctx.send(f"Hi")

def setup(bot):
    bot.add_cog(ReactionRole(bot))