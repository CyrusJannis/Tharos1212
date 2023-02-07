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
        button1 = Button(label="Accept", style=nextcord.ButtonStyle.green)
        async def button1_callback(interaction):
            role=discord.utils.get(interaction.guild.roles, id=1005230473599008898)
            await interaction.user.add_roles(role)
            await interaction.response.send_message("You now have the role of a client", ephemeral=True)
            with open("./cogs/db/Clientquitting.json", "r") as f:
                data = json.load(f)
            data[str(interaction.user.id)] = 0
            with open("./cogs/db/Clientquitting.json", "w") as f:
                json.dump(data, f, indent=4)
        button1.callback = button1_callback
        view = View(timeout=None)
        view.add_item(button1)
        embed = nextcord.Embed(description="Please click this button to accept the terms and conditions for clients and Experts.", color=0x35C5FF)
        await ctx.send(embed=embed, file=nextcord.File(r"./cogs/files/Terms and Conditions for Clients and Experts.pdf"), view=view)


def setup(client):
    client.add_cog(Verify(client))