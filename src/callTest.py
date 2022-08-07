from Call import *
import time
print("testing call end times")
a=Call()
a.setStartTime()
print("call created, and start time set")
a.zTestPrintCallStartAndEndTime()
print("sleeping for 15 seconds")
time.sleep(15)
print("ending call")
a.setEndTime()
a.zTestPrintCallStartAndEndTime()
print("call time should be about +15 seconds after the first")