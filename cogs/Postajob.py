import nextcord
from nextcord.ui import Select, View, Button, Modal
from nextcord.ext import commands
import json
import asyncio
import random
import os
import discord.utils

class Postajob(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def postajob(self, ctx):
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
            title="To post the job, fill out the form below.",
            timeout=None,            
        )
        tit = nextcord.ui.TextInput(label="job title", min_length=5, max_length=100, required=True, placeholder="e.g. write a book for me", style=nextcord.TextInputStyle.short)
        Modal1.add_item(tit)
        desc = nextcord.ui.TextInput(label="description", min_length=20, max_length=1000, required=True, placeholder="e.g. the book should be about ...", style=nextcord.TextInputStyle.paragraph)
        Modal1.add_item(desc)
        amount =  nextcord.ui.TextInput(label="approximate payment in USD $", min_length=1, max_length=4, required=True, placeholder="e.g. 30", style=nextcord.TextInputStyle.short)
        Modal1.add_item(amount)
        async def modal_callback(interaction):
            what = {
                "web": 1009849070933782560,
                "apps": 1009849089883635723,
                "oso":  1009849120879558847,
                "des": 1009849133470851072,
                "ma": 1009849146594824294,
                "wr": 1009849160054345792,
                "phvi": 1009849206904717352,
                "aud": 1009849220502650960,
                "other": 1009849240517869568
            }
            channel = self.bot.get_channel(what[select.values[0]])
            embed = nextcord.Embed(title=tit.value, description=f"{desc.value}\n\n{amount.value}$", color=0x0BBAB5)

            #  ---   Contact Button   ---
            button1 = Button(label="Contact", style=nextcord.ButtonStyle.green, custom_id="jocontact")
            button1.callback = None
            view2 = View(timeout=None)
            view2.add_item(button1)
            msg2 = await channel.send(embed=embed, view=view2)
            button2 = Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="jodelete", disabled=False)
            view3 = View(timeout=None)
            view3.add_item(button2)
            msg = await interaction.user.send(f"You have made the following job posting:\n\n{tit.value}\n{desc.value}\n\nYou can delete this job at any time.", view=view3)
            with open("C:/Users/Jannis Dietrich/OneDrive/Dokumente/...tharos/cogs/db/delete_messages.json", "r") as f:
                data = json.load(f)
            data[msg.id] = {}
            data[msg.id]["1"] = msg2.id
            data[msg.id]["2"] = channel.id
            data[msg.id]["3"] = "no"           
            with open("C:/Users/Jannis Dietrich/OneDrive/Dokumente/...tharos/cogs/db/delete_messages.json", "w") as f:
                json.dump(data, f, indent=4)
            with open("C:/Users/Jannis Dietrich/OneDrive/Dokumente/...tharos/cogs/db/wgzn.json", "r") as f:
                data = json.load(f)
            data[str(msg2.id)] = str(interaction.user.id)
            with open("C:/Users/Jannis Dietrich/OneDrive/Dokumente/...tharos/cogs/db/wgzn.json", "w") as f:
                json.dump(data, f, indent=4)
        Modal1.callback = modal_callback
        async def select_callback(interaction):
            await interaction.response.send_modal(Modal1)
        select.callback = select_callback
        view = View(timeout=None)
        view.add_item(select)
        await ctx.channel.send("Hi! Do you want an Expert to do a job for you? Then please select which category the job belongs to. When you submit a job, our Experts will be informed and can contact you. Please note that when you click on 'submit', the job will be posted and you will not be able to make any more changes.", view=view)

def setup(client):
    client.add_cog(Postajob(client))