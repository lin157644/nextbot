import discord
from discord.ext import commands
import json

#Discord.py 1.5 新增Intents selective receive event
#https://discordpy.readthedocs.io/en/latest/intents.html#member-intent
intents = discord.Intents.all()


#('File name', 'mode', encoding)
with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

#Build Entity
bot = commands.Bot(command_prefix='#',intents = intents)

@bot.event
#協程 def
async def on_ready():
    print("\\OuO Bot is online/")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['Bot_channel']))
    #協成函數Coroutine 需使用Await
    await channel.send(f'{member} Joined!')
    print(f'{member} Joined!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['Bot_channel']))
    await channel.send(f'{member} Leaved...')
    print(f"{member} Leaved...")


@bot.command()
#ctx = context (上下文)
#A:(上文) (user, id, user current server, user channel)
#latency is float in second
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')

#Inside Json, the arrengement of data is 字典的型態
#every data have a corrspond key
bot.run(jdata['TOKEN'])
