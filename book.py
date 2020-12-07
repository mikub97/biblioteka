class Book():
    name = ""
    author = ""
    date_of_publishing = ""
    publisher = ""

    def __init__(self, nazwa, autor, data, wydawca):
        self.name = nazwa
        self.author = autor
        self.date_of_publishing = data
        self.publisher = wydawca

    def __str__(self):
        return (f'({self.name},{self.author},{self.date_of_publishing},{self.publisher})')