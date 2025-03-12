class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}, {self.num_pages} pages"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __contains__(self, word):
        return word in self.title


book1 = Book("Brave New World", "Aldous Huxley", 311)
book2 = Book("1984", "George Orwell", 328)
book3 = Book("Animal Farm", "George Orwell", 140)
book4 = Book("Animal Farm", "George Orwell", 112)

print(book1)
print(book3 == book4)
print(book1 < book2)
print(book1 > book2)
print("Brave" in book1)