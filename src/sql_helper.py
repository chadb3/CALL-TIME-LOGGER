import sys
from src.Call import Call
import sqlite3
database="data/callDB.sqlite3"
DB=["CALL","COMPANY","LOGS"]
#SELECT name from sqlite_master WHERE type='table';
"""class Call:
    def __init__(this, callNumber=-1):
        #this.callDate = ""
        this.callEnded=False
        this._callTime = ""
        this._callEndTime=""
        #this.callEndDate=""
        this._callNumber = callNumber
        this.setStartTime()"""
class callTimeDB:
    def __init__(this):
        this.DB="data/callDB.sqlite3"
        #this.MODE="?mode=rw" under review if needed also ,uri=True
        this.TABLES=["CALL","COMPANY","LOGS"]
        None
    def INSERT_CALL(this, call_IN):
        sqlConnection=sqlite3.connect(this.DB)
        ins=call_IN.getValues()
        #[this._callNumber,this._callTime.time(),this._callTime.date(),this._callEndTime.time(),this._callEndTime.date()]
        sqlCursor=sqlConnection.execute("""INSERT INTO CALL
        (CALL_NUM_S,CALL_TIME,CALL_DATE,CALL_TIME_END,CALL_DATE_END) 
        VALUES
        ('{}','{}','{}','{}','{}')""".format(ins[0],ins[1],ins[2],ins[3],ins[4]))
        sqlConnection.commit()
        sqlConnection.close()
        None
    def SELECT_CALL(this, call_ID_IN):
        sqlConnection=sqlite3.connect(this.DB)
        sqlConnection.close()
        None
    def UPDATE_END_TIME(this,call_in):
        sqlConnection=sqlite3.connect(this.DB)
        sqlConnection.close()
        None
    def REMOVE_CALL(this, call_ID_IN):
        sqlConnection=sqlite3.connect(this.DB)
        sqlConnection.close()
        None
    def testing_select_call(this,testCallIn):
        ssqlConnection=sqlite3.connect(this.DB)
        sqlConnection.close()
        None