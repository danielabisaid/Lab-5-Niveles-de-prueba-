from library import Library
from book import Book
from user import User

def run():
    lib = Library()
    lib.add_book(Book("1984", "George Orwell", 1949, "ISBN001"))
    lib.add_user(User("Anna", "U001"))

    while True:
        print("\n--- Library System ---")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. View user history")
        print("0. Exit")

        option = input("Choose an option: ")

        if option == "0":
            break
        elif option == "1":
            isbn = input("Enter book ISBN: ")
            user_id = input("Enter user ID: ")
            try:
                lib.borrow_book(user_id, isbn)
                print("Book successfully borrowed")
            except ValueError as e:
                print("Error:", e)
        elif option == "2":
            isbn = input("Enter book ISBN: ")
            user_id = input("Enter user ID: ")
            try:
                lib.return_book(user_id, isbn)
                print("Book successfully returned")
            except ValueError as e:
                print("Error:", e)
        elif option == "3":
            user_id = input("Enter user ID: ")
            try:
                user = lib._find_user(user_id)
                print("User history:", user.get_history())
            except ValueError as e:
                print("Error:", e)
        else:
            print("Invalid option")

if __name__ == "__main__":
    run()
