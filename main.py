import nextcord
from nextcord.ui import Select, View, Button, Modal
from nextcord.ext import commands
import json
import asyncio
import random
import os
import discord.utils
import deepl
client = commands.Bot(command_prefix="!", intents=nextcord.Intents.all())

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_interaction(interaction):
    print(interaction.type)
    if str(interaction.type) == "InteractionType.application_command":
        return
    if interaction.data["custom_id"] == "jocontact":
        with open("./cogs/db/buttoncheck.json", "r") as f:
            data = json.load(f)
        id  = interaction.user.id
        if str(interaction.message.id) not in data:
            data[str(interaction.message.id)] = []
            data[str(interaction.message.id)].append(interaction.user.id)
            can_continue = True
        else:
            users = data[str(interaction.message.id)]
            if interaction.user.id in users:
                can_continue = False
                await interaction.response.send_message('You have already applied for this job. It is not possible to apply a second time.', ephemeral=True)
            else:
                data[str(interaction.message.id)].append(interaction.user.id)
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
                application = nextcord.ui.TextInput(label="Tell the customer a few words about yourself", min_length=50, max_length=1000, required=True, placeholder=" ~ Application ~ ", style=nextcord.TextInputStyle.paragraph)
                Modal2.add_item(application)
                async def modal2_callback(interaction):
                    embed9 = nextcord.Embed(description=f"Your application for the job '{title}' has been successfully sent. As soon as the customer accepts it, you can chat with him.", color=0x0BBAB5)
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
                    embed = nextcord.Embed(description=f"An Expert has sent you an application for '{title}'. Find it under 'your Experts'.\n[View the channel](https://discord.com/channels/{interaction.guild.id}/{jpclientchannel.id})", color=0x0BBAB5)
                    await interaction.guild.get_member(int(client_id)).send(embed=embed)
                    btn = Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="jpapplicationdelete2")
                    view6 = View(timeout=None)
                    view6.add_item(btn)
                    embed = nextcord.Embed(description="You can now chat with the client. Please follow the rules, which you can find under [rules for Experts](https://discord.com/channels/1004869688251134033/1009830178211504148).\n\nIf you click on 'delete', the channel will be deleted. Please note, that after deleting, the communication can not be restored.", color=0x0BBAB5)
                    qq = await jpexpertchannel.send(embed=embed, view=view6)
                    embed2 = nextcord.Embed(description="Quick guide:\nafter you have reached an agreement with the customer, you can send him the invoice using the command /pay. When the customer has paid, you will recieve a confirmation and you can start working. When you are done, hand over the work to the customer and ask for his opinion with the command /happy. If the customer is satisfied, you recieve the money and the customer leaves you a star rating.\n\nYou can find more information here: [help for experts](https://discord.com/channels/1004869688251134033/1009849367760482455)", color=0x0BBAB5)
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
                    view55 = View(timeout=None)
                    view55.add_item(button12)
                    view55.add_item(button13)
                    embed3 = nextcord.Embed(description=f"{application.value}\n\nExpert's star review: {starrating}.\n\nIf you accept the Expert, then you can chat with them. If you click on 'delete', the channel will be deleted. This function is also available after accepting. Please note, that after deleting, the communication can not be restored.", color=0x0BBAB5)
                    mm = await jpclientchannel.send(embed=embed3, view=view55)
                    with open("./cogs/db/delete-in-der-communication.json", "r") as f:
                        data = json.load(f)
                    data[str(jpclientchannel)] = str(mm.id)
                    data[str(jpexpertchannel.id)] = str(qq.id)
                    with open("./cogs/db/delete-in-der-communication.json", "w") as f:
                        json.dump(data, f, indent=4)
                Modal2.callback = modal2_callback
                await interaction.response.send_modal(modal=Modal2)
            button99.callback = btn99_callback
            view3 = View(timeout=None)
            view3.add_item(button99)
            msg7 = await interaction.response.send_message("To apply for this job offer, tell the customer a few words about yourself. Most importantly, tell them what qualifies you for this job.", view=view3, ephemeral=True)
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
        await interaction.response.defer()
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
        contents = interaction.message.content.split(" ")
        id = contents[1]
        user = await interaction.guild.fetch_member(int(id))
        role = discord.utils.get(client.get_guild(1004869688251134033).roles, id=1004884670745411595)
        await user.add_roles(role)
        role = discord.utils.get(client.get_guild(1004869688251134033).roles, id=1005230473599008898)
        await user.remove_roles(role)
        await user.send("You are now successfully registered with Tharos as an Expert")
        await interaction.message.delete()
    elif interaction.data["custom_id"] == "expertdeny":
        contents = interaction.message.content.split(" ")
        id = contents[1]
        with open("./cogs/db/experts.json", "r") as f:
            data = json.load(f)
        del data[str(id)]
        with open("./cogs/db/experts.json", "w") as f:
            json.dump(data, f, indent=4)
        user = await interaction.guild.fetch_member(int(id))
        await user.send("Your registration as an Expert has been rejected. You can try again at any time")
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
        embed2 = nextcord.Embed(description=f"Your application for the job '{job_title}' has been accepted. You can now chat with the customer\n[View the channel](https://discord.com/channels/{interaction.guild.id}/{int(connected_channel)})", color=0x0BBAB5)
        await expert.send(embed=embed2)
        button = Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="jpapplicationdelete2")
        button.callback = None
        view = View(timeout=None)
        view.add_item(button)
        embed = nextcord.Embed(description="You can now chat with the Expert. Please follow the rules which you can find under [rules](https://discord.com/channels/1004869688251134033/1009830091192283206). More information for clients can be found at [help for clients](https://discord.com/channels/1004869688251134033/1009849321614737469).\nYou can delete the channel at any time, but after deleting, there is no way to restore the communication.", color=0x0BBAB5)
        await interaction.message.edit("", embed=embed, view=view)
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
        message = interaction.message.id
        buttonyes = Button(label="I am sure I want to delete it", style=nextcord.ButtonStyle.red, custom_id="jpexpertdelete")
        view = View(timeout=None)
        view.add_item(buttonyes)
        button2 = Button(label="<", style=nextcord.ButtonStyle.blurple, custom_id="jpdeleteback2", disabled=False)
        view5 = View(timeout=None)
        view5.add_item(buttonyes)
        view5.add_item(button2)
        t = interaction.message.content
        msg99 = await interaction.message.edit(interaction.message.content, view = view5)
    elif interaction.data["custom_id"] == "jpdeleteback2":
        button3 = Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="jpapplicationdelete2", disabled=False)
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
        await expert.send(f"A customer has broken off communication with you on the subject '{interaction.channel.name}'. The project is therefore terminated.")
        await interaction.channel.delete()
        await expertchannel.delete()
        del data[str(interaction.channel.id)]
        del data[str(expertchannel_id)]
        with open("./cogs/db/chats.json", "w") as f:
            json.dump(data, f, indent=4)
    elif interaction.data["custom_id"] == "jpexpertdelete":
        with open("./cogs/db/chats.json", "r") as f:
            data = json.load(f)
        clientchannel_id = data[str(interaction.channel.id)]["connect"]
        clientchannel = client.get_channel(int(clientchannel_id))
        clientid = data[str(clientchannel_id)]["owner"]
        client1 = interaction.guild.get_member(int(clientid))
        await client1.send(f"An Expert has broken off communication with you on the subject '{interaction.channel.name}'. The project is therefore terminated.")
        await interaction.channel.delete()
        await clientchannel.delete()
        del data[str(interaction.channel.id)]
        del data[str(clientchannel_id)]
        with open("./cogs/db/chats.json", "w") as f:
            json.dump(data, f, indent=4)
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
                await interaction.response.send_message('You have already contacted the Expert for this work offer. This is not possible twice.', ephemeral=True)
            else:
                data[str(interaction.message.id)].append(interaction.user.id)
                can_continue = True
        with open("./cogs/db/buttoncheck.json", "w") as f:
            json.dump(data, f, indent=4)
        if can_continue == True:
            await interaction.response.defer()
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
            embed = nextcord.Embed(description=f"You are now connected with an Expert for the offer '{interaction.message.embeds[0].title}'. Find the channel under 'your Experts'. [view the channel](https://discord.com/channels/{interaction.guild.id}/{owclientchannel.id})", color=0x0BBAB5)
            await interaction.user.send(embed=embed)
            embed23 = nextcord.Embed(description=f"A client has shown interest in your offer '{interaction.message.embeds[0].title}'. You are now connected with the client. Find the channel under 'your Clients'. [view the channel](https://discord.com/channels/{interaction.guild.id}/{owexpertchannel.id})", color=0x0BBAB5)
            expert = interaction.guild.get_member(int(expert_id))
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
            button2 = Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="owclientdelete", disabled=False)
            button2.callback = None
            view = View(timeout=None)
            view.add_item(button2)
            embed1 = nextcord.Embed(description="You can now chat with the Expert. Please follow the rules, which you can find under [rules for clients](https://discord.com/channels/1004869688251134033/1009830091192283206). More information for clients can be found at [help for clients](https://discord.com/channels/1004869688251134033/1009849321614737469). If you click on 'Delete', the channel will be deleted. Please note, that after deleting, the communication can not be restored.", color=0x0BBAB5)
            mm = await owclientchannel.send(embed=embed1, view=view)
            button3 = Button(label="Delete", style=nextcord.ButtonStyle.red, custom_id="owexpertdelete")
            button3.callback = None
            view2 = View(timeout=None)
            view2.add_item(button3)
            embed2 = nextcord.Embed(description="You can now chat with the client. Please follow the rules, which you can find under [rules for Experts](https://discord.com/channels/1004869688251134033/1009830178211504148)", color=0x0BBAB5)
            qq = await owexpertchannel.send(embed=embed2, view=view2)
            embed2 = nextcord.Embed(
                description="Quick guide:\nafter you have reached an agreement with the customer, you can send him the invoice using the command /pay. When the customer has paid, you will recieve a confirmation and you can start working. When you are done, hand over the work to the customer and ask for his opinion with the command /happy. If the customer is satisfied, you recieve the money and the customer leaves you a star rating.\n\nYou can find more information here: [help for experts](https://discord.com/channels/1004869688251134033/1009849367760482455)",
                color=0x0BBAB5)
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
        embed = nextcord.Embed(description=f"A customer has broken off communication with you on the subject '{interaction.channel.name}'. The project is therefore terminated.", color=0x0BBAB5)
        await expert.send(embed = embed)
        await interaction.channel.delete()
        await expertchannel.delete()
        del data[str(interaction.channel.id)]
        del data[str(expertchannel_id)]
        with open("./cogs/db/chats.json", "w") as f:
            json.dump(data, f, indent=4)
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
        embed = nextcord.Embed(description=f"An Expert has broken off communication with you on the subject '{interaction.channel.name}'. The project is therefore terminated.", color=0x0BBAB5)
        await client2.send(embed = embed)
        await interaction.channel.delete()
        await clientchannel.delete()
        del data[str(interaction.channel.id)]
        del data[str(clientchannel_id)]
        with open("./cogs/db/chats.json", "w") as f:
            json.dump(data, f, indent=4)
    elif interaction.data["custom_id"] == "pay-enter":
        Modal1 = Modal(
            custom_id="pay-modal",
            title="Payment",
            timeout=None,
            auto_defer=True
        )
        with open("./cogs/db/wgzn.json", "r") as f:
            data = json.load(f)
        amount = nextcord.ui.TextInput(label="Amount in USD", min_length=1, max_length=4, required=True, style=nextcord.TextInputStyle.paragraph)
        Modal1.add_item(amount)
        global time
        time = nextcord.ui.TextInput(label="Maximum time in days", min_length=1, max_length=2, required=True, style=nextcord.TextInputStyle.paragraph)
        Modal1.add_item(time)
        async def modal_callback(interaction):
            print(amount.value)
            print(time.value)
            try:
                print(int(amount.value))
                int(amount.value)
                int(time.value)
                if int(amount.value) < 1 or int(time.value) < 1:
                    button = Button(label="Enter", style=nextcord.ButtonStyle.blurple, custom_id="pay-enter")
                    button.callback = None
                    view=View(timeout=None)
                    view.add_item(button)
                    await interaction.channel.send("The amount or time you entered is/are not an integer above 0. Please try again.", view=view)
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
                    embed = nextcord.Embed(description=f"Please confirm the following data so that an invoice can be created:\nThe price for this project is {amount.value}$.\nThe Expert has indicated to complete the project within {time.value} days.\nNote that you can claim your money back only after this time.", color=0x0BBAB5)
                    await channel.send(embed=embed, view=view)
            except:
                button = Button(label="Enter", style=nextcord.ButtonStyle.blurple, custom_id="pay-enter")
                button.callback = None
                view=View(timeout=None)
                view.add_item(button)
                await interaction.channel.send("The amount and time have to be an integer above 0. Please try again.", view=view)
        Modal1.callback = modal_callback
        await interaction.response.send_modal(modal=Modal1)
        await interaction.message.delete()
        
    elif interaction.data["custom_id"] == "pay-confirm":
        await interaction.message.delete()
        embed = nextcord.Embed(description=f"The Expert has sent you an invoice. You can pay it through the link below. After your payment the Expert will start working.\nIf the Expert does not finish the work in {time.value} days after your payment, you can report him and get your money back.\nLINK\n", color=0x0BBAB5)
        await interaction.channel.send(embed=embed)
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
        await channel.send("The customer has rejected the data you have entered. Please come to an agreement with the customer and enter the data again.", view=view)





@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.content != "!pay":
        if message.content != "!happy":
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
    auth_key = "68aec437-4999-8215-be80-d8cb28fe54b3:fx"
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


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run("MTA0OTQwMzI5ODUwMDgzNzM3Nw.GTJ3qY.V2z-SvnK9Mt8-78UokawKay1mNiNPAVnEN5YNU")