import discord
from discord.ext import  tasks, commands
from core.classes import Cog_Extension
import json, asyncio, datetime

class Task(Cog_Extension):

    def __init__(self, *args, **kwargs):
        # 父類別.初始化屬性
        super().__init__(*args, **kwargs)
        # self.index = 0
        # self.printer.start()
    
        async def interval():
            print('Waiting...')
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(770144271503720469)
            print('good')
            while not self.bot.is_closed():
                # await self.channel.send(f'現在時間:{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
                await asyncio.sleep(10)
        
        self.bg_task = self.bot.loop.create_task(interval())
    
    @commands.command()
    async def set_channel(self, ctx, ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set Channel: {self.channel.mention}')

    #內建task
    # def cog_unload(self):
    #     self.printer.cancel()
    
    # @tasks.loop(seconds=5.0)
    # async def printer(self):
    #     print(self.index)
    #     self.index += 1

    # @printer.before_loop
    # async def before_printer(self):
    #     print('Waiting...')
    #     await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(Task(bot))