import discord
from discord.ext import commands
from .classes import Cog_Extension

class Error(Cog_Extension):
    @commands.Cog.listener()
    async def on_command_error(self, ctx, exception):
        if hasattr(ctx.command, 'on_error'):
            return
        if isinstance(exception, discord.ext.commands.CommandError):
            await ctx.send(f'指令不存在:\n{exception}')
        elif isinstance(exception, discord.ext.commands.MissingRequiredArgument):
            await ctx.send(f'缺少必要參數:\n{exception}')
        else:
            await ctx.send(f'發生未定一錯誤，請回報作者。')

def setup(bot):
    bot.add_cog(Error(bot))