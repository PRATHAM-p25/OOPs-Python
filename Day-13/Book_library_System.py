class Publisher:
    def __init__(self, publisher):
        self.publisher=publisher

class Series(Publisher):
    def __init__(self, publisher, series_name):
        super().__init__(publisher)
        self.series_name=series_name

class Book(Series):
    def __init__(self, publisher, series_name, title):
        super().__init__(publisher,series_name)
        self.title=title

    def info(self):
        return f'{self.title} is part of the {self.series_name} series published by {self.publisher}.'

b1 = Book("Harper", "Earth Saga", "Final Planet")
print( b1.info())