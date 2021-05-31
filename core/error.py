from discord import Embed
from discord.ext import commands
import discord_slash.error
from .classes import Cog_Extension
from datetime import datetime
from cogs.voiceroom import RoomLimitReached

class Error(Cog_Extension):
    @commands.Cog.listener()
    async def on_command_error(self, ctx, exception):
        print(f'Error Handler invoked:{type(exception)}')
        print(exception)
        if hasattr(ctx.command, 'on_error'):
            return
        if isinstance(exception, commands.CommandError):
            if isinstance(exception, commands.CommandNotFound):
                embed=Embed(title=f"該指令不存在", color=0xDA5044, timestamp=datetime.now())
                await ctx.send("", embed=embed)
            elif isinstance(exception, commands.MissingRequiredArgument):
                embed=Embed(title=f"缺少必要參數", color=0xDA5044, timestamp=datetime.now())
                await ctx.send("", embed=embed)
            elif isinstance(exception, commands.CheckFailure):
                if isinstance(exception, commands.NotOwner):
                    embed=Embed(title=f"您不是該伺服器的擁有者或管理員", color=0xDA5044, timestamp=datetime.now())
                    await ctx.send("", embed=embed)
                elif isinstance(exception, commands.MissingPermissions):
                    embed=Embed(title=f"您可能不具備必要權限或身分組", color=0xDA5044, timestamp=datetime.now())
                    await ctx.send("", embed=embed)
        elif isinstance(exception, RoomLimitReached):
            embed=Embed(title=f"達到房間上限", color=0xDA5044, timestamp=datetime.now())
            await ctx.send("", embed=embed)
        else:
            await ctx.send(f'發生未定義錯誤，請回報作者。')

    @commands.Cog.listener()
    async def on_slash_command_error(self, ctx, exception):
        print(f'Error Handler invoked:{type(exception)}')
        if isinstance(exception, commands.MissingPermissions):
            embed=Embed(title=f"您可能不具備必要權限或身分組", color=0xDA5044, timestamp=datetime.now())
            await ctx.send("", embed=embed)
        elif isinstance(exception, discord_slash.error.CheckFailure):
            embed=Embed(title=f"Permission Denied, you are not the server owner.", color=0x34CB78, timestamp=datetime.now())
            await ctx.send("", embed=embed)
        else:
            await ctx.send(f'發生未定義錯誤，請回報作者。')
def setup(bot):
    bot.add_cog(Error(bot))