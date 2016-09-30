#!/usr/bin/env python3

import sqlite3
import sys

# build db in current directory if it doesn't exist
if len(sys.argv) > 1:
    dbPath = str(sys.argv[1])
    try:
        dbObj = sqlite3.connect(dbPath)
        dbCursor = dbObj.cursor()
        print("Initializing database file")
        dbCursor.execute("CREATE TABLE posts(postID integer primary key autoincrement, title text, desc text, timestamp unsigned big integer, rating unsigned integer);")
        print("Created table posts")
        print("Committing changes")
        dbObj.commit()
        print("Closing DB connection")
        dbObj.close()
        print("DB connection closed")
    except:
        print("Error Occured - most likely a database issue")
else:
    print("Not enough arguments")

