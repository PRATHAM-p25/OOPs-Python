class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"Book: {self.title} by {self.author} - ₹{self.price}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', price={self.price})"


b1 = Book("Clean Code", "Robert C. Martin", 499)
b2 = Book("Atomic Habits", "James Clear", 399)

print(b1)
print(b2)

book_list = [b1, b2]
print(book_list)
