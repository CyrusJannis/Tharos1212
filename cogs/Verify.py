import nextcord
from nextcord.ui import Select, View, Button, Modal
from nextcord.ext import commands
import json
import asyncio
import random
import os
import discord.utils

class Verify(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def verify(self, ctx):
        button1 = Button(label="verify", style=nextcord.ButtonStyle.green)
        async def button1_callback(interaction):
            role=discord.utils.get(interaction.guild.roles, id=1005230473599008898)
            await interaction.user.add_roles(role)
            await interaction.response.send_message("You are now verified", ephemeral=True)
        button1.callback = button1_callback
        view = View(timeout=None)
        view.add_item(button1)
        await ctx.send("Click on the button below to verify yourself", view=view)


def setup(client):
    client.add_cog(Verify(client))