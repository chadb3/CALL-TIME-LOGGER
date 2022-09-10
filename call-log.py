from src.callManager import *
from src.commandController import *
from time import sleep
import sqlite3
def main():
    filepath="/config/commands.txt"
    callM=callManager()
    COMMAND=commandController()
    print("STARTING")
    true=True
    while(true):
        usrInput=input("call-logger>> ")
        usrInput=usrInput.upper()
        if(usrInput=="EXIT" or usrInput=="EXIT()"):
            break
        elif(usrInput=="Y" or usrInput=="NEW CALL" or usrInput =="YES"):
            callM.newCall()
            callM.printCalls()
        elif(usrInput=="EPC" or usrInput=="ECC"):
            #callM.endCurrentCall()
            if(callM.endCurrentCall()):
                callM.printCalls()
        elif(usrInput=="DURATION"):
            callM.askDuration()
        elif(usrInput=="PRINT"):
            callM.printCalls()
        elif(usrInput=="PRINT 2"):
            #print("CALLED")
            callM.printCallsAlternate()
    return 0

if __name__ == "__main__":
	main()

# currently working on
# make duration not print 0 while call is current.
# -see notes under Call.py
# add database