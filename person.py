class Person():
    name = ""
    surname = ""
    date_of_birth = ""
    place_of_birth = ""

    def __init__(self, imie, nazwisko, data, miejsce):
        self.name = imie
        self.surname = nazwisko
        self.date_of_birth = data
        self.place_of_birth = miejsce
    def __str__(self):
        return (f'({self.name},{self.surname},{self.date_of_birth},{self.place_of_birth})')

obiekt1 = Person("Michał","Weiss","20.10.1997","Piła")

print(obiekt1)