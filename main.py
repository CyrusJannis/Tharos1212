import nextcord
from nextcord.ui import Select, View, Button, Modal
from nextcord.ext import commands, tasks
import json
import numpy as np
import paypalrestsdk
from paypalrestsdk import Payout, ResourceNotFound
paypalrestsdk.configure({
    "mode": "sandbox", # sandbox or live
    "client_id": "AfCGzxhK6rwCh9ZtSZcrwP39gYtxu6yhcOMmLvzF0fO-4ZzKnC9ROKAh78aB6ked4WnqM2ca8-Px0EXM",
    "client_secret": "EI4JV6BL5pt_L-HuEk0e0qzwGzHidNGosxpC0fXIUJNsPKGYNmpq2-kr_UoQbkT20T3SX76sVV-Whrj6"
})
import asyncio
import random
import os
import discord.utils
import deepl
import time
from datetime import datetime
client = commands.Bot(command_prefix="!", intents=nextcord.Intents.all())

@client.event
async def on_ready():
    print("Bot ready")
    while True:
        with open("./cogs/db/3Tage.json", "r") as f:
            data = json.load(f)
        print(list(data.values()))
        for i in range(len(list(data.values()))):
            x = data.values()
            d2 = list(x)
            date = d2[int(i)]
            timevar = date
            split = timevar.split(" ")
            left = split[0].split("-")
            right = split[1].split(":")
            year = left[0]
            month = left[1]
            day = left[2]
            hours = right[0]
            minutes = right[1]
            sec = right[-1].split(".")
            seconds = sec[0]
            then = datetime(int(year), int(month), int(day), int(hours), int(minutes), int(seconds))
            now = datetime.now()
            difference = now - then
            duration2 = difference.total_seconds()
            total_days = duration2 / 86400
            print(total_days)
            if total_days >= 3:
                print("GA3")
                ecid2 = data.keys()
                ecid = list(ecid2)[int(i)]
                echannelid = ecid
                echannel = client.get_channel(int(echannelid))
                with open("./cogs/db/chats.json", "r") as f:
                    data = json.load(f)
                ccid = data[str(echannel.id)]["connect"]
                cchannel = client.get_channel(int(ccid))
                with open( "./cogs/db/3Tagedeletenachrichten.json", "r") as f:
                    data = json.load(f)
                x = data[str(cchannel.id)]
                for i in x:
                    print(i)
                    print(cchannel.id)
                    try:
                        msg = await cchannel.fetch_message(int(i))
                        print(1)
                        await msg.delete()
                        print(2)
                    except Exception as e:
                        print(e)
                with open( "./cogs/db/3Tagedeletenachrichten.json", "r") as f:
                    data = json.load(f)
                del data[str(cchannel.id)]
                with open( "./cogs/db/3Tagedeletenachrichten.json", "w") as f:
                    json.dump(data, f, indent=4)
                with open("./cogs/db/chats.json", "r") as f:
                    data = json.load(f)
                expertid = data[str(echannelid)]["owner"]
                clientchannelid = data[str(echannelid)]["connect"]
                clientid = data[str(clientchannelid)]["owner"]
                with open("./cogs/db/3Tage.json", "r") as f:
                    data = json.load(f)
                try:
                    del data[str(echannelid)]
                except:
                    print("Key error")
                with open("./cogs/db/3Tage.json", "w") as f:
                    json.dump(data, f, indent=4)
                with open("./cogs/db/experts.json", "r") as f:
                    data = json.load(f)
                j = data[str(expertid)]["jobsdone"]
                data[str(expertid)]["jobsdone"] = j+1
                with open("./cogs/db/experts.json", "w") as f:
                    json.dump(data, f, indent=4)
                with open("./cogs/db/expertzahlinfos.json", "r") as f:
                    data = json.load(f)
                email = data[str(echannelid)]["email"]
                with open("./cogs/db/payments.json", "r") as f:
                    data = json.load(f)
                n = data[str(echannelid)]["n"]
                amount = data[str(echannelid)][str(n)]["amount"]
                new_amount = 90*(int(amount) * 92 / 100 - 0.49) / 100
                amount2 = round(new_amount, 2)
                pchannel = client.get_channel(1086726507814195340)
                embed = nextcord.Embed(title="ZAHLUNG", description=f"Receiver: {email}\nAmount: {amount2}\n\n\n{echannelid}")
                worked = Button(label="Payment Worked", style=nextcord.ButtonStyle.green, custom_id="payment_worked")
                didnt_work = Button(label="Payment Failed", style=nextcord.ButtonStyle.red, custom_id="payment_didnt_work")
                view = View()
                view.add_item(worked)
                view.add_item(didnt_work)
                await pchannel.send(embed=embed, view=view)
        await asyncio.sleep(3600)




