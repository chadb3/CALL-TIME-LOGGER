from Command import *
from Call import *

print("\n\t*** Test 1: listing commands ***\n")
#a = Command()
#a.zAppendCommandTest()
#a.listOfCommands()
print("\n\t*** Test 2: datetime ***\n")
a = Command()
#DT = a.zDateTimeTest()
#print("DT: {}\n".format(DT))
print("practcing creating command")
b=Command({"y":Call(1)},"Command",[],{"Yes":Call(1)},"None")
call=b.getCommand()['y']
print(call)
try:
    fail = b.getCommand()['yer']
except:
    print("ERROR !!!")

c=Command({"y":Call(2)},"Command",[],{"Yes":Call(2)},"None")
print_test=c.run("y")
print("tst: {}".format(print_test))