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
        sqlCursor=sqlConnection.execute("SELECT CALL WHERE CALL_ID ={}".format(call_ID_IN))
        sqlConnection.commit()
        sqlConnection.close()
        None
    def UPDATE_END_TIME(this,call_id,call_IN):
        sqlConnection=sqlite3.connect(this.DB)
        ins=call_IN.getValues()
        sqlCursor=sqlConnection.execute("UPDATE CALL SET CALL_TIME_END={},CALL_DATE_END={} WHERE CALL_ID={}".format(ins[3],ins[4],call_id))
        sqlConnection.commit()
        sqlConnection.close()
        None
    def REMOVE_CALL(this, call_ID_IN):
        sqlConnection=sqlite3.connect(this.DB)
        sqlConnection.close()
        None
    def SELECT_LAST_CALL_ID(this):
        sqlConnection=sqlite3.connect(this.DB)
        sqlCursor=sqlConnection.execute("SELECT CALL_NUM FROM CALL ORDER BY CALL_NUM DESC LIMIT 1")
        try:
            ret=sqlCursor.fetchone()
            sqlCursor.close()
            return ret
        except Exception as ex:
            sqlCursor.close()
            print(ex)
            return None
        sqlConnection.close()
    def testing_select_call(this,testCallIn):
        sqlConnection=sqlite3.connect(this.DB)
        sqlConnection.close()
        None
