import discord
from discord.ext import commands, tasks
from core.classes import Cog_Extension
import json, asyncio, datetime

class Task(Cog_Extension):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 父類別.初始化屬性

    @tasks.loop(seconds=5.0)
    async def printer(self):
        print(self.index)
        self.index += 1

def setup(bot):
    bot.add_cog(Task(bot))