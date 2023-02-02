from datetime import date

# definir class voiture
class Voiture:
    def __init__(self, matricule="", marque="", date_circulation=date.today(), kilometrage=0, cylindre=0, couleur="", vitesse=0):
        self.matricule = matricule
        self.marque = marque
        self.date_circulation = date_circulation
        self.kilometrage = kilometrage
        self.cylindre = cylindre
        self.couleur = couleur
        self.vitesse = vitesse
        
    def saisi_voiture(self):
        self.matricule = input("Matricule: ")
        self.marque = input("Marque: ")
        self.date_circulation = input("Date de circulation: ")
        self.date_circulation = self.date_circulation.split("/")
        self.date_circulation = date(int(self.date_circulation[2]), int(self.date_circulation[1]), int(self.date_circulation[0]))
        self.kilometrage = int(input("Kilometrage: "))
        self.cylindre = int(input("Cylindre: "))
        self.couleur = input("Couleur: ")
        self.vitesse = int(input("Vitesse: "))
    

    def afficher_voiture(self):
        print("\n*** Voiture ***\n")
        print(f"Matricule: %s \nMarque: %s \nDate de circulation: %s \nKilometrage: %s \nCylindre: %s \nCouleur: %s \nVitesse: %s" % (self.matricule, self.marque, self.date_circulation, self.kilometrage, self.cylindre, self.couleur, self.vitesse))