@client.event
async def on_interaction(interaction):
    print(interaction.type)
    if str(interaction.type) == "InteractionType.application_command":
        return
    if interaction.data["custom_id"] == "jocontact":
        inter = interaction
        with open("./cogs/db/buttoncheck.json", "r") as f:
            data = json.load(f)
        id  = interaction.user.id
        if str(interaction.message.id) in data:
            users = data[str(interaction.message.id)]
            if interaction.user.id in users:
                can_continue = False
                embed34 = nextcord.Embed(description="You have already applied for this job. It is not possible to apply a second time.", color=0x35C5FF)
                await interaction.response.send_message(embed=embed34, ephemeral=True)
            else:
                can_continue = True
        else:
            can_continue = True
        with open("./cogs/db/buttoncheck.json", "w") as f:
            json.dump(data, f, indent=4)
        if can_continue == True:
            co_id = interaction.message.id
            title = interaction.message.embeds[0].title
            button99 = Button(label="Continue", style=nextcord.ButtonStyle.blurple)
            async def btn99_callback(interaction):
                #  ---   2. Modal (Application)   ---
                Modal2 = Modal(
                    custom_id="modal",
                    title="Application",
                    timeout=None,
                    auto_defer=True
                )
                with open("./cogs/db/wgzn.json", "r") as f:
                    data = json.load(f)
                client_id = data[str(co_id)]
                application = nextcord.ui.TextInput(label="Tell the client a few words about yourself", min_length=50, max_length=1000, required=True, placeholder=" ~ Application ~ ", style=nextcord.TextInputStyle.paragraph)
                Modal2.add_item(application)
                async def modal2_callback(interaction):
                    with open("./cogs/db/buttoncheck.json", "r") as f:
                        data = json.load(f)
                    if str(inter.message.id) in data:
                        users = data[str(inter.message.id)]
                        if interaction.user.id in users:
                            embed34 = nextcord.Embed(description="You have already applied for this job. It is not possible to apply a second time.", color=0x35C5FF)
                            await interaction.response.send_message(embed=embed34, ephemeral=True)
                            can_continue2 = False
                        else:
                            data[str(inter.message.id)].append(inter.user.id)
                            can_continue2 = True
                    else:
                        data[str(inter.message.id)] = []
                        data[str(inter.message.id)].append(inter.user.id)
                        can_continue2 = True
                    if can_continue2 == True:
                        with open("./cogs/db/buttoncheck.json", "w") as f:
                            json.dump(data, f, indent=4)
                        embed9 = nextcord.Embed(description=f"Your application for the job '{title}' has been successfully sent. As soon as the client accepts it, you can chat with them.", color=0x35C5FF)
                        await interaction.response.send_message(embed=embed9, ephemeral=True)
                        await msg7.delete()
                        category = interaction.guild.get_channel(1009811084380753941)
                        jpclientchannel = await category.create_text_channel(title)
                        await jpclientchannel.set_permissions(
                            interaction.guild.get_member(int(client_id)),
                            view_channel = True,
                            send_messages = False,
                            read_messages = True
                        )
                        category = interaction.guild.get_channel(1009828164928807012)
                        jpexpertchannel = await category.create_text_channel(title)
                        perms = jpexpertchannel.overwrites_for(interaction.guild.get_member(int(interaction.user.id)))
                        perms.view_channel = False
                        await jpexpertchannel.set_permissions(interaction.guild.get_member(int(interaction.user.id)), overwrite=perms)
                        with open("./cogs/db/wasgeht.json", "r") as f:
                            data = json.load(f)
                        data[str(jpexpertchannel.id)] = "b"
                        with open("./cogs/db/wasgeht.json", "w") as f:
                            json.dump(data, f, indent=4)
                        with open("./cogs/db/chats.json", "r") as f:
                            data = json.load(f)
                        data[str(jpexpertchannel.id)] = {}
                        data[str(jpexpertchannel.id)]["connect"] = jpclientchannel.id
                        data[str(jpexpertchannel.id)]["owner"] = interaction.user.id
                        data[str(jpclientchannel.id)]  = {}
                        data[str(jpclientchannel.id)]["connect"] = jpexpertchannel.id
                        data[str(jpclientchannel.id)]["owner"] = client_id
                        with open("./cogs/db/chats.json", "w") as f:
                            json.dump(data, f, indent=4)
                        with open("./cogs/db/payments.json", "r") as f:
                            data = json.load(f)
                        data[str(jpexpertchannel.id)] = {}
                        data[str(jpexpertchannel.id)]["client"] = client_id
                        data[str(jpexpertchannel.id)]["expert"] = interaction.user.id
                        data[str(jpexpertchannel.id)]["n"] = 0
                        with open("./cogs/db/payments.json", "w") as f:
                            json.dump(data, f, indent=4)
                        embed = nextcord.Embed(description=f"An Expert has sent you an application for '{title}'. Find it under 'my Experts'.\n[View the channel](https://discord.com/channels/{interaction.guild.id}/{jpclientchannel.id})", color=0x35C5FF)
                        await interaction.guild.get_member(int(client_id)).send(embed=embed)
                        btn = Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="jpapplicationdelete2")
                        btn.callback = None
                        view6 = View(timeout=None)
                        view6.add_item(btn)
                        embed = nextcord.Embed(description="You can now chat with the client. Please follow the rules, which you can find under [rules for Experts](https://discord.com/channels/1004869688251134033/1009830178211504148).\n\nIf you click on 'delete', the channel will be deleted. Please note, that after deleting, the communication can not be restored.", color=0x35C5FF)
                        qq = await jpexpertchannel.send(embed=embed, view=view6)
                        embed2 = nextcord.Embed(description="Quick guide:\nAfter you have reached an agreement with the client, you can send them the invoice using the command !pay. When the client has paid, you will recieve a confirmation and you can start working. When you are done, hand over the work to the client and ask for their opinion with the command !happy. If the client is satisfied, you recieve the money and the client leaves you a star rating.\n\nYou can find more information here: [help for experts](https://discord.com/channels/1004869688251134033/1009849367760482455)", color=0x35C5FF)
                        await jpexpertchannel.send(embed=embed2)
                        with open("./cogs/db/experts.json", "r") as f:
                            data = json.load(f)
                        rating = data[str(interaction.user.id)]["starrating"]
                        if rating == "no reviews":
                            starrating = "no reviews"
                        else:
                            rounded_rating = round(rating)
                            if rounded_rating == 0:
                                starrating = "zero stars"
                            elif rounded_rating == 1:
                                    starrating = "⭐"
                            elif rounded_rating == 2:
                                    starrating = "⭐⭐"
                            elif rounded_rating == 3:
                                    starrating = "⭐⭐⭐"
                            elif rounded_rating == 4:
                                    starrating = "⭐⭐⭐⭐"
                            else:
                                starrating = "⭐⭐⭐⭐⭐"
                        button12 = Button(label="Accept", style=nextcord.ButtonStyle.green, custom_id="jpapplicationaccept")
                        button13 = Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="jpapplicationdelete1")
                        button13.callback = None
                        button12.callback = None
                        view55 = View(timeout=None)
                        view55.add_item(button12)
                        view55.add_item(button13)
                        embed3 = nextcord.Embed(description=f"{application.value}\n\nExpert's star review: {starrating}\n\nIf you accept the Expert, then you can chat with them. If you click on 'delete', the channel will be deleted. This function is also available after accepting. Please note, that after deleting, the communication can not be restored.", color=0x35C5FF)
                        mm = await jpclientchannel.send(embed=embed3, view=view55)
                        with open("./cogs/db/delete-in-der-communication.json", "r") as f:
                            data = json.load(f)
                        data[str(jpclientchannel.id)] = str(mm.id)
                        data[str(jpexpertchannel.id)] = str(qq.id)
                        with open("./cogs/db/delete-in-der-communication.json", "w") as f:
                            json.dump(data, f, indent=4)
                Modal2.callback = modal2_callback
                await interaction.response.send_modal(modal=Modal2)
            button99.callback = btn99_callback
            view3 = View(timeout=None)
            view3.add_item(button99)
            embed = nextcord.Embed(description="To apply for this job offer, tell the client a few words about yourself. Most importantly, tell them what qualifies you for this job.", color=0x35C5FF)
            msg7 = await inter.response.send_message(embed=embed, view=view3, ephemeral=True)
    elif interaction.data["custom_id"] == "jodelete":
        #               -----                          
        with open("./cogs/db/delete_messages.json", "r") as f:
            data = json.load(f)
        message = interaction.message.id
        buttonyes = Button(label="I am sure I want to delete it", style=nextcord.ButtonStyle.red, custom_id="deleteyes")
        buttonyes.callback = None
        view = View(timeout=None)
        view.add_item(buttonyes)
        with open("./cogs/db/delete_messages.json", "w") as f:
            json.dump(data, f, indent=4)
        button2 = Button(label="<", style=nextcord.ButtonStyle.blurple, custom_id="deleteback", disabled=False)
        button2.callback = None
        try:
            await interaction.response.defer()
        except:
            print("Couldn't defer")
        view5 = View(timeout=None)
        view5.add_item(buttonyes)
        view5.add_item(button2)
        t = interaction.message.content
        msg99 = await interaction.message.edit(interaction.message.content, view = view5)
        print(interaction.message.content)
        print(interaction)
    elif interaction.data["custom_id"] == "deleteback":
        button3 = Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="jodelete", disabled=False)
        button3.callback = None
        await interaction.response.defer()
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
    elif interaction.data["custom_id"] == "expertaccept":
        try:
            await interaction.response.defer()
        except Exception as e:
            print(e)
        contents = interaction.message.content.split(" ")
        id = contents[-1]
        user = await interaction.guild.fetch_member(int(id))
        role = discord.utils.get(client.get_guild(1004869688251134033).roles, id=1004884670745411595)
        await user.add_roles(role)
        role = discord.utils.get(client.get_guild(1004869688251134033).roles, id=1005230473599008898)
        with open("./cogs/db/Expertquitting.json", "r") as f:
            data = json.load(f)
        data[str(id)] = 0
        with open("./cogs/db/Expertquitting.json", "w") as f:
            json.dump(data, f, indent=4)
        await user.remove_roles(role)
        embed22 = nextcord.Embed(description="You are now successfully registered with THAROS as an Expert.", color=0x35C5FF)
        await user.send(embed=embed22)
        await interaction.message.delete()
        with open("./cogs/db/raaebutton.json", "r") as f:
            data = json.load(f)
        del data[str(user.id)]
        with open("./cogs/db/raaebutton.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/wojodelete.json", "r") as f:
            data = json.load(f)
        if str(user.id) in data:
            msgids = data[str(user.id)]["messages"]
            channelids = data[str(user.id)]["channels"]
            for i in range(len(msgids)):
                msgid = msgids[i]
                channelid = channelids[i]
                channel2 = client.get_channel(int(channelid))
                post = await channel2.fetch_message(int(msgid))
                try:
                    await post.delete()
                except:
                    print("Message was already deleted")
            del data[str(user.id)]
        with open("./cogs/db/wojodelete.json", "w") as f:
            json.dump(data, f, indent=4)
    elif interaction.data["custom_id"] == "expertdeny":
        contents = interaction.message.content.split(" ")
        id = contents[-1]
        with open("./cogs/db/experts.json", "r") as f:
            data = json.load(f)
        del data[str(id)]
        with open("./cogs/db/experts.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/raaebutton.json", "r") as f:
            data = json.load(f)
        del data[str(id)]
        with open("./cogs/db/raaebutton.json", "w") as f:
            json.dump(data, f, indent=4)
        user = await interaction.guild.fetch_member(int(id))
        embed17=nextcord.Embed(description="Your registration as an Expert has been rejected. You can try again at any time.", color=0x35C5FF)
        await user.send(embed=embed17)
        await interaction.message.delete()
    elif interaction.data["custom_id"] == "jpapplicationaccept":
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        connected_channel = data[str(interaction.channel.id)]["connect"]
        expert_id = data[str(connected_channel)]["owner"]
        expert = interaction.guild.get_member(int(expert_id))
        job_title = interaction.channel.name
        expert_channel = client.get_channel(int(connected_channel))
        perms = expert_channel.overwrites_for(interaction.guild.get_member(int(expert_id)))
        perms.view_channel=True
        await expert_channel.set_permissions(interaction.guild.get_member(int(expert_id)), overwrite=perms)
        perms = client.get_channel(interaction.channel.id).overwrites_for(interaction.guild.get_member(int(interaction.user.id)))
        perms.send_messages=True
        await client.get_channel(interaction.channel.id).set_permissions(interaction.guild.get_member(int(interaction.user.id)), overwrite=perms)
        embed2 = nextcord.Embed(description=f"Your application for the job '{job_title}' has been accepted. You can now chat with the client.\n[View the channel](https://discord.com/channels/{interaction.guild.id}/{int(connected_channel)})", color=0x35C5FF)
        await expert.send(embed=embed2)
        button = Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="jpapplicationdelete5")
        button.callback = None
        view = View(timeout=None)
        view.add_item(button)
        with open("./cogs/db/Expertquitting.json", "r") as f:
            data = json.load(f)
        x = data[str(expert_id)]
        x += 1
        data[str(expert_id)] = x
        with open("./cogs/db/Expertquitting.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/Clientquitting.json", "r") as f:
            data = json.load(f)
        y = data[str(interaction.user.id)]
        y += 1
        data[str(interaction.user.id)] = y
        with open("./cogs/db/Clientquitting.json", "w") as f:
            json.dump(data, f, indent=4)
        embed = nextcord.Embed(description="You can now chat with the Expert. Please follow the rules which you can find under [rules](https://discord.com/channels/1004869688251134033/1009830091192283206). More information for clients can be found at [help for clients](https://discord.com/channels/1004869688251134033/1009849321614737469).\nYou can delete the channel at any time, but after deleting, there is no way to restore the communication.", color=0x35C5FF)
        await interaction.message.edit("", embed=embed, view=view)
        try:
            await interaction.response.defer()
        except Exception as e:
            print(e)
    elif interaction.data["custom_id"] == "jpapplicationdelete1":
        message = interaction.message.id
        buttonyes = Button(label="I am sure I want to delete it", style=nextcord.ButtonStyle.red, custom_id="jpclientdelete")
        buttonyes.callback = None
        await interaction.response.defer()
        view = View(timeout=None)
        view.add_item(buttonyes)
        button2 = Button(label="<", style=nextcord.ButtonStyle.blurple, custom_id="jpdeleteback", disabled=False)
        button2.callback = None
        view5 = View(timeout=None)
        view5.add_item(buttonyes)
        view5.add_item(button2)
        t = interaction.message.content
        msg99 = await interaction.message.edit(interaction.message.content, view = view5)
    elif interaction.data["custom_id"] == "jpdeleteback":
        button12 = Button(label="Accept", style=nextcord.ButtonStyle.green, custom_id="jpapplicationaccept")
        button3 = Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="jpapplicationdelete1", disabled=False)
        button3.callback = None
        button12.callback = None
        await interaction.response.defer()
        view6 = View(timeout=None)
        view6.add_item(button12)
        view6.add_item(button3)
        await interaction.message.edit(str(interaction.message.content),  view=view6)
    elif interaction.data["custom_id"] == "jpapplicationdelete2":
        await interaction.response.defer()
        message = interaction.message.id
        buttonyes = Button(label="I am sure I want to delete it", style=nextcord.ButtonStyle.red, custom_id="jpexpertdelete")
        buttonyes.callback = None
        view = View(timeout=None)
        view.add_item(buttonyes)
        button2 = Button(label="<", style=nextcord.ButtonStyle.blurple, custom_id="jpdeleteback2", disabled=False)
        button2.callback = None
        view5 = View(timeout=None)
        view5.add_item(buttonyes)
        view5.add_item(button2)
        t = interaction.message.content
        msg99 = await interaction.message.edit(interaction.message.content, view = view5)
    elif interaction.data["custom_id"] == "jpdeleteback2":
        await interaction.response.defer()
        button3 = Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="jpapplicationdelete2", disabled=False)
        button3.callback = None
        view6 = View(timeout=None)
        view6.add_item(button3)
        await interaction.message.edit(str(interaction.message.content),  view=view6)
    elif interaction.data["custom_id"] == "jpclientdelete":
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        expertchannel_id = data[str(interaction.channel.id)]["connect"]
        expertchannel = client.get_channel(int(expertchannel_id))
        expertid = data[str(expertchannel_id)]["owner"]
        expert = interaction.guild.get_member(expertid)
        embed244 = nextcord.Embed(description=f"A client has rejected your application for the job '{interaction.channel.name}'.", color=0x35C5FF)
        await expert.send(embed=embed244)
        await interaction.channel.delete()
        await expertchannel.delete()
        del data[str(interaction.channel.id)]
        del data[str(expertchannel_id)]
        with open("./cogs/db/chats.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/wasgeht.json", "r") as f:
            data = json.load(f)
        del data[str(expertchannel_id)]
        with open("./cogs/db/wasgeht.json", "w") as f:
            json.dump(data, f,  indent=4)
        with open("./cogs/db/buttoncheck.json", "r") as f:
            data = json.load(f)
        
    elif interaction.data["custom_id"] == "jpapplicationdelete5":
        message = interaction.message.id
        buttonyes = Button(label="I am sure I want to delete it", style=nextcord.ButtonStyle.red, custom_id="jpclientdelete6")
        buttonyes.callback = None
        await interaction.response.defer()
        view = View(timeout=None)
        view.add_item(buttonyes)
        button2 = Button(label="<", style=nextcord.ButtonStyle.blurple, custom_id="jpdeleteback6", disabled=False)
        button2.callback = None
        view5 = View(timeout=None)
        view5.add_item(buttonyes)
        view5.add_item(button2)
        t = interaction.message.content
        msg99 = await interaction.message.edit(interaction.message.content, view = view5)
    elif interaction.data["custom_id"] == "jpdeleteback6":
        button3 = Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="jpapplicationdelete5", disabled=False)
        button3.callback = None
        await interaction.response.defer()
        view6 = View(timeout=None)
        view6.add_item(button3)
        await interaction.message.edit(str(interaction.message.content),  view=view6)
    elif interaction.data["custom_id"] == "jpclientdelete6":
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        expertchannel_id = data[str(interaction.channel.id)]["connect"]
        expertchannel = client.get_channel(int(expertchannel_id))
        expertid = data[str(expertchannel_id)]["owner"]
        expert = interaction.guild.get_member(expertid)
        embed244 = nextcord.Embed(description=f"A client has broken off communication with you on the subject '{interaction.channel.name}'. The project is therefore terminated.", color=0x35C5FF)
        await expert.send(embed=embed244)
        await interaction.channel.delete()
        await expertchannel.delete()
        del data[str(interaction.channel.id)]
        del data[str(expertchannel_id)]
        with open("./cogs/db/chats.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/Expertquitting.json", "r") as f:
            data = json.load(f)
        x = data[str(expertid)]
        x -= 1
        data[str(expertid)] = x
        with open("./cogs/db/Expertquitting.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/Clientquitting.json", "r") as f:
            data = json.load(f)
        y = data[str(interaction.user.id)]
        y -= 1
        data[str(interaction.user.id)] = y
        with open("./cogs/db/Clientquitting.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/wasgeht.json", "r") as f:
            data = json.load(f)
        del data[str(expertchannel_id)]
        with open("./cogs/db/wasgeht.json", "w") as f:
            json.dump(data, f,  indent=4)
    elif interaction.data["custom_id"] == "jpexpertdelete":
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        clientchannel_id = data[str(interaction.channel.id)]["connect"]
        clientchannel = client.get_channel(int(clientchannel_id))
        clientid = data[str(clientchannel_id)]["owner"]
        client1 = interaction.guild.get_member(int(clientid))
        embed239 = nextcord.Embed(description=f"An Expert has broken off communication with you on the subject '{interaction.channel.name}'. The project is therefore terminated.", color=0x35C5FF)
        await client1.send(embed=embed239)
        await interaction.channel.delete()
        await clientchannel.delete()
        with open("./cogs/db/Expertquitting.json", "r") as f:
            data = json.load(f)
        x = data[str(interaction.user.id)]
        x -= 1
        data[str(interaction.user.id)] = x
        with open("./cogs/db/Expertquitting.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/Clientquitting.json", "r") as f:
            data = json.load(f)
        y = data[str(clientid)]
        y -= 1
        data[str(clientid)] = y
        with open("./cogs/db/Clientquitting.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        del data[str(interaction.channel.id)]
        del data[str(clientchannel_id)]
        with open("./cogs/db/chats.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/wasgeht.json", "r") as f:
            data = json.load(f)
        del data[str(interaction.channel.id)]
        with open("./cogs/db/wasgeht.json", "w") as f:
            json.dump(data, f,  indent=4)
    elif interaction.data["custom_id"] == "owcontact":
        with open("./cogs/db/buttoncheck.json", "r") as f:
            data = json.load(f)
        id = interaction.user.id
        if str(interaction.message.id) not in data:
            data[str(interaction.message.id)] = []
            data[str(interaction.message.id)].append(interaction.user.id)
            can_continue = True
        else:
            users = data[str(interaction.message.id)]
            if interaction.user.id in users:
                can_continue = False
                embed57=nextcord.Embed(description="You have already contacted the Expert for this work offer. This is not possible twice.", color=0x35C5FF)
                await interaction.response.send_message(embed=embed57, ephemeral=True)
            else:
                data[str(interaction.message.id)].append(interaction.user.id)
                can_continue = True
        with open("./cogs/db/buttoncheck.json", "w") as f:
            json.dump(data, f, indent=4)
        if can_continue == True:
            title3 = interaction.message.embeds[0].title
            embed33=nextcord.Embed(description=f"You are now connected with an Expert for the job offer '{title3}'.", color=0x35C5FF)
            await interaction.response.send_message(embed=embed33, ephemeral=True)
            with open("./cogs/db/wgzn.json", "r") as f:
                data = json.load(f)
            expert_id = data[str(interaction.message.id)]
            print(expert_id)
            category = interaction.guild.get_channel(1009811084380753941)
            owclientchannel = await category.create_text_channel(interaction.message.embeds[0].title)

            await owclientchannel.set_permissions(
                interaction.guild.get_member(int(interaction.user.id)),
                view_channel = True,
                send_messages = True,
                read_messages = True
            )
            category = interaction.guild.get_channel(1009828164928807012)
            owexpertchannel = await category.create_text_channel(interaction.message.embeds[0].title)
            perms = owexpertchannel.overwrites_for(interaction.guild.get_member(int(expert_id)))
            perms.view_channel = True
            await owexpertchannel.set_permissions(interaction.guild.get_member(int(expert_id)), overwrite=perms)
            embed = nextcord.Embed(description=f"You are now connected with an Expert for the offer '{interaction.message.embeds[0].title}'. Find the channel under 'your Experts'. [view the channel](https://discord.com/channels/{interaction.guild.id}/{owclientchannel.id})", color=0x35C5FF)
            await interaction.user.send(embed=embed)
            embed23 = nextcord.Embed(description=f"A client has shown interest in your offer '{interaction.message.embeds[0].title}'. You are now connected with the client. Find the channel under 'your clients'. [view the channel](https://discord.com/channels/{interaction.guild.id}/{owexpertchannel.id})", color=0x35C5FF)
            expert = interaction.guild.get_member(int(expert_id))
            with open("./cogs/db/Expertquitting.json", "r") as f:
                data = json.load(f)
            x = data[str(expert_id)]
            x += 1
            data[str(expert_id)] = x
            with open("./cogs/db/Expertquitting.json", "w") as f:
                json.dump(data, f, indent=4)
            with open("./cogs/db/Clientquitting.json", "r") as f:
                data = json.load(f)
            y = data[str(interaction.user.id)]
            y += 1
            data[str(interaction.user.id)] = y
            with open("./cogs/db/Clientquitting.json", "w") as f:
                json.dump(data, f, indent=4)
            with open("./cogs/db/wasgeht.json", "r") as f:
                data = json.load(f)
            data[str(owexpertchannel.id)] = "b"
            with open("./cogs/db/wasgeht.json", "w") as f:
                json.dump(data, f, indent=4)
            print(expert)
            await expert.send(embed=embed23)
            with open("./cogs/db/chats.json", "r") as f:
                data = json.load(f)
            data[str(owexpertchannel.id)] = {}
            data[str(owexpertchannel.id)]["connect"] = owclientchannel.id
            data[str(owexpertchannel.id)]["owner"] = expert_id
            data[str(owclientchannel.id)]  = {}
            data[str(owclientchannel.id)]["connect"] = owexpertchannel.id
            data[str(owclientchannel.id)]["owner"] = interaction.user.id
            with open("./cogs/db/chats.json", "w") as f:
                json.dump(data, f, indent=4)
            with open("./cogs/db/payments.json", "r") as f:
                data = json.load(f)
            data[str(owexpertchannel.id)] = {}
            data[str(owexpertchannel.id)]["client"] = interaction.user.id
            data[str(owexpertchannel.id)]["expert"] = expert_id
            data[str(owexpertchannel.id)]["n"] = 0
            with open("./cogs/db/payments.json", "w") as f:
                json.dump(data, f, indent=4)
            button2 = Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="owclientdelete", disabled=False)
            button2.callback = None
            view = View(timeout=None)
            view.add_item(button2)
            embed1 = nextcord.Embed(description="You can now chat with the Expert. Please follow the rules, which you can find under [rules for clients](https://discord.com/channels/1004869688251134033/1009830091192283206). More information for clients can be found at [help for clients](https://discord.com/channels/1004869688251134033/1009849321614737469). If you click on 'Delete', the channel will be deleted. Please note, that after deleting, the communication can not be restored.", color=0x35C5FF)
            mm = await owclientchannel.send(embed=embed1, view=view)
            button3 = Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="owexpertdelete")
            button3.callback = None
            view2 = View(timeout=None)
            view2.add_item(button3)
            embed2 = nextcord.Embed(description="You can now chat with the client. Please follow the rules, which you can find under [rules for Experts](https://discord.com/channels/1004869688251134033/1009830178211504148).", color=0x35C5FF)
            qq = await owexpertchannel.send(embed=embed2, view=view2)
            embed2 = nextcord.Embed(
                description="Quick guide:\nAfter you have reached an agreement with the client, you can send them the invoice using the command !pay. When the client has paid, you will recieve a confirmation and you can start working. When you are done, hand over the work to the client and ask for their opinion with the command !happy. If the client is satisfied, you recieve the money and the client leaves you a star rating.\n\nYou can find more information here: [help for experts](https://discord.com/channels/1004869688251134033/1009849367760482455)",
                color=0x35C5FF)
            await owexpertchannel.send(embed=embed2)
            with open("./cogs/db/delete-in-der-communication.json", "r") as f:
                data = json.load(f)
            data[str(owclientchannel.id)] = str(mm.id)
            data[str(owexpertchannel.id)] = str(qq.id)
            with open("./cogs/db/delete-in-der-communication.json", "w") as f:
                json.dump(data, f, indent=4)
    elif interaction.data["custom_id"] == "owclientdelete":
        buttonyes = Button(label="I am sure I want to delete it", style=nextcord.ButtonStyle.red, custom_id="owclientdelete2")
        buttonyes.callback = None
        view = View(timeout=None)
        view.add_item(buttonyes)
        button2 = Button(label="<", style=nextcord.ButtonStyle.blurple, custom_id="owclientdeleteback", disabled=False)
        button2.callback = None
        view5 = View(timeout=None)
        view5.add_item(buttonyes)
        view5.add_item(button2)
        await interaction.response.defer()
        await interaction.message.edit(interaction.message.content, view = view5)
    elif interaction.data["custom_id"] == "owclientdeleteback":
        button3 = Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="owclientdelete", disabled=False)
        button3.callback = None
        await interaction.response.defer()
        view6 = View(timeout=None)
        view6.add_item(button3)
        await interaction.message.edit(str(interaction.message.content),  view=view6)
    elif interaction.data["custom_id"] == "owclientdelete2":
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        expertchannel_id = data[str(interaction.channel.id)]["connect"]
        expertchannel = client.get_channel(int(expertchannel_id))
        expertid = data[str(expertchannel_id)]["owner"]
        print(expertid)
        expert = interaction.guild.get_member(int(expertid))
        print(expert)
        embed = nextcord.Embed(description=f"A client has broken off communication with you on the subject '{interaction.channel.name}'. The project is therefore terminated.", color=0x35C5FF)
        await expert.send(embed = embed)
        await interaction.channel.delete()
        await expertchannel.delete()
        with open("./cogs/db/Expertquitting.json", "r") as f:
            data = json.load(f)
        x = data[str(expertid)]
        x -= 1
        data[str(expertid)] = x
        with open("./cogs/db/Expertquitting.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/Clientquitting.json", "r") as f:
            data = json.load(f)
        y = data[str(interaction.user.id)]
        y -= 1
        data[str(interaction.user.id)] = y
        with open("./cogs/db/Clientquitting.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        del data[str(interaction.channel.id)]
        del data[str(expertchannel_id)]
        with open("./cogs/db/chats.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/wasgeht.json", "r") as f:
            data = json.load(f)
        del data[str(expertchannel_id)]
        with open("./cogs/db/wasgeht.json", "w") as f:
            json.dump(data, f,  indent=4)
    elif interaction.data["custom_id"] == "owexpertdelete":
        buttonyes = Button(label="I am sure I want to delete it", style=nextcord.ButtonStyle.red, custom_id="owexpertdelete2")
        buttonyes.callback = None
        await interaction.response.defer()
        view = View(timeout=None)
        view.add_item(buttonyes)
        button2 = Button(label="<", style=nextcord.ButtonStyle.blurple, custom_id="owexpertdeleteback", disabled=False)
        button2.callback = None
        view5 = View(timeout=None)
        view5.add_item(buttonyes)
        view5.add_item(button2)
        await interaction.message.edit(interaction.message.content, view = view5)
    elif interaction.data["custom_id"] == "owexpertdeleteback":
        button3 = Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="owexpertdelete", disabled=False)
        button3.callback = None
        await interaction.response.defer()
        view6 = View(timeout=None)
        view6.add_item(button3)
        await interaction.message.edit(str(interaction.message.content),  view=view6)
    elif interaction.data["custom_id"] == "owexpertdelete2":
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        clientchannel_id = data[str(interaction.channel.id)]["connect"]
        clientchannel = client.get_channel(int(clientchannel_id))
        clientid = data[str(clientchannel_id)]["owner"]
        client2 = interaction.guild.get_member(int(clientid))
        print(client2)
        embed = nextcord.Embed(description=f"An Expert has broken off communication with you on the subject '{interaction.channel.name}'. The project is therefore terminated.", color=0x35C5FF)
        await client2.send(embed = embed)
        await interaction.channel.delete()
        await clientchannel.delete()
        with open("./cogs/db/Expertquitting.json", "r") as f:
            data = json.load(f)
        x = data[str(interaction.user.id)]
        x -= 1
        data[str(interaction.user.id)] = x
        with open("./cogs/db/Expertquitting.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/Clientquitting.json", "r") as f:
            data = json.load(f)
        y = data[str(clientid)]
        y -= 1
        data[str(clientid)] = y
        with open("./cogs/db/Clientquitting.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        del data[str(interaction.channel.id)]
        del data[str(clientchannel_id)]
        with open("./cogs/db/chats.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/wasgeht.json", "r") as f:
            data = json.load(f)
        del data[str(interaction.channel.id)]
        with open("./cogs/db/wasgeht.json", "w") as f:
            json.dump(data, f,  indent=4)
    elif interaction.data["custom_id"] == "pay-enter":
        Modal1 = Modal(
            custom_id="pay-modal",
            title="Payment",
            timeout=None,
            auto_defer=True
        )
        with open("./cogs/db/wgzn.json", "r") as f:
            data = json.load(f)
        amount = nextcord.ui.TextInput(label="Amount in USD", min_length=1, max_length=4, required=True, style=nextcord.TextInputStyle.short)
        Modal1.add_item(amount)
        global time
        msg = interaction.message
        time = nextcord.ui.TextInput(label="Maximum time in days", min_length=1, max_length=2, required=True, style=nextcord.TextInputStyle.short)
        Modal1.add_item(time)
        async def modal_callback(interaction):
            await msg.delete()
            embed = nextcord.Embed(description="The invoice has been sent to the client. Once the payment is completed, you will be notified.", color=0x35C5FF)
            await interaction.response.send_message(embed=embed)
            with open("./cogs/db/trash1.json", "r") as f:
                data = json.load(f)
            data[str(interaction.channel.id)] = {}
            data[str(interaction.channel.id)]["amount"] = amount.value
            data[str(interaction.channel.id)]["time"] = time.value
            with open("./cogs/db/trash1.json", "w") as f:
                json.dump(data, f, indent=4)
            print(amount.value)
            print(time.value)
            try:
                print(int(amount.value))
                int(amount.value)
                int(time.value)
                if int(amount.value) < 5 or int(time.value) < 1:
                    button = Button(label="Enter", style=nextcord.ButtonStyle.blurple, custom_id="pay-enter")
                    button.callback = None
                    view=View(timeout=None)
                    view.add_item(button)
                    embed = nextcord.Embed(description="The amount has to be an integer which is at least five. The time has to be a positive integer. Please try again.", color=0x35C5FF)
                    await interaction.channel.send(embed = embed, view=view)
                else:
                    with open("./cogs/db/chats.json", "r") as f:
                        data = json.load(f)
                    ccid = data[str(interaction.channel.id)]["connect"]
                    channel = client.get_channel(int(ccid))
                    button = Button(label="Confirm", style=nextcord.ButtonStyle.green, custom_id="pay-confirm")
                    button2 = Button(label="Decline", style=nextcord.ButtonStyle.red, custom_id="pay-decline")
                    button.callback = None
                    button2.callback = None
                    view=View(timeout=None)
                    view.add_item(button)
                    view.add_item(button2)
                    embed = nextcord.Embed(description=f"Please confirm the following data so that an invoice can be created:\nThe price for this project is {amount.value}$.\nThe Expert has indicated to complete the project within {time.value} days.\nNote that you can claim your money back only after this time.", color=0x35C5FF)
                    await channel.send(embed=embed, view=view)
            except:
                button = Button(label="Enter", style=nextcord.ButtonStyle.blurple, custom_id="pay-enter")
                button.callback = None
                view=View(timeout=None)
                view.add_item(button)
                embed = nextcord.Embed(description="The amount and time have to be an integer above 0. Please try again.", color=0x35C5FF)
                await interaction.channel.send(embed=embed, view=view)
        Modal1.callback = modal_callback
        await interaction.response.send_modal(modal=Modal1)
    elif interaction.data["custom_id"] == "pay-confirm":
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        ecid = data[str(interaction.channel.id)]["connect"]
        print(ecid)
        with open("./cogs/db/trash1.json", "r") as f:
            data = json.load(f)
        time1 = data[str(ecid)]["time"]
        with open("./cogs/db/trash1.json", "r") as f:
            data = json.load(f)
        price = data[str(ecid)]["amount"]
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "redirect_urls": {
                "return_url": "https://tharos.eu/index.php/payment-successful/",
                "cancel_url": "https://paypal.com/"},
            "transactions": [{
                "item_list": {
                    "items": [{
                        "name": "THAROS Service",
                        "sku": "item",
                        "price": int(price),
                        "currency": "USD",
                        "quantity": 1
                        }]},
                "amount": {
                    "total": int(price),
                    "currency": "USD"},
                "description": "This invoice was commissioned by a THAROS Expert"}]})
        if payment.create():
                print("Payment created successfully")
        else:
            print(payment.error)
            print(payment.id)
        for link in payment.links:
            if link.rel == "approval_url":
                approval_url = str(link.href)
        await interaction.message.delete()
        with open("./cogs/db/paymentid.json", "r") as f:
            data = json.load(f)
        data[str(interaction.channel.id)] = payment.id
        with open("./cogs/db/paymentid.json", "w") as f:
            json.dump(data, f, indent=4)
        embed = nextcord.Embed(description=f"The Expert has sent you an invoice. You can pay it through the link below. After your payment the Expert will start working.\nIf the Expert does not finish the work in {time1} days after your payment, you can report them and get your money back.\n{approval_url}", color=0x35C5FF)
        await interaction.channel.send(embed=embed)
        button = Button(label="Confirm", style=nextcord.ButtonStyle.blurple, custom_id="confirm-payment")
        button.callback = None
        view = View(timeout=None)
        view.add_item(button)
        embed = nextcord.Embed(description=f"Please press this button once you have confirmed the payment on PayPal. Then the Expert will be notified and can start working.", color=0x35C5FF)
        await interaction.channel.send(embed=embed, view=view)
    elif interaction.data["custom_id"] == "pay-decline":
        await interaction.message.delete()
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        id = data[str(interaction.channel.id)]["connect"]
        channel = client.get_channel(int(id))
        button = Button(label="Enter", style=nextcord.ButtonStyle.blurple, custom_id="pay-enter")
        button.callback = None
        view=View(timeout=None)
        view.add_item(button)
        embed = nextcord.Embed(description=f"The client has rejected the data you have entered. Please come to an agreement with the client and enter the data again.", color=0x35C5FF)
        await channel.send(embed=embed, view=view)
    elif interaction.data["custom_id"] == "confirm-payment":
        await interaction.response.defer()
        with open("./cogs/db/paymentid.json", "r") as f:
            data = json.load(f)
        id = data[str(interaction.channel.id)]
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        ecid = data[str(interaction.channel.id)]["connect"]
        with open("./cogs/db/trash1.json", "r") as f:
            data = json.load(f)
        time1 = data[str(ecid)]["time"]
        amount1 = data[str(ecid)]["amount"]
        i = interaction
        async def payment_worked():
            await interaction.message.delete()
            embed = nextcord.Embed(description=f"Thank you for your payment. If the Expert does not get back to you within {time1} days you can report them and get your money back.", color=0x35C5FF)
            btn = Button(label="Report the Expert", style=nextcord.ButtonStyle.red, custom_id="report-expert")
            btn.callback = None
            view = View(timeout=None)
            view.add_item(btn)
            message2 = await i.channel.send(embed=embed, view=view)
            with open("./cogs/db/Reportbuttondelete.json", "r") as f:
                data = json.load(f)
            data[str(interaction.channel.id)] = message2.id
            with open("./cogs/db/Reportbuttondelete.json", "w") as f:
                json.dump(data, f, indent=4)
            with open("./cogs/db/chats.json", "r") as f:
                data = json.load(f)
            ecid = data[str(i.channel.id)]["connect"]
            echat = client.get_channel(int(ecid))
            embed = nextcord.Embed(description=f"We have received the payment from the client. You can start the work now. Please note that the client can ask for their money back after {time1} days.", color=0x35C5FF)
            await echat.send(embed=embed)
            with open("./cogs/db/delete-in-der-communication.json", "r") as f:
                data = json.load(f)
            cbuttonid = data[str(i.channel.id)]
            ebuttonid = data[str(ecid)]
            msg = await i.channel.fetch_message(cbuttonid)
            await msg.edit(msg.content, view=None)
            msg2 = await echat.fetch_message(ebuttonid)
            await msg2.edit(msg2.content, view=None)
            with open("./cogs/db/wasgeht.json", "r") as f:
                data = json.load(f)
            data[str(ecid)] = f"a/{amount1}/{time1}"
            with open("./cogs/db/wasgeht.json", "w") as f:
                json.dump(data, f, indent=4)
            with open("./cogs/db/payments.json", "r") as f:
                data = json.load(f)
            n = data[str(ecid)]["n"]
            n += 1
            data[str(ecid)]["n"] = n
            data[str(ecid)][int(n)] = {}
            data[str(ecid)][int(n)]["amount"] = amount1
            data[str(ecid)][int(n)]["status"] = "NB"
            time_now = datetime.now()
            data[str(ecid)][int(n)]["time"] = str(time_now)
            with open("./cogs/db/payments.json", "w") as f:
                json.dump(data, f, indent=4)
            with open("./cogs/db/finanzen.json", "r") as f:
                data = json.load(f)
            ank = int(amount1)*92/100-0.49
            gesamt = data["Gesamt"]
            gesamt += ank
            data["Gesamt"] = gesamt
            p = data["p"]
            g = p * ank
            schulden = data["Schulden"]
            schulden += g
            data["Schulden"] = schulden
            cspendings = data["Cspendings"]
            cspendings += int(amount1)
            data["Cspendings"] = cspendings
            with open("./cogs/db/finanzen.json", "w") as f:
                json.dump(data, f, indent=4)
            
        payment = paypalrestsdk.Payment.find(id)
        try:
            if payment.execute({"payer_id": payment.payer.payer_info.payer_id}):
                await payment_worked()
        except Exception as e:
            print(e)
            embed = nextcord.Embed(description="Please confirm the payment on the PayPal website first.", color=0x35C5FF)
            await interaction.channel.send(embed=embed)
    elif interaction.data["custom_id"] == "report-expert":
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        ecid = data[str(interaction.channel.id)]["connect"]
        with open("./cogs/db/wasgeht.json", "r") as f:
            data = json.load(f)
        status = data[str(ecid)]
        if status.startswith("a"):
            with open("./cogs/db/payments.json") as f:
                data = json.load(f)
            n = data[str(ecid)]["n"]
            timevar = data[str(ecid)][str(n)]["time"]
            split = timevar.split(" ")
            left = split[0].split("-")
            right = split[1].split(":")
            year = left[0]
            month = left[1]
            day = left[2]
            hours = right[0]
            minutes = right[1]
            sec = right[-1].split(".")
            seconds = sec[0]
            then = datetime(int(year), int(month), int(day), int(hours), int(minutes), int(seconds))
            now = datetime.now()
            difference = now - then
            duration2 = difference.total_seconds()
            total_days = duration2 / 86400
            with open("./cogs/db/trash1.json", "r") as f:
                data = json.load(f)
            time2 = data[str(ecid)]["time"]
            if total_days >= int(time2):
                await interaction.message.delete()
                button=Button(label="Enter", style=nextcord.ButtonStyle.blurple, custom_id="money-back")
                button.callback = None
                view=View(timeout=None)
                view.add_item(button)
                embed=nextcord.Embed(description="Please enter the email address associated with your PayPal account to get your money back.", color=0x35C5FF)
                await interaction.channel.send(embed=embed, view=view)
                with open("./cogs/db/wasgeht.json", "r") as f:
                    data = json.load(f)
                data[str(ecid)] = "f"
                with open("./cogs/db/wasgeht.json", "w") as f:
                    json.dump(data, f, indent=4)
            else:
                await interaction.response.defer()
                embed = nextcord.Embed(description="At this time it is not possible for you to report the Expert. The working time of the Expert has not expired yet.", color=0x35C5FF)
                await interaction.channel.send(embed=embed)
            print(duration2)
        else:
            await interaction.response.defer()
            embed = nextcord.Embed(description="At this time it is not possible for you to report the Expert.", color=0x35C5FF)
            await interaction.channel.send(embed=embed)
    elif interaction.data["custom_id"] == "money-back":
        msg11  = interaction.message
        Modal1 = Modal( 
            custom_id="money-back-modal",
            title="Money refund",
            timeout=None,
            auto_defer=True
        )
        email = nextcord.ui.TextInput(label="Enter your PayPal E-Mail Address", min_length=4, max_length=50, required=True, style=nextcord.TextInputStyle.short)
        Modal1.add_item(email)
        async def modal_callback(interaction):
            print(msg11.content)
            await msg11.delete()
            with open("./cogs/db/chats.json", "r") as f:
                data = json.load(f)
            ecid = data[str(interaction.channel.id)]["connect"]
            with open("./cogs/db/payments.json", "r") as f:
                data = json.load(f)
            n = data[str(ecid)]["n"]
            amount = data[str(ecid)][str(n)]["amount"]
            new_amount = int(amount) * 92 / 100 - 0.49
            amount2 = round(new_amount, 2)
            print(new_amount)
            print(email.value)
            pchannel = client.get_channel(1086726507814195340)
            embed = nextcord.Embed(title="ZAHLUNG", description=f"Receiver: {email.value}\nAmount: {amount2}\n\n\n{ecid}")
            worked = Button(label="Payment Worked", style=nextcord.ButtonStyle.green, custom_id="payment_worked2")
            didnt_work = Button(label="Payment Failed", style=nextcord.ButtonStyle.red, custom_id="payment_didnt_work2")
            view = View()
            view.add_item(worked)
            view.add_item(didnt_work)
            await pchannel.send(embed=embed, view=view)
            embed2 = nextcord.Embed(description="The payment is now being processed. You will get your money back within 24 hours.")
            await interaction.channel.send(embed=embed2)
        Modal1.callback = modal_callback
        await interaction.response.send_modal(modal=Modal1)
    elif interaction.data["custom_id"] == "cdeletecom2":
        message = interaction.message.id
        buttonyes = Button(label="I am sure I want to delete it", style=nextcord.ButtonStyle.red, custom_id="cdeletecom3")
        buttonyes.callback = None
        await interaction.response.defer()
        view = View(timeout=None)
        view.add_item(buttonyes)
        button2 = Button(label="<", style=nextcord.ButtonStyle.blurple, custom_id="cdeletecomback", disabled=False)
        button2.callback = None
        view5 = View(timeout=None)
        view5.add_item(buttonyes)
        view5.add_item(button2)
        t = interaction.message.content
        msg99 = await interaction.message.edit(interaction.message.content, view = view5)
    elif interaction.data["custom_id"] == "cdeletecomback":
        button3 = Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="cdeletecom2", disabled=False)
        button3.callback = None
        await interaction.response.defer()
        view6 = View(timeout=None)
        view6.add_item(button3)
        await interaction.message.edit(str(interaction.message.content),  view=view6)
    elif interaction.data["custom_id"] == "cdeletecom3":
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        expertchannel_id = data[str(interaction.channel.id)]["connect"]
        expertchannel = client.get_channel(int(expertchannel_id))
        expertid = data[str(expertchannel_id)]["owner"]
        print(expertchannel_id)
        print(expertid)
        expert = interaction.guild.get_member(int(expertid))
        embed = nextcord.Embed(description=f"A client has broken off communication with you on the subject '{interaction.channel.name}'. The project is therefore terminated.", color=0x35C5FF)
        await expert.send(embed=embed)
        await interaction.channel.delete()
        await expertchannel.delete()
        with open("./cogs/db/Expertquitting.json", "r") as f:
            data = json.load(f)
        x = data[str(expertid)]
        x -= 1
        data[str(expertid)] = x
        with open("./cogs/db/Expertquitting.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/Clientquitting.json", "r") as f:
            data = json.load(f)
        y = data[str(interaction.user.id)]
        y -= 1
        data[str(interaction.user.id)] = y
        with open("./cogs/db/Clientquitting.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        del data[str(interaction.channel.id)]
        del data[str(expertchannel_id)]
        with open("./cogs/db/chats.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/wasgeht.json", "r") as f:
            data = json.load(f)
        del data[str(expertchannel_id)]
        with open("./cogs/db/wasgeht.json", "w") as f:
            json.dump(data, f,  indent=4)
    elif interaction.data["custom_id"] == "edeletecom2":
        message = interaction.message.id
        buttonyes = Button(label="I am sure I want to delete it", style=nextcord.ButtonStyle.red, custom_id="edeletecom3")
        buttonyes.callback = None
        await interaction.response.defer()
        view = View(timeout=None)
        view.add_item(buttonyes)
        button2 = Button(label="<", style=nextcord.ButtonStyle.blurple, custom_id="edeletecomback", disabled=False)
        button2.callback = None
        view5 = View(timeout=None)
        view5.add_item(buttonyes)
        view5.add_item(button2)
        t = interaction.message.content
        msg99 = await interaction.message.edit(interaction.message.content, view = view5)
    elif interaction.data["custom_id"] == "edeletecomback":
        button3 = Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="edeletecom2", disabled=False)
        button3.callback = None
        await interaction.response.defer()
        view6 = View(timeout=None)
        view6.add_item(button3)
        await interaction.message.edit(str(interaction.message.content),  view=view6)
    elif interaction.data["custom_id"] == "edeletecom3":
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        clientchannel_id = data[str(interaction.channel.id)]["connect"]
        clientchannel = client.get_channel(int(clientchannel_id))
        clientid = data[str(clientchannel_id)]["owner"]
        print(clientchannel_id)
        print(clientid)
        client1 = interaction.guild.get_member(int(clientid))
        embed = nextcord.Embed(description=f"An Expert has broken off communication with you on the subject '{interaction.channel.name}'. The project is therefore terminated.", color=0x35C5FF)
        await client1.send(embed=embed)
        await interaction.channel.delete()
        await clientchannel.delete()
        with open("./cogs/db/Expertquitting.json", "r") as f:
            data = json.load(f)
        x = data[str(interaction.user.id)]
        x -= 1
        data[str(interaction.user.id)] = x
        with open("./cogs/db/Expertquitting.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/Clientquitting.json", "r") as f:
            data = json.load(f)
        y = data[str(clientid)]
        y -= 1
        data[str(clientid)] = y
        with open("./cogs/db/Clientquitting.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        del data[str(interaction.channel.id)]
        del data[str(clientchannel_id)]
        with open("./cogs/db/chats.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/wasgeht.json", "r") as f:
            data = json.load(f)
        del data[str(interaction.channel.id)]
        with open("./cogs/db/wasgeht.json", "w") as f:
            json.dump(data, f,  indent=4)
    elif interaction.data["custom_id"] == "happy-cancel":
        await interaction.message.delete()
        with open("./cogs/db/wasgeht.json", "r") as f:
            data = json.load(f)
        data[str(interaction.channel.id)] = "a"
        with open("./cogs/db/wasgeht.json", "w") as f:
            json.dump(data, f,  indent=4)
    elif interaction.data["custom_id"] == "happy-confirm":
        await interaction.message.delete()
        button = Button(label="Enter", style=nextcord.ButtonStyle.blurple, custom_id="happy-enter")
        button.callback = None
        view = View(timeout=None)
        view.add_item(button)
        embed = nextcord.Embed(description="If the client indicates that they are satisfied with the result, you will receive your money. Please enter the E-Mail address which is associated with your PayPal account.", color=0x35C5FF)
        await interaction.response.send_message(embed=embed, view=view)
    elif interaction.data["custom_id"] == "happy-enter":
        msg3 = interaction.message
        Modal1 = Modal(
            custom_id="happy-paypal",
            title="Payment Information",
            timeout=None,
            auto_defer=True
        )
        email = nextcord.ui.TextInput(label="Enter your PayPal E-Mail Address", min_length=4, max_length=50, required=True, style=nextcord.TextInputStyle.short)
        Modal1.add_item(email)
        async def modal_callback(interaction):
            await msg3.delete()
            embed19=nextcord.Embed(description="The client is now asked about their satisfaction. If the client does not answer, you will receive your money within three days.", color=0x35C5FF)
            await interaction.response.send_message(embed=embed19)
            with open("./cogs/db/3Tage.json", "r") as f:
                data = json.load(f)
            data[str(interaction.channel.id)] = str(datetime.now())
            with open("./cogs/db/3Tage.json", "w") as f:
                json.dump(data, f, indent=4)
            with open("./cogs/db/expertzahlinfos.json", "r") as f:
                data = json.load(f)
            data[str(interaction.channel.id)] = {}
            data[str(interaction.channel.id)]["email"] = email.value
            data[str(interaction.channel.id)]["time"] = str(datetime.now())
            with open("./cogs/db/expertzahlinfos.json", "w") as f:
                json.dump(data, f, indent=4)
            with open("./cogs/db/chats.json", "r") as f:
                data = json.load(f)
            cchatid = data[str(interaction.channel.id)]["connect"]
            clientchat = client.get_channel(int(cchatid))
            with open("./cogs/db/Reportbuttondelete.json", "r") as f:
                data = json.load(f)
            msgid2 = data[str(cchatid)]
            msg2 = await clientchat.fetch_message(int(msgid2))
            await msg2.delete()
            button = Button(label="Satisfied", style=nextcord.ButtonStyle.green, custom_id="happy-satisfied")
            button2 = Button(label="Dissatisfied", style=nextcord.ButtonStyle.red, custom_id="happy-dissatisfied")
            button.callback = None
            button2.callback = None
            view = View(timeout=None)
            view.add_item(button)
            view.add_item(button2)
            embed = nextcord.Embed(description="Please indicate if you are satisfied with the result. If you are satisfied the project will be completed and the Expert will receive their money. Please decide within three days, otherwise it will be assumed that you are satisfied.", color=0x35C5FF)
            message = await clientchat.send(embed=embed, view=view)
            with open("./cogs/db/3Tagedeletenachrichten.json", "r") as f:
                data = json.load(f)
            if str(cchatid) in data:
                data[str(cchatid)].append(message.id)
            else:
                data[str(cchatid)] = []
                data[str(cchatid)].append(message.id)
            with open("./cogs/db/3Tagedeletenachrichten.json", "w") as f:
                json.dump(data, f, indent=4)
        Modal1.callback = modal_callback
        await interaction.response.send_modal(modal=Modal1)
    elif interaction.data["custom_id"] == "happy-dissatisfied":
        await interaction.message.delete()
        await interaction.response.defer()
        button = Button(label="Yes", style=nextcord.ButtonStyle.blurple, custom_id="happy-yes")
        button2 = Button(label="No", style=nextcord.ButtonStyle.blurple, custom_id="happy-no")
        button.callback = None
        button2.callback = None
        view = View(timeout=None)
        view.add_item(button)
        view.add_item(button2)
        embed = nextcord.Embed(description="Do you want a supporter to take a look at the work? The supporter will then decide whether you get your money back. If you click 'No', there is no possibility for you to get your money back.", color=0x35C5FF)
        message = await interaction.channel.send(embed=embed, view=view)
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        ecid = data[str(interaction.channel.id)]["connect"]
        with open("./cogs/db/3Tagedeletenachrichten.json", "r") as f:
            data = json.load(f)
        if str(interaction.channel.id) in data:
            data[str(interaction.channel.id)].append(message.id)
        else:
            data[str(interaction.channel.id)] = []
            data[str(interaction.channel.id)].append(message.id)
        with open("./cogs/db/3Tagedeletenachrichten.json", "w") as f:
            json.dump(data, f, indent=4)
    elif interaction.data["custom_id"] == "happy-yes":
        await interaction.message.delete()
        await interaction.response.defer()
        embed = nextcord.Embed(description="A supporter will now look at the work.", color=0x35C5FF)
        await interaction.channel.send(embed=embed)
        support_role = discord.utils.get(interaction.guild.roles,id=1009803906055934015)
        await interaction.channel.set_permissions(support_role, view_channel=True)
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        connected_channel = data[str(interaction.channel.id)]["connect"]
        expertchannel = client.get_channel(int(connected_channel))
        await expertchannel.set_permissions(support_role, view_channel=True)
        embed2 = nextcord.Embed(description=f"{interaction.channel.mention}\n{expertchannel.mention}\n//{interaction.channel.id}", color=0x35C5FF)
        dfchannel = client.get_channel(1066792081823109190)
        button = Button(label="Money back", style=nextcord.ButtonStyle.blurple, custom_id="happy-mb")
        button2 = Button(label="No refund", style=nextcord.ButtonStyle.blurple, custom_id="happy-nr")
        button.callback = None
        button2.callback = None
        view = View(timeout=None)
        view.add_item(button)
        view.add_item(button2)
        await dfchannel.send(embed=embed2, view=view)
    elif interaction.data["custom_id"] == "happy-mb":
        await interaction.message.delete()
        spl = interaction.message.embeds[0].description.split("//")
        id = spl[1]
        embed = nextcord.Embed(description="A supporter has decided that you will receive your money back. Please enter the email address associated with your PayPal account.", color=0x35C5FF)
        button = Button(label="Enter", style=nextcord.ButtonStyle.blurple, custom_id="happy-entermb")
        button.callback = None
        view = View(timeout=None)
        view.add_item(button)
        clientchannel = client.get_channel(int(id))
        await interaction.response.defer()
        await clientchannel.send(embed=embed, view=view)
        support_role = discord.utils.get(interaction.guild.roles,id=1009803906055934015)
        await clientchannel.set_permissions(support_role, view_channel=False)
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        echannel = data[str(clientchannel.id)]["connect"]
        exchannel = client.get_channel(int(echannel))
        await exchannel.set_permissions(support_role, view_channel=False)
        with open("./cogs/db/3Tage.json", "r") as f:
            data = json.load(f)
        try:
            del data[str(exchannel.id)]
        except:
            print("Key error lol")
        with open("./cogs/db/3Tage.json", "w") as f:
            json.dump(data, f, indent=4)
    elif interaction.data["custom_id"] == "happy-entermb":
        msg11 = interaction.message
        Modal1 = Modal( 
            custom_id="money-back-modal12",
            title="Money refund",
            timeout=None,
            auto_defer=True
        )
        email = nextcord.ui.TextInput(label="Enter your PayPal E-Mail Address", min_length=4, max_length=50, required=True, style=nextcord.TextInputStyle.short)
        Modal1.add_item(email)
        async def modal_callback(interaction):
            await msg11.delete()
            with open("./cogs/db/chats.json", "r") as f:
                data = json.load(f)
            ecid = data[str(interaction.channel.id)]["connect"]
            with open("./cogs/db/payments.json", "r") as f:
                data = json.load(f)
            n = data[str(ecid)]["n"]
            amount = data[str(ecid)][str(n)]["amount"]
            new_amount = int(amount) * 92 / 100 - 0.49
            amount2 = round(new_amount, 2)
            pchannel = client.get_channel(1086726507814195340)
            embed = nextcord.Embed(title="ZAHLUNG", description=f"Receiver: {email.value}\nAmount: {amount2}\n\n\n{ecid}")
            worked = Button(label="Payment Worked", style=nextcord.ButtonStyle.green, custom_id="payment_worked3")
            didnt_work = Button(label="Payment Failed", style=nextcord.ButtonStyle.red, custom_id="payment_didnt_work3")
            view = View()
            view.add_item(worked)
            view.add_item(didnt_work)
            await pchannel.send(embed=embed, view=view)
            embed2 = nextcord.Embed(description="The payment is now being processed. You will get your money back within 24 hours.")
            await interaction.channel.send(embed=embed2)
        Modal1.callback = modal_callback
        await interaction.response.send_modal(modal=Modal1)
    elif interaction.data["custom_id"] == "cdeletecom4":
        message = interaction.message.id
        buttonyes = Button(label="I am sure I want to delete it", style=nextcord.ButtonStyle.red, custom_id="cdeletecom5")
        buttonyes.callback = None
        await interaction.response.defer()
        view = View(timeout=None)
        view.add_item(buttonyes)
        button2 = Button(label="<", style=nextcord.ButtonStyle.blurple, custom_id="cdeletecomback2", disabled=False)
        button2.callback = None
        view5 = View(timeout=None)
        view5.add_item(buttonyes)
        view5.add_item(button2)
        t = interaction.message.content
        msg99 = await interaction.message.edit(interaction.message.content, view = view5)
    elif interaction.data["custom_id"] == "cdeletecomback2":
        button3 = Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="cdeletecom4", disabled=False)
        button3.callback = None
        await interaction.response.defer()
        view6 = View(timeout=None)
        view6.add_item(button3)
        await interaction.message.edit(str(interaction.message.content),  view=view6)
    elif interaction.data["custom_id"] == "cdeletecom5":
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        expertchannel_id = data[str(interaction.channel.id)]["connect"]
        expertchannel = client.get_channel(int(expertchannel_id))
        expertid = data[str(expertchannel_id)]["owner"]
        print(expertchannel_id)
        print(expertid)
        expert = interaction.guild.get_member(int(expertid))
        embed = nextcord.Embed(description=f"A client has broken off communication with you on the subject '{interaction.channel.name}'. The project is therefore terminated.", color=0x35C5FF)
        await expert.send(embed=embed)
        await interaction.channel.delete()
        await expertchannel.delete()
        with open("./cogs/db/Expertquitting.json", "r") as f:
            data = json.load(f)
        x = data[str(expertid)]
        x -= 1
        data[str(expertid)] = x
        with open("./cogs/db/Expertquitting.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/Clientquitting.json", "r") as f:
            data = json.load(f)
        y = data[str(interaction.user.id)]
        y -= 1
        data[str(interaction.user.id)] = y
        with open("./cogs/db/Clientquitting.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        del data[str(interaction.channel.id)]
        del data[str(expertchannel_id)]
        with open("./cogs/db/chats.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/wasgeht.json", "r") as f:
            data = json.load(f)
        del data[str(expertchannel_id)]
        with open("./cogs/db/wasgeht.json", "w") as f:
            json.dump(data, f,  indent=4)
    elif interaction.data["custom_id"] == "edeletecom4":
        message = interaction.message.id
        buttonyes = Button(label="I am sure I want to delete it", style=nextcord.ButtonStyle.red, custom_id="edeletecom5")
        buttonyes.callback = None
        await interaction.response.defer()
        view = View(timeout=None)
        view.add_item(buttonyes)
        button2 = Button(label="<", style=nextcord.ButtonStyle.blurple, custom_id="edeletecomback2", disabled=False)
        button2.callback = None
        view5 = View(timeout=None)
        view5.add_item(buttonyes)
        view5.add_item(button2)
        t = interaction.message.content
        msg99 = await interaction.message.edit(interaction.message.content, view = view5)
    elif interaction.data["custom_id"] == "edeletecomback2":
        button3 = Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="edeletecom4", disabled=False)
        button3.callback = None
        await interaction.response.defer()
        view6 = View(timeout=None)
        view6.add_item(button3)
        await interaction.message.edit(str(interaction.message.content),  view=view6)
    elif interaction.data["custom_id"] == "edeletecom5":
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        clientchannel_id = data[str(interaction.channel.id)]["connect"]
        clientchannel = client.get_channel(int(clientchannel_id))
        clientid = data[str(clientchannel_id)]["owner"]
        print(clientchannel_id)
        print(clientid)
        client1 = interaction.guild.get_member(int(clientid))
        embed = nextcord.Embed(description=f"An Expert has broken off communication with you on the subject '{interaction.channel.name}'. The project is therefore terminated.", color=0x35C5FF)
        await client1.send(embed=embed)
        await interaction.channel.delete()
        await clientchannel.delete()
        with open("./cogs/db/Expertquitting.json", "r") as f:
            data = json.load(f)
        x = data[str(interaction.user.id)]
        x -= 1
        data[str(interaction.user.id)] = x
        with open("./cogs/db/Expertquitting.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/Clientquitting.json", "r") as f:
            data = json.load(f)
        y = data[str(clientid)]
        y -= 1
        data[str(clientid)] = y
        with open("./cogs/db/Clientquitting.json", "w") as f:
            json.dump(data, f, indent=4)
        del data[str(interaction.channel.id)]
        del data[str(clientchannel_id)]
        with open("./cogs/db/chats.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/wasgeht.json", "r") as f:
            data = json.load(f)
        del data[str(interaction.channel.id)]
        with open("./cogs/db/wasgeht.json", "w") as f:
            json.dump(data, f,  indent=4)
    elif interaction.data["custom_id"] == "happy-nr":
        await interaction.message.delete()
        print(interaction.message.embeds[0])
        splitted = interaction.message.embeds[0].description.split("//")
        print(splitted)
        id = splitted[1]
        cchannel = client.get_channel(int(id))
        embed = nextcord.Embed(description="The supporter has refused to refund your money because they consider the Expert's work satisfactory.", color=0x35C5FF)
        await cchannel.send(embed=embed)
        embed = nextcord.Embed(description="Please give the Expert a star rating out of five.", color=0x35C5FF)
        button1 = Button(label="⭐", style=nextcord.ButtonStyle.blurple, custom_id="happy-star1", row=1)
        button2 = Button(label="⭐⭐", style=nextcord.ButtonStyle.blurple, custom_id="happy-star2", row=1)
        button3 = Button(label="⭐⭐⭐", style=nextcord.ButtonStyle.blurple, custom_id="happy-star3", row=1)
        button4 = Button(label="⭐⭐⭐⭐", style=nextcord.ButtonStyle.blurple, custom_id="happy-star4", row=2)
        button5 = Button(label="⭐⭐⭐⭐⭐", style=nextcord.ButtonStyle.blurple, custom_id="happy-star5", row=2)
        button1.callback = None
        button2.callback = None
        button3.callback = None
        button4.callback = None
        button5.callback = None
        view = View(timeout=None)
        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)
        view.add_item(button4)
        view.add_item(button5)
        message = await cchannel.send(embed=embed, view=view)
        await interaction.response.defer()
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        ecid = data[str(cchannel.id)]["connect"]
        with open("./cogs/db/3Tagedeletenachrichten.json", "r") as f:
            data = json.load(f)
        if str(interaction.channel.id) in data:
            data[str(interaction.channel.id)].append(message.id)
        else:
            data[str(interaction.channel.id)] = []
            data[str(interaction.channel.id)].append(message.id)
        with open("./cogs/db/3Tagedeletenachrichten.json", "w") as f:
            json.dump(data, f, indent=4)
    elif interaction.data["custom_id"] == "happy-no":
        await interaction.message.delete()
        embed = nextcord.Embed(description="Please give the Expert a star rating out of five.", color=0x35C5FF)
        button1 = Button(label="⭐", style=nextcord.ButtonStyle.blurple, custom_id="happy-star1", row=1)
        button2 = Button(label="⭐⭐", style=nextcord.ButtonStyle.blurple, custom_id="happy-star2", row=1)
        button3 = Button(label="⭐⭐⭐", style=nextcord.ButtonStyle.blurple, custom_id="happy-star3", row=1)
        button4 = Button(label="⭐⭐⭐⭐", style=nextcord.ButtonStyle.blurple, custom_id="happy-star4", row=2)
        button5 = Button(label="⭐⭐⭐⭐⭐", style=nextcord.ButtonStyle.blurple, custom_id="happy-star5", row=2)
        button1.callback = None
        button2.callback = None
        button3.callback = None
        button4.callback = None
        button5.callback = None
        view = View(timeout=None)
        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)
        view.add_item(button4)
        view.add_item(button5)
        message = await interaction.channel.send(embed=embed, view=view)
        await interaction.response.defer()
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        ecid = data[str(interaction.channel.id)]["connect"]
        with open("./cogs/db/3Tagedeletenachrichten.json", "r") as f:
            data = json.load(f)
        if str(interaction.channel.id) in data:
            data[str(interaction.channel.id)].append(message.id)
        else:
            data[str(interaction.channel.id)] = []
            data[str(interaction.channel.id)].append(message.id)
        with open("./cogs/db/3Tagedeletenachrichten.json", "w") as f:
            json.dump(data, f, indent=4)
    elif interaction.data["custom_id"] == "happy-satisfied":
        await interaction.message.delete()
        embed = nextcord.Embed(description="Please give the Expert a star rating out of five.", color=0x35C5FF)
        button1 = Button(label="⭐", style=nextcord.ButtonStyle.blurple, custom_id="happy-star1", row=1)
        button2 = Button(label="⭐⭐", style=nextcord.ButtonStyle.blurple, custom_id="happy-star2", row=1)
        button3 = Button(label="⭐⭐⭐", style=nextcord.ButtonStyle.blurple, custom_id="happy-star3", row=1)
        button4 = Button(label="⭐⭐⭐⭐", style=nextcord.ButtonStyle.blurple, custom_id="happy-star4", row=2)
        button5 = Button(label="⭐⭐⭐⭐⭐", style=nextcord.ButtonStyle.blurple, custom_id="happy-star5", row=2)
        button1.callback = None
        button2.callback = None
        button3.callback = None
        button4.callback = None
        button5.callback = None
        view = View(timeout=None)
        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)
        view.add_item(button4)
        view.add_item(button5)
        message = await interaction.channel.send(embed=embed, view=view)
        await interaction.response.defer()
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        ecid = data[str(interaction.channel.id)]["connect"]
        with open("./cogs/db/3Tagedeletenachrichten.json", "r") as f:
            data = json.load(f)
        if str(interaction.channel.id) in data:
            data[str(interaction.channel.id)].append(message.id)
        else:
            data[str(interaction.channel.id)] = []
            data[str(interaction.channel.id)].append(message.id)
        with open("./cogs/db/3Tagedeletenachrichten.json", "w") as f:
            json.dump(data, f, indent=4)
    elif interaction.data["custom_id"] in ["happy-star1", "happy-star2", "happy-star3", "happy-star4", "happy-star5"]:
        await interaction.response.defer()
        await interaction.message.delete()
        pc = interaction.data["custom_id"].split("r")
        stars = pc[1]
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        echannelid = data[str(interaction.channel.id)]["connect"]
        expertid = data[str(echannelid)]["owner"]
        with open("./cogs/db/chats.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/3Tage.json", "r") as f:
            data = json.load(f)
        try:
            del data[str(echannelid)]
        except:
            print("Key error lol")
        with open("./cogs/db/3Tage.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/experts.json", "r") as f:
            data = json.load(f)
        j = data[str(expertid)]["jobsdone"]
        data[str(expertid)]["jobsdone"] = j+1
        r = data[str(expertid)]["reviews"]
        s = data[str(expertid)]["starrating"]
        data[str(expertid)]["reviews"] = r+1
        if s == "no reviews":
            data[str(expertid)]["starrating"] = int(stars)
        else:
            data[str(expertid)]["starrating"] = (s*r + int(stars))/(r+1)
        with open("./cogs/db/experts.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/expertzahlinfos.json", "r") as f:
            data = json.load(f)
        email = data[str(echannelid)]["email"]
        with open("./cogs/db/payments.json", "r") as f:
            data = json.load(f)
        n = data[str(echannelid)]["n"]
        amount = data[str(echannelid)][str(n)]["amount"]
        new_amount = 90*(int(amount) * 92 / 100 - 0.49) / 100
        amount2 = round(new_amount, 2)
        pchannel = client.get_channel(1086726507814195340)
        embed = nextcord.Embed(title="ZAHLUNG", description=f"Receiver: {email}\nAmount: {amount2}\n\n\n{echannelid}")
        worked = Button(label="Payment Worked", style=nextcord.ButtonStyle.green, custom_id="payment_worked4")
        didnt_work = Button(label="Payment Failed", style=nextcord.ButtonStyle.red, custom_id="payment_didnt_work4")
        view = View()
        view.add_item(worked)
        view.add_item(didnt_work)
        await pchannel.send(embed=embed, view=view)
        embed2 = nextcord.Embed(description="The client has rated your work as satisfactory. The payment is now being processed. You will receive your money within 24 hours.")
        echannel = client.get_channel(echannelid)
        await echannel.send(embed=embed2)
    elif interaction.data["custom_id"] == "enter7":
        Modal2 = Modal( 
            custom_id="expertpayouttryagain",
            title="Enter your PayPal email address",
            timeout=None,
            auto_defer=True
        )
        email = nextcord.ui.TextInput(label="Enter your PayPal E-Mail Address", min_length=4, max_length=50, required=True, style=nextcord.TextInputStyle.short)
        Modal2.add_item(email)
        async def modal_callback(interaction):
            echannelid = interaction.channel.id
            with open("./cogs/db/payments.json", "r") as f:
                data = json.load(f)
            n = data[str(echannelid)]["n"]
            amount = data[str(echannelid)][str(n)]["amount"]
            new_amount = 90*(int(amount) * 92 / 100 - 0.49) / 100
            amount2 = round(new_amount, 2)
            pchannel = client.get_channel(1086726507814195340)
            embed = nextcord.Embed(title="ZAHLUNG", description=f"Receiver: {email.value}\nAmount: {amount2}\n\n\n{echannelid}")
            worked = Button(label="Payment Worked", style=nextcord.ButtonStyle.green, custom_id="payment_worked5")
            didnt_work = Button(label="Payment Failed", style=nextcord.ButtonStyle.red, custom_id="payment_didnt_work5")
            view = View()
            view.add_item(worked)
            view.add_item(didnt_work)
            await pchannel.send(embed=embed, view=view)
            embed2 = nextcord.Embed(description="The payment is now being processed. You will receive your money within 24 hours.")
            echannel = client.get_channel(echannelid)
            await echannel.send(embed=embed2)
        Modal2.callback = modal_callback
        await interaction.response.send_modal(modal=Modal2)
    elif interaction.data["custom_id"] == "enter8":
        msg8 = interaction.message
        Modal7 = Modal( 
            custom_id="expertpayouttryagain8",
            title="Enter your PayPal email address",
            timeout=None,
            auto_defer=True
        )
        email = nextcord.ui.TextInput(label="Enter your PayPal E-Mail Address", min_length=4, max_length=50, required=True, style=nextcord.TextInputStyle.short)
        Modal7.add_item(email)
        async def modal_callback(interaction):
            await msg8.delete()
            echannelid = interaction.channel.id
            with open("./cogs/db/payments.json", "r") as f:
                data = json.load(f)
            n = data[str(echannelid)]["n"]
            amount = data[str(echannelid)][str(n)]["amount"]
            new_amount = 90*(int(amount) * 92 / 100 - 0.49) / 100
            amount2 = round(new_amount, 2)
            pchannel = client.get_channel(1086726507814195340)
            embed = nextcord.Embed(title="ZAHLUNG", description=f"Receiver: {email.value}\nAmount: {amount2}\n\n\n{echannelid}")
            worked = Button(label="Payment Worked", style=nextcord.ButtonStyle.green, custom_id="payment_worked6")
            didnt_work = Button(label="Payment Failed", style=nextcord.ButtonStyle.red, custom_id="payment_didnt_work6")
            view = View()
            view.add_item(worked)
            view.add_item(didnt_work)
            await pchannel.send(embed=embed, view=view)
            embed2 = nextcord.Embed(description="The payment is now being processed. You will receive your money within 24 hours.")
            echannel = client.get_channel(echannelid)
            await echannel.send(embed=embed2)
        Modal7.callback = modal_callback
        await interaction.response.send_modal(modal=Modal7)
    elif interaction.data["custom_id"] == "qaae":
        with open("./cogs/db/Expertquitting.json", "r") as f:
            data = json.load(f)
        x = data[str(interaction.user.id)]
        if x == 0:
            role = discord.utils.get(client.get_guild(1004869688251134033).roles, id=1004884670745411595)
            await interaction.user.remove_roles(role)
            role2 = discord.utils.get(client.get_guild(1004869688251134033).roles, id=1005230473599008898)
            await interaction.user.add_roles(role2)
            await interaction.response.defer()
            with open("./cogs/db/experts.json", "r") as f:
                data = json.load(f)
            del data[str(interaction.user.id)]
            with open("./cogs/db/experts.json", "w") as f:
                json.dump(data, f, indent=4)
            with open("./cogs/db/Expertquitting.json", "r") as f:
                data = json.load(f)
            del data[str(interaction.user.id)]
            with open("./cogs/db/Expertquitting.json", "w") as f:
                json.dump(data, f, indent=4)
            with open("./cogs/db/wojodelete.json", "r") as f:
                data = json.load(f)
            if str(interaction.user.id) in data:
                msgids = data[str(interaction.user.id)]["messages"]
                channelids = data[str(interaction.user.id)]["channels"]
                for i in range(len(msgids)):
                    msgid = msgids[i]
                    channelid = channelids[i]
                    channel2 = client.get_channel(int(channelid))
                    post = await channel2.fetch_message(int(msgid))
                    try:
                        await post.delete()
                    except:
                        print("Message was already deleted")
                del data[str(interaction.user.id)]
            with open("./cogs/db/wojodelete.json", "w") as f:
                json.dump(data, f, indent=4)
        else:
            embed=nextcord.Embed(description="Please complete all your orders first and delete the respective channels.", color=0x35C5FF)
            await interaction.response.send_message(embed=embed, ephemeral=True)
    elif interaction.data["custom_id"] == "cs":
        with open("./cogs/db/nureinsupportchannel.json", "r") as f:
            data = json.load(f)
        if str(interaction.user.id) in data:
            if data[str(interaction.user.id)] > 0:
                embed = nextcord.Embed(description="You already have a channel with the support team. It is not possible to open a second one.", color=0x35C5FF)
                await interaction.response.send_message(embed=embed, ephemeral=True)
            else:
                category = interaction.guild.get_channel(1070083235159224441)
                channel = await category.create_text_channel(f"support-{interaction.user.name}")
                await channel.set_permissions(
                    interaction.guild.get_member(int(interaction.user.id)),
                    view_channel = True,
                    send_messages = True,
                    read_messages = True
                )
                embed = nextcord.Embed(description="You are now connected to the support team. You can delete this chat at any time.", color=0x35C5FF)
                support = discord.utils.get(client.get_guild(1004869688251134033).roles, id=1009803906055934015)
                button=Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="csdelete")
                button.callback = None
                view=View(timeout=None)
                view.add_item(button)
                await channel.send(f"{support.mention}", embed=embed, view=view)#
                embed2 = nextcord.Embed(description=f"The text channel {channel.mention} was created for you to chat with our supporters privately.", color=0x35C5FF)
                await interaction.response.send_message(embed=embed2, ephemeral=True)
                try:
                    await interaction.response.defer()
                except Exception as e:
                    print(e)
                with open("./cogs/db/nureinsupportchannel.json", "r") as f:
                    data = json.load(f)
                data[str(interaction.user.id)] = 1
                data[str(channel.id)] = str(interaction.user.id)
                with open("./cogs/db/nureinsupportchannel.json", "w") as f:
                    json.dump(data, f, indent=4)
        else:
            category = interaction.guild.get_channel(1070083235159224441)
            channel = await category.create_text_channel(f"support-{interaction.user.name}")
            await channel.set_permissions(
                interaction.guild.get_member(int(interaction.user.id)),
                view_channel = True,
                send_messages = True,
                read_messages = True
            )
            embed = nextcord.Embed(description="You are now connected to the support team. You can delete this chat at any time.", color=0x35C5FF)
            support = discord.utils.get(client.get_guild(1004869688251134033).roles, id=1009803906055934015)
            button=Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="csdelete")
            button.callback = None
            view=View(timeout=None)
            view.add_item(button)
            await channel.send(f"{support.mention}", embed=embed, view=view)#
            embed2 = nextcord.Embed(description=f"The text channel {channel.mention} was created for you to chat with our supporters privately.", color=0x35C5FF)
            await interaction.response.send_message(embed=embed2, ephemeral=True)
            try:
                await interaction.response.defer()
            except Exception as e:
                print(e)
            with open("./cogs/db/nureinsupportchannel.json", "r") as f:
                data = json.load(f)
            data[str(interaction.user.id)] = 1
            data[str(channel.id)] = str(interaction.user.id)
            with open("./cogs/db/nureinsupportchannel.json", "w") as f:
                json.dump(data, f, indent=4)
    elif interaction.data["custom_id"] == "csdelete":
        await interaction.channel.delete()
        with open("./cogs/db/nureinsupportchannel.json", "r") as f:
            data = json.load(f)
        user = data[str(interaction.channel.id)]
        data[str(user)] = 0
        del data[str(interaction.channel.id)]
        with open("./cogs/db/nureinsupportchannel.json", "w") as f:
            json.dump(data, f, indent=4)
    elif interaction.data["custom_id"] == "verify999":
        print("11")
        role = discord.utils.get(interaction.guild.roles, id=1005230473599008898)
        await interaction.user.add_roles(role)
        await interaction.response.send_message("You now have the role of a client", ephemeral=True)
        with open("./cogs/db/Clientquitting.json", "r") as f:
            data = json.load(f)
        data[str(interaction.user.id)] = 0
        with open("./cogs/db/Clientquitting.json", "w") as f:
            json.dump(data, f, indent=4)
    elif interaction.data["custom_id"] == "raae1k9":
        button2 = Button(label="do the test", style=nextcord.ButtonStyle.green)
        async def button2_callback(interaction):
            with open("./cogs/db/Clientquitting.json", "r") as f:
                data = json.load(f)
            x = data[str(interaction.user.id)]
            if x == 0:
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
                    print(1)
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
                            if score >= 7:
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
                                        with open("./cogs/db/raaebutton.json", "r") as f:
                                            data = json.load(f)
                                        if str(interaction.user.id) in data:
                                            embed16=nextcord.Embed(description="You have already applied to be an Expert. Please wait for the registration process to be completed.", color=0x35C5FF)
                                            await interaction.response.send_message(embed=embed16, ephemeral=True)
                                        else:
                                            with open("./cogs/db/raaebutton.json", "r") as f:
                                                data = json.load(f)
                                            data[str(interaction.user.id)] = "1"
                                            with open("./cogs/db/raaebutton.json", "w") as f:
                                                json.dump(data, f, indent=4)
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
                                            embed14=nextcord.Embed(description="To complete the Expert registration, send a photo of the front of your identity card. Please note that for a successful registration the following message must contain the photo. The verification may take a few hours.", color=0x35C5FF)
                                            message = await interaction.user.send(embed=embed14)
                                            embed13=nextcord.Embed(description="The last step of your registration takes place in your DM's.", color=0x35C5FF)
                                            await interaction.response.send_message(embed=embed13, ephemeral=True)
                                            image = await client.wait_for("message", check=lambda i: i.author == interaction.user and i.channel.type is nextcord.ChannelType.private)
                                            verify_channel = client.get_channel(1051246577425055844)
                                            btn6 = Button(label="accept", style=nextcord.ButtonStyle.green, custom_id="expertaccept")
                                            btn7 = Button(label="deny", style=nextcord.ButtonStyle.red, custom_id="expertdeny")
                                            view6 = View(timeout=None)
                                            view6.add_item(btn6)
                                            view6.add_item(btn7)
                                            try:
                                                photo = image.attachments[0]
                                                await verify_channel.send(f"{photo}\n{first_name.value}\n{last_name.value}\n{dob.value}\n\n {interaction.user.id}", view=view6)
                                            except:
                                                await verify_channel.send(f"{image.content}\n{first_name.value}\n{last_name.value}\n{dob.value}\n\n {interaction.user.id}", view=view6)
                                            embed15 = nextcord.Embed(description="The photo has been successfully forwarded. Once this has been verified, you are an Expert.", color=0x35C5FF)
                                            await interaction.user.send(embed=embed15)


                                    Modal3.callback = modal3_callback
                                    await interaction.response.send_modal(Modal3)
                                button3.callback = button3_callback
                                view3  = View(timeout=None)
                                view3.add_item(button3)
                                embed11=nextcord.Embed(description="Congratulations! You have successfully passed the test. In the next step we need you to enter your personal data.", color=0x35C5FF)
                                await interaction.response.send_message(embed=embed11, view=view3, ephemeral=True)
                            else:
                                embed12=nextcord.Embed(description="Unfortunately, you did not pass the test. Try again at any time.", color=0x35C5FF)
                                await interaction.response.send_message(embed=embed12, ephemeral=True)
                        Modal2.callback = modal2_callback
                        await interaction.response.send_modal(Modal2)
                    button2.callback = button2_callback
                    view2 = View(timeout=None)
                    view2.add_item(button2)
                    embed10=nextcord.Embed(description="Now take the second part of the test. This tests your knowledge of the rules and information for Experts.", color=0x35C5FF)
                    await interaction.response.send_message(embed=embed10, view=view2, ephemeral=True)
                Modal1.callback = modal_callback
                await interaction.response.send_modal(Modal1)
            else:
                embed=nextcord.Embed(description="Please finish all your projects first and close the related chats.", color=0x35C5FF)
                await interaction.response.send_message(embed=embed, ephemeral=True)
        button2.callback = button2_callback
        view2 = View(timeout=None)
        view2.add_item(button2)
        embed = nextcord.Embed(description="Please note that it is prohibited to to bypass the THAROS payment system. For violation of this rule an Expert can be banned.", color=0x35C5FF)
        await interaction.response.send_message(embed=embed, view=view2, ephemeral=True)
    elif interaction.data["custom_id"] == "postajob00":
        inter = interaction
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
            try:
                (int(amount.value))
                can_continue = True
            except:
                embed = nextcord.Embed(description="The amount has to be an integer which is at least five. Please try again.", color=0x35C5FF)
                await interaction.response.send_message(embed=embed, ephemeral=True)
                can_continue = False
            if can_continue == True:
                if int(amount.value) > 4:
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
                    channel = client.get_channel(what[inter.data["values"][0]])
                    embed = nextcord.Embed(title=tit.value, description=f"{desc.value}\n\n{amount.value}$", color=0x35C5FF)
                    #  ---   Contact Button   ---
                    button1 = Button(label="Contact", style=nextcord.ButtonStyle.blurple, custom_id="jocontact")
                    button1.callback = None
                    view2 = View(timeout=None)
                    view2.add_item(button1)
                    msg2 = await channel.send(embed=embed, view=view2)
                    button2 = Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="jodelete", disabled=False)
                    view3 = View(timeout=None)
                    view3.add_item(button2)
                    embed2 = nextcord.Embed(description=f"You have made the following job posting:\n\n{tit.value}\n{desc.value}\n\nYou can delete this job at any time.", color=0x35C5FF)
                    msg = await interaction.user.send(embed=embed2, view=view3)
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
                    with open("./cogs/db/wojodelete.json", "r") as f:
                        data = json.load(f)
                    if str(interaction.user.id) in data:
                        data[str(interaction.user.id)]["messages"].append(str(msg2.id))
                        data[str(interaction.user.id)]["channels"].append(str(channel.id))
                    else:
                        data[str(interaction.user.id)] = {}
                        data[str(interaction.user.id)]["messages"] = []
                        data[str(interaction.user.id)]["messages"].append(str(msg2.id))
                        data[str(interaction.user.id)]["channels"] = []
                        data[str(interaction.user.id)]["channels"].append(str(channel.id))
                    with open("./cogs/db/wojodelete.json", "w") as f:
                        json.dump(data, f, indent=4)
                    embed77 = nextcord.Embed(description="Your job has been successfully posted.", color=0x35C5FF)
                    await interaction.response.send_message(embed=embed77, ephemeral=True)
                else:
                    embed = nextcord.Embed(description="The amount has to be an integer which is at least five. Please try again.", color=0x35C5FF)
                    await interaction.response.send_message(embed=embed, ephemeral=True)
        Modal1.callback = modal_callback
        await interaction.response.send_modal(Modal1)
    elif interaction.data["custom_id"] == "postajob222":
        inter = interaction
        #  ---   1.  Modal (Job post)   ---
        Modal1 = Modal(
            custom_id="modal",
            title="To offer your work, fill out the form below.",
            timeout=None,            
        )
        tit = nextcord.ui.TextInput(label="service title", min_length=5, max_length=100, required=True, placeholder="e.g. I will write a book for you", style=nextcord.TextInputStyle.short)
        Modal1.add_item(tit)
        desc = nextcord.ui.TextInput(label="description", min_length=20, max_length=1000, required=True, placeholder="e.g. I can write novels, ...", style=nextcord.TextInputStyle.paragraph)
        Modal1.add_item(desc)
        amount =  nextcord.ui.TextInput(label="approximate price in USD $", min_length=1, max_length=4, required=True, placeholder="e.g. 30", style=nextcord.TextInputStyle.short)
        Modal1.add_item(amount)
        async def modal_callback(interaction):
            try:
                print(1)
                (int(amount.value))
                print(amount.value)
                can_continue = True
            except Exception as e:
                print(e)
                embed = nextcord.Embed(description="The amount has to be an integer which is at least five. Please try again.", color=0x35C5FF)
                await interaction.response.send_message(embed=embed, ephemeral=True)
                can_continue = False
            if can_continue == True:
                if int(amount.value) > 4:
                    embed = nextcord.Embed(description="Your work offer was successfully sent.", color=0x35C5FF)
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                    print(1)
                    what = {
                        "web": 1009848187646910476,
                        "apps": 1009848261303087115,
                        "oso":  1009848445693083690,
                        "des": 1009848723435683990,
                        "ma": 1009848740628144200,
                        "wr": 1009848703110098954,
                        "phvi": 1009848510872559807,
                        "aud": 1009848466568138862,
                        "other": 1009848764925759632
                    }
                    with open("./cogs/db/experts.json", "r") as f:
                        data = json.load(f)
                    rating = data[str(interaction.user.id)]["starrating"]
                    if rating == "no reviews":
                        starrating = "no reviews"
                    else:
                        rounded_rating = round(rating)
                        if rounded_rating == 0:
                            starrating = "zero stars"
                        elif rounded_rating == 1:
                                starrating = "⭐"
                        elif rounded_rating == 2:
                                starrating = "⭐⭐"
                        elif rounded_rating == 3:
                                starrating = "⭐⭐⭐"
                        elif rounded_rating == 4:
                                starrating = "⭐⭐⭐⭐"
                        else:
                            starrating = "⭐⭐⭐⭐⭐"
                    channel = client.get_channel(what[inter.data["values"][0]])
                    embed = nextcord.Embed(title=tit.value, description=f"{desc.value}\n\n{amount.value}$\n\nStar rating: {starrating}", color=0x35C5FF)

                    #  ---   Contact Button   ---
                    button1 = Button(label="Contact", style=nextcord.ButtonStyle.blurple, custom_id="owcontact")
                    button1.callback = None
                    view2 = View(timeout=None)
                    view2.add_item(button1)
                    msg2 = await channel.send(embed=embed, view=view2)
                    button2 = Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="jodelete", disabled=False)
                    view3 = View(timeout=None)
                    view3.add_item(button2)
                    embed = nextcord.Embed(description=f"You have made the following work offer:\n\n{tit.value}\n{desc.value}\n\nYou can delete this offer at any time.", color=0x35C5FF)
                    msg = await interaction.user.send(embed=embed, view=view3)
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
                    with open("./cogs/db/wojodelete.json", "r") as f:
                        data = json.load(f)
                    if str(interaction.user.id) in data:
                        data[str(interaction.user.id)]["messages"].append(str(msg2.id))
                        data[str(interaction.user.id)]["channels"].append(str(channel.id))
                    else:
                        data[str(interaction.user.id)] = {}
                        data[str(interaction.user.id)]["messages"] = []
                        data[str(interaction.user.id)]["messages"].append(str(msg2.id))
                        data[str(interaction.user.id)]["channels"] = []
                        data[str(interaction.user.id)]["channels"].append(str(channel.id))
                    with open("./cogs/db/wojodelete.json", "w") as f:
                        json.dump(data, f, indent=4)
                else:
                    embed = nextcord.Embed(description="The amount has to be an integer which is at least five. Please try again.", color=0x35C5FF)
                    await interaction.response.send_message(embed=embed, ephemeral=True)
        Modal1.callback = modal_callback
        await interaction.response.send_modal(Modal1)
    elif interaction.data["custom_id"] == "payment_worked":
        split = interaction.message.embeds[0].description.split("\n\n\n")
        echannelid = split[1]
        await interaction.message.delete()
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        clientchannelid = data[str(echannelid)]["connect"]
        with open("./cogs/db/expertzahlinfos.json", "r") as f:
            data = json.load(f)
        del data[str(echannelid)]
        with open("./cogs/db/expertzahlinfos.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/wasgeht.json", "r") as f:
            data = json.load(f)
        data[str(echannelid)] = "b"
        with open("./cogs/db/wasgeht.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/payments.json", "r") as f:
            data = json.load(f)
        n = data[str(echannelid)]["n"]
        amount = data[str(echannelid)][str(n)]["amount"]
        data[str(echannelid)][str(n)]["status"] = str(datetime.now())
        with open("./cogs/db/payments.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/finanzen.json", "r") as f:
            data = json.load(f)
            ank = int(amount)*92/100-0.49
            ges = 97*90*ank/10000-0.49
            gesamt = data["Gesamt"]
            gesamt -= 90*ank/100
            data["Gesamt"] = gesamt
            p = data["p"]
            schulden = data["Schulden"]
            schulden -= 90*ank/100
            data["Schulden"] = schulden
            Gewinn = data["Gewinn"]
            Gewinn += (1 - 90/100)*ank
            data["Gewinn"] = Gewinn
            Eearnings = data["Eearnings"]
            Eearnings += ges
            data["Eearnings"] = Eearnings
        with open("./cogs/db/finanzen.json", "w") as f:
            json.dump(data, f, indent=4)
        button1=Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="cdeletecom2")
        button2=Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="edeletecom2")
        button1.callback = None
        button2.callback = None
        view1=View(timeout=None)
        view1.add_item(button1)
        view2=View(timeout=None)
        view2.add_item(button2)
        embed1 = nextcord.Embed(description="You have not answered for three days. Therefore the Expert was paid. This project is hereby completed. You can close the chat by clicking 'delete'.", color=0x35C5FF)
        embed2 = nextcord.Embed(description="The client did not answer for three days. Therefore you received your money. This project is hereby completed. You can close the chat by clicking 'delete'.", color=0x35C5FF)
        cchat = client.get_channel(int(clientchannelid))
        cmsg = await cchat.send(embed=embed1, view=view1)
        echat = client.get_channel(int(echannelid))
        emsg = await echat.send(embed=embed2, view=view2)
        with open("./cogs/db/delete-in-der-communication.json", "r") as f:
            data = json.load(f)
        data[str(clientchannelid)] = str(cmsg.id)
        data[str(echannelid)] = str(emsg.id)
        with open("./cogs/db/delete-in-der-communication.json", "w") as f:
            json.dump(data, f, indent=4)
    elif interaction.data["custom_id"] == "payment_didnt_work":
        split = interaction.message.embeds[0].description.split("\n\n\n")
        echannelid = split[1]
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        clientchannelid = data[str(echannelid)]["connect"]
        await interaction.message.delete()
        button=Button(label="Enter", style=nextcord.ButtonStyle.blurple, custom_id="enter8")
        button.callback = None
        view=View(timeout=None)
        view.add_item(button)
        embed=nextcord.Embed(description="The client did not answer for three days. But the payment did not work. Please enter a valid email address which is associated with your PayPal account to receive your money.", color=0x35C5FF)
        echannel = client.get_channel(int(echannelid))
        await echannel.send(embed=embed, view=view)
    elif interaction.data["custom_id"] == "payment_worked2":
        split = interaction.message.embeds[0].description.split("\n\n\n")
        ecid = split[1]
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        ccid = data[str(ecid)]["connect"]
        await interaction.message.delete()
        with open("./cogs/db/wasgeht.json", "r") as f:
            data = json.load(f)
        data[str(ecid)] = "b"
        with open("./cogs/db/wasgeht.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/payments.json", "r") as f:
            data = json.load(f)
        n = data[str(ecid)]["n"]
        amount = data[str(ecid)][str(n)]["amount"]
        data[str(ecid)][str(n)]["status"] = "Z"
        with open("./cogs/db/payments.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/finanzen.json", "r") as f:
            data = json.load(f)
            ank = int(amount)*92/100-0.49
            ges = 97*ank/100-0.49
            gesamt = data["Gesamt"]
            gesamt -= ank
            data["Gesamt"] = gesamt
            p = data["p"]
            g = p * ank
            schulden = data["Schulden"]
            schulden -= g
            data["Schulden"] = schulden
            cspendings = data["Cspendings"]
            cspendings -= ges
            data["Cspendings"] = cspendings
        with open("./cogs/db/finanzen.json", "w") as f:
            json.dump(data, f, indent=4)
        button1=Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="cdeletecom2")
        button2=Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="edeletecom2")
        button1.callback = None
        button2.callback = None
        view1=View(timeout=None)
        view1.add_item(button1)
        view2=View(timeout=None)
        view2.add_item(button2)
        embed1 = nextcord.Embed(description="You received your money back. You can close this chat by clicking on 'delete'.", color=0x35C5FF)
        embed2 = nextcord.Embed(description="The time you specified expired without completing the project with the !happy command. The client has asked for their money back. This project is therefore terminated. You can close this chat by clicking on 'delete'.", color=0x35C5FF)
        cchat = client.get_channel(ccid)
        cmsg = await cchat.send(embed=embed1, view=view1)
        echat = client.get_channel(int(ecid))
        emsg = await echat.send(embed=embed2, view=view2)
        with open("./cogs/db/delete-in-der-communication.json", "r") as f:
            data = json.load(f)
        data[str(cchat.id)] = str(cmsg.id)
        data[str(ecid)] = str(emsg.id)
        with open("./cogs/db/delete-in-der-communication.json", "w") as f:
            json.dump(data, f, indent=4)
    elif interaction.data["custom_id"] == "payment_didnt_work2":
        split = interaction.message.embeds[0].description.split("\n\n\n")
        ecid = split[1]
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        ccid = data[str(ecid)]["connect"]
        await interaction.message.delete()
        button=Button(label="Enter", style=nextcord.ButtonStyle.blurple, custom_id="money-back")
        button.callback = None
        view=View(timeout=None)
        view.add_item(button)
        embed=nextcord.Embed(description="The payment did not work. Please enter a valid email address which is associated with your PayPal account.", color=0x35C5FF)
        cchannel = client.get_channel(int(ccid))
        await cchannel.send(embed=embed, view=view)
    elif interaction.data["custom_id"] == "payment_worked3":
        split = interaction.message.embeds[0].description.split("\n\n\n")
        ecid = split[1]
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        ccid = data[str(ecid)]["connect"]
        await interaction.message.delete()
        with open("./cogs/db/wasgeht.json", "r") as f:
            data = json.load(f)
        data[str(ecid)] = "b"
        with open("./cogs/db/wasgeht.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/payments.json", "r") as f:
            data = json.load(f)
        n = data[str(ecid)]["n"]
        amount = data[str(ecid)][str(n)]["amount"]
        data[str(ecid)][str(n)]["status"] = "Z"
        with open("./cogs/db/payments.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/finanzen.json", "r") as f:
            data = json.load(f)
            ank = int(amount)*92/100-0.49
            ges = 97*ank/100-0.49
            gesamt = data["Gesamt"]
            gesamt -= ank
            data["Gesamt"] = gesamt
            p = data["p"]
            g = p * ank
            schulden = data["Schulden"]
            schulden -= g
            data["Schulden"] = schulden
            cspendings = data["Cspendings"]
            cspendings -= ges
            data["Cspendings"] = cspendings
        with open("./cogs/db/finanzen.json", "w") as f:
            json.dump(data, f, indent=4)
        button1=Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="cdeletecom4")
        button2=Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="edeletecom4")
        button1.callback = None
        button2.callback = None
        view1=View(timeout=None)
        view1.add_item(button1)
        view2=View(timeout=None)
        view2.add_item(button2)
        embed1 = nextcord.Embed(description="You received your money back. You can close this chat by clicking on 'delete'.", color=0x35C5FF)
        embed2 = nextcord.Embed(description="The client was not satisfied with your work. A supporter then judged the work as insufficient and the client got their money back. This project is therefore terminated. You can close this chat by clicking on 'delete'.", color=0x35C5FF)
        cchat = client.get_channel(int(ccid))
        cmsg = await cchat.send(embed=embed1, view=view1)
        echat = client.get_channel(int(ecid))
        emsg = await echat.send(embed=embed2, view=view2)
        with open("./cogs/db/delete-in-der-communication.json", "r") as f:
            data = json.load(f)
        data[str(ccid)] = str(cmsg.id)
        data[str(ecid)] = str(emsg.id)
        with open("./cogs/db/delete-in-der-communication.json", "w") as f:
            json.dump(data, f, indent=4)
    elif interaction.data["custom_id"] == "payment_didnt_work3":
        split = interaction.message.embeds[0].description.split("\n\n\n")
        ecid = split[1]
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        ccid = data[str(ecid)]["connect"]
        await interaction.message.delete()
        button=Button(label="Enter", style=nextcord.ButtonStyle.blurple, custom_id="happy-entermb")
        button.callback = None
        view=View(timeout=None)
        view.add_item(button)
        embed=nextcord.Embed(description="The payment did not work. Please enter a valid email address which is associated with your PayPal account.", color=0x35C5FF)
        cchannel = client.get_channel(ccid)
        await cchannel.send(embed=embed, view=view)
    elif interaction.data["custom_id"] == "payment_worked4":
        split = interaction.message.embeds[0].description.split("\n\n\n")
        echannelid = split[1]
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        cchannelid = data[str(echannelid)]["connect"]
        await interaction.message.delete()
        with open("./cogs/db/expertzahlinfos.json", "r") as f:
            data = json.load(f)
        del data[str(echannelid)]
        with open("./cogs/db/expertzahlinfos.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/wasgeht.json", "r") as f:
            data = json.load(f)
        data[str(echannelid)] = "b"
        with open("./cogs/db/wasgeht.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/payments.json", "r") as f:
            data = json.load(f)
        n = data[str(echannelid)]["n"]
        amount = data[str(echannelid)][str(n)]["amount"]
        data[str(echannelid)][str(n)]["status"] = str(datetime.now())
        with open("./cogs/db/payments.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/finanzen.json", "r") as f:
            data = json.load(f)
            ank = int(amount)*92/100-0.49
            ges = 97*90*ank/10000-0.49
            gesamt = data["Gesamt"]
            gesamt -= 90*ank/100
            data["Gesamt"] = gesamt
            p = data["p"]
            schulden = data["Schulden"]
            schulden -= 90*ank/100
            data["Schulden"] = schulden
            Gewinn = data["Gewinn"]
            Gewinn += (1 - 90/100)*ank
            data["Gewinn"] = Gewinn
            Eearnings = data["Eearnings"]
            Eearnings += ges
            data["Eearnings"] = Eearnings
        with open("./cogs/db/finanzen.json", "w") as f:
            json.dump(data, f, indent=4)
        button1=Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="cdeletecom2")
        button2=Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="edeletecom2")
        button1.callback = None
        button2.callback = None
        view1=View(timeout=None)
        view1.add_item(button1)
        view2=View(timeout=None)
        view2.add_item(button2)
        embed1 = nextcord.Embed(description="The Expert was successfully paid. This project is hereby completed. You can close the chat by clicking 'delete'.", color=0x35C5FF)
        embed2 = nextcord.Embed(description="You have been paid successfully. You can close this chat by clicking on 'delete'.", color=0x35C5FF)
        cchat = client.get_channel(cchannelid.id)
        cmsg = await cchat.send(embed=embed1, view=view1)
        echat = client.get_channel(int(echannelid))
        emsg = await echat.send(embed=embed2, view=view2)
        with open("./cogs/db/delete-in-der-communication.json", "r") as f:
            data = json.load(f)
        data[str(cchat.id)] = str(cmsg.id)
        data[str(echannelid)] = str(emsg.id)
        with open("./cogs/db/delete-in-der-communication.json", "w") as f:
            json.dump(data, f, indent=4)
    elif interaction.data["custom_id"] == "payment_didnt_work4":
            split = interaction.message.embeds[0].description.split("\n\n\n")
            echannelid = split[1]
            await interaction.message.delete()
            button=Button(label="Enter", style=nextcord.ButtonStyle.blurple, custom_id="enter7")
            button.callback = None
            view=View(timeout=None)
            view.add_item(button)
            with open("./cogs/db/chats.json", "r") as f:
                data = json.load(f)
            echannel = client.get_channel(int(echannelid))
            embed = nextcord.Embed(description="The payment did not work. Please enter a valid email address which is associated with your PayPal account.", color=0x35C5FF)
            await echannel.send(embed=embed, view=view)
    elif interaction.data["custom_id"] == "payment_worked5":
        split = interaction.message.embeds[0].description.split("\n\n\n")
        echannelid = split[1]
        await interaction.message.delete()
        with open("./cogs/db/expertzahlinfos.json", "r") as f:
            data = json.load(f)
        del data[str(echannelid)]
        with open("./cogs/db/expertzahlinfos.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/wasgeht.json", "r") as f:
            data = json.load(f)
        data[str(echannelid)] = "b"
        with open("./cogs/db/wasgeht.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/payments.json", "r") as f:
            data = json.load(f)
        n = data[str(echannelid)]["n"]
        amount = data[str(echannelid)][str(n)]["amount"]
        data[str(echannelid)][str(n)]["status"] = str(datetime.now())
        with open("./cogs/db/payments.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/finanzen.json", "r") as f:
            data = json.load(f)
            ank = int(amount)*92/100-0.49
            ges = 97*90*ank/10000-0.49
            gesamt = data["Gesamt"]
            gesamt -= 90*ank/100
            data["Gesamt"] = gesamt
            p = data["p"]
            schulden = data["Schulden"]
            schulden -= 90*ank/100
            data["Schulden"] = schulden
            Gewinn = data["Gewinn"]
            Gewinn += (1 - 90/100)*ank
            data["Gewinn"] = Gewinn
            Eearnings = data["Eearnings"]
            Eearnings += ges
            data["Eearnings"] = Eearnings
        with open("./cogs/db/finanzen.json", "w") as f:
            json.dump(data, f, indent=4)
        button1=Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="cdeletecom2")
        button2=Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="edeletecom2")
        button1.callback = None
        button2.callback = None
        view1=View(timeout=None)
        view1.add_item(button1)
        view2=View(timeout=None)
        view2.add_item(button2)
        embed1 = nextcord.Embed(description="The Expert was successfully paid. This project is hereby completed. You can close the chat by clicking 'delete'.", color=0x35C5FF)
        embed2 = nextcord.Embed(description="The client has rated your work as satisfactory. You have been paid successfully. You can close this chat by clicking on 'delete'.", color=0x35C5FF)
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        cchannelid3 = data[str(echannelid)]["connect"]
        cchat = client.get_channel(int(cchannelid3))
        cmsg = await cchat.send(embed=embed1, view=view1)
        echat = client.get_channel(int(echannelid))
        emsg = await echat.send(embed=embed2, view=view2)
        with open("./cogs/db/delete-in-der-communication.json", "r") as f:
            data = json.load(f)
        data[str(cchannelid3)] = str(cmsg.id)
        data[str(echannelid)] = str(emsg.id)
        with open("./cogs/db/delete-in-der-communication.json", "w") as f:
            json.dump(data, f, indent=4)
    elif interaction.data["custom_id"] == "payment_didnt_work5":
        split = interaction.message.embeds[0].description.split("\n\n\n")
        echannelid = split[1]
        await interaction.message.delete()
        button=Button(label="Enter", style=nextcord.ButtonStyle.blurple, custom_id="enter7")
        button.callback = None
        view=View(timeout=None)
        view.add_item(button)
        echannel = client.get_channel(int(echannelid))
        embed=nextcord.Embed(description="The payment did not work. Please enter a valid email address which is associated with your PayPal account.", color=0x35C5FF)
        await echannel.send(embed=embed, view=view)
    elif interaction.data["custom_id"] == "payment_worked6":
        split = interaction.message.embeds[0].description.split("\n\n\n")
        echannelid = split[1]
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        cchannelid = data[str(echannelid)]["connect"]
        await interaction.message.delete()
        with open("./cogs/db/expertzahlinfos.json", "r") as f:
            data = json.load(f)
        del data[str(echannelid)]
        with open("./cogs/db/expertzahlinfos.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/wasgeht.json", "r") as f:
            data = json.load(f)
        data[str(echannelid)] = "b"
        with open("./cogs/db/wasgeht.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/payments.json", "r") as f:
            data = json.load(f)
        n = data[str(echannelid)]["n"]
        amount = data[str(echannelid)][str(n)]["amount"]
        data[str(echannelid)][str(n)]["status"] = str(datetime.now())
        with open("./cogs/db/payments.json", "w") as f:
            json.dump(data, f, indent=4)
        with open("./cogs/db/finanzen.json", "r") as f:
            data = json.load(f)
            ank = int(amount)*92/100-0.49
            ges = 97*90*ank/10000-0.49
            gesamt = data["Gesamt"]
            gesamt -= 90*ank/100
            data["Gesamt"] = gesamt
            p = data["p"]
            schulden = data["Schulden"]
            schulden -= 90*ank/100
            data["Schulden"] = schulden
            Gewinn = data["Gewinn"]
            Gewinn += (1 - 90/100)*ank
            data["Gewinn"] = Gewinn
            Eearnings = data["Eearnings"]
            Eearnings += ges
            data["Eearnings"] = Eearnings
        with open("./cogs/db/finanzen.json", "w") as f:
            json.dump(data, f, indent=4)
        button1=Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="cdeletecom2")
        button2=Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="edeletecom2")
        button1.callback = None
        button2.callback = None
        view1=View(timeout=None)
        view1.add_item(button1)
        view2=View(timeout=None)
        view2.add_item(button2)
        embed1 = nextcord.Embed(description="You have not answered for three days. Therefore the Expert was paid. This project is hereby completed. You can close the chat by clicking 'delete'.", color=0x35C5FF)
        embed2 = nextcord.Embed(description="The client did not answer for three days. Therefore you received your money. This project is hereby completed. You can close the chat by clicking 'delete'.", color=0x35C5FF)
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        cchannelid3 = data[str(cchannelid)]["connect"]
        cchat = client.get_channel(int(cchannelid3))
        cmsg = await cchat.send(embed=embed1, view=view1)
        echat = client.get_channel(int(echannelid))
        emsg = await echat.send(embed=embed2, view=view2)
        with open("./cogs/db/delete-in-der-communication.json", "r") as f:
            data = json.load(f)
        data[str(cchannelid3)] = str(cmsg.id)
        data[str(echannelid)] = str(emsg.id)
        with open("./cogs/db/delete-in-der-communication.json", "w") as f:
            json.dump(data, f, indent=4)
    elif interaction.data["custom_id"] == "payment_didnt_work6":
        split = interaction.message.embeds[0].description.split("\n\n\n")
        echannelid = split[1]
        await interaction.message.delete()   
        button=Button(label="Enter", style=nextcord.ButtonStyle.blurple, custom_id="enter8")
        button.callback = None
        view=View(timeout=None)
        view.add_item(button)
        echannel = client.get_channel(int(echannelid))
        embed=nextcord.Embed(description="The payment did not work. Please enter a valid email address which is associated with your PayPal account.", color=0x35C5FF)
        await echannel.send(embed=embed, view=view)

