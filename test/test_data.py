import sys
import os
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, os.path.abspath('../src'))
import datalayer as dl
from entry import *



def test_getdate(dataobj):
    try:
        dataobj.getdate("Sheesh")
        dataobj.getdate(-11)
        dataobj.getdate(0)
    except ValueError:
        pass
    else:
        return "FAILED", "Didn't raise ValueError exception for a wrong parameter."

    validentry = Entry(4321, 14, 8, 1997, True)
    dataobj.setdate(validentry)
    entryfetched = dataobj.getdate(4321)

    if entryfetched == None:
        return "FAILED", "Didn't return anything for a correct entry - REQUIRES SETDATE()"

    if not validentry.equals(entryfetched):
        return "FAILED", "Didn't return the good entry - REQUIRES SETDATE()"

    return "OK", "Successfully passed the test!"



def test_getdatebydate(dataobj):
    try:
        dataobj.getdatebydate("hihi", "haha", "huhu")
        dataobj.getdatebydate(100, 1, 2000)
        dataobj.getdatebydate(1, 100, 2000)
        dataobj.getdatebydate(1, 1, 1000)
        dataobj.getdatebydate(-1,-1,-1)
    except ValueError:
        pass
    else:
        return "FAILED", "Didn't raise ValueError exception for a wrong parameter."


    return "OK", "Successfully passed the test!"
    validentry = Entry(4444, 12, 12, 2020, False)
    dataobj.setdate(validentry)
    entryfetched = getdatebydate(12, 12, 2020)
    if entryfetched == None:
        return "FAILED", "Didn't return anything when fetching a correct entry - REQUIRES SETDATE()"
    if not validentry.equals(entryfetched):
        return "FAILED", "Didn't return the good entry - REQUIRES SETDATE()"



def test_setdate(dataobj):
    try:
        dataobj.setdate(1234)
        dataobj.setdate("Hello hello")
    except ValueError:
        pass
    except:
        return "FAILED", "Didn't raise correct exception for a wrong parameter."
    else:
        return "FAILED", "Didn't raise ValueError exception for a wrong parameter."

    wrongentry1 = Entry(1, 100, 1, 1997, True)
    wrongentry2 = Entry(2, 18, 20, 1997, True)
    wrongentry3 = Entry(3,-1,-2,1997, False)
    try:
        dataobj.setdate(wrongentry1)
        dataobj.setdate(wrongentry2)
        dataobj.setdate(wrongentry3)
    except ValueError:
        pass
    except:
        return "FAILED", "Didn't raise correct exception for an invalid Entry() parameter."
    else:
        return "FAILED", "Didn't raise ValueError exception for an invalid Entry() parameter."

    validentry = Entry(9876, 14, 8, 1997, True)

    returnvalue = dataobj.setdate(validentry)
    if returnvalue == False:
        return "FAILED", "Didn't return true at the end of the execution."

    entryfetched = dataobj.getdate(9876)
    if entryfetched == None or not entryfetched.equals(validentry):
        return "FAILURE", "The entry wasn't saved properly - REQUIRES GETDATE()"

    modifiedentry = Entry(9876, 1, 9, 2001, True)
    dataobj.setdate(modifiedentry)
    entryfetched2 = dataobj.getdate(9876)
    if not modifiedentry.equals(entryfetched2):
        return "FAILED", "The entry wasn't updated properly - REQUIRES GETDATE()"

    return "OK", "Successfully passed the test!"



def test_save(dataobj):
    validentry = Entry(1472, 14, 10, 1998, True)
    dataobj.setdate(validentry)
    dataobj.save()

    dataobj2 = dl.Data('test_rss/')
    dataobj2.reload()

    entryfetched = dataobj2.getdate(1472)
    if entryfetched == None:
        return "FAILED", "The entries weren't saved - REQUIRES RELOAD(), GETDATE()"

    if not validentry.equals(entryfetched):
        return "FAILED", "The entries weren't saved properly - REQUIRES RELOAD(), GETDATE()"

    return "OK", "Successfully passed the test!"



def test_reload(dataobj):
    validentry = Entry(1472, 14, 10, 1998, True)
    dataobj.setdate(validentry)
    dataobj.save()

    dataobj2 = dl.Data('test_rss/')
    dataobj2.reload()

    entryfetched = dataobj2.getdate(1472)
    if entryfetched == None:
        return "FAILED", "The entries weren't reloaded - REQUIRES SAVE(), GETDATE()"

    if not validentry.equals(entryfetched):
        return "FAILED", "The entries weren't reloaded properly - REQUIRES SAVE(), GETDATE()"
    return "OK", "Successfully passed the test!"



def test_userexists(dataobj):
    validentry = Entry(8521, 12, 2, 1996, False)

    try:
        dataobj.userexists("Smooch")
        dataobj.userexists(-1)
        dataobj.userexists(validentry)
    except ValueError:
        pass
    else:
        return "FAILED", "Didn't raise ValueError exception when passed wrong-typed parameter."

    if dataobj.userexists(8521):
        return "FAILED", "Non-existing user deemed as existing."

    dataobj.setdate(validentry)
    if not dataobj.userexists(8521):
        return "FAILED", "Existing user deemed as non-existing"

    return "OK", "Successfully passed the test!"



def test_dateexists(dataobj):
    validentry = Entry(1111, 1, 2, 1950, False)
    try:
        dataobj.dateexists(50, 1, 2010)
        dataobj.dateexists(-5, 2, 2020)
        dataobj.dateexists(10, 120, 2010)
        dataobj.dateexists(14, -8, 2000)
        dataobj.dateexists(541, 1024, -111)
    except ValueError:
        pass
    else:
        return "FAILED", "Didn't raise ValueError exception when passed wrong parameter."

    if dataobj.dateexists(1, 2, 1950):
        return "FAILED", "Non-existing date deemed as existing."

    dataobj.setdate(validentry)
    if not dataobj.dateexists(1, 2, 1950):
        return "FAILED", "Existing date deemed as non-existing"

    return "OK", "Successfully passed the test!"





if __name__ == '__main__':
    testpassed = 0
    print("\nStarting test for the data layer!\n")
    dataobj = dl.Data('test_rss/')

    code, details = test_getdate(dataobj)
    print(" - test_getdate(): " + code + "! (Output: " + details + ")")
    if code == "OK":
        testpassed = testpassed + 1

    code, details = test_getdatebydate(dataobj)
    print(" - test_getdatebydate(): " + code + "! (Output: " + details + ")")
    if code == "OK":
        testpassed = testpassed + 1

    code, details = test_setdate(dataobj)
    print(" - test_setdate(): " + code + "! (Output: " + details + ")")
    if code == "OK":
        testpassed = testpassed + 1

    code, details = test_save(dataobj)
    print(" - test_save(): " + code + "! (Output: " + details + ")")
    if code == "OK":
        testpassed = testpassed + 1

    code, details = test_reload(dataobj)
    print(" - test_reload(): " + code + "! (Output: " + details + ")")
    if code == "OK":
        testpassed = testpassed + 1

    code, details = test_userexists(dataobj)
    print(" - test_userexists(): " + code + "! (Output: " + details + ")")
    if code == "OK":
        testpassed = testpassed + 1

    code, details = test_dateexists(dataobj)
    print(" - test_dateexists(): " + code + "! (Output: " + details + ")")
    if code == "OK":
        testpassed = testpassed + 1

    percentage = int(testpassed/7*100)
    print("\n--------\nAmount of tests passed: " + str(testpassed) + "/7 (" + str(percentage) + "%)\n")
