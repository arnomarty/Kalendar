import discord as dc
import datalayer as dl
from entry import Entry

databox = dl.Data('rss')

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
    # Hints:
    # - Look the discord.py documentation, more specificly, for the Guild()
    #   and User() objects documentation.
    return []


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
    # Hints:
    # - Make sure to verify the parameters. You can look at already made
    #   functions to get examples
    # - Look at entry.py and datalayer.py. More specificly, the setdate()
    #   function should be handy
    return False


# Tries to fetch a user ID and its associated birthday from a valid date
# passed in parameters. If the date doesn't meet the requirements listed below,
# does nothing.
# Parameters :
#   - day: Integer. 0 < day < 32
#   - month: Integer. 0 < month < 13
#   - year: Integer. year <= 1950
# Returns :
#   - A corresponding Entry() object if a birthdate was found, None otherwise.
#
def getbybirthdate(day, month, year):
    return None


# Performs a similar action than the function above. However, this time, the
# research criteria is the ID of the user passed in parameters. Here as well,
# if the parameters doesn't meet the requirements listed below, does nothing.
# Parameters :
#   - user: User() discord object. Must point to a valid user.
# Returns :
#   - A corresponding Entry() object if a birthdate was found, None otherwise.
#
def getbyid(user):
    return None


# Verifies if there is any birthday set on the date passed in parameters. If the
# date is invalid, i.e. if it doesn't meet the requirements listed below, does
# nothing.
# Parameters:
#   - day: Integer. 0 < day < 32
#   - month: Integer. 0 < month < 13
# Returns :
#   - A User() object if successful, None otherwise.
#
async def geteventsoftheday(client, day, month):
    if day < 1 or day > 31:
        return None
    if month < 1 or month > 12:
        return None

    entry = databox.getdatebydate(day, month)
    if entry != None:
        u = await client.fetch_user(entry.getid())
        return u

    return None
