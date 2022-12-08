import nextcord
from nextcord.ui import Select, View, Button, Modal
from nextcord.ext import commands
import json
import asyncio
from nextcord.utils import get
import random
import os
import discord.utils

class Offerwork(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def offerwork(self, ctx):
        await ctx.message.delete()

        #  ---   Select   ---
        select =  Select(
            placeholder = "Select category",
            max_values=1,
            custom_id="postajob",
            options = [
                discord.SelectOption(value="web", label="Website development"),
                discord.SelectOption(value="apps", label="Apps and games"),
                discord.SelectOption(value="oso", label="Other software"),
                discord.SelectOption(value="des", label="Design"),
                discord.SelectOption(value="ma", label="Marketing"),
                discord.SelectOption(value="wr", label="Writing"),
                discord.SelectOption(value="phvi", label="Photography & videography"),
                discord.SelectOption(value="aud", label="Audio"),
                discord.SelectOption(value="other", label="Other services"),
            ]
        )

        #  ---   1.  Modal (Job post)   ---
        Modal1 = Modal(
            custom_id="modal",
            title="To offer your work, fill out the form below.",
            timeout=None,            
        )
        tit = nextcord.ui.TextInput(label="service title", min_length=5, max_length=100, required=True, placeholder="e.g. I will write a book for you", style=nextcord.TextInputStyle.short)
        Modal1.add_item(tit)
        desc = nextcord.ui.TextInput(label="description", min_length=20, max_length=1000, required=True, placeholder="e.g. I can write novels, ...", style=nextcord.TextInputStyle.paragraph)
        Modal1.add_item(desc)
        amount =  nextcord.ui.TextInput(label="approximate price in USD $", min_length=1, max_length=4, required=True, placeholder="e.g. 30", style=nextcord.TextInputStyle.short)
        Modal1.add_item(amount)
        async def modal_callback(interaction):
            what = {
                "web": 1009848187646910476,
                "apps": 1009848261303087115,
                "oso":  1009848445693083690,
                "des": 1009848723435683990,
                "ma": 1009848740628144200,
                "wr": 1009848703110098954,
                "phvi": 1009848510872559807,
                "aud": 1009848466568138862,
                "other": 1009848764925759632
            }
            channel = self.bot.get_channel(what[select.values[0]])
            embed = nextcord.Embed(title=tit.value, description=f"{desc.value}\n\n{amount.value}$", color=nextcord.Color.green())

            #  ---   Contact Button   ---
            button1 = Button(label="Contact", style=nextcord.ButtonStyle.green, custom_id="owcontact")
            view2 = View(timeout=None)
            view2.add_item(button1)
            msg2 = await channel.send(embed=embed, view=view2)
            button2 = Button(label="Delete", style=nextcord.ButtonStyle.green, custom_id="jodelete", disabled=False)
            view3 = View(timeout=None)
            view3.add_item(button2)
            msg = await interaction.user.send(f"You have made the following work offer:\n\n{tit.value}\n{desc.value}\n\nYou can delete this offer at any time.", view=view3)
            with open("C:/Users/Jannis Dietrich/OneDrive/Dokumente/...tharos/cogs/db/delete_messages.json", "r") as f:
                data = json.load(f)
            data[msg.id] = {}
            data[msg.id]["1"] = msg2.id
            data[msg.id]["2"] = channel.id
            data[msg.id]["3"] = "no"
            with open("C:/Users/Jannis Dietrich/OneDrive/Dokumente/...tharos/cogs/db/delete_messages.json", "w") as f:
                json.dump(data, f, indent=4)
        Modal1.callback = modal_callback
        async def select_callback(interaction):
            await interaction.response.send_modal(Modal1)
        select.callback = select_callback
        view = View(timeout=None)
        view.add_item(select)
        await ctx.channel.send("Hi! Do you want to offer a service to clients? Then please select which category the service belongs to. When you submit the service offer, clients can see it and can contact you. Please note that when you click on 'submit', the service offer will be posted and you will not be able to make any more changes.", view=view)

def setup(client):
    client.add_cog(Offerwork(client))
