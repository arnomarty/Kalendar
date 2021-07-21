import discord as dc
import datalayer as dl
from entry import Entry
from datetime import datetime


databox = dl.Data('../rss')

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
#   - server: Guild() object. Must point to a valid Discord server.
# Returns :
#   - The Channel() object associated, None if it doesn't exist in memory.
#
def serverbinding(server):
    return server.get_channel(databox.getboundchannel(server.id))


# Will browse the list of registered servers and returns a list of those in which a user
# is present in. If the parameter does not meet the requirements listed below, does nothing.
# Parameters :
#   - user: User() object. Must point to a valid Discord user.
#   - serverlist: List[Guild()]. The list of servers the bot is present in.
# Returns :
#   - List[Guild()] where the user is present. Otherwise, returns [].
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


# Verifies if there is any birthday set on the date passed in parameters. If the
# date is invalid, i.e. if it doesn't meet the requirements listed below, does
# nothing.
# Parameters:
#   - day: Integer. 0 < day < 32
#   - month: Integer. 0 < month < 13
# Returns :
#   - A User() object if successful, None otherwise.
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


async def helpprompt(channel):
    await channel.send("**Common commands list:** \n \
  - **%kal set {xx/yy} {EU/US}:** \
Sets xx/yy as your birthdate. You need to specify the time format.\n \
  - **%kal set {xx/yy/zzzz} {EU/US}:** \
Sets xx/yy/zzzz as your birthdate. You also need to specify the time format.\n \
  - **%kal fetch @user:** Fetches an user's birthday.\n\n \
**Admin commands list:** \n \
  - **%bind:** To be used in the channel the bot must send birthday reminders to.")


def smallbrain(date):
    if len(date) != 3 and len(date) != 2:
        return True
    for i in date:
        if not i.isdigit():
            return True
    if len(date) != 2 and int(date[2]) > datetime.now().year - 4:
        return True
    return False



def handleaddition(message):
    cmd = message.content.lower().split()
    if len(cmd) != 4 or cmd[3] not in ['eu', 'us']:
        return False
    separator = '/'
    for c in cmd[2]:
        if not c.isdigit():
            separator = c
            break

    date = cmd[2].split(separator)

    if smallbrain(date):
        return False

    if len(date) == 2:
        y = 6969
    else:
        y = date[2]
    if cmd[3] == 'eu':
        d, m = int(date[0]), int(date[1])
    else:
        d, m = int(date[1]), int(date[0])

    return setbirthday(message.author, d, m, y)
