


def test_bindto(dataobj):
    return "FAILED", "Not yet implemented!"

def test_getuserservers(dataobj):
    return "FAILED", "Not yet implemented!"

def test_setbirthday(dataobj):
    return "FAILED", "Not yet implemented!"

def test_getbybirthdate(dataobj):
    return "FAILED", "Not yet implemented!"

def test_getbyid(dataobj):
    return "FAILED", "Not yet implemented!"

def test_geteventsoftheday(dataobj):
    return "FAILED", "Not yet implemented!"


if __name__ == '__main__':
    testpassed = 0
    print("\nStarting test for the logic layer!\n")
    dataobj = dl.Data('test_rss/')

    code, details = test_bindto(dataobj)
    print(" - test_bindto(): " + code + "! Output: " + details)
    if code == "OK":
        testpassed = testpassed + 1

    code, details = test_getuserservers(dataobj)
    print(" - test_getuserservers(): " + code + "! (Output: " + details + ")")
    if code == "OK":
        testpassed = testpassed + 1

    code, details = test_setbirthday(dataobj)
    print(" - test_setbirthday(): " + code + "! (Output: " + details + ")")
    if code == "OK":
        testpassed = testpassed + 1

    code, details = test_getbybirthdate(dataobj)
    print(" - test_getbybirthdate(): " + code + "! (Output: " + details + ")")
    if code == "OK":
        testpassed = testpassed + 1

    code, details = test_getbyid(dataobj)
    print(" - test_getbyid(): " + code + "! (Output: " + details + ")")
    if code == "OK":
        testpassed = testpassed + 1

    code, details = test_geteventsoftheday(dataobj)
    print(" - test_geteventsoftheday(): " + code + "! (Output: " + details + ")")
    if code == "OK":
        testpassed = testpassed + 1

    percentage = int(testpassed/6*100)
    print("\n--------\nAmount of tests passed: " + str(testpassed) + "/6 (" + str(percentage) + "%)\n")
