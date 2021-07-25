import discord
from discord.ext import tasks, commands
from dotenv import load_dotenv
import logiclayer as ll
import datetime as dt
import os
#import schedule
#import threading


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


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
    print('Bot logged as: {0.user}'.format(client))
    for guild in client.guilds:
        print('  - Connected to {0.name}'.format(guild))
    print('\n')


@client.event
async def on_message(message):

    # To avoid message analysis recursion.
    if message.author == client.user:
        return

    # '%kal fetch @user' command. Sends a user's birth date. (TO BE IMPLEMENTED)
    if message.content.lower().startswith('%kal fetch') and len(message.mentions) == 1:
        target = message.mentions[0]
        date = ll.getbirthday(target)
        if date == None:
            await message.channel.send('no lmao')
        else:
            await message.channel.send('{0.mention}\'s birthday is on {1}!'.format(target, date))

    # '%kal help' command. Sends back the commands list.
    if message.content.lower() == '%kal help':
        await ll.helpprompt(message.channel)

    # '%kal set xx/yy(/zzzz) {EU/US}' command. Registers xx/yy(/zzzz) as the author's birth date.
    if message.content.lower().startswith('%kal set'):
        if ll.handleaddition(message):
            await message.channel.send('{0.mention} Birthdate successfully registered!'.format(message.author))
        else:
            await message.channel.send('Wrong command syntax! Type %kal help or mention the bot for more informations')

    # Action to perform when the bot is mentionned.
    if len(message.mentions) == 1 and message.mentions[0] == client.user:
        await message.channel.send("Stfu, if ure lost just type '%kal help' u donkey")
        print('{0.author} : {1.id}'.format(message, message.author))


    # Server administrators' commands:
    if isinstance(message.author, discord.Member) and message.author.guild_permissions.administrator:
        # '%bind' command. The channel in which it was posted will be saved for upcoming event messages.
        if message.content.lower() == '%bind':
            ll.bindto(message.channel, message.guild)
            await message.channel.send('Event messages are now bound to the {0.channel.mention} channel!'.format(message))

        # '%channelbound' command. Will return the channel to which the bot is bound in the current server.
        if message.content.lower() == '%channelbound':
            channelbound = ll.serverbinding(message.guild)
            if channelbound != None:
                await message.channel.send('I am bound to the {0.mention} channel!'.format(ll.serverbinding(message.guild)))
            else:
                await message.channel.send('I am not bound to any channel yet!')


dailycheck.start()
client.run(TOKEN)
