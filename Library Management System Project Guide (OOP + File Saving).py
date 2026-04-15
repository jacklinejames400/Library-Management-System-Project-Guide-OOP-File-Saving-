import json
import os
class Book:
    def __init__(self, title, author, isbn, available = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
    def borrow(self):
        self.available = False
    def return_book(self) :
        self.available = True
    def to_dict(self):
        return{
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available
        }
    @staticmethod
    def from_dict(self):
        return Book(data["title"], data["author"], data["isbn"], data["available"])
    
class User:
    def __init__(self, name, user_id, borrowed_books = None):
        self.name = Name
        self.user_id = user_id
        self.borrowed_books = borrowed_books if borrowed_books else []
    def borrow_book(self, isbn):
        self.borrowed_books.append(isbn)
    def return_book(self, isbn):
        if isbn in self.borrowed_books:
           self.borrowed_books.remove(isbn)
    def to_dict(self):
        return{
            "name": self.name,
            "user_id": self.user_id,
            "borrowed_books": self.borrowed_books
        }
    @staticmethod
    def from_dict(data):
        return User(data["name"], data["user-id"], data["borrowed_books"])
class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.load_data()
    def load_data(self):
        if os.path.exists("books.json"):
            with open("books.json", "r") as f:
                users_data = json.load(f)
                self.books = [Book.from_dict(b) for b in books_data]
        if os.path.exists("users.json"):
            with open("users.json","r" ) as f:
                users_data = json.load(f)
                self.books = [User.from_dict(b) for b in users_data ]
    def save_data(self):
        with open("books.json", "w") as f:
            json.dump([b.to_dict() for b in self.books], f, indent = 4)
        with open("users.json", "w") as f:
            json.dump([u.to_dict() for u in self.users], f, indent = 4)

    def add_book(self, title,author,isbn):
        if self.find_book(isbn):
            print("Book already exists!")
            return
        self.users.append(User(name, user_id))
        self.save_data()
        print("User registered successfully!")
    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return Book
        return None
    def find_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return User
        return None
    def display_books(self):
        if not self.books:
            print("No Books available.")
            return
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f"{book.title} by {book.author} | ISBN: {book.isbn} | {status}")
    def borrow_book(self, user_id, isbn):
        user = self.find_user(user_id)
        book = self.find_book(isbn)
        if not user:
            print("User not found!")
            return
        if not book:
            print("Book not found!")
            return
        user.borrow_book(isbn)
        book.borrow()
        self.save_data()
        print("Book borrowed successfully!")

    def return_book(self, user_id, isbn):
        user = self.find_user(user_id)
        book = self.find_book(isbn)
        if not user or not book:
            print("User or Book not found!")
            return
        if isbn not in user.borrowed_books:
            print("This user did not borrow this book!")
            return
        user.return_book(isbn)
        book.return_book()
        self.save_data()
        print("Book returned successfully!")
def main():
        library = Library()
        while True:
            print("\n--- Library Menu ---")
            print("1. Add Book")
            print("2. Register User")
            print("3. Dispay All Books")
            print("4. Borrow Book")
            print("5. Return Book")
            print("6. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                title =  input("Title: ")
                author = input("Author: ")
                isbn = input("ISBN: ")
                library.add_book(title, author, isbn)
            elif choice == "2":
                name  = input("Name: ")
                user_id = input("User ID: ")
                library.register_user(name, user_id)

            elif choice == "3":
                library.display_books()
                
            elif choice == "4":
                user_id = input("user ID: ")
                isbn = input("ISBN: ")
                library.borrow_book(user_id, isbn)
            elif choice == "5":
                user_id = input("User ID: ")
                library.return_book(user_id, isbn)
            elif choice == "6":
                print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

        
        
            
        
