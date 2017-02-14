import sqlite3

DBINITSTRING = "CREATE TABLE IF NOT EXISTS vidData (vidName TEXT, vidDesc TEXT, categoryOne TEXT, categoryTwo TEXT, uploadDate INT);"

# uploadDate is stored as a Unix time stamp
# a Unix time stamp is the measure of the
# seconds since Jan 1, 1970 00:00:00 UTC

def getDBCon(dbPath):
    dbConObj = sqlite3.connect(dbPath)
    return dbConObj

def dbInit(dbObj):
    cursor = dbObj.cursor()
    #init cursor for db init
    cursor.execute(DBINITSTRING)
    #commit to db and leave cursor to die
    dbObj.commit()

def dbClose(dbObj):
    #commit and close
    dbObj.commit()
    dbObj.close()

def queryDBSimple(dbObj, limit):
    cursor = dbObj.cursor()
    #execute SQL statement
    cursor.execute("SELECT vidName, vidDesc, categoryOne, categoryTwo, uploadDate FROM vidData;")
    #get all queries
    return cursor.fetchall()
