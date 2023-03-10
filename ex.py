class Commande:
    def __init__(self, date, numero, prix = 0):
        self.date = date
        self.numero = numero
        self.prix = prix

    def get_date(self):
        return self.date

    def get_numero(self):
        return self.numero

    def get_prix(self):
        return self.prix

    def calculTVA(self):
        return self.prix * 0.196

    def __add__(self, other_commande):
        if(self.numero > other_commande.numero):
            return Commande(self.date, self.numero + 1, self.prix + other_commande.prix)
        else:
            return Commande(other_commande.date, other_commande.numero + 1, self.prix + other_commande.prix)

    def acquitter(self, todayDate):
        return CommandeAcquitter(self.date, self.numero, self.prix, todayDate)


class CommandeAcquitter(Commande):
    def __init__(self, date, numero, prix = 0, paiementDate):
        super().__init__(date, numero, prix)

class Client:
    def __init__(self, nom, addresse):
        self.nom = nom
        self.addresse = addresse

    def get_nom(self):
        return self.date

    def get_addresse(self):
        return self.numero

    def contacter(self):
        print("Nom du Client :", self.nom, "\nAddresse du Client :", self.addresse)

commande = Commande(20, 23, 2000.99)
commande2 = Commande(20, 13, 230.99)
print("Date :", commande.get_date(), "\nPrix :", commande.get_prix())
print("Calcul de la TVA :", commande.calculTVA())
newCommande = commande2.__add__(commande)
print("Date :", newCommande.get_date(), "\nPrix :", newCommande.get_prix(), "\nNumero :", newCommande.numero)