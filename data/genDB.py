# don't know how the below got imported. 
#from fileinput import filename
import sqlite3
test_filename="PNDB_test.sqlite3"
filename="PNDB.sqlite3"

call="""CREATE TABLE "CALL" (
	"CALL_NUM"	INTEGER NOT NULL DEFAULT 1 UNIQUE,
	"CALL_NUM_S"	INTEGER NOT NULL,
	"CALL_TIME"	NUMERIC NOT NULL,
	"CALL_DATE"	NUMERIC NOT NULL,
	"CALL_TIME_END"	NUMERIC NOT NULL,
	"CALL_DATE_END"	NUMERIC NOT NULL,
	PRIMARY KEY("CALL_NUM" AUTOINCREMENT)
)"""
company ="""CREATE TABLE "COMPANY" (
	"COMPANY_DB_ID"	INTEGER NOT NULL DEFAULT 1 UNIQUE,
	"COMPANY_ID"	INTEGER UNIQUE,
	"COMPANY_NAME"	TEXT DEFAULT 'N/A',
	"ALAIS"	TEXT DEFAULT 'N/A',
	"IS_CLIENT"	NUMERIC DEFAULT 'TRUE',
	"IS_INTERNAL"	NUMERIC DEFAULT 'FALSE',
	PRIMARY KEY("COMPANY_DB_ID" AUTOINCREMENT)
)"""

logs="""CREATE TABLE "LOGS" (
	"LOG_ID"	INTEGER NOT NULL DEFAULT 1 UNIQUE,
	"LOG_ID_S"	INTEGER,
	"DATE_TIME"	NUMERIC NOT NULL,
	"DATA"	TEXT NOT NULL,
	PRIMARY KEY("LOG_ID" AUTOINCREMENT)
)"""

def test_createDB():
    try:
        con=sqlite3.connect(test_filename)
        cur=con.cursor()
        cur.execute(call)
        cur.execute(company)
        cur.execute(logs)
        con.commit()
        con.close()
    except Exception as e:
        print(e)

def addTable():
    None

def addData():
    None

def main():
    print("ATTEMPTING TO CREATE DB")
    test_createDB()
    addTable()
    addData()
    print("DB CREATED")

if __name__=='__main__':
    main()