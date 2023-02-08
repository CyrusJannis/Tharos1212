import nextcord
from nextcord.ui import Select, View, Button, Modal
from nextcord.ext import commands
import json
import numpy as np

class Pay(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    @commands.has_any_role(1004884670745411595)
    async def pay(self, ctx):
        print("1")
        if ctx.channel.category_id == 1009828164928807012:
            print("2")
            with open("./cogs/db/wasgeht.json", "r") as f:
                data = json.load(f)
            status = data[str(ctx.channel.id)]
            if status == "b":
                data[str(ctx.channel.id)] = "c"
                with open("./cogs/db/wasgeht.json", "w") as f:
                    json.dump(data, f, indent=4)
                button = Button(label="Enter", style=nextcord.ButtonStyle.blurple, custom_id="pay-enter")
                button.callback = None
                view=View(timeout=None)
                view.add_item(button)
                embed = nextcord.Embed(description="Please enter the amount you want the client to pay for your work. For amounts over 40$ you will receive approximately 80% of the amount. For more detailed information visit [Help for Experts](https://discord.com/channels/1004869688251134033/1009849367760482455). Then enter the maximum time the job will take. Please note that after this period the client can ask for their money back. Send !happy before this time passed.", color=0x35C5FF)
                await ctx.channel.send(embed=embed, view=view)
            else:
                if status == "c":
                    embed=nextcord.Embed(description="You can not use !pay twice in a row.", color=0x35C5FF)
                    await ctx.channel.send(embed=embed)
                elif status.startswith("c"):
                    embed=nextcord.Embed(description="Please complete the previous project first.", color=0x35C5FF)
                    await ctx.channel.send(embed=embed)
                elif status.startswith("a"):
                    embed=nextcord.Embed(description="You must first complete the previous project by sending !happy and receiving your payment.", color=0x35C5FF)
                    await ctx.channel.send(embed=embed)
                elif status.startswith("f"):
                    embed=nextcord.Embed(description="The client has asked for their money back because your work time has expired. The execution of !pay is not possible at the moment.", color=0x35C5FF)
                    await ctx.channel.send(embed=embed)
                else: print(1)

def setup(client):
    client.add_cog(Pay(client))