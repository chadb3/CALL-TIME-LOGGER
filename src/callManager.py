from Call import *
from datetime import datetime

class callManager:
    def __init__(this):
        this.initTime=datetime.now()
        this.timeFirstCall=0
        this.callList = []
        this.callCount = 0
    def newCall(this):
        if(this.callCount>0):
            #debug
            #print("HIT")
            if(not this.callList[this.callCount-1].callEnded):
                this.callList[this.callCount-1].setEndTime()
        this.callCount+=1
        this.callList.append(Call(this.callCount))
        if(len(this.callList)==1 and this.timeFirstCall==0):
            this.timeFirstCall=datetime.now()
    def printCalls(this):
        for call in this.callList:
            print(call)
    def askDuration(this):
        #print("asking current delta/Duration")
        lenList=len(this.callList)
        if(lenList>0):
            this.callList[lenList-1].currentDelta()
    def getTimeToFirstCall(this):
        print("Time to first call")
        if(len(this.callList)==1):
            #print("LEN=1")
            print("Time to First: {}".format(str(this.timeFirstCall-this.initTime)[0:7]))
