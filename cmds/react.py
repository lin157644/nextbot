import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random

#1.5後的Discord.py使用intent以減低listen負擔
intents = discord.Intents.all()

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    
    @commands.command()
    async def randompic(self, ctx):
        #兩個反斜線轉譯 避免意外
        random_pic = random.choice(jdata['Dir_random_pic'])
        pic = discord.File(random_pic)
        await ctx.send(file = pic)
    
    @commands.command()
    async def urlpic(self, ctx, url):
        # await ctx.send(jdata['urlpic'])
        await ctx.message.delete()
        await ctx.send(url)

def setup(bot):
    bot.add_cog(React(bot))