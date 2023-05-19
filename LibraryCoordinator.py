from BookManager import BookManager
from AuthorManager import AuthorManager
from PeopleManager import PeopleManager
from function import *


class LibraryCoordinator:
    def __init__(self):
        self.bookMan = BookManager()
        self.peopleMan = PeopleManager()

    # Library functions
    def addBook(self, title, category, price, fName, lName):
        authorId = self.peopleMan.getAuthorId(fName, lName)
        if authorId == -1:
            if yes_no(f"Author '{fName} {lName}' does not exist. Do you want to add this author?"):
                email = input("Please enter email for this author: ")
                self.peopleMan.addAuthor(fName, lName, email)
                authorId = self.peopleMan.getAuthorId(fName, lName)
                if yes_no(f"Add the book {title} to this author?"):
                    self.bookMan.addBook(title, category, price, authorId)
        else:
            self.bookMan.addBook(title, category, price, authorId)

    def addAuthor(self, firstName, lastName, email):
        self.peopleMan.addAuthor(firstName, lastName, email)

    def listAuthor(self):
        self.peopleMan.listAuthor()

    def displayBooks(self):
        return self.bookMan.getBooks()

    def displayBooksByAuthorName(self, firstName, lastName):
        return self.bookMan.getBooksByAuthorName(firstName, lastName)

    def displayBookByTitle(self, title):
        return self.bookMan.getBooksByTitle(title)

    def displayBooksByCategory(self, category):
        return self.bookMan.getBooksByCategory(category)

    def displayBooksByAuthorAndCat(self, firstName, lastName, category):
        return self.bookMan.getBooksByAuthorAndCat(firstName, lastName, category)

    def addPatron(self, fname, lname, email):
        self.peopleMan.addPatron(fname, lname, email)

    def listPatron(self):
        self.peopleMan.listPatron()

    def addBookToPatronCart(self, patron, book):
        patron.addBook(book)

    def checkOutAPatron(self, patron):
        self.peopleMan.checkOutAPatron(patron)

    def getPatronObj(self, fname, lname, email):
        return self.peopleMan.getPatronObj(fname, lname, email)

    def viewPatronBorrowHistory(self, fname, lname, email):
        self.peopleMan.viewPatronBorrowHistory(fname, lname, email)
