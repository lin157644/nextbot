import json
from core.classes import Cog_Extension
from core.database import Database
from os import getenv
from discord.ext import commands
from dotenv import load_dotenv
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
GUILD_ID=jdata['guild_id']

class Setting(Cog_Extension):
    def __init__(self, bot):
        super().__init__(bot)
        db_user = getenv('DB_USER')
        db_passwd = getenv('DB_PASSWORD')
        self.db = Database(db_user, db_passwd)
        self.db.cur.execute("USE nextbot;")
    
    @commands.command(name="setbotchannel")
    async def _setbotchannel(self, ctx, msg):
        if ctx.author == ctx.guild.owner:
            channel = await commands.TextChannelConverter().convert(ctx, msg)
            self.db.cur.execute("INSERT INTO guild_setting (guild_id, bot_channel) VALUE (?, ?);", (channel.guild.id , channel.id))
            await ctx.send(content=f"Botchannel set to {channel.mention}", mention_author=True)

    @commands.command()
    async def setautorole(self, ctx):
        await ctx.send(123)
    
    @commands.command()
    async def setroomlimit(self, ctx):
        await ctx.send(123)

def setup(bot):
    bot.add_cog(Setting(bot))
