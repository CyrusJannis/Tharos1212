import nextcord
from nextcord.ui import Select, View, Button, Modal
from nextcord.ext import commands
import json
import numpy as np
import discord.utils

class Registerasanexpert(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def raae(self, ctx):
        await ctx.message.delete()
        embed1 = nextcord.Embed(description="Experts are the working force behind THAROS.\nAs an Expert you earn money by providing services to your clients.\nPlease note that it is necessary for Experts to have a PayPal account.", color=0x35C5FF)
        await ctx.send(embed=embed1)
        embed2 = nextcord.Embed(description="If you want to register as an Expert at THAROS please read the following information and rules carefully.", color=0x35C5FF)
        await ctx.send(embed=embed2)
        await ctx.send(file=nextcord.File(r"./cogs/files/Information_for_Experts.pdf"))
        await ctx.send(file=nextcord.File(r"./cogs/files/Rules_for_Experts.pdf"))
        button1 = Button(label="continue", style=nextcord.ButtonStyle.blurple, custom_id="raae1k9")
        button1.callback = None
        view = View(timeout=None)
        view.add_item(button1)
        embed = nextcord.Embed(description="Now continue by taking a short test. The first part tests your logical thinking skills.", color=0x35C5FF)
        await ctx.send(embed=embed, view=view)

        

def setup(client):
    client.add_cog(Registerasanexpert(client))