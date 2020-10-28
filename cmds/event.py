import discord
from discord.ext import commands
from core.classes import Cog_Extension  
import json
import random

with open('C:\\Users\\linxs\\Desktop\\Project\\Github\\ouobot\\setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()

class Event(Cog_Extension):
    
    #@裝飾器
    #User Joined
    #Cog關鍵字觸發
    #bot.event 的Cog版
    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(int(jdata['Bot_channel']))
        #協成函數Coroutine 需使用Await
        await channel.send(f'{member} 加入了!')
        print(f'{member} Joined!')

    #User Leaved
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(int(jdata['Bot_channel']))
        await channel.send(f'{member} Leaved...')
        print(f"{member} Leaved...")
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == 'hi':
            await msg.channel.send(random.choice(jdata['hi']))
        
        #end'string'with
        if msg.content.endswith('hello'):
            await msg.channel.send(random.choice(jdata['hi']))

def setup(bot):
    bot.add_cog(Event(bot))