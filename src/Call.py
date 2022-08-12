from datetime import datetime, timedelta

class Call:
    def __init__(this, callNumber=-1):
        #this.callDate = ""
        this.callTime = ""
        this.callEndTime=""
        #this.callEndDate=""
        this.callNumber = callNumber
        this.setStartTime()
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
        try:
         ans = int(input("Estimated Time (in seconds): "))
        except:
         print("Error: cannot convert to numbers\nTry Again!")
         ans=0
        this.callEndTime=this.callEndTime-timedelta(seconds=ans)
        return 0
    # used to ajust call number. To increse callNumber by 1.
    def increaseCallNum(this):
        if(this.callNumber>0):
           this.callNumber+=1
        else:
           print("set call number")
    # used to adjust call number. To decrease callNumber by 1.
    def decreaseCallNum(this):
        if(this.callNumber>1):
           this.callNumber-=1
        else:
           print("call number < 1")
