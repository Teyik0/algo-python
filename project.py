from tkinter import *


class AB:
    def __init__(self, racine=[None], gauche=None, droite=None):
        self.racine = racine
        self.gauche = gauche
        self.droite = droite

    def get_racine(self):
        return self.racine

    def set_racine(self, racine):
        self.racine = racine

    def get_gauche(self):
        return self.gauche

    def set_gauche(self, gauche):
        self.gauche = gauche

    def get_droite(self):
        return self.droite

    def set_droite(self, droite):
        self.droite = droite

    def estVide(self):
        return self.racine == [None] and self.gauche is None and self.droite is None

    def size(self):
        if self.estVide():
            return 0
        else:
            return 1 + (self.gauche.size() if self.gauche is not None else 0) + \
                (self.droite.size() if self.droite is not None else 0)

    def prefixe(self):
        if not self.estVide():
            print(self.racine)
            if self.gauche is not None:
                self.gauche.prefixe()
            if self.droite is not None:
                self.droite.prefixe()

    def postfixe(self):
        if not self.estVide():
            if self.gauche is not None:
                self.gauche.postfixe()
            if self.droite is not None:
                self.droite.postfixe()
            print(self.racine)

    def infixe(self):
        if not self.estVide():
            if self.gauche is not None:
                self.gauche.infixe()
            print(self.racine)
            if self.droite is not None:
                self.droite.infixe()

    def hauteur(self):
        if self.estVide():
            return -1
        else:
            return 1 + max(self.gauche.hauteur() if self.gauche is not None else -1,
                           self.droite.hauteur() if self.droite is not None else -1)

    def estABR(self):
        if self.estVide():
            return True
        elif self.gauche is None and self.droite is None:
            return True
        elif self.gauche is None:
            return self.droite.racine > self.racine and self.droite.estABR()
        elif self.droite is None:
            return self.gauche.racine < self.racine and self.gauche.estABR()
        else:
            return self.gauche.racine < self.racine < self.droite.racine and self.gauche.estABR() and self.droite.estABR()


A1 = AB()
print(A1.estVide())
A2 = AB([5])
print(A2.estVide())
A3 = AB([5])
A2.set_gauche(A3)

Atest = AB([10],
           AB([5], AB([3]), AB([8])),
           AB([12]))

Atest2 = AB([10],
           AB([5], AB([3], AB([5])), AB([8])),
           AB([12], AB([5])))

print("TESTING ATEST")
print("Noeud de droite ? :", Atest.get_droite().get_racine())
print("Taille de l'arbre", Atest.size())
print(Atest.prefixe())
print(Atest.postfixe())
print(Atest.infixe())
print("Hauteur de l'arbre : ", Atest.hauteur())
print("Est ABR : ", Atest.estABR())

fenetre = Tk()
fenetre.geometry('800x400')
fenetre.title('Tkinter AB Tracer')
fenetre.resizable(height=True, width=True)

canvas = Canvas(fenetre, width=800, height=400, bg='white')
canvas.pack()


def dessinerArbre(AB, incr, x0=375, y0=25, x1=425, y1=75):
    if not AB.estVide():
        canvas.create_oval(x0, y0, x1, y1, fill="blue", width=0)
        label = canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=str(AB.get_racine()[0]), fill='white',
                                   font=("Caveat", 20, "bold"))
        canvas.tag_raise(label)

        if AB.get_gauche() is not None:
            canvas.create_line((x0 + x1) / 2, y1, x0 - incr/1.2, y1 + (incr / 1.5))
            dessinerArbre(AB.get_gauche(), incr/2, x0 - incr, y0 + incr, x1 - incr, y1 + incr)

        if AB.get_droite() is not None:
            canvas.create_line((x0 + x1) / 2, y1, x1 + incr/1.2, y1 + (incr / 1.5))
            dessinerArbre(AB.get_droite(), incr/2, x0 + incr, y0 + incr, x1 + incr, y1 + incr)


dessinerArbre(Atest2, Atest2.hauteur() * 50)

fenetre.mainloop()
