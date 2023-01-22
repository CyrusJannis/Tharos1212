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

class Happy(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    @commands.has_any_role(1004884670745411595)
    async def happy(self, ctx):
        if ctx.channel.category_id == 1009828164928807012:
            with open("./cogs/db/wasgeht.json", "r") as f:
                data = json.load(f)
            status = data[str(ctx.channel.id)]
            if status.startswith("a"):
                button = Button(label="Confirm", style=nextcord.ButtonStyle.blurple, custom_id="happy-confirm")
                button2 = Button(label="Cancel", style=nextcord.ButtonStyle.blurple, custom_id="happy-cancel")
                button.callback = None
                button2.callback = None
                view=View(timeout=None)
                view.add_item(button)
                view.add_item(button2)
                embed = nextcord.Embed(description="Please confirm that the customer has received your work.", color=0x0BBAB5)
                await ctx.channel.send(embed=embed, view=view)
            else:
                if status == "b":
                    embed=nextcord.Embed(description="You have not started a new project yet", color=0x0BBAB5)
                    await ctx.channel.send(embed=embed)
                elif status == "c":
                    embed=nextcord.Embed(description="The previous project is not yet completed.", color=0x0BBAB5)
                    await ctx.channel.send(embed=embed)
                elif status.startswith("c"):
                    embed=nextcord.Embed(description="You can't use !happy twice in a row.", color=0x0BBAB5)
                    await ctx.channel.send(embed=embed)
                else: print(1)


def setup(client):
    client.add_cog(Happy(client))