import nextcord
from nextcord.ui import Select, View, Button, Modal
from nextcord.ext import commands
from nextcord import Interaction, SlashOption, ChannelType
from nextcord.abc import GuildChannel
import json
import asyncio
import random
import os
import discord.utils
import numpy as np

class Pay(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    @commands.has_any_role(1004884670745411595)
    async def pay(self, ctx):
        print("1")
        if ctx.channel.category_id == 1009828164928807012:
            print("2")
            with open("./cogs/db/wasgeht.json", "r") as f:
                data = json.load(f)
            status = data[str(ctx.channel.id)]
            if status == "b":
                data[str(ctx.channel.id)] = "c"
                with open("./cogs/db/wasgeht.json", "w") as f:
                    json.dump(data, f, indent=4)
                button = Button(label="Enter", style=nextcord.ButtonStyle.blurple, custom_id="pay-enter")
                button.callback = None
                view=View(timeout=None)
                view.add_item(button)
                embed = nextcord.Embed(description="Please enter the amount you want the customer to pay for your work. You will receive ((())) of the amount. Then enter the maximum time the job will take. Please note that after this period the customer can ask for their money back. Send /happy before this time passed. PORNO LALALALALALALLA", color=0x0BBAB5)
                await ctx.channel.send(embed=embed, view=view)
            else:
                if status == "c":
                    embed=nextcord.Embed(description="You cannot use /pay twice in a row.", color=0x0BBAB5)
                    await ctx.channel.send(embed=embed)
                elif status.startswith("c"):
                    embed=nextcord.Embed(description="Please complete the previous project first.", color=0x0BBAB5)
                    await ctx.channel.send(embed=embed)
                elif status.startswith("a"):
                    embed=nextcord.Embed(description="You must first complete the previous project by sending /happy and receiving your payment.", color=0x0BBAB5)
                    await ctx.channel.send(embed=embed)#
                else: print(1)
        else:
            interaction.response.defer()


def setup(client):
    client.add_cog(Pay(client))