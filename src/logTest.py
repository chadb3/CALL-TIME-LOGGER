from Log import *
from datetime import *
import time
logging = Log()
logging.logCommand(datetime.now(),"Help Command")
time.sleep(10)
logging.logUserInput(datetime.now(), "asdfasdf")
time.sleep(1)
logging.logUserInput(datetime.now(), "yes")
time.sleep(60)
logging.logSystem(datetime.now(),"System True")
time.sleep(60)
print(logging.endLogging(datetime.now()))