#15
liste = [17, 38, 10, 25, 72]
liste.sort()
print(liste)
liste.append(12)
print(liste)
liste.reverse()
print(liste)
print(liste.index(17))
liste.remove(38)
print(liste)
print(liste[1:3])
print(liste[:2])
print(liste[2:])
print(liste[:])

#16
chaine = input("Entrez une chaine de caractère à inverser : ")
print(chaine[::-1])

#17
chaine = input("Entrez une chaine qui est peut-être un palindrome : ")
if chaine == chaine[::-1]:
    print(chaine, "est un palindrome")


#18
chaine = input("Entrez un email valide ou non : ")
if '@' in chaine and '.' in chaine:
    before, after = chaine.rsplit(".", 1)
    if len(after) <= 3:
        print("La chaîne est un email valide")
    else:
        print("La chaîne n'est pas un email valide : trop de caractères après le point")
else:
    print("La chaîne n'est pas un email valide : pas de @")


#19
truc = []  # initialise une liste vide
machin = [0.0] * 5  # initialise une liste de 5 flottants nuls
print(truc)  # affiche []
print(machin)  # affiche [0.0, 0.0, 0.0, 0.0, 0.0]


#20
# les entiers de 0 à 3
for i in range(4):
    print(i)
# les entiers de 4 à 7
for i in range(4, 8):
    print(i)
# les entiers de 2 à 8 par pas de 2
for i in range(2, 9, 2):
    print(i)
chose = [0, 1, 2, 3, 4, 5]
print(3 in chose)
print(6 in chose)


