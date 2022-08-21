from Call import *

class callManager:
    def __init__(this):
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
    def printCalls(this):
        for call in this.callList:
            print(call)
    def askDuration(this):
        print("asking current delta/Duration")
        lenList=len(this.callList)
        if(lenList>0):
            this.callList[lenList-1].currentDelta()