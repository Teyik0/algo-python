# Demander à l'utilisateur un nombre x chaine de caractère
x = int(input("Entrez un nombre de chaine de caractère : "))
# Ouvrir le fichier "data.txt" en mode écriture
with open("data.txt", "w") as f:
    # Demander à l'utilisateur x chaînes de caractères
    for i in range(x):
        chaine = input(f"Entrez la chaîne {i+1} : ")
        # Écrire la chaîne dans le fichier
        f.write(chaine + "\n")


# Ouvrir le fichier "data.txt" en mode lecture
with open("data.txt", "r") as f:
    # Lire les lignes du fichier
    lignes = f.readlines()
    # Parcourir chaque ligne et vérifier si elle est une adresse e-mail
    for ligne in lignes:
        # Supprimer les espaces en début et fin de ligne
        ligne = ligne.strip()
        # Vérifier si la ligne contient "@" et ".com"
        if "@" in ligne and ligne.endswith(".com"):
            print(f"{ligne} est une adresse e-mail valide.")
        else:
            print(f"{ligne} n'est pas une adresse e-mail valide.")


def compterMots(chaine):
    # Séparer la chaîne en une liste de mots
    mots = chaine.split()
    # Initialiser un dictionnaire vide pour stocker la fréquence des mots
    freq = {}
    # Parcourir chaque mot et compter sa fréquence
    for mot in mots:
        # Si le mot est déjà dans le dictionnaire, ajouter 1 à sa fréquence
        if mot in freq:
            freq[mot] += 1
        # Sinon, ajouter le mot au dictionnaire avec une fréquence de 1
        else:
            freq[mot] = 1
    # Renvoyer le dictionnaire de fréquence
    return freq


def cube(x):
    return x ** 3
def volumeSphere(r):
    pi = 3.14159
    return (4 / 3) * pi * cube(r)
# Tester la fonction volumeSphere avec un rayon de 5
rayon = 5
volume = volumeSphere(rayon)
print(f"Le volume d'une sphère de rayon {rayon} est {volume}")


def somme(a, b, c):
    return a + b + c
t = (1, 2, 3)
resultat = somme(*t)
print(resultat)
