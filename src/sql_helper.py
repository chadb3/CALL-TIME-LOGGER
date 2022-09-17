import sqlite3
database="data/callDB.sqlite3"
DB=["CALL","COMPANY","LOGS"]
#SELECT name from sqlite_master WHERE type='table';

class callTimeDB:
    def __init__(this):
        this.DB="data/callDB.sqlite3"
        this.MODE="?mode=rw"
        this.TABLES=["CALL","COMPANY","LOGS"]
        None
    def INSERT_CALL(this, call_IN):
        None
    def SELECT_CALL(this, call_ID_IN):
        None
    def REMOVE_CALL(this, call_ID_IN):
        None
    def testing_select_call(this,testCallIn):
        None