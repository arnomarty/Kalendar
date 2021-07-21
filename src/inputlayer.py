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


def smallbrain(date):
    if len(date) != 3 and len(date) != 2:
        return True
    for i in date:
        if not i.isdigit():
            return True
    if len(date) != 2 and int(date[2]) > dt.datetime.now().year - 4:
        return True
    return False


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
        print(' - Connected to {0.name}'.format(guild) )


@client.event
async def on_message(message):

    if message.author == client.user:
        return


    if message.content.lower().startswith('%test birthday'):
        print("I'm in!")
        cmd = message.content.lower().split()
        if len(cmd) != 4:
            await message.channel.send('Wrong syntax! Type %help or mention the bot')
            return

        separator = '/'
        for c in cmd[2]:
            if not c.isdigit():
                separator = c
                break

        date = cmd[2].split(separator)
        print(date)
        if smallbrain(date) or (cmd[3] != 'std' and cmd[3] != 'us'):
            await message.channel.send('Wrong syntax! Type %help or mention the bot')
            return

        if len(date) == 2:
            y = 6969
        else:
            y = date[2]

        if cmd[3] == 'std':
            d, m = int(date[0]), int(date[1])
        else:
            d, m = int(date[1]), int(date[0])

        if ll.setbirthday(message.author, d, m, y):
            await message.channel.send('{0.mention} Birthdate successfully registered!'.format(message.author))
        else:
            await message.channel.send('Why u so dumb?')




    # When an administrator uses the "%bindto" command
    if message.content.lower() == '%bind' and message.author.guild_permissions.administrator:
        ll.bindto(message.channel, message.guild)
        await message.channel.send('Event messages are now bound to the {0.channel.mention} channel!'.format(message))

    if message.content.lower() == '%channelbound' and message.author.guild_permissions.administrator:
        await message.channel.send('I am bound to the {0.mention} channel!'.format(ll.serverbinding(message.guild)))

    if len(message.mentions) > 0 and message.mentions[0] == client.user:
        await message.channel.send("Stfu")
        print('{0.author} : {1.id}'.format(message, message.author))

dailycheck.start()
client.run(TOKEN)
