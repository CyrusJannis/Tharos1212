import nextcord
from nextcord.ui import Select, View, Button, Modal
from nextcord.ext import commands
import json
import asyncio
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
        await ctx.send("Experts are the working force behind Tharos.\nAs an Expert you earn money by providing services to your customers.")
        await ctx.send("If you want to register as an Expert at Tharos please read the following information and rules carefully.")
        await ctx.send(file=nextcord.File(r"./cogs/files/Information_for_Experts.pdf"))
        await ctx.send(file=nextcord.File(r"./cogs/files/Rules_for_Experts.pdf"))
        button1 = Button(label="do the test", style=nextcord.ButtonStyle.green)
        async def button1_callback(interaction):
            numbers = list(np.random.permutation(np.arange(1,17))[:5])
            Modal1 = Modal(
                custom_id="modal",
                title="Please fill out the test",
                timeout=60,            
            )
            with open("C:/Users/Jannis Dietrich/OneDrive/Dokumente/...tharos/cogs/db/eqs_questions.json", "r") as f:
                data = json.load(f)
            que_1 = data[f"{numbers[0]}l"]
            input_que_1 = nextcord.ui.TextInput(
                label=f"{que_1['f']}",
                min_length=1,
                max_length=50,
                required=True,
                placeholder="",
                style=nextcord.TextInputStyle.short
            )
            que_2 = data[f"{numbers[1]}l"]
            input_que_2 = nextcord.ui.TextInput(
                label=f"{que_2['f']}",
                min_length=1,
                max_length=50,
                required=True,
                placeholder="",
                style=nextcord.TextInputStyle.short
            )
            que_3 = data[f"{numbers[2]}l"]
            input_que_3 = nextcord.ui.TextInput(
                label=f"{que_3['f']}",
                min_length=1,
                max_length=50,
                required=True,
                placeholder="",
                style=nextcord.TextInputStyle.short
            )
            que_4 = data[f"{numbers[3]}l"]
            input_que_4 = nextcord.ui.TextInput(
                label=f"{que_4['f']}",
                min_length=1,
                max_length=50,
                required=True,
                placeholder="",
                style=nextcord.TextInputStyle.short
            )
            que_5 = data[f"{numbers[4]}l"]
            input_que_5 = nextcord.ui.TextInput(
                label=f"{que_5['f']}",
                min_length=1,
                max_length=50,
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
                button2 = Button(label="continue the test", style=nextcord.ButtonStyle.green)
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
                    if ans1 in right1:
                        score += 1
                    if ans2 in right2:
                        score += 1
                    if ans3 in right3:
                        score += 1
                    if ans4 in right4:
                        score += 1
                    if ans5 in right5:
                        score += 1
                    numbers = list(np.random.permutation(np.arange(1,6))[:5])
                    Modal2 = Modal(
                        custom_id="modal",
                        title="Please fill out the test",
                        timeout=60, 
                    )
                    que_6 = data[f"{numbers[0]}r"]
                    input_que_6 = nextcord.ui.TextInput(
                        label=f"{que_6['f']}",
                        min_length=1,
                        max_length=50,
                        required=True,
                        placeholder="",
                        style=nextcord.TextInputStyle.short
                    )
                    que_7 = data[f"{numbers[1]}r"]
                    input_que_7 = nextcord.ui.TextInput(
                        label=f"{que_7['f']}",
                        min_length=1,
                        max_length=50,
                        required=True,
                        placeholder="",
                        style=nextcord.TextInputStyle.short
                    )
                    que_8 = data[f"{numbers[2]}r"]
                    input_que_8 = nextcord.ui.TextInput(
                        label=f"{que_8['f']}",
                        min_length=1,
                        max_length=50,
                        required=True,
                        placeholder="",
                        style=nextcord.TextInputStyle.short
                    )
                    que_9 = data[f"{numbers[3]}r"]
                    input_que_9 = nextcord.ui.TextInput(
                        label=f"{que_9['f']}",
                        min_length=1,
                        max_length=50,
                        required=True,
                        placeholder="",
                        style=nextcord.TextInputStyle.short
                    )
                    que_10 = data[f"{numbers[4]}r"]
                    input_que_10 = nextcord.ui.TextInput(
                        label=f"{que_10['f']}",
                        min_length=1,
                        max_length=50,
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
                        if ans6 in right6:
                            score += 1
                        if ans7 in right7:
                            score += 1
                        if ans8 in right8:
                            score += 1
                        if ans9 in right9:
                            score += 1
                        if ans10 in right10:
                            score += 1
                        if score >= 0:
                            button3 = Button(label="continue", style=nextcord.ButtonStyle.green)
                            async def button3_callback(interaction):
                                Modal3 = Modal(
                                    custom_id="modal",
                                    title="Please enter your personal data.",
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
                                    min_length=8,
                                    max_length=10,
                                    required=True,
                                    placeholder="",
                                    style=nextcord.TextInputStyle.short
                                )
                                Modal3.add_item(first_name)
                                Modal3.add_item(last_name)
                                Modal3.add_item(dob)
                                async def modal3_callback(interaction):
                                    with open("C:/Users/Jannis Dietrich/OneDrive/Dokumente/...tharos/cogs/db/experts.json", "r") as f:
                                        data = json.load(f)
                                    data[str(interaction.user.id)] = {}
                                    data[str(interaction.user.id)]["firstname"] = first_name.value
                                    data[str(interaction.user.id)]["lastname"] = last_name.value
                                    data[str(interaction.user.id)]["dateofbirth"] = dob.value
                                    data[str(interaction.user.id)]["jobsdone"] = 0
                                    data[str(interaction.user.id)]["reviews"] = 0
                                    data[str(interaction.user.id)]["starrating"] = "no reviews"
                                    with open("./cogs/db/experts.json", "w") as f:
                                        json.dump(data, f, indent=4)
                                    message = await interaction.user.send("To complete the Expert registration, send a photo of the front of your identity card. Please note that for successful registration the following message must include the photo. The verification may take a few hours.")
                                    await interaction.response.send_message("The last step of your registration takes place in your DMs", ephemeral=True)
                                    image = await self.bot.wait_for("message", check=lambda i: i.author == interaction.user and i.channel.type is nextcord.ChannelType.private)
                                    verify_channel = self.bot.get_channel(1051246577425055844)
                                    btn6 = Button(label="accept", style=nextcord.ButtonStyle.green, custom_id="expertaccept")
                                    btn7 = Button(label="deny", style=nextcord.ButtonStyle.red, custom_id="expertdeny")
                                    view6 = View(timeout=None)
                                    view6.add_item(btn6)
                                    view6.add_item(btn7)
                                    try:
                                        photo =  image.attachments[0]
                                        await verify_channel.send(f"{photo}\n{first_name.value}\n{last_name.value}\n{dob.value}\n\n {interaction.user.id}", view=view6)
                                    except:
                                        await verify_channel.send(f"{image.content}\n{first_name.value}\n{last_name.value}\n{dob.value}\n\n {interaction.user.id}", view=view6)
                                    await interaction.user.send("The photo has been successfully forwarded. Once this has been verified, you are an Expert.")
                                Modal3.callback = modal3_callback
                                await interaction.response.send_modal(Modal3)
                            button3.callback = button3_callback
                            view3  = View(timeout=None)
                            view3.add_item(button3)
                            await interaction.response.send_message("Congratulations! You have successfully passed the test. In the next step we need you to enter your personal data.", view=view3, ephemeral=True)
                        else:
                            await interaction.response.send_message("Unfortunately, you did not pass the test. Try again at any time.", ephemeral=True)
                    Modal2.callback = modal2_callback
                    await interaction.response.send_modal(Modal2)
                button2.callback = button2_callback
                view2 = View(timeout=None)
                view2.add_item(button2)
                await interaction.response.send_message("Now take the second part of the test. This tests your knowledge of the rules and information for Experts.", view=view2, ephemeral=True)
            Modal1.callback = modal_callback
            await interaction.response.send_modal(Modal1)
        button1.callback = button1_callback
        view = View(timeout=None)
        view.add_item(button1)
        await ctx.send("Now continue by taking a short test. The first part tests your logical thinking skills.", view=view)

        

def setup(client):
    client.add_cog(Registerasanexpert(client))