class Account:
    def __init__(self,soldeInitial=0):
        self.soldeInitial=soldeInitial
        self.soldeActuel = self.soldeInitial
    def getBalance(self):
        return self.soldeActuel
    def deposer(self,montant):
        self.soldeActuel=self.soldeActuel+montant
    def retirer(self,montant):
        self.soldeActuel = self.soldeActuel - montant
    def ajouterInteret(self,taux):
        self.soldeActuel=self.soldeActuel*(1+taux)
compte=Account()
compte.deposer(1000)
compte.retirer(70)
compte.ajouterInteret(4)
print(compte.getBalance())