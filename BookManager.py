from Patron import Patron
from function import *
from Book import Book

class BookManager:
    def __init__(self):
        pass

    def addBook(self, title, category, price, authorId):
        if (self.bookTitleExists(title)):
            print(f"Book with title '{title}' is already existed")
        else:
            query = "INSERT INTO Book values (?, null, ?, ?, ?)"
            executor(query, authorId, title, price, category)

    def bookTitleExists(self, title):
        query = "SELECT * from Book where Title = ?"
        result = executor(query, title)
        return len(result) > 0

    def getBook(self, result, authorJoined=False):
        count = 0
        if len(result) == 0:
            print("Currently empty...")
        else:
            if authorJoined:
                for row in result:
                    print(f"{count + 1}. Title: {row['Title']} | Category: {row['Category']} |"
                          f" Price: ${row['Price']} | Author: {row['FirstName']} {row['LastName']}")
                    count += 1
            else:
                for row in result:
                    print(f"{count + 1}. Title: {row['Title']} | Category: {row['Category']} | Price: ${row['Price']} ")
                    count += 1
            if count > 0:
                bookChoice = get_int("Choose (enter 0 if you don't want any): ", 0, count) - 1
                if bookChoice != -1:
                    book = result[bookChoice]
                    book = Book(book['Title'], book['Category'], float(book['Price']), int(book['BookId']))
                    print(f"'{book.title}' added")
                    return book
        return None

    def getBooks(self):
        query = "SELECT * from Book b join Author a on b.AuthorId = a.AuthorId"
        result = executor(query)
        return self.getBook(result, authorJoined=True)

    def getBooksByAuthorName(self, firstName, lastName):
        query = "SELECT * from Book b join Author a on b.AuthorId = a.AuthorId where FirstName = ? and LastName = ?"
        return self.getBook(executor(query, firstName, lastName))

    def getBooksByTitle(self, title):
        query = "SELECT * from Book where Title = ?"
        return self.getBook(executor(query, title))

    def getBooksByCategory(self, category):
        query = "SELECT * from Book where Category = ?"
        return self.getBook(executor(query, category))

    def getBooksByAuthorAndCat(self, firstName, lastName, category):
        query = "SELECT * from Book b join Author a on b.AuthorId = a.AuthorId " \
                "where FirstName = ? and LastName = ? and category = ?"
        return self.getBook(executor(query, firstName, lastName, category))

