file = open("people_file", "r")
l1=file.read()
lista=l1.split("\n")
osoby=[]
for osoba in lista:
    osoby.append(osoba.split(" "))
file.close()

print(osoby)