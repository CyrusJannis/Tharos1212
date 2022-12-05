import discord
from discord.ui import Select, View, Button
from discord.ext import commands
import json
import asyncio
from discord.utils import get
import random
import os
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    await client.process_commands(message)
    channels = [1005120172685795409, 1005226324283117639]
    if message.channel.id in channels:
        await asyncio.sleep(300)
        await message.delete()


@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, id=1005230473599008898)
    await member.add_roles(role)

client.load_extension("cogs.verifyyourself")
async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
load()
#test
client.run("MTA0OTQwMzI5ODUwMDgzNzM3Nw.Gfpw4n.zf5wnDb4yCNLNMKX2hBEVvai1-RNunl5B_WAMA")