@client.command()
@commands.has_permissions(administrator=True)
async def ccontact_support(ctx):
    await ctx.message.delete()
    button=Button(label="Contact Support", style=nextcord.ButtonStyle.blurple, custom_id="cs")
    button.callback = None
    view=View(timeout=None)
    view.add_item(button)
    embed1 = nextcord.Embed(description="**Here you can find frequently asked questions:**", color=0x35C5FF)
    await ctx.send(embed=embed1)
    embed2 = nextcord.Embed(description="***What is the mission of THAROS?***\nThe mission of THAROS is to reconnect freelancers and clients for online services. THAROS wants to create a market for freelancers worldwide and offer clients numerous, easily accessible online services. Diversity of offerings and maximum client support are the top priorities.", color=0x35C5FF)
    await ctx.send(embed=embed2)
    embed3 = nextcord.Embed(description="***How can I connect with an Expert?***\nA client can either [post their own job](https://discord.com/channels/1004869688251134033/1009804668299395123) or find exciting [work offers from Experts](https://discord.com/channels/1004869688251134033/1009848187646910476). If the interests of the client and the Expert coincide, a separate channel is created for both.", color=0x35C5FF)
    await ctx.send(embed=embed3)
    embed4 = nextcord.Embed(description="***How can I pay?***\nAn Expert sends an invoice before starting work. If the client pays this invoice, the money goes to THAROS in full. This guarantees the client that they can get their money back in case of poor work performance. When the Expert sends an invoice, the client must confirm the amount and the working time of the Expert.", color=0x35C5FF)
    await ctx.send(embed=embed4)
    embed5 = nextcord.Embed(description="***How can I get my money back if the Expert does not start the work?***\nIf the working time has expired and the client has not received the work, they can ask for their money back.", color=0x35C5FF)
    await ctx.send(embed=embed5)
    embed6 = nextcord.Embed(description="***When will the Expert be paid?***\nWhen the work is completed the Expert asks for the clients satisfaction with the result. If a client indicates their satisfaction, the Expert receives the money and the job is completed.", color=0x35C5FF)
    await ctx.send(embed=embed6)
    embed7 = nextcord.Embed(description="***How do I get my money back if I am dissatisfied with the work?***\nIf the client is dissatisfied with the work, a supporter will decide whether they get the money back.", color=0x35C5FF)
    await ctx.send(embed=embed7)
    embed8 = nextcord.Embed(description="***Can I do multiple projects with the same Expert?***\nYes! Any number of jobs can be done in one chat.", color=0x35C5FF)
    await ctx.send(embed=embed8)
    embed9 = nextcord.Embed(description="***How can I register as an Expert?***\nClients can easily register as an Expert at THAROS by answering some questions and providing personal data. An Expert has the opportunity to connect with a client and earn money with their work.", color=0x35C5FF)
    await ctx.send(embed=embed9)
    embed10 = nextcord.Embed(description="***What does the Expert's star rating mean?***\nAfter a successfull project, the client can give the Expert a star rating. Star rating is a way to evaluate the quality of work performance. The star rating goes from one to five.", color=0x35C5FF)
    await ctx.send(embed=embed10, view=view)

