import discord
from discord.ext import commands
import json
from core.classes import Cog_Extension
import os
from dotenv import load_dotenv
from cmds.slash import Slash


from discord_slash import cog_ext
from discord_slash import SlashCommand
from discord_slash import SlashContext
from discord_slash import http
from discord_slash import utils

# Hide my token
load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')

# Discord.py 1.5 新增Intents selective receive event
# https://discordpy.readthedocs.io/en/latest/intents.html#member-intent
intents = discord.Intents.all()

# ('File name', 'mode', encoding)
with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

# Build Entity
bot = commands.Bot(command_prefix='$',intents = intents)

# Bot Ready
# 不用加()
@bot.event
# 協程 def
async def on_ready():
    channel = bot.get_channel(int(jdata['Bot_channel']))
    await channel.send('OuO Bot is now Online')
    print("\\OuO Bot is online/")

#:Load Cog
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    print(f'Extension {extension} Loaded!')
    await ctx.send(f'Extension {extension} Loaded!')

#Unload Cog
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    print(f'Extension {extension} Unloaded!')
    await ctx.send(f'Extension {extension} Unloaded!')

#Relaod Cog
@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    print(f'Extension {extension} Reloaded!')
    await ctx.send(f'Extension {extension} Reloaded!')


#Load default extension
for filename in os.listdir('./cmds'):
    if filename.endswith('.py') and not(filename.startswith('__')):
        #filename[:-3] 省略後三字 (.py)
        bot.load_extension(f'cmds.{filename[:-3]}')
        print(f'Imported {filename}!')


#Inside Json, the arrengement of data is 字典的型態
#every data have a corrspond key
#__name__如果該檔案是被引用，其值會是模組名稱；
#但若該檔案是(透過命令列)直接執行，其值會是 __main__
#所以好像不必要???
if __name__ == "__main__":
    bot.run(TOKEN)


