class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

    def display_book_details(self):
        print('The title of the book is', self.title)
        print('The author of the book is', self.author)

class IssuedBook(Book):
    def __init__(self,title,author,issued_to,issued_date):
        super().__init__(title,author)
        self.issued_to=issued_to
        self.issued_date=issued_date

    def display_issued_book_details(self):
        super().display_book_details()
        print(f'The book {self.title} issued to',self.issued_to)
        print(f'The issued date of the book {self.title} is',self.issued_date)

obj=IssuedBook('A song of ice and fire','George RR Martin','Jon Snow','1999-10-17')
obj.display_issued_book_details()