@client.command()
@commands.has_permissions(administrator=True)
async def econtact_support(ctx):
    await ctx.message.delete()
    button=Button(label="Contact Support", style=nextcord.ButtonStyle.blurple, custom_id="cs")
    button.callback = None
    view=View(timeout=None)
    view.add_item(button)
    embed1 = nextcord.Embed(description="**Here you can find frequently asked questions:**", color=0x35C5FF)
    await ctx.send(embed=embed1)
    embed2 = nextcord.Embed(description="***What is the mission of THAROS?***\nThe mission of THAROS is to reconnect freelancers and clients for online services. THAROS wants to create a market for freelancers worldwide and offer clients numerous, easily accessible online services. Diversity of offerings and maximum client support are the top priorities.", color=0x35C5FF)
    await ctx.send(embed=embed2)
    embed3 = nextcord.Embed(description="***How can I connect with a client?***\nAn Expert can connect with a client by applying for a [job offer](https://discord.com/channels/1004869688251134033/1009849070933782560) or posting a [work offer](https://discord.com/channels/1004869688251134033/1071866897622114415) themself. In both cases, clients can see their star rating. This is issued by clients after a successful job.", color=0x35C5FF)
    await ctx.send(embed=embed3)
    embed4 = nextcord.Embed(description="***How can I send an invoice to the client?***\nThe command !pay creates an invoice for the client. This command is sent once an agreement has been reached with the client and before the Expert starts the work. The Expert will be asked for the amount and the maximum time to complete the project.", color=0x35C5FF)
    await ctx.send(embed=embed4)
    embed5 = nextcord.Embed(description="***What happens after the working time I specified has expired?***\nThe Expert must submit their work to the client within this time and send the !happy command. Otherwise, the client can ask for their money back.", color=0x35C5FF)
    await ctx.send(embed=embed5)
    embed6 = nextcord.Embed(description="***When can I receive my money?***\nAfter the Expert has submitted their work to the client, they can receive their money using the !happy command. Then the client is asked if they are satisfied with the project. If the client is satisfied, the Expert receives their money immediately. If the client does not respond to !happy, the Expert will receive their money after three days.", color=0x35C5FF)
    await ctx.send(embed=embed6)
    embed7 = nextcord.Embed(description="***What happens if the client is dissatisfied?***\nIf the client is not satisfied, they can call a supporter. The supporter decides about the refund of the money.", color=0x35C5FF)
    await ctx.send(embed=embed7)
    embed8 = nextcord.Embed(description="***Can I do multiple projects with the same client?***\nYes! Any number of jobs can be done in one chat.", color=0x35C5FF)
    await ctx.send(embed=embed8)
    embed9 = nextcord.Embed(description="***What does my star rating mean?***\nAfter a successfull project, the client can give the Expert a star rating. Star rating is a way to evaluate the quality of work performance. The star rating goes from one to five. The own star rating can be viewed with the command !mystars.", color=0x35C5FF)
    await ctx.send(embed=embed9)
    embed = nextcord.Embed(description="***How can I quit my status as an Expert?***\nThe status as an Expert can be quit at any time, under the condition that all jobs are completed and all chats with clients are closed.", color=0x35C5FF)
    await ctx.send(embed=embed, view=view)

