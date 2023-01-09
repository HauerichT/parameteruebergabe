integer = 10
string = "Hallo"
liste = [1, 2, 3]


def callByValueOReference(typ):
    typ = "Call By Value"
    print(typ)


def listChangeElement(list):
    if len(list) >= 1:
        list[1] = "changed"
    print(list)


def listNewElement(list):
    list = [3, 2, 1]
    print(list)


print("Vorher:")
print(integer)
print(string + "\n")

callByValueOReference(integer)
callByValueOReference(string)
print("\nNachher:")
print(integer)
print(string + "\n")

print("Vorher:")
print(liste)
print("Nach der Change-Funktion:")
listChangeElement(liste)
print("Nach der New-Funktion:")
listNewElement(liste)
