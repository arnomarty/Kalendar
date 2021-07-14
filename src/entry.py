class Entry:

    def __init__(self, user_id, day, month, year, is_birthday):
        self.id = user_id
        self.day = day
        self.month = month
        self.year = year
        self.is_birthday = is_birthday

    def getid(self):
        return self.id

    def getdate(self):
        return self.day, self.month, self.year

    def isbirthday(self):
        return self.is_birthday


    def tostring(self):
        resultstring = "User: " + str(self.id) + "\n"
        resultstring = resultstring + "Date: (" + str(self.day) + "/" + str(self.month) + "/" + str(self.year) + ")\n"
        resultstring = resultstring + "Is it a birthday: " + str(self.is_birthday) + "\n"
        return resultstring

    def tocsvformat(self):
        return [ self.id, self.day, self.month, self.year, int(self.is_birthday)]


    def equals(self, obj):
        if not isinstance(obj, Entry):
            return False
        d, m, y = obj.getdate()

        return self.id == obj.getid() and self.day == d and self.month == m and self.year == y and self.is_birthday == obj.isbirthday()
