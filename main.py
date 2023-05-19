# Should have planned this ahead before going straight to code...
from LibraryCoordinator import LibraryCoordinator
from function import *
a = 12.123
a = "{:.2f}".format(a)
print(a)
def main_menu():
    print("_______________ Main _______________")
    print("|\t1. Librarian                   |")
    print("|\t2. Rent Books                  |")
    print("|\t3. Patron                      |")
    print("|\t4. Exit                        |")
    print("____________________________________")


def librarian_menu():
    print("_______________ Librarian _______________")
    print("|\t1. Add author                       |")
    print("|\t2. Add book                         |")
    print("|\t3. View authors                     |")
    print("|\t4. Back to main                     |")
    print("_________________________________________")


def getNames(type="author"):
    fname = input(f"Enter {type} first name: ")
    lname = input(f"Enter {type} last name: ")
    return fname, lname


def addAuthor():
    names = getNames()
    email = input("Enter author email: ")
    coordinator.addAuthor(names[0], names[1], email)


def addBook():
    title = input("Enter book title: ")
    category = input("Enter book category: ")
    price = get_float("Enter price: ")
    names = getNames()
    coordinator.addBook(title, category, price, names[0], names[1])


def viewAuthors():
    coordinator.listAuthor()


def book_menu():
    print("___________________ Book ___________________")
    print("|\t1. All books                           |")
    print("|\t2. By category                         |")
    print("|\t3. From an author                      |")
    print("|\t4. By category and author              |")
    print("|\t5. By title                            |")
    print("|\t6. Back to main / check out            |")
    print("____________________________________________")


def viewAllBooks():
    return coordinator.displayBooks()


def viewBooksByCat():
    cat = input("Enter category: ")
    return coordinator.displayBooksByCategory(cat)


def viewBooksFromAuthor():
    names = getNames()
    return coordinator.displayBooksByAuthorName(names[0], names[1])


def viewBooksByAuthorAndCat():
    cat = input("Enter category: ")
    names = getNames()
    return coordinator.displayBooksByAuthorAndCat(names[0], names[1], cat)


def searchBookByTitle():
    title = input("Enter book title: ")
    return coordinator.displayBookByTitle(title)


def patron_menu():
    print("___________________ Patron ___________________")
    print("|\t1. Add patron                            |")
    print("|\t2. View patrons                          |")
    print("|\t3. View borrow history of a patron       |")
    print("|\t4. Back to main                          |")
    print("______________________________________________")


def addPatron():
    names = getNames("patron")
    email = input("Enter patron email: ")
    coordinator.addPatron(names[0], names[1], email)


def viewPatrons():
    coordinator.listPatron()


def viewBorrowHistory():
    names = getNames("patron")
    email = input("Enter patron email: ")
    coordinator.viewPatronBorrowHistory(names[0], names[1], email)


def getPatronObj():
    names = getNames("patron")
    email = input("Enter patron email: ")
    patron = coordinator.getPatronObj(names[0], names[1], email)
    if patron is None:
        print(f"Patron {names[0]} {names[1]} does not exist")
    return patron


def addBookToPatronCart(patron, book):
    coordinator.addBookToPatronCart(patron, book)


coordinator = LibraryCoordinator()
main_menu()
choice = get_int("Please pick: ", 1, 4)
while choice != 4:
    # Librarian
    if choice == 1:
        librarian_menu()
        choice = get_int("Please pick: ", 1, 4)
        while choice != 4:
            if choice == 1:
                addAuthor()
            elif choice == 2:
                addBook()
            elif choice == 3:
                viewAuthors()
            librarian_menu()
            choice = get_int("Please pick: ", 1, 4)
    elif choice == 2:
        patron = getPatronObj()
        if patron is not None:
            book_menu()
            choice = get_int("Please pick: ", 1, 6)
            while choice != 6:
                if choice == 1:
                    book = viewAllBooks()
                elif choice == 2:
                    book = viewBooksByCat()
                elif choice == 3:
                    book = viewBooksFromAuthor()
                elif choice == 4:
                    book = viewBooksByAuthorAndCat()
                elif choice == 5:
                    book = searchBookByTitle()
                if book is not None:
                    addBookToPatronCart(patron, book)
                book_menu()
                choice = get_int("Please pick: ", 1, 6)
            patron.confirmBooks()
            patron = None
        else:
            print("This patron does not exist. You will be send back to main menu")
    elif choice == 3:
        patron_menu()
        choice = get_int("Please pick: ", 1, 4)
        while choice != 4:
            if choice == 1:
                addPatron()
            elif choice == 2:
                viewPatrons()
            elif choice == 3:
                viewBorrowHistory()
            patron_menu()
            choice = get_int("Please pick: ", 1, 4)
    main_menu()
    choice = get_int("Please pick: ", 1, 4)
closeConnections()
