from callManager import *
from commandController import *
from time import sleep
class test:
    def __init__(this, controler):
        this.cc = controler
    def testManagerAPI(this):
        this.cc.commandAPItest(0)
        sleep(5)
        this.cc.commandAPItest(1)
        this.cc.commandAPItest(0)
        sleep(5)
        this.cc.commandAPItest(1)
        this.cc.commandAPItest(2)



callM=callManager()
a=test(callM)
a.testManagerAPI()
print("calling from callManager object directly")
#note need to add function to set duration if not ended
#be the total time call was open...
callM.printCalls()