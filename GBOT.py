import json
import discord
import os
from discord.ext import commands
from discord.utils import get

#Opening Data
with open('Json file dir')as jfile:
    data=json.load(jfile)
    temp=data


#saving Data
def write_json(data, filename='Json file dir'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

#checking if user exists in data
def check_json(authorID):
    with open('Json file dir')as jfile:
        data=json.load(jfile)
        for dataID in data:
            if(dataID['userID']==authorID):
                return True
        return False

client = commands.Bot(command_prefix='.')

#EVENTS
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Hello World'))
    print('Bot is ready')

#COMMANDS
@client.command()
@commands.has_role('Adm')
async def channel_del(ctx):
    with open('Json file dir')as jfile:
        data = json.load(jfile)
        new_data = []
        guild = ctx.guild
        for elem in data:
            if(elem['channelID']==ctx.message.channel.id):
                channel = discord.utils.get(guild.channels, id=elem['channelID'])
                await channel.delete()
            else:
                new_data.append(elem)
                write_json(new_data)
        


@client.command()
async def Help(ctx):
     with open('Json file dir')as jfile:
        data=json.load(jfile)
        temp=data
        if(check_json(ctx.message.author.id)==False):
            guild = ctx.guild
            user = ctx.message.author
            admin = get(guild.roles, name='adm rank')
            overwrites = {
                            guild.default_role: discord.PermissionOverwrite(read_messages=False),
                            guild.me: discord.PermissionOverwrite(read_messages=True),
                            user: discord.PermissionOverwrite(read_messages=True),
                            admin: discord.PermissionOverwrite(read_messages=True),
                        }
            channel = await guild.create_text_channel(f'Help-{ctx.message.author.name}', category=guild.get_channel(738015143732183062), overwrites=overwrites)
            y = {"userID":ctx.message.author.id, "channelID":channel.id}
            temp.append(y)
            write_json(data)
            await channel.send("Hi :)")
        else:
            await ctx.send("You already have help channel!")




client.run('TOKEN')
