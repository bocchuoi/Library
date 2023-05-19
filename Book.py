from function import *


class Book:
    def __init__(self, title:str, category:str, price:float, bookdId:int):
        self.title = title
        self.category = category
        self.price = price
        self.bookId = bookdId

    def set(self, cursor, column:str, value):
        query = f"SET {column} = ? WHERE bookId = ?"
        executor(query, cursor, (value, self.bookId))

    def delete(self, cursor, column:str, value):
        query = "DELETE from Book where bookId = ?"
        executor(query, cursor, self.bookId)

    def calCost(self, days):
        return self.price * days

    def __str__(self):
        print(f"Title: {self.title} | Category: {self.category} | Price: {self.price} ")