class Log:
    def __init__(this):
        #filepath to history file
        this.filepath = "../data/"
        this.filename ="history.txt"
        #datetime COMMAND: commandIn
        this.commandStr = "{} COMMAND: {}"
        #datetime SYSTEM: \"SYSTEM OUTPUT\"
        this.systemStr = "{} SYSTEM: {}"
        #datetime INPUT: "user input that wasn't a command or other."
        this.userInputStr = "{} INPUT: {}"
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
        return 0
    def endLogging(this, dateTimeIn):
        return 0
    def _writeToFile(this, thingIn):
        file =open(this.filepath+this.filename,'a')
        return 0