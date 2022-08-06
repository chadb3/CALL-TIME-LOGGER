from datetime import *

class Call:
    def __int__(this):
        this.callDate = ""
        this.callTime = ""
        this.callEndTime=""
        this.callEndDate=""
        this.callNumber = ""
    def setStartTime(this):
        # need to split out
        this.callDate = datetime.now()
        this.callTime = datetime.now()
    def setCallNumber(this, numberIn):
        this.callNumber = numberIn
    def zTestPrintCallNum(this):
        print(this.callNumber)