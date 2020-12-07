import read_files as reader
import person, book


lista_osob_str = reader.read(file_name="people_file")
people = [] #lista obiektóœ typu Person
people.append(person.Person("Jacek","Kaczmarski","3243234-32","Warszawa"))

for os in lista_osob_str:
    people.append(person.Person(os[0],os[1],os[2],os[3]))

lista_ksiazek_str = reader.read(file_name="books_file")
print(lista_ksiazek_str)
print("koniec")