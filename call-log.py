from src.callManager import *
from src.commandController import *
from time import sleep
import sqlite3
from random import randint
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
            ran=randint(0,99999)
            #easter egg
            if(ran==1001 or ran==2001 or ran==3001 or ran==4001 or ran==5001 or ran==6001 or ran==7001 or ran==8001 or ran==9001 or ran==10001):
                print("Bye\n:^)")
            print(ran)
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