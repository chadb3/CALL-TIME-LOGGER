from Command import *
print("\n\t*** Test 1: listing commands ***\n")
a = Command()
a.zAppendCommandTest()
a.listOfCommands()
print("\n\t*** Test 2: datetime ***\n")
a = Command()
DT = a.zDateTimeTest()
print("DT: {}\n".format(DT))
