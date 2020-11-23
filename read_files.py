def read(file_name):
    file = open(file_name, "r")
    l1=file.read()
    lista=l1.split("\n")
    osoby=[]
    for osoba in lista:
        osoby.append(osoba.split(" "))
    file.close()
    return(osoby)

