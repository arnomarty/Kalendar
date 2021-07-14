import os
import csv
from entry import *

"""
CLASS OVERVIEW :
    Arguments:
        - database (Stores the user IDs with their birthdates)
        - bindtable (Stores the Server/Channel couples)
    Methods:
        -  [line 28] CONSTRUCTOR(rsspath: str)
        -  [line 54] getdate(id: int)
        -  [line 77] getdatebydate(day: int, month: int, year: int)
        - [line 104] setdate(entry: Entry)
        - [line 133] save(void)
        - [line 152] reload(void)
        - [line 179] userexists(id: int)
        - [line 199] dateexists(day: int, month: int, year: int)
        - [line 226] loadbindtable(void)
        - [line 253] savebindtable(void)
        - [line 276] getboundchannel(serverid: int)
        - [line 297] addboundchannel(serverid: int, channelid: int)
"""


class Data:

    def __init__(self, rsspath):
        self.database = dict()
        self.bindtable = dict()

        self.path = os.path.abspath(rsspath)
        if not os.path.isdir(self.path):
            os.mkdir(self.path)

        self.tablepath = self.path + '/bindtable.csv'
        self.path = self.path + '/dates.csv'

        if not os.path.isfile(self.path):
            open(self.path, 'x')
        if not os.path.isfile(self.tablepath):
            open(self.tablepath, 'x')



    # Roams trough the existing dates database and fetches the birthday date
    # associated to the user ID passed in parameters. Raises a ValueError
    # exception if the parameter doesn't meet the requirements listed below.
    # Parameters :
    #   - id: Integer. Must be greater than 0.
    # Returns :
    #   - An Entry() object if the ID is in the database. None otherwise.
    #
    def getdate(self, id):
        if not isinstance(id, int):
            raise ValueError("Parameter 'id' must be an integer")
        if id < 1:
            raise ValueError("Invalid ID parameter: " + str(id))

        if id in self.database:
            return self.database[id]

        return None


    # Does the exact same thing as the function above. However, this one will
    # fetch the birthday entry based on a date passed in parameters. Raises a
    # ValueError exception if the parameters don't meet the requirements listed
    # below.
    # Parameters :
    #   - day: Integer. 0 < day < 32
    #   - month: Integer. 0 < month < 13
    #   - year: Integer. year > 1900
    # Returns :
    #   - An Entry() object if the date is in the database. None otherwise.
    #
    def getdatebydate(self, day, month, year):
        if not isinstance(day, int) or not isinstance(month, int) or not isinstance(year, int):
            raise ValueError("All parameters must be integers")
        if day < 1 or day > 31:
            raise ValueError("Invalid 'day' parameter: " + str(day))
        if month < 1 or month > 12:
            raise ValueError("Invalid 'month' parameter: " + str(month))
        if year < 1900:
            raise ValueError("Invalid 'year' parameter: " + str(year))

        for entry in self.database.values():
            d, m, y = entry.getdate()
            if d == day and m == month and y == year:
                return entry

        return None



    # Creates a new birthday entry into the existing database. Raises a ValueError
    # exception if the parameter doesn't meet the requirements listed below.
    # Parameters :
    #   - entry: Entry() object. Must contain a valid DD/MM/YYYY date.
    #            ( 0 < DD < 32, 0 < MM < 13, YYYY > 1900 )
    # Returns :
    #   - True if the value was properly saved, False otherwise.
    #
    def setdate(self, entry):
        if not isinstance(entry, Entry):
            raise ValueError("Parameter 'entry' must be an Entry() object")
        d, m, y = entry.getdate()
        if d < 1 or d > 31:
            raise ValueError("Invalid day attribute: " + str(d))
        if m < 1 or m > 12:
            raise ValueError("Invalid month attribute: " + str(m))
        if y < 1900:
            raise ValueError("Invalid year attribute: " + str(y))

        id = entry.getid()
        try:
            self.database[id] = Entry(id, d, m, y, entry.isbirthday())
        except:
            return False

        return True



    # Saves the current database in a "dates.csv" file, located in a folder whose
    # path is stored inside the self.path attribute. If it doesn't exist,
    # the function creates it.
    # The format must be "UserID, Day, Month, Year, isBirthday". Each row equals
    # to one entry.
    # Returns :
    #   - True if the database was properly saved, False otherwise.
    #
    def save(self):
        try:
            with open(self.path, 'w') as csvfile:
                csvwriter = csv.writer(csvfile)
                for entry in self.database.values():
                    csvwriter.writerow(entry.tocsvformat())
        except:
            return False

        return True



    # Updates the current database based on a "dates.csv" file, located into a
    # folder whose path is stored into the self.path attribute. Raises a
    # FileNotFoundError exception if that file doesn't exist.
    # Returns :
    #   - True if the database was properly updated, False otherwise.
    #
    def reload(self):
        if not os.path.isfile(self.path):
            raise FileNotFoundError("Error: File " + self.path + " doesn't exist!")

        self.database = dict()
        try:
            with open(self.path, 'r') as csvfile:
                csvreader = csv.reader(csvfile)
                for row in csvreader:
                    entry = Entry(int(row[0]), int(row[1]), int(row[2]), int(row[3]), bool(row[4]))
                    self.database[ int(row[0]) ] = entry
        except Exception as e:
            print("Warning: " + e.args)
            return False

        return True



    # Will browse through the database to see if any entry matches with the ID
    # passed as a parameter. Raises a ValueError exception if the parameter
    # doesn't meet the requirements listed below.
    # Parameters :
    #   - id: Integer. Must be greater than 0.
    # Returns :
    #   - True if the user exists in the database, False otherwise.
    #
    def userexists(self, id):
        if not isinstance(id, int):
            raise ValueError("Parameter 'id' must be an integer")
        if id < 1:
            raise ValueError("Invalid ID parameter: " + str(id) )

        return id in self.database.keys()



    # Will browse through the database to see if any entry matches with the date
    # passed in parameters. Raises a ValueError exception if the parameter doesn't
    # meet the requirements listed below.
    # Parameters :
    #   - day: Integer. 0 < day < 32
    #   - month: Integer. 0 < month < 13
    #   - year: Integer. year > 1900
    # Returns :
    #   - True if the date exists in the database, False otherwise.
    #
    def dateexists(self, day, month, year):
        if not isinstance(day, int) or not isinstance(month, int) or not isinstance(year, int):
            raise ValueError("All parameters must be integers")
        if day < 1 or day > 31:
            raise ValueError("Invalid 'day' parameter: " + str(day))
        if month < 1 or month > 12:
            raise ValueError("Invalid 'month' parameter: " + str(month))
        if year < 1900:
            raise ValueError("Invalid 'year' parameter: " + str(year))

        for entry in self.database.values():
            d, m, y = entry.getdate()
            if d == day and m == month and y == year:
                return True

        return False



    # Will load the server/channel binding table located in a CSV file whose
    # path is stored in the 'tablepath' attribute. That file MUST exist for
    # the function to run. If it doesn't, raises a FileNotFoundError exception.
    # Parameters :
    #   None
    # Returns :
    #   - True if the table was successfully loaded, False otherwise.
    #
    def loadbindtable(self):
        if not os.path.isfile(self.tablepath):
            raise FileNotFoundError("Error: File " + self.tablepath + " doesn't exist!")

        self.bindtable = dict()
        try:
            with open(self.tablepath, 'r') as csvfile:
                csvreader = csv.reader(csvfile)
                for row in csvreader:
                    if len(row) != 2:
                        raise ValueError("Bind table corrupted!")
                    self.bindtable[ int(row[0]) ] = int(row[1])
        except Exception as e:
            print("Warning: " + e.args)
            return False

        return True



    # Saves the current server/channel binding table into a CSV file which can
    # be found in the directory pointed by the 'tablepath' attribute.
    # Parameters :
    #   None
    # Returns :
    #   - True if the table was successfully saved, False otherwise.
    #
    def savebindtable(self):
        if len(self.bindtable) == 0:
            return False
        try:
            with open(self.tablepath, 'w') as csvfile:
                csvwriter = csv.writer(csvfile)
                for serverid in self.bindtable.keys():
                    csvwriter.writerow([serverid, self.bindtable[serverid]])
        except:
            return False

        return True



    # Will look into the bindtable attribute for a matching server ID. If the
    # parameters don't meet the requirements listed below, raises a ValueError
    # exception.
    # Parameters :
    #   - serverid: Integer. serverid > 0
    # Returns :
    #   - If march found, the channel ID associated. -1 otherwise.
    #
    def getboundchannel(self, serverid):
        if not isinstance(serverid, int):
            raise ValueError("Parameter 'serverid' must be an integer!")
        if serverid <= 0:
            raise ValueError("Invalid value for parameter 'serverid': " + str(serverid))

        if serverid in self.bindtable.keys():
            return self.bindtable[serverid]
        return -1



    # Will add a server/channel couple into the bindtable. On the given server,
    # birthday messages will be written on the given channel. Raises a ValueError
    # exception if the parameters don't meet the requirements listed below.
    # Parameters :
    #   - serverid: Integer. serverid < 0
    #   - channelid: Integer. channelid < 0
    # Returns :
    #   - True if the operation was a success, False otherwise.
    #
    def addboundchannel(self, serverid, channelid):
        if not isinstance(serverid, int) or not isinstance(channelid, int):
            raise ValueError("All parameters must be integers!")
        if serverid <= 0 or channelid <= 0:
            raise ValueError("All parameters must be positive!")

        self.bindtable[serverid] = channelid
        return True
