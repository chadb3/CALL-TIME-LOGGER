from datetime import datetime, timedelta

class Call:
    def __init__(this, callNumber=-1):
        #this.callDate = ""
        this._callTime = ""
        this._callEndTime=""
        #this.callEndDate=""
        this._callNumber = callNumber
        this.setStartTime()
    # sets the call start time
    # note: also sets the end time.
    # set the end time to the start time
    def setStartTime(this):
        # need to split out
        #this.callDate = datetime.now()
        this._callTime = datetime.now()
        this._callEndTime = this._callTime
    # sets the call number
    def setCallNumber(this, numberIn):
        this._callNumber = numberIn
    # sets the end time.
    def setEndTime(this):
        this._callEndTime=datetime.now()
    # used to see if it prints the correct call number
    # also used to test to see if call numbers hold if added to a list 
    def zTestPrintCallNum(this):
        print(this._callNumber)
    #used to test if start and endtimes are working correctly
    def zTestPrintCallStartAndEndTime(this):
        print("start: {}\nend: {}".format(this._callTime,this._callEndTime))
    #This is for adjusting the end time of a call
    #Just in case the user forgets to manually end the call time. 
    #WIP
    def adjustEndTime(this):
        try:
         ans = int(input("Estimated Time (in seconds): "))
        except:
         print("Error: cannot convert to numbers\nTry Again!")
         ans=0
        this.callEndTime=this.callEndTime-timedelta(seconds=ans)
        return 0
    # used to ajust call number. To increse callNumber by 1.
    def increaseCallNum(this):
        if(this._callNumber>0):
           this._callNumber+=1
        else:
           print("set call number")
    # used to adjust call number. To decrease callNumber by 1.
    def decreaseCallNum(this):
        if(this._callNumber>1):
           this._callNumber-=1
        else:
           print("call number < 1")
    def __str__(this):
        if(this._callTime==this._callEndTime):
            return " Call: {}\tDate: {}\tTime: {}\tDuration: 0\t".format(this._callNumber,this._callTime.date(),str(this._callTime.time())[0:8])
        else:
            return " Call: {}\tDate: {}\tTime: {}\tDuration: {}\t".format(this._callNumber,this._callTime.date(),str(this._callTime.time())[0:8],str(this._callEndTime-this._callTime)[0:7])