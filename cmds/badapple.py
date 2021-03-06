import discord
from PIL import Image
import time
from discord.ext import commands
from core.classes import Cog_Extension
import asyncio
import datetime

class Badapple(Cog_Extension):

    ASCII_CHARS = [".",".",":","-","=","+","*","#","%", "@", "@"]

    def pix2chars(self, image):
        pixels = image.getdata()
        characters = "".join([self.ASCII_CHARS[pixel//25] for pixel in pixels])
        return characters

    def generate_frame(self, image):
        new_width=70
        new_image_data = self.pix2chars(image.convert('L'))

        total_pixels = len(new_image_data)
        # print(total_pixels)

        ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, total_pixels, new_width)])

        return "`"+ascii_image+"`"
    
    async def art(self, ctx):
        if(True):
            i = 0
            isCreated = False
            msg = None
            while i < 7000:
                # i = i + 4
                i = i + 24
                img = Image.open(f"files/newframes/frame{i}.png")
                frame = self.generate_frame(img)
                if frame != None:
                    if isCreated == False:
                        # temp=datetime.datetime.now()
                        msg = await ctx.send(frame)
                        # print(datetime.datetime.now()-temp)
                        isCreated = True
                        await asyncio.sleep(0.76)
                    else:
                        # temp=datetime.datetime.now()
                        await msg.edit(content=frame)
                        # print(datetime.datetime.now()-temp)
                        await asyncio.sleep(0.76)
                        
            await ctx.send("That's all")
            
    @commands.command()
    async def badapple(self, ctx):

        voiceChannel = ctx.author.voice.channel     
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice == None:
            await voiceChannel.connect()
            voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        
        voice.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('files/bad_apple.mp3')))
        await self.art(ctx)
        
        

def setup(bot):
    bot.add_cog(Badapple(bot))