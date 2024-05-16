class Etudiant:
    def __init__(self,nom,note1,note2):
        self.nom=nom
        self.note1=note1
        self.note2=note2
    def calc_moy(self):
        self.moyenne=(self.note1+self.note2)/2
        return (self.note1+self.note2)/2
    def afficher(self):
        print(f"Nom: ",self.nom,"et","Moyenne: ",self.moyenne)
nom=input("Entrez le nom de l'etudiant: ")
note1=float(input("Entrez la note numero 1: "))
note2=float(input("Entrez la note numero 2: "))
etudiant=Etudiant(nom,note1,note2)
etudiant.calc_moy()
etudiant.afficher()