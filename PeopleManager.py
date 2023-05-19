from function import *
from Patron import Patron

class PeopleManager:
    def __init__(self):
        pass

    def addAuthor(self, firstName, lastName, email):
        if self.__emailExists(email, "Author"):
            print(f"The email {email} is already in use!")
        else:
            query = "INSERT INTO Author values (?, ?, null, ?)"
            executor(query, firstName, lastName, email)

    def addPatron(self, firstName, lastName, email):
        if self.__emailExists(email, "Patron"):
            print(f"The email {email} is already in use!")
        else:
            query = "INSERT INTO Patron values (null, ?, ?, ?)"
            executor(query, firstName, lastName, email)
            return True

    def getPatronObj(self, fname, lname, email):
        query = "SELECT * from Patron where FirstName = ? and LastName = ? and Email = ?"
        result = executor(query, fname, lname, email)
        if len(result) == 0:
            return None
        else:
            return Patron(result[0]['PatronId'], fname, lname, email)

    def viewPatronBorrowHistory(self, fname, lname, email):
        patron = self.getPatronObj(fname, lname, email)
        if patron is not None:
            patron.viewBorrowHistory()

    def viewPatronCart(self, fname, lname, email):
        patron = self.getPatronObj(fname, lname, email)
        if patron is not None:
            patron.displayBooksInCart()

    def checkOut(self, fname, lname, email):
        patron = self.getPatronObj(fname, lname, email)
        if patron is not None:
            patron.confirmBooks()

    def listAuthor(self):
        query = "SELECT * from Author"
        self.__displayResult(executor(query))

    def listPatron(self):
        query = "SELECT * from Patron"
        self.__displayResult(executor(query))

    def __displayResult(self, result):
        if len(result) == 0:
            print("Currently empty...")
        else:
            count = 1
            for row in result:
                print(f"{count}. Name: {row['FirstName']} {row['LastName']} | Email: {row['Email']} ")
                count += 1

    def getAuthorId(self, fname, lname):
        return self.__getId(fname, lname, "Author")

    def getPatronId(self, fname, lname):
        return self.__getId(fname, lname, "Patron")

    def __getId(self, firstName, lastName, table):
        query = f"SELECT * FROM {table} where firstName = ? and lastName = ?"
        result = executor(query, firstName, lastName)
        if len(result) > 1:
            print(f"There are {table} with same name. Please choose one from the list:")
            self.displayResult(result)
            userChoice = get_int("Choose: ", 1, len(result)) - 1
            print(result[userChoice]['Email'])
            return result[userChoice][f'{table}Id']
        elif len(result) == 1:
            return result[0][f'{table}Id']
        else:
            print(f"'{firstName} {lastName}' doesn't exist!")
            return -1

    def __remove(self, fname, lname, table):
        if table == "Patron":
            id = self.__getPatronId(fname, lname)
        elif table == "Author":
            id = self.__getPatronId(fname, lname)
        if id != -1:
            query = f"DELETE from {table} where {table}Id = ?"
            executor(query, id)

    def __emailExists(self, email, table):
        query = f"SELECT * from {table} where Email = ?"
        result = executor(query, email)
        return len(result) > 0

    def checkOutAPatron(self, patron):
        patron.confirmBooks()