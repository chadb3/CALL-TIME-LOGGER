from datetime import *

class Call:
    def __int__(this):
        #this.callDate = ""
        this.callTime = ""
        this.callEndTime=""
        #this.callEndDate=""
        this.callNumber = ""
    # sets the call start time
    # note: also sets the end time.
    # set the end time to the start time
    def setStartTime(this):
        # need to split out
        #this.callDate = datetime.now()
        this.callTime = datetime.now()
        this.callEndTime = this.callTime
    # sets the call number
    def setCallNumber(this, numberIn):
        this.callNumber = numberIn
    # sets the end time.
    def setEndTime(this):
        this.callEndTime=datetime.now()
    # used to see if it prints the correct call number
    # also used to test to see if call numbers hold if added to a list 
    def zTestPrintCallNum(this):
        print(this.callNumber)
    #used to test if start and endtimes are working correctly
    def zTestPrintCallStartAndEndTime(this):
        print("start: {}\nend: {}".format(this.callTime,this.callEndTime))
    #This is for adjusting the end time of a call
    #Just in case the user forgets to manually end the call time. 
    #WIP
    def adjustEndTime(this):
        ans = input("Estimated Time: ")
        return 0