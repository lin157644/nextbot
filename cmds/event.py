import discord
from discord.ext import commands
from core.classes import Cog_Extension  
import json
import random

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()

class Event(Cog_Extension):
    
    #@裝飾器
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
        #可以拿去json儲存
        keyword = ['apple','pen','abc']
        #self.bot.user
        #這裡傳入的msg是一個class
        if msg.content == 'hi' and msg.author != self.bot.user:
            await msg.channel.send(random.choice(jdata['hi']))
        
        #end'string'with
        if msg.content.endswith('hello'):
            await msg.channel.send(random.choice(jdata['hi']))

        #Keyword
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send('Keyword!')
        
        keyword_kick = ['滿', '漢', '大', '餐', '珍', '味', '牛', '肉', '麵']

        if msg.author != self.bot.user :
            if msg.author.id not in jdata['ignore'] :
              keyword_count = 0
              for i in keyword_kick:
                if msg.content.find(i) != -1:
                  keyword_count += 1
              if keyword_count >= 9:
                await msg.author.kick(reason='滿漢大餐珍味牛肉麵')
                await msg.channel.send(f'已處決『{msg.author.name}』')


def setup(bot):
    bot.add_cog(Event(bot))