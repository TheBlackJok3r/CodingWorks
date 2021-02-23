import json
import discord
import os
from discord.ext import commands

#Opening Data
with open('DIRECTORY TO JSON FILE')as jfile:
    data=json.load(jfile)
    temp=data["user"]


#saving Data
def write_json(data, filename='DIRECTORY TO JSON FILE'):
    with open(filename, "w") as f:
        json.dump(data, f, indent=3)

#checking if user exists in data
def check_json(authorID):
    for dataID in data["user"]:
        if(dataID["userID"]==authorID):
            return True
    return False

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Hello World'))
    print('Bot is ready')

@client.command()
async def pomoc(ctx):
    if(check_json(ctx.message.author.id)==False):
        guild = ctx.message.guild
        await guild.create_text_channel(f'Pomoc-{ctx.message.author.name}', category=guild.get_channel(738015143732183062))
        y={"userID":ctx.message.author.id}
        temp.append(y)
        write_json(data)
    else:
        await ctx.send("Masz już aktywny kanał pomocy!")



client.run('TOKEN')
