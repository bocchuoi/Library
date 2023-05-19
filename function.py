from sqlite3 import DatabaseError
import sqlite3
import datetime

try:
    dbCon = sqlite3.connect("Library.db")
except:
    print("Database connection error")
dbCon.row_factory = sqlite3.Row
cursor = dbCon.cursor()

log = open("databaseErrorLog.txt", "a")


def executor(query, *values):
    global cursor, dbCon, log
    # printQuery = query
    # for value in values:
    #     printQuery = printQuery.replace("?", str(value), 1)
    try:
        # print("--- Executing ---")
        # print(f"Query: {printQuery}")
        if values:
            cursor.execute(query, (values))
        else:
            cursor.execute(query)
        dbCon.commit()
    except DatabaseError as e:
        log.write(f"{datetime.datetime.now()} - Error {e}")
    return cursor.fetchall()


def get_int(prompt, lowerLim, upperLim=2147483647):
    userInput = input(prompt)
    while not userInput.isnumeric() or int(userInput) < lowerLim or int(userInput) > upperLim:
        userInput = input(prompt)
    return int(userInput)


def get_float(prompt):
    userInput = input(prompt)
    # Replace first instance of "." For example, 2.00 -> 200 and then check with isdidgit()
    while not userInput.replace(".", "", 1).isdigit():
        userInput = input(prompt)
    return float(userInput)


# Return true if user enters yes
def yes_no(prompt="One more time?"):
    userInput = input(f"{prompt} (type yes or no): ").lower()
    # Force user to enter only yes or no
    while userInput != "yes" and userInput != "no":
        userInput = input("Please type \"yes\" or \"no\": ").lower()
    return userInput == "yes"


def closeConnections():
    global dbCon, cursor, log
    cursor.close()
    dbCon.close()
    log.close()

