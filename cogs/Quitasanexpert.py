import nextcord
from nextcord.ui import View, Button
from nextcord.ext import commands

class Quitasanexpert(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def qaae(self, ctx):
        await ctx.message.delete()
        button1 = Button(label="Quit", style=nextcord.ButtonStyle.green, custom_id="qaae")
        button1.callback = None
        view = View(timeout=None)
        view.add_item(button1)
        embed = nextcord.Embed(description="Do you want to give up your status as an Expert at THAROS? Then please finish all your orders from customers and close the chats.", color=0x0BBAB5)
        await ctx.send(embed=embed, view=view)

        

def setup(client):
    client.add_cog(Quitasanexpert(client))