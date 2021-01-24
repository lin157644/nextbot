from discord.ext import  tasks
from core.classes import Cog_Extension

class Task(Cog_Extension):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.index = 0
        # self.printer.start()
        # 父類別.初始化屬性
    
    def cog_unload(self):
        self.printer.cancel()
    
    @tasks.loop(seconds=5.0)
    async def printer(self):
        print(self.index)
        self.index += 1

    @printer.before_loop
    async def before_printer(self):
        print('printer waiting...')
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(Task(bot))