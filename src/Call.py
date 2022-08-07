from datetime import *

class Call:
    def __int__(this):
        #this.callDate = ""
        this.callTime = ""
        this.callEndTime=""
        #this.callEndDate=""
        this.callNumber = ""
    def setStartTime(this):
        # need to split out
        #this.callDate = datetime.now()
        this.callTime = datetime.now()
        this.callEndTime = this.callTime
    def setCallNumber(this, numberIn):
        this.callNumber = numberIn
    def zTestPrintCallNum(this):
        print(this.callNumber)
    def zTestPrintCallStartAndEndTime(this):
        print("start: {}\nend: {}".format(this.callTime,this.callEndTime))
    def setEndTime(this):
        this.callEndTime=datetime.now()