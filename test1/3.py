class Book:
    library_name = "ABC Library"
    def __init__(self, book_name, author, pages):
        self.book_name = book_name
        self.author = author
        self.pages = pages
        print("**************", Book.library_name, "***************")
        print("Book Name:", self.book_name, "\nAuthor:", self.book_name, "Number of Pages:", self.pages)


book_name = input("Book Name:")
author = input("Author Name:")
pages = input("Number of Pages:")
wings = Book(book_name, author, pages)
