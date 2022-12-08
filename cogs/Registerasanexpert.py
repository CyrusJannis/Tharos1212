import nextcord
from nextcord.ui import Select, View, Button, Modal
from nextcord.ext import commands
import json
import asyncio
from nextcord.utils import get
import random
import os
import discord.utils
import numpy as np

class Registerasanexpert(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def raae(self, ctx):
        await ctx.message.delete()
        await ctx.send("Experts are the woring force behind Tharos.\nAs an Expert you earn money by providing services to your customers.")
        await ctx.send("If you want to register as an Expert at Tharos please read the following information and rules carefully.")
        await ctx.send(file=nextcord.File(r"./cogs/files/Information_for_Experts.pdf"))
        await ctx.send(file=nextcord.File(r"./cogs/files/Rules_for_Experts.pdf"))
        button1 = Button(label="do the text", style=nextcord.ButtonStyle.green)
        async def button1_callback(interaction):
            numbers = list(np.random.permutation(np.arange(1,3))[:2])
            print(numbers)
            Modal1 = Modal(
                custom_id="modal",
                title="Enter the letter of the right solution",
                timeout=None,            
            )
            with open("C:/Users/Jannis Dietrich/OneDrive/Dokumente/...tharos/cogs/db/eqs_questions.json", "r") as f:
                data = json.load(f)
            print(data)
            print(data[str(numbers[0])])
            que_1 = data[str(numbers[0])]
            input_que_1 = nextcord.ui.TextInput(
                label=f"{que_1['f']}\na: {que_1['a']}\nb: {que_1['b']}\nc: {que_1['c']}\nd: {que_1['d']}",
                min_length=1,
                max_length=1,
                required=True,
                placeholder="",
                style=nextcord.TextInputStyle.short
            )
            que_2 = data[str(numbers[1])]
            input_que_2 = nextcord.ui.TextInput(
                label=f"{que_2['f']}\na: {que_2['a']}\nb: {que_2['b']}\nc: {que_2['c']}\nd: {que_2['d']}",
                min_length=1,
                max_length=1,
                required=True,
                placeholder="",
                style=nextcord.TextInputStyle.short
            )
            Modal1.add_item(input_que_1)
            Modal1.add_item(input_que_2)
            await interaction.response.send_modal(Modal1)
        button1.callback = button1_callback
        view = View(timeout=None)
        view.add_item(button1)
        await ctx.send("Now continue by taking a short test. his includes questions about the information and rules as well as some logic question", view=view)

        

def setup(client):
    client.add_cog(Registerasanexpert(client))
