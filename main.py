integer = 10
string = "Hallo"
liste = [1, 2, 3]
liste2 = [3, 2, 1]


def callByValueOReference(typ):
    typ = "Call By Value"
    print(typ)


def listChangeElement(li):
    if len(li) >= 1:
        li[1] = "changed"
    print(li)


def listNewElement(li):
    li = liste2
    print(li)


print("Vorher:")
print(integer)
callByValueOReference(integer)
print("Nachher:")
print(integer)

print("\nVorher:")
print(string)
callByValueOReference(string)
print("Nachher:")
print(string)

print("\nVorher:")
print(liste)
print("Nach der Change-Funktion:")
listChangeElement(liste)
print("Nach der New-Funktion:")
listNewElement(liste)
