import discord
import logiclayer as ll
from dotenv import load_dotenv
import os


load_dotenv()
client = discord.Client()
TOKEN = os.getenv('DISCORD_TOKEN')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    for guild in client.guilds:
        print(' - Connected to {0.name}'.format(guild) )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # When an administrator uses the "%bindto" command
    if message.content.lower() == '%bind' and message.author.guild_permissions.administrator:
        ll.bindto(message.channel, message.guild)
        await message.channel.send('Event messages are now bound to the {0.channel.mention} channel!'.format(message))
        #await message.channel.send('{0.author.mention} I got access to this channel!'.format(message))

    if len(message.mentions) > 0 and message.mentions[0] == client.user:
        await message.channel.send("Stfu")


client.run(TOKEN)
