from Command import *

class commandController:
    def __init__(this):
        this.commands=[]
    def readCommandsIn(this):
        print("Reading Commands")
    def readTESTCOMMANDSIN(this):
        tmpStorage=[]
        print("Reading Test Commands In")
        file=open("commands.txt","r")
        for line in file:
            #print(line, end="")
            tmpStorage.append(line.strip())
        for command in tmpStorage:
            print(command)