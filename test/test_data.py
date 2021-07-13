import sys
import os
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, os.path.abspath('../src'))
import datalayer as dl



def test_getdate(dataobj):
    return "FAILED", "Not yet implemented"


def test_setdate(dataobj):
    return "FAILED", "Not yet implemented"


def test_save(dataobj):
    return "FAILED", "Not yet implemented"


def test_reload(dataobj):
    return "FAILED", "Not yet implemented"


def test_userexists(dataobj):
    return "FAILED", "Not yet implemented"


def test_dateexists(dataobj):
    return "FAILED", "Not yet implemented"



if __name__ == '__main__':
    testpassed = 0
    print("\nStarting test for the data layer!\n")
    dataobj = dl.Data('test_rss/')

    code, details = test_getdate(dataobj)
    print(" - test_getdate(): " + code + "! (Output: " + details + ")")
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

    percentage = int(testpassed/6*100)
    print("\n--------\nAmount of tests passed: " + str(testpassed) + "/6 (" + str(percentage) + "%)\n")
