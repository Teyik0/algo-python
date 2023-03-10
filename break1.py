#1
temps = 6.892
distance = 19.7
vitesse = distance / temps
print("La vitesse est:", vitesse, "m/s")


#2
nom = input("Entrez votre nom : ")
age = int(input("Entrez votre âge : "))
print("Vous vous appelez", nom, "et vous avez", age, "ans.")


#3
import math
x = float(input("Entrez un nombre flottant : "))
if x >= 0:
    racine = math.sqrt(x)
    print("La racine carrée de", x, "est", racine)
else:
    print("Erreur : le nombre saisi est négatif.")


# 4
mot1 = input("Entrez le premier mot : ")
mot2 = input("Entrez le deuxième mot : ")
if mot1 < mot2:
    print("Le mot", mot1, "vient avant", mot2, "dans l'ordre lexicographique.")
elif mot1 > mot2:
    print("Le mot", mot2, "vient avant", mot1, "dans l'ordre lexicographique.")
else:
    print("Les deux mots sont identiques.")

#5
pSeuil = 2.3
vSeuil = 7.41
pression = float(input("Entrez la pression courante de l'enceinte : "))
volume = float(input("Entrez le volume courant de l'enceinte : "))
if pression > pSeuil and volume > vSeuil:
    print("Arrêt immédiat : pression et volume trop élevés !")
elif pression > pSeuil:
    print("La pression est trop élevée. Augmentez le volume de l'enceinte.")
elif volume > vSeuil:
    print("Le volume est trop élevé. Diminuez le volume de l'enceinte.")
else:
    print("Tout va bien : pression et volume dans les limites autorisées.")