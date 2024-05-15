class Somme:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def som(self):
        return self.n1+self.n2
nbr1=int(input("Tapez le nombre 1: "))
nbr2=int(input("Tapez le nombre 2: "))
somme=Somme(nbr1,nbr2)
valeur=somme.som()
print(f"Le resultat de l'addition de ces deux nombres donne: {valeur}")
