class Book:
    # Constructor to initialize the book's title, author, and number of pages
    def __init__(self, title, author, num_pages):
        self.title = title  # Title of the book
        self.author = author  # Author of the book
        self.num_pages = num_pages  # Number of pages in the book

    # Method to return a string representation of the book
    def __str__(self):
        return f"{self.title} by {self.author}, {self.num_pages} pages"


book1 = Book("Brave New World", "Aldous Huxley", 311)
book2 = Book("1984", "George Orwell", 328)
book3 = Book("Animal Farm", "George Orwell", 112)

print(book1)
print(book2)
print(book3)

# Output:
# Brave New World by Aldous Huxley, 311 pages
# 1984 by George Orwell, 328 pages
# Animal Farm by George Orwell, 112 pages
# Note: The __str__ method is called when we print the object
#       It allows us to define how the object is represented as a string