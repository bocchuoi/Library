from function import *


class AuthorManager:
    def __init__(self):
        pass

    def addAuthor(self, firstName, lastName, email):
        query = "INSERT INTO Author values (?, ?, null, ?)"
        executor(query, firstName, lastName, email)

    def list(self):
        query = "SELECT * from Author"
        result = executor(query)
        self.displayResult(result)

    def displayResult(self, result):
        count = 1
        for row in result:
            print(f"{count}. Author Name: {row['FirstName']} {row['LastName']} | Email: {row['Email']} ")
            count += 1

    def getId(self, firstName, lastName):
        query = "SELECT * FROM Author where firstName = ? and lastName = ?"
        result = executor(query, firstName, lastName)
        if len(result) > 1:
            count = 1
            print("There are authors with same name. Please choose one from the list:")
            self.displayResult(result)
            userChoice = get_int("Choose: ", 1, len(result)) - 1
            print(result[userChoice]['Email'])
            return result[userChoice]['AuthorId']
        elif len(result) == 1:
            return result[0]['AuthorId']
        else:
            return -1