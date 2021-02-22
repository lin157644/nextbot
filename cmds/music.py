import discord
from discord.ext import commands
from core.classes import Cog_Extension
import os
import youtube_dl

class Music(Cog_Extension):    

    @commands.command()
    async def play(self, ctx, url:str):
        songExist = os.path.isfile("song.mp3")
        try:
            if songExist:
                os.remove('song.mp3')
        except PermissionError:
            await ctx.send('請等待當前撥放歌曲結束')
            return

        
        voiceChannel = ctx.author.voice.channel     
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice == None:
            await voiceChannel.connect()
            voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
            
        

        ydl_opts = {
            'format' : 'bestaudio/best',
            'postprocessors':[{
                'key' : 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : '192'
            }]
        }
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        for file in os.listdir("./"):
            if file.endswith('.mp3'):
                os.rename(file, 'song.mp3')
        
        voice.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('song.mp3')))

    
    @commands.command()
    async def fuckoff(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            await voice.disconnect()
        else:
            await ctx.send("未連接至語音頻道")
    
    @commands.command()
    async def pause(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send("")
    
    @commands.command()
    async def resume(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            await voice.resume()
        else:
            await ctx.send("")
    
    @commands.command()
    async def stop(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        voice.stop()
    
    @commands.command()
    async def volume(self, ctx, vol:float):
        volume = max(0.0, min(1.0, vol / 100))

        source = ctx.guild.voice_client.source

        # if not isinstance(source, discord.PCMVolumeTransformer):
        #     return await ctx.send("This source doesn't support adjusting volume or "
        #                           "the interface to do so is not exposed.")

        source.volume = volume

        await ctx.send(f"音量:{volume * 100:.2f}%")

def setup(bot):
    bot.add_cog(Music(bot))
