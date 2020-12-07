import read_files as reader
import person, book

# CZYTANIE OSÓB Z PLIKU
lista_osob_str = reader.read(file_name="people_file")
people = [] #lista obiektóœ typu Person
for os in lista_osob_str:
    people.append(person.Person(os[0],os[1],os[2],os[3]))


#CZYTANIE KSIĄŻEK Z PLIKÓW
books = [] #lista obiektów typu '# Book
lista_ksiazek_str = reader.read(file_name="books_file")
for b in lista_ksiazek_str:
    books.append(book.Book(b[0],b[1],b[2],b[3]))


# W TYM MIEJSCU MAMY :
#  books - lista obiektów typu Book (wyczytany z pliku books_file)
#  people - lista obiektów typu Person (wyczytany z pliku people_file)

#ŚCIĄGA
kubus = books[1]
wiedzmin = books[2]
daniel = people[3]
michal = people[0]
daniel.rent_book(kubus)
daniel.rent_book(wiedzmin)
print(daniel.list_of_books)
daniel.give_back_all_books()


print("koniec")