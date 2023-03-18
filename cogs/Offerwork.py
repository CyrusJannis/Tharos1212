import nextcord
from nextcord.ui import Select, View, Button, Modal
from nextcord.ext import commands
import json
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
            custom_id="postajob222",
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
        select.callback = None
        view = View(timeout=None)
        view.add_item(select)
        embed = nextcord.Embed(description="Hi! Do you want to offer a service to clients? Then please select which category the service belongs to. When you submit the service offer, clients can see it and can contact you. Please note that when you click on 'submit', the service offer will be posted and you will not be able to make any more changes.", color=0x35C5FF)
        await ctx.channel.send(embed=embed, view=view)

def setup(client):
    client.add_cog(Offerwork(client))