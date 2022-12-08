import nextcord
from nextcord.ui import Select, View, Button, Modal
from nextcord.ext import commands
import json
import asyncio
from nextcord.utils import get
import random
import os
import discord.utils

client = commands.Bot(command_prefix="!", intents=nextcord.Intents.all())

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_interaction(interaction):
    if interaction.data["custom_id"] == "jocontact":
        #  ---   2. Modal (Application)   ---
        Modal2 = Modal(
            custom_id="modal",
            title="To apply for this job, enter your application",
            timeout=None,            
        )
        application = nextcord.ui.TextInput(label="Your application", min_length=50, max_length=1000, required=True, placeholder=" ~ Application ~ ", style=nextcord.TextInputStyle.paragraph)
        Modal2.add_item(application)
        async def modal2_callback(interaction):
            await interaction.user.send(f"Your application for the job '{interaction.message.embeds[0].title}' has been successfully sent. As son as the customer accepts it, you can chat with him")
        Modal2.callback = modal2_callback
        await interaction.response.send_modal(Modal2)
    elif interaction.data["custom_id"] == "jodelete":
        #               -----                          
        with open("./cogs/db/delete_messages.json", "r") as f:
            data = json.load(f)
        message = interaction.message.id
        buttonyes = Button(label="I am sure I want to delete it", style=nextcord.ButtonStyle.red, custom_id="deleteyes")
        view = View(timeout=None)
        view.add_item(buttonyes)
        with open("./cogs/db/delete_messages.json", "w") as f:
            json.dump(data, f, indent=4)
        button2 = Button(label="<", style=nextcord.ButtonStyle.blurple, custom_id="deleteback", disabled=False)
        view5 = View(timeout=None)
        view5.add_item(buttonyes)
        view5.add_item(button2)
        t = interaction.message.content
        msg99 = await interaction.message.edit(interaction.message.content, view = view5)
        print(interaction.message.content)
        print(interaction)
    elif interaction.data["custom_id"] == "deleteback":
        button3 = Button(label="Delete", style=nextcord.ButtonStyle.green, custom_id="jodelete", disabled=False)
        view6 = View(timeout=None)
        view6.add_item(button3)
        await interaction.message.edit(str(interaction.message.content),  view=view6)
    elif interaction.data["custom_id"] == "deleteyes":
        with open("./cogs/db/delete_messages.json", "r") as f:
            data = json.load(f)
        message = interaction.message.id
        messagetodelete = data[str(message)]["1"]
        channel2 = data[str(message)]["2"]
        channel3 = client.get_channel(channel2)
        msg22 = await channel3.fetch_message(messagetodelete)
        await msg22.delete()
        await interaction.message.delete()
        del data[str(message)]
        with open("./cogs/db/delete_messages.json", "w") as f:
            json.dump(data, f, indent=4)

@client.event
async def on_message(message):
    await client.process_commands(message)



@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def test(ctx):
    choices = ["1", "2"]
    choice1 = random.choice(choices)
    if choice1 == "1":
        a = random.randint(1,10)
        x = f'{a}'
        x2 = a
    else:
        a = random.randint(1,10)
        b = random.randint(1,10)
        x =f'{a}*{b}'
        x2 = a*b
    choice2 = random.choice(choices)
    if choice1 == "1":
        operator = "+"
    else:
        operator = "-"
    choice3 = random.choice(choices)
    if choice3 == "1":
        c = random.randint(1,10)
        y = f'{c}'
        y2 = c
    else:
        c = random.randint(1,10)
        d = random.randint(1,10)
        y = f'{c}*{d}'
        y2 = c*d
    choices2 = ["1", "2", "3", "4", "5"]
    choice4 = random.choice(choices2)
    if choice4 == "3":
        e = random.randint(2,4)
        if operator == "+":
            erg1 = "(" + x + operator + y + f") * {e}"
            erg2 = (x2 + y2) * e
        else:
            erg1 = "(" + x + operator + y + f") * {e}"
            erg2 = (x2 - y2) *e
    else:
        if operator == "+":
            erg1 = x + operator + y
            erg2 = x2 + y2
        else:
            erg1 = x + operator + y
            erg2 = x2 - y2
    await ctx.send("Rechnung:")     
    await ctx.send(f"```{erg1}```")
    await ctx.send("Ergebnis:")   
    await ctx.send(f"```{erg2}```")

@client.command()
async def test2(ctx):
    liste = []
    for i in range(70):
        for member in ctx.guild.members:
            liste.append(member.mention)
        await ctx.send(''.join(liste))



@client.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)


@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, id=1005230473599008898)
    await member.add_roles(role)


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run("MTA0OTQwMzI5ODUwMDgzNzM3Nw.Gsv9zu.AxLpf_FuQh6xCh_Q6Cxz4Vi3rUYQIugj6UoQr0")