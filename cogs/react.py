import json
import random
import discord
from discord.ext import commands
from core.classes import Cog_Extension

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