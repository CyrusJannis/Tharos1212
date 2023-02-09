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
        button1 = Button(label="Quit", style=nextcord.ButtonStyle.red, custom_id="qaae")
        button1.callback = None
        view = View(timeout=None)
        view.add_item(button1)
        embed = nextcord.Embed(description="Do you want to give up your status as an Expert at THAROS? Then please finish all your orders from clients and close the chats. If you press this button your Account will be cancelled and your data will be deleted from the database. There is no way to restore your Account.", color=0x35C5FF)
        await ctx.send(embed=embed, view=view)

        

def setup(client):
    client.add_cog(Quitasanexpert(client))