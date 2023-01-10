integer = 10
string = "Hallo"
liste = [1, 2, 3]

print("Vorher:")
print("Integer: " + str(integer))
print("String: " + string)
print("Liste: " + str(liste))


def changeInt(a):
    a = 22


def changeString(b):
    b = "Test"


def changeList(c):
    d = ["blabla", 49]
    c = d


def changeElementList(d):
    d[1] = "changed"


changeInt(integer)
changeString(string)
changeList(liste)
print("changedListe: " + str(liste))
changeElementList(liste)

print("\nNachher:")
print("Integer: " + str(integer))
print("String: " + string)
print("Liste: " + str(liste))
