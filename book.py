class Book():
    #KONSTRUKTOR - TWORZY OBIEKTY
    def __init__(self, nazwa, autor, data, wydawca):
        self.name = nazwa
        self.author = autor
        self.date_of_publishing = data
        self.publisher = wydawca
        self.is_rented = False
    def rent (self):
        self.is_rented = True
    def give_back(self):
        self.is_rented = False

    def __str__(self):
        return (f'({self.name},{self.author},{self.date_of_publishing},{self.publisher})')