@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.content != "!pay":
        if message.content != "!happy":
            if message.content != "!mystars":
                with open("./cogs/db/chats.json", "r") as f:
                    data = json.load(f)
                if not message.author.bot:
                    if str(message.channel.id) in data:
                        print("yes")
                        connected = data[str(message.channel.id)]["connect"]
                        channel = client.get_channel(int(connected))
                        try:
                            await channel.send(message.attachments[0])
                            await channel.send(message.content)
                        except:
                            await channel.send(message.content)


@client.command()
async def translate(ctx, lang, *, prompt):
    auth_key = "REDACTED_DEEPL_KEY"
    translator = deepl.Translator(auth_key)
    result = translator.translate_text(prompt, target_lang=lang)
    await ctx.send(result.text)

@client.command()
@commands.has_permissions(administrator=True)
async def delete(ctx):
    c = client.get_channel(1009828164928807012)
    for channel in c.text_channels:
        await channel.delete()
    c2 = client.get_channel(1009811084380753941)
    for c3 in c2.text_channels:
        await c3.delete()
    c = client.get_channel(1009849070933782560)
    await c.purge(limit=99)
    c2 = client.get_channel(1009849089883635723)
    await c2.purge(limit=99)
    c = client.get_channel(1009849120879558847)
    await c.purge(limit=99)
    c2 = client.get_channel(1009849133470851072)
    await c2.purge(limit=99)
    c = client.get_channel(1009849146594824294)
    await c.purge(limit=99)
    c2 = client.get_channel(1009849160054345792)
    await c2.purge(limit=99)
    c = client.get_channel(1009849206904717352)
    await c.purge(limit=99)
    c2 = client.get_channel(1009849220502650960)
    await c2.purge(limit=99)
    c = client.get_channel(1009849240517869568)
    await c.purge(limit=99)
    c2 = client.get_channel(1009848187646910476)
    await c2.purge(limit=99)
    c = client.get_channel(1009848261303087115)
    await c.purge(limit=99)
    c2 = client.get_channel(1009848445693083690)
    await c2.purge(limit=99)
    c2 = client.get_channel(1009848723435683990)
    await c2.purge(limit=99)
    c = client.get_channel(1009848740628144200)
    await c.purge(limit=99)
    c2 = client.get_channel(1009848740628144200)
    await c2.purge(limit=99)
    c2 = client.get_channel(1009848510872559807)
    await c2.purge(limit=99)
    c = client.get_channel(1009848466568138862)
    await c.purge(limit=99)
    c2 = client.get_channel(1009848764925759632)
    await c2.purge(limit=99)

@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)


@client.command()
@commands.has_permissions(administrator=True)
async def embed(ctx, *, msg):
    try:
        if ctx.message.attachments[0]:
            print("Image")
            image = ctx.message.attachments[0]
            await ctx.message.delete()
            embed = nextcord.Embed(description=f"{msg}\n{image}", color=0x35C5FF)
            await ctx.send(embed=embed)
    except:
        await ctx.message.delete()
        embed = nextcord.Embed(description=f"{msg}", color=0x35C5FF)
        await ctx.send(embed=embed)

@client.command()
async def mystars(ctx):
    with open("./cogs/db/experts.json", "r") as f:
        data = json.load(f)
    stars2 = data[str(ctx.message.author.id)]["starrating"]
    stars = round(stars2, 2)
    await ctx.message.author.send(f"{stars}")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run("REDACTED_DISCORD_TOKEN")