class Person():

    #KONSTRUKTOR - TWORZY OBIEKTY
    def __init__(self, imie, nazwisko, data, miejsce):
        self.name = imie
        self.surname = nazwisko
        self.date_of_birth = data
        self.place_of_birth = miejsce
        self.list_of_books = []

    def __str__(self):
        return (f'({self.name},{self.surname},{self.date_of_birth},{self.place_of_birth})')


    def rent_book(self,book):
        self.list_of_books.append(book)
        print(f"{book.name} została wypożyczona przez {self.name}")

    def give_back_all_books(self):
        for b in self.list_of_books:
            print(f"{b.name} została oddana przez {self.name}")
        self.list_of_books = []


