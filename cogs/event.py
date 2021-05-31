import json
from os import getenv
from discord.ext import commands
from core.database import Database
from core.classes import Cog_Extension  

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):

    def __init__(self, bot):
        super().__init__(bot)
        db_user = getenv('DB_USER')
        db_passwd = getenv('DB_PASSWORD')
        self.db = Database(db_user, db_passwd)
        self.db.cur.execute("USE nextbot;")

    #bot.event w/ Cog
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['Bot_channel']))
        self.db.cur.execute("SELECT auto_role FROM guild_setting WHERE guild_id=?;",(member.guild.id,))
        for auto_role in self.db.cur:
            await member.add_roles(auto_role)
        await channel.send(f'{member} 加入了!')
        print(f'{member} Joined!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['Bot_channel']))
        await channel.send(f'{member} 離開了...')
        print(f"{member} 離開了...")
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        #可以拿去json儲存
        # keyword = ['apple','pen','abc']
        #這裡傳入的msg是一個class
        # if msg.content == 'hi' and msg.author != self.bot.user:
        #     await msg.channel.send(random.choice(jdata['hi']))
        
        #end'string'with
        # if msg.content.endswith('hello'):
        #     await msg.channel.send(random.choice(jdata['hi']))

        #Keyword
        # if msg.content in keyword and msg.author != self.bot.user:
        #     await msg.channel.send('Keyword!')
        
        keyword_kick = ['滿', '漢', '大', '餐', '珍', '味', '牛', '肉', '麵']

        if msg.author != self.bot.user :
            if msg.author.id not in jdata['ignore']:
              keyword_count = 0
              for i in keyword_kick:
                if msg.content.find(i) != -1:
                  keyword_count += 1
              if keyword_count >= 9:
                await msg.author.kick(reason='滿漢大餐珍味牛肉麵')
                await msg.channel.send(f'已處決『{msg.author.name}』')
    
    @commands.Cog.listener()
    async def on_message_delete(self, msg):
        if msg.author != self.bot.user:
            #await msg.channel.send(f"刪除訊息:{msg.content}")
            print(f"刪除訊息:{msg.content}")
    
    @commands.Cog.listener()
    async def on_slash_command(self, ctx):
        pass

def setup(bot):
    bot.add_cog(Event(bot))