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
        button1 = Button(label="do the logic test", style=nextcord.ButtonStyle.green)
        async def button1_callback(interaction):
            numbers = list(np.random.permutation(np.arange(1,17))[:5])
            print(numbers)
            Modal1 = Modal(
                custom_id="modal",
                title="Enter the letter of the right solution",
                timeout=None,            
            )
            with open("C:/Users/Jannis Dietrich/OneDrive/Dokumente/...tharos/cogs/db/eqs_questions.json", "r") as f:
                data = json.load(f)
            print(data)
            print(data[f"{numbers[0]}l"])
            que_1 = data[f"{numbers[0]}l"]
            input_que_1 = nextcord.ui.TextInput(
                label=f"{que_1['f']}",
                min_length=1,
                max_length=5,
                required=True,
                placeholder="",
                style=nextcord.TextInputStyle.short
            )
            que_2 = data[f"{numbers[1]}l"]
            input_que_2 = nextcord.ui.TextInput(
                label=f"{que_2['f']}",
                min_length=1,
                max_length=5,
                required=True,
                placeholder="",
                style=nextcord.TextInputStyle.short
            )
            que_3 = data[f"{numbers[2]}l"]
            input_que_3 = nextcord.ui.TextInput(
                label=f"{que_3['f']}",
                min_length=1,
                max_length=5,
                required=True,
                placeholder="",
                style=nextcord.TextInputStyle.short
            )
            que_4 = data[f"{numbers[3]}l"]
            input_que_4 = nextcord.ui.TextInput(
                label=f"{que_4['f']}",
                min_length=1,
                max_length=5,
                required=True,
                placeholder="",
                style=nextcord.TextInputStyle.short
            )
            que_5 = data[f"{numbers[4]}l"]
            input_que_5 = nextcord.ui.TextInput(
                label=f"{que_5['f']}",
                min_length=1,
                max_length=5,
                required=True,
                placeholder="",
                style=nextcord.TextInputStyle.short
            )
            Modal1.add_item(input_que_1)
            Modal1.add_item(input_que_2)
            Modal1.add_item(input_que_3)
            Modal1.add_item(input_que_4)
            Modal1.add_item(input_que_5)
            async def modal_callback(interaction):
                button2 = Button(label="do the 2nd part", style=nextcord.ButtonStyle.green)
                async def button2_callback(interaction):
                    global score
                    score = 0
                    ans1 = input_que_1.value
                    right1 = que_1["right"]
                    ans2 = input_que_2.value
                    right2 = que_2["right"]
                    ans3 = input_que_3.value
                    right3 = que_3["right"]
                    ans4 = input_que_4.value
                    right4 = que_4["right"]
                    ans5 = input_que_5.value
                    right5 = que_5["right"]
                    if ans1 == right1:
                        score += 1
                    if ans2 == right2:
                        score += 1
                    if ans3 == right3:
                        score += 1
                    if ans4 == right4:
                        score += 1
                    if ans5 == right5:
                        score += 1
                    print(score)
                    numbers = list(np.random.permutation(np.arange(1,17))[:5])
                    Modal2 = Modal(
                        custom_id="modal",
                        title="Enter the letter of the right solution",
                        timeout=None, 
                    )
                    que_6 = data[f"{numbers[0]}r"]
                    input_que_6 = nextcord.ui.TextInput(
                        label=f"{que_6['f']}",
                        min_length=1,
                        max_length=5,
                        required=True,
                        placeholder="",
                        style=nextcord.TextInputStyle.short
                    )
                    que_7 = data[f"{numbers[1]}r"]
                    input_que_7 = nextcord.ui.TextInput(
                        label=f"{que_7['f']}",
                        min_length=1,
                        max_length=5,
                        required=True,
                        placeholder="",
                        style=nextcord.TextInputStyle.short
                    )
                    que_8 = data[f"{numbers[2]}r"]
                    input_que_8 = nextcord.ui.TextInput(
                        label=f"{que_8['f']}",
                        min_length=1,
                        max_length=5,
                        required=True,
                        placeholder="",
                        style=nextcord.TextInputStyle.short
                    )
                    que_9 = data[f"{numbers[3]}r"]
                    input_que_9 = nextcord.ui.TextInput(
                        label=f"{que_9['f']}",
                        min_length=1,
                        max_length=5,
                        required=True,
                        placeholder="",
                        style=nextcord.TextInputStyle.short
                    )
                    que_10 = data[f"{numbers[4]}r"]
                    input_que_10 = nextcord.ui.TextInput(
                        label=f"{que_10['f']}",
                        min_length=1,
                        max_length=5,
                        required=True,
                        placeholder="",
                        style=nextcord.TextInputStyle.short
                    )
                    Modal2.add_item(input_que_6)
                    Modal2.add_item(input_que_7)
                    Modal2.add_item(input_que_8)
                    Modal2.add_item(input_que_9)
                    Modal2.add_item(input_que_10)
                    async def modal2_callback(interaction):
                        global score
                        ans6 = input_que_6.value
                        right6 = que_6["right"]
                        ans7 = input_que_7.value
                        right7 = que_7["right"]
                        ans8 = input_que_8.value
                        right8 = que_8["right"]
                        ans9 = input_que_9.value
                        right9 = que_9["right"]
                        ans10 = input_que_10.value
                        right10 = que_10["right"]
                        if ans6 == right6:
                            score += 1
                        if ans7 == right7:
                            score += 1
                        if ans8 == right8:
                            score += 1
                        if ans9 == right9:
                            score += 1
                        if ans10 == right10:
                            score += 1
                        print(score)
                        if score >= 7:
                            button3 = Button(label="do the text", style=nextcord.ButtonStyle.green)
                            async def button3_callback(interaction):
                                Modal3 = Modal(
                                    custom_id="modal",
                                    title="Enter your infos",
                                    timeout=None, 
                                )
                                first_name = nextcord.ui.TextInput(
                                    label="first name",
                                    min_length=1,
                                    max_length=30,
                                    required=True,
                                    placeholder="",
                                    style=nextcord.TextInputStyle.short
                                )
                                last_name = nextcord.ui.TextInput(
                                    label="last name",
                                    min_length=1,
                                    max_length=30,
                                    required=True,
                                    placeholder="",
                                    style=nextcord.TextInputStyle.short
                                )
                                dob = nextcord.ui.TextInput(
                                    label="date of birth",
                                    min_length=1,
                                    max_length=10,
                                    required=True,
                                    placeholder="",
                                    style=nextcord.TextInputStyle.short
                                )
                                Modal3.add_item(first_name)
                                Modal3.add_item(last_name)
                                Modal3.add_item(dob)
                                async def modal3_callback(interaction):
                                    with open("./cogs/db/experts.json", "r") as f:
                                        data = json.load(f)
                                    data[int(interaction.user.id)] = {
                                        "firstname": first_name.value,
                                        "lastname": last_name.value,
                                        "dateofbirth": dob.value,
                                        "jobsdone": 0,
                                        "reviews": 0,
                                        "starrating": "noreviews"
                                    }
                                    with open("./cogs/db/experts.json", "w") as f:
                                        json.dump(data, f, indent=4)
                                    message = await interaction.user.send("To complete the Expert registration,, send a photo of the front of your identity card. Please note that for successful registration the following message must include the photo. The verification may take a few days.")
                                    button5 = Button(label="jump there", style=nextcord.ButtonStyle.link, url=f"https://discordapp.com/channels/guild_id/channel_id/{message.id}")
                                    view5 = View(timeout=None)
                                    view5.add_item(button5)
                                    await interaction.response.send_message("Take a look at your DMs", view=view5, ephemeral=True)
                                    image = await self.bot.wait_for("message", check=lambda i: i.author == interaction.user and i.channel.type is nextcord.ChannelType.private)
                                    print(image.content)
                                    verify_channel = self.bot.get_channel(1051246577425055844)
                                    await verify_channel.send(image.content)
                                    await verify_channel.send(first_name.value)
                                    await verify_channel.send(last_name.value)
                                    await verify_channel.send(dob.value)
                                    btn6 = Button(label="accept", style=nextcord.ButtonStyle.green, custom_id="expertaccept")
                                    btn7 = Button(label="deny", style=nextcord.ButtonStyle.red, custom_id="expertdeny")
                                    view6 = View(timeout=None)
                                    view6.add_item(btn6)
                                    view6.add_item(btn7)
                                    await verify_channel.send(interaction.user.id, view=view6)
                                Modal3.callback = modal3_callback
                                await interaction.response.send_modal(Modal3)
                            button3.callback = button3_callback
                            view3  = View(timeout=None)
                            view3.add_item(button3)
                            await interaction.response.send_message(f"Everything worked. You're now an Expert with the score of {score}", view=view3, ephemeral=True)
                        else:
                            await interaction.response.send_message(f"Your score's too low.", ephemeral=True)
                    Modal2.callback = modal2_callback
                    await interaction.response.send_modal(Modal2)
                button2.callback = button2_callback
                view2 = View(timeout=None)
                view2.add_item(button2)
                await interaction.response.send_message(f"Congrats! You finished the first par successfully. Finish the second part to see if you are qualified for being an Expert at Tharos", view=view2, ephemeral=True)
            Modal1.callback = modal_callback
            await interaction.response.send_modal(Modal1)
        button1.callback = button1_callback
        view = View(timeout=None)
        view.add_item(button1)
        await ctx.send("Now continue by taking two short tests. They include questions about the information and rules as well as some logic questions", view=view)

        

def setup(client):
    client.add_cog(Registerasanexpert(client))