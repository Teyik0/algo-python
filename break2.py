#6
chaine = input("Entrez un email : ")
if '@' in chaine and chaine.endswith('.com'):
    print("C'est un email valide.")
else:
    print("Ce n'est pas un email valide.")


#7
message = input("Entrez le message à afficher : ")
for i in range(10):
    print("Ceci est le message numéro", i+1, ":", message)


#8
mot = input("Entrez un mot : ")
for lettre in mot:
    print(lettre)

#9
a = 0
b = 10
while a < b:
    print("a =", a)
    a += 1
#10
while b != 0:
    b -= 1
    if b % 2 == 1:
        print("b =", b)


#11
while True:
    saisie = input("Saisir un entier entre 1 et 10 : ")
    try:
        entier = int(saisie)
    except ValueError:
        print("Erreur : saisie non valide.")
        continue
    if entier < 1 or entier > 10:
        print("Erreur : l'entier doit être entre 1 et 10.")
        continue
    break
print("Vous avez saisi :", entier)

#12
chaine = "Bonjour tout le monde !"
for caractere in chaine:
    print(caractere)
liste = [1, 2, 3, 4, 5]
for element in liste:
    print(element)
for i in range(0, 15, 3):
    print(i)


#13
n = int(input("Entrez un entier positif : "))
i = 0
compteur = 0
while compteur < n:
    if i % 2 == 0:
        print(i)
        compteur += 1
    i += 1
n = int(input("Entrez un entier positif : "))
compteur = 0
for i in range(0, n*2, 2):
    if compteur < n:
        print(i)
        compteur += 1
    else:
        break