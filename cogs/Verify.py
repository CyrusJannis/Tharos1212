import nextcord
from nextcord.ui import Select, View, Button
from nextcord.ext import commands
import discord.utils
import json

class Verify(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def verify(self, ctx):
        await ctx.message.delete()
        button1 = Button(label="Accept", style=nextcord.ButtonStyle.green, custom_id="verify999")
        button1.callback = None
        view = View(timeout=None)
        view.add_item(button1)
        embed = nextcord.Embed(description="Please click this button to accept the terms and conditions for clients and Experts.", color=0x35C5FF)
        await ctx.send(embed=embed, file=nextcord.File(r"./cogs/files/Terms and Conditions for Clients and Experts.pdf"), view=view)


def setup(client):
    client.add_cog(Verify(client))