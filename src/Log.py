from random import randint
class Log:
    def __init__(this):
        #filepath to history file
        this.sessionStartStr = "{} - SESSION START - {}"
        this.sessionEndStr ="{} - SESSION END - {}"
        this.filepath = "../data/"
        this.filename ="history.txt"
        #datetime COMMAND: commandIn
        this.commandStr = "{} - COMMAND: {}"
        #datetime SYSTEM: \"SYSTEM OUTPUT\"
        this.systemStr = "{} - SYSTEM: {}"
        #datetime INPUT: "user input that wasn't a command or other."
        this.userInputStr = "{} - INPUT: {}"
    def logCommand(this, dateTimeIn, commandIn):
        this._writeToFile(this.commandStr.format(dateTimeIn, commandIn))
        return 0
    def logSystem(this,dateTimeIn, systemTextIn):
        this._writeToFile(this.systemStr.format(dateTimeIn,systemTextIn))
        return 0
    def logUserInput(this,dateTimeIn, userInputIn):
        this._writeToFile(this.userInputStr.format(dateTimeIn,userInputIn))
        return 0
    def _startLogging(this, dateTimeIn):
        #datetime - SESSION START - this.filename
        return 0
    def endLogging(this, dateTimeIn):
        #datetime - SESSION END - :)
        #datetime - SESSION END - :^)
        randNum=randint(1,5999)
        endSessionStr = ""
        if(randNum%3==0):
            endSessionStr= ":^)"
        else:
            endSessionStr= ":)"
        this._writeToFile(this.sessionEndStr.format(dateTimeIn,endSessionStr))
        return endSessionStr
    def _writeToFile(this, thingIn):
        file =open(this.filepath+this.filename,'a')
        file.write(thingIn+"\n")
        file.close()
        return 0