from discord import Embed
from discord.ext import commands 
from discord_components import Button, ButtonStyle
from core.classes import Cog_Extension

from asyncio import TimeoutError, sleep
from random import choice

class Component(Cog_Extension):

    def __init__(self, bot):
        super().__init__(bot)
        self.session_message ={}
    @commands.command()
    async def button(self, ctx):
        await ctx.send(
            "Look! A cool Button",
            components = [
                Button(label = "WOW button!")
            ]
        )

        interaction = await self.bot.wait_for("button_click", check = lambda i: i.component.label.startswith("WOW"))
        await interaction.respond(content = "Button clicked!")

    @commands.command()
    async def cointoss(self, ctx):
        embed = Embed(
            color=0xF5F5F5,
            title=f"{ctx.author.name} 擲出了一枚硬幣",
            description="在下方選擇正面或反面",
        )

        menu_components = [
            [
                Button(style=ButtonStyle.grey, label="正面"),
                Button(style=ButtonStyle.grey, label="反面"),
            ]
        ]
        heads_components = [
            [
                Button(style=ButtonStyle.green, label="正面", disabled=True),
                Button(style=ButtonStyle.red, label="反面", disabled=True),
            ],
            Button(style=ButtonStyle.blue, label="再玩一次?", disabled=False),
        ]
        tails_components = [
            [
                Button(style=ButtonStyle.red, label="正面", disabled=True),
                Button(style=ButtonStyle.green, label="反面", disabled=True),
            ],
            Button(style=ButtonStyle.blue, label="再玩一次?", disabled=False),
        ]

        if ctx.author.id in self.session_message:
            msg = self.session_message[ctx.author.id]
            await msg.edit(embed=embed, components=menu_components)
        else:
            msg = await ctx.send(embed=embed, components=menu_components)
            self.session_message[ctx.author.id] = msg

        def check(res):
            return res.user.id == ctx.author.id and res.channel.id == ctx.channel.id

        try:
            res = await self.bot.wait_for("button_click", check=check, timeout=20)
        except TimeoutError:
            await msg.edit(
                embed=Embed(color=0xED564E, title="時間到!", description="沒有人做出反應"),
                components=[
                    Button(style=ButtonStyle.red, label="時間到! 遊戲結束!", disabled=True)
                ],
            )
            return

        await res.respond(
            type=7,
            embed=Embed(
                color=0xF5F5F5,
                title=f"{ctx.author.name} 擲出了一枚硬幣",
                description=f"你選 **{res.component.label.lower()}**!",
            ),
            components=menu_components,
        )

        game_choice = choice(["正面", "反面"])
        await sleep(2)

        if game_choice == res.component.label:
            embed = Embed(
                color=0x65DD65,
                title=f" {ctx.author.name} 擲出了一枚硬幣",
                description=f"你選 **{res.component.label.lower()}**!\n\n> **恭喜!**",
            )
        else:
            embed = Embed(
                color=0xED564E,
                title=f"{ctx.author.name} 擲出了一枚硬幣",
                description=f"你選 **{res.component.label.lower()}**!\n\n> 你輸了!",
            )

        await msg.edit(
            embed=embed,
            components=tails_components if game_choice == "反面" else heads_components,
        )

        try:
            res = await self.bot.wait_for("button_click", check=check, timeout=20)
        except TimeoutError:
            await msg.delete()
            del self.session_message[ctx.author.id]
            return

        await res.respond(type=6)
        if res.component.label == "再玩一次?":
            self.session_message[ctx.author.id] = msg
            await self.cointoss(ctx)

def setup(bot):
    bot.add_cog(Component(bot))