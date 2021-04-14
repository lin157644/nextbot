import discord, datetime
import os
import youtube_dl
from core.classes import Cog_Extension
from dotenv import load_dotenv
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option, create_choice

load_dotenv()
GUILD_ID=os.getenv('GUILD_ID')

class Music(Cog_Extension):    

    guild_ids = [231851662761918464]

    @cog_ext.cog_slash(name="play",
        description="Play Music",
        options=[
        create_option(
            name="platform",
            description="請輸入要播放的平台",
            option_type=4,
            required=True,
            choices=[
                create_choice(
                    name='Youtube',
                    value=1
                ),
                create_choice(
                    name='Pornhub',
                    value=1
                )
            ]
        ),
        create_option(
            name="url",
            description="請輸入要播放的網址",
            option_type=3,
            required=True
        )
        ],
        guild_ids=guild_ids)
    async def play(self, ctx, url:str):

        await ctx.defer()

        # Connect to Current voice channel
        voiceChannel = ctx.author.voice.channel     
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice == None:
            await voiceChannel.connect()
            voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

        # Downlaod info
        ydl_opts = {'format' : 'bestaudio/best', 'get-thumbnail' : 'true'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            URL = info['formats'][0]['url']
        
        # Respond
        try:
            embed=discord.Embed(title="正在播放: \n"+info['title'], url="", color=0x575757, timestamp=datetime.datetime.now())
            embed.set_thumbnail(url=info['thumbnails'][-1]['url'])
            await ctx.send("", embed=embed)
        except:
            await ctx.send("Fail QQ")

        # Play
        voice.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS)))
    
    @cog_ext.cog_slash(name="disconnect", description="讓機器人從當前的語音頻道中退出", guild_ids=guild_ids)
    async def disconnect(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            await voice.disconnect()
        else:
            await ctx.send("未連接至語音頻道")
    
    @cog_ext.cog_slash(name="pause", description="暫停當前播放的音樂", guild_ids=guild_ids)
    async def pause(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send("")
    
    @cog_ext.cog_slash(name="resume", description="繼續播放當前的音樂", guild_ids=guild_ids)
    async def resume(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            await voice.resume()
        else:
            await ctx.send("")
    
    @cog_ext.cog_slash(name="stop", description="中止所有播放(請小心使用)", guild_ids=guild_ids)
    async def stop(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        voice.stop()
    
    @cog_ext.cog_slash(name="volume", description="改變音量(0~100)", options=[create_option(name="percentage", description="請輸入音量0~100", option_type=4, required=True)], guild_ids=guild_ids)
    async def volume(self, ctx, percentage:float):
        volume = max(0.0, min(1.0, percentage / 100))

        source = ctx.guild.voice_client.source
        source.volume = volume

        await ctx.send(f"音量:{percentage:.2f}%")

def setup(bot):
    bot.add_cog(Music(bot))
