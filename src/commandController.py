from src.Command import Command

class commandController:
    def __init__(this):
        this.commands=[]
        this.testStorage=[]
    def readCommandsIn(this):
        print("Reading Commands")
    def addCommand(this, command):
        this.commands.append(command)
    def readTESTCOMMANDSIN(this):
        #tmpStorage=[]
        print("Reading Test Commands In")
        file=open("src/commands.txt","r")
        for line in file:
            #print(line, end="")
            if(line[0]!='#'):
                this.testStorage.append(line.strip())
        print("Printing Commands")
        for command in this.testStorage:
            print(command)
    def printCommandHelp(this, command):
        #may need to adjust
        for ccommand in this.commands:
            ccommand.getCommandHelp()
    def printCommandList(this):
        print("Printing Commands: ")
        for command in this.commands:
            print(command)
    def testCheckInput(this, input):
        print("input in: {}".format(input))