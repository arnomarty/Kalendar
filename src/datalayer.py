class Data:

    def __init__(self, rsspath):
        print("WARNING: Data constructor not yet implemented!")


    # Roams trough the existing dates database and fetches the birthday date
    # associated to the user ID passed in parameters. Raises a ValueError
    # exception if the parameter doesn't meet the requirements listed below.
    # Parameters :
    #   - id: Integer. Must be greater than 0.
    # Returns :
    #   - An Entry() object if the ID is in the database. None otherwise.
    #
    def getdate(self, id):
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
        return False


    # Saves the current database in a "dates.csv" file, located in a folder whose
    # path is stored inside the self.path attribute. If it doesn't exist,
    # the function creates it.
    # The format must be "UserID, Day, Month, Year, isBirthday". Each row equals
    # to one entry.
    # Returns :
    #   - True if the database was properly saved, False otherwise.
    #
    def save(self):
        return False


    # Updates the current database based on a "dates.csv" file, located into a
    # folder whose path is stored into the self.path attribute. That file MUST
    # exist in order for the database to be updated.
    # Returns :
    #   - True if the database was properly updated, False otherwise.
    #
    def reload(self):
        return False


    # Will browse through the database to see if any entry matches with the ID
    # passed as a parameter. Raises a ValueError exception if the parameter
    # doesn't meet the requirements listed below.
    # Parameters :
    #   - id: Integer. Must be greater than 0.
    # Returns :
    #   - True if the user exists in the database, False otherwise.
    #
    def userexists(self, id):
        return False

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
        return False
