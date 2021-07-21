import discord
import logiclayer as ll
from dotenv import load_dotenv
import os
import datetime as dt
import schedule
import threading
from discord.ext import tasks, commands


load_dotenv()
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
TOKEN = os.getenv('DISCORD_TOKEN')


@tasks.loop(hours=24)
async def dailycheck():
    print('Daily check launched!')
    today = dt.datetime.now()
    user = ll.geteventsoftheday(client, today.day, today.month)
    if user != None:
        print('Found birthday for user {0.name}'.format(user))
        present_in = ll.getuserservers(user, client.guilds)
        for server in present_in:
            print(' - Present in {0.name}!'.format(server))
            channel = ll.serverbinding(server)
            if channel != None:
                print(' --- Server {0.name} bound to channel {1.name}!'.format(server, channel))
                await channel.send('It\'s {0.mention}\'s birthday!'.format(user))


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    for guild in client.guilds:
        print(' - Connected to {0.name}'.format(guild))


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.lower().startswith('%kal fetch'):
        await message.channel.send('no lmao')

    if message.content.lower() == '%kal help':
        await ll.helpprompt(message.channel)

    if message.content.lower().startswith('%kal set'):
        if ll.handleaddition(message):
            await message.channel.send('{0.mention} Birthdate successfully registered!'.format(message.author))
        else:
            await message.channel.send('Wrong command syntax! Type %help or mention the bot for more informations')

    if len(message.mentions) == 1 and message.mentions[0] == client.user:
        await message.channel.send("Stfu, if ure lost just type '%kal help' u donkey")
        print('{0.author} : {1.id}'.format(message, message.author))


    if isinstance(message.author, discord.Member) and message.author.guild_permissions.administrator:
        if message.content.lower() == '%bind' and message.author.guild_permissions.administrator:
            ll.bindto(message.channel, message.guild)
            await message.channel.send('Event messages are now bound to the {0.channel.mention} channel!'.format(message))

        if message.content.lower() == '%channelbound' and message.author.guild_permissions.administrator:
            await message.channel.send('I am bound to the {0.mention} channel!'.format(ll.serverbinding(message.guild)))


dailycheck.start()
client.run(TOKEN)
