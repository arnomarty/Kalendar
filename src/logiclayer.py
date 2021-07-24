import discord as dc
import datalayer as dl
from entry import Entry
from datetime import datetime


# Global object that will handle every memory-related operation.
databox = dl.Data('rss')
months_names = [ 'None', 'January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December' ]
days_per_month = [ -1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# When the channel and the server ID are valid, this function saves and stores
# the channel in which the bot is supposed to send the birthday reminders.
# Raises a ValueError exception when the parameters don't meet the requirements
# listed below.
# Parameters :
#   - channel: Channel object. Must correspond to an existing Discord channel.
#   - server: Server object. Must correspond to an existing Discord server.
# Returns :
#   - True if the binding was successful, False otherwise.
#
def bindto(channel, server):
    print('{0.id} <--> {1.id}'.format(channel, server))
    databox.addboundchannel(server.id, channel.id)
    databox.savebindtable()
    return True


# Returns the channel to which the bot is bound in a specific server (i.e. a
# channel where the %bind channel has been used at least once)
# Parameters :
#   - server: Guild object. Must point to a valid Discord server.
# Returns :
#   - The Channel object associated, None if it doesn't exist in memory.
#
def serverbinding(server):
    return server.get_channel(databox.getboundchannel(server.id))


# Will browse the list of registered servers and returns a list of those in which a user
# is present in. If the parameter does not meet the requirements listed below, does nothing.
# Parameters :
#   - user: User object. Must point to a valid Discord user.
#   - serverlist: List[Guild]. The list of servers the bot is present in.
# Returns :
#   - List[Guild] where the user is present. Otherwise, returns [].
def getuserservers(user, serverlist):
    result = []
    for guild in serverlist:
        if user in guild.members:
            result.append(guild)
    return result


# If the user and the date are both valid, saves and stores the user ID and its
# associated birthday. Otherwise, does nothing if the date doesn't meet the
# requirements listed below.
# Parameters :
#   - user: User object. Must correspond to an existing Discord user.
#   - day: Integer. 0 < day < 32
#   - month: Integer. 0 < month < 13
#   - year: Integer. year >= 1900
# Returns :
#   - True if the date was successfuly stored, False otherwise.
#
def setbirthday(user, day, month, year):
    id = user.id
    e = Entry(id, int(day), int(month), int(year), True)
    try:
        databox.setdate(e)
        databox.save()
    except ValueError:
        return False

    print(e.tostring())
    return True


# Will look into the database to find the birth date associated to a specific
# user.
# Parameters :
#   - user: Discord User object. Must be associated to a valid discord user.
# Returns :
#   - A String object if a date was found. None otherwise
#
def getbirthday(user):
    e = databox.getdate(user.id)
    if e != None:
        d, m, y = e.getdate()
        return months_names[m] + " " + str(d)
    return None



# Verifies if there is any birthday set on the date passed in parameters. If the
# date is invalid, i.e. if it doesn't meet the requirements listed below, does
# nothing.
# Parameters:
#   - day: Integer. 0 < day < 32
#   - month: Integer. 0 < month < 13
# Returns :
#   - A User object if successful, None otherwise.
#
def geteventsoftheday(client, day, month):
    if day < 1 or day > 31:
        return None
    if month < 1 or month > 12:
        return None

    entry = databox.getdatebydate(day, month)
    if entry != None:
        u = client.get_user(entry.getid())
        return u

    return None


# This contains the message that will be sent to an user when the command
# %kal help is used. TODO: Use the embed format to make it look nicer.
# Parameters :
#   - channel: Discord Channel object. The channel in which we want the message
#              to be sent in.
#
async def helpprompt(channel):
    await channel.send("**Common commands list:** \n \
  - **%kal set {xx/yy} {EU/US}:** \
Sets xx/yy as your birthdate. You need to specify the time format.\n \
  - **%kal set {xx/yy/zzzz} {EU/US}:** \
Sets xx/yy/zzzz as your birthdate. You also need to specify the time format.\n \
  - **%kal fetch @user:** Fetches an user's birthday.\n\n \
**Admin commands list:** \n \
  - **%bind:** To be used in the channel the bot must send birthday reminders to.")


# As the prototype implies, this function is used to check the validity of
# a date passed by the end-user. That is, the correct time format syntax
# (can be xx/yy, or xx/yy/zzzz). TODO: Differenciate 30/31-days months
# Parameters :
#   - date: list(). Stores each part of the date, [xx, yy, zzzz] for the
#           previous example.
# Returns :
#   - True if the format isn't respected, False otherwise.
#
def smallbrain(date):
    if len(date) not in [2, 3]:
        return True
    for i in date:
        if not i.isdigit():
            return True

    if len(date) != 2:
        if int(date[2]) > datetime.now().year - 4:
            return True

    if int(date[0]) > days_per_month[ int(date[1]) ]:
        return True

    return False


# Function called when the user uses the '%kal set' command. After checking
# the syntax validity of the command, will save and store the birth date and
# its associated user.
# Parameters :
#   - message: Discord Message object. Its content must be under the exact
#              form '%kal set xx/yy(/zzzz) {EU/US}'.
#              xx, yy and zzzz must be integers and represent a valid date.
# Returns :
#   - True if the conditions are respected and the date got saved, False otherwise.
#
def handleaddition(message):
    cmd = message.content.lower().split()
    if len(cmd) != 4 or cmd[3] not in ['eu', 'us']:
        return False

    separator = '/'
    for c in cmd[2]:
        # This allows user to use whatever time separator (/ . ' ...)
        if not c.isdigit():
            separator = c
            break

    date = cmd[2].split(separator)

    if smallbrain(date):
        return False

    if len(date) == 2:
        y = Entry.NOTSPECIFIED
    else:
        y = date[2]
    if cmd[3] == 'eu':
        d, m = int(date[0]), int(date[1])
    else:
        d, m = int(date[1]), int(date[0])

    return setbirthday(message.author, d, m, y)
