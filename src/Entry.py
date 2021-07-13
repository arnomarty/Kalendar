class Entry:

    def __init__(self, user_id, day, month, year, is_birthday):
        self.id = user_id
        self.day = day
        self.month = month
        self.year = year
        self.is_birthday = is_birthday

    def tostring(self):
        resultstring = "User: " + str(self.id) + "\n"
        resultstring = resultstring + "Date: (" + str(self.day) + "/" + str(self.month) + "/" + str(self.year) + ")\n"
        resultstring = resultstring + "Is it a birthday: " + str(self.is_birthday) + "\n"
        return resultstring
