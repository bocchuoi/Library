from Person import Person
from Book import Book
from function import *
from datetime import datetime
from datetime import timedelta


class Patron(Person):
    def __init__(self, id, firstName, lastName, email):
        super().__init__(id, firstName, lastName, email)
        self.books = []

    def addBook(self, book:Book):
        self.books.append(book)

    def displayBooksInCart(self):
        for book in self.books:
            book.__str__()

    def viewBorrowHistory(self):
        query = "SELECT * FROM BorrowHistory bh join Book b on bh.BookId = b.BookId WHERE PatronId = ?"
        result = executor(query, self._id)
        print(f"--- Borrow history of {self.firstName} {self.lastName} ---")
        if len(result) > 0:
            for row in result:
                formattedFloat = "{:.2f}".format(row['FeePaid'])
                print(f"Book title: {row['title']} | Return Date: {row['ReturnDate']} | Fee Paid: ${formattedFloat}")
        else:
            print("This patron have never borrowed any books...")

    def confirmBooks(self):
        newBooks = self.books.copy()
        for book in newBooks:
            book.__str__()
            days = get_int("How many days do you want to borrow? (Enter 0 to drop this book): ", 0, 60)
            if days != 0:
                fee = book.calCost(days)
                returnDate = (datetime.now() + timedelta(days=days)).strftime("%d/%m/%Y %H:%M:%S")
                formattedFloat = "{:.2f}".format(fee)
                if yes_no(f"Renting {book.title} for {days} days will cost you ${formattedFloat}. Is that ok? "):
                    query = "INSERT INTO BorrowHistory values (?, ?, ?, ?, null)"
                    executor(query, self._id, book.bookId, fee, returnDate)
                    self.books.remove(book)
            else:
                self.books.remove(book)

