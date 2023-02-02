# definir class aggence
class Agence:
    def __init__(self, nom="", adresse="", telephone="", email="", liste_voitures=[]):
        self.nom = nom
        self.adresse = adresse
        self.telephone = telephone
        self.email = email
        self.liste_voitures = liste_voitures

        
    def afficher_agence(self):
        print("Nom: ", self.nom)
        print("Adresse: ", self.adresse)
        print("Telephone: ", self.telephone)
        print("Email: ", self.email)
        print("Liste des voitures: ")
        for voiture in self.liste_voitures:
            voiture.afficher_voiture()
        
    def supp_voiture(self, voiture):
        self.liste_voitures.remove(voiture)
    
    def rechercher_voiture(self, matricule):
        for voiture in self.liste_voitures:
            if voiture.matricule == matricule:
                return voiture
        return None
    
    def trier_selon_dateCirculation(self):
        self.liste_voitures.sort(key=lambda voiture: voiture.date_circulation)
    
    def get_voiture_plusRecente(self):
        print("Voiture la plus recente: ")
        return self.liste_voitures[-1]
    
    def get_voiture_plusAncienne(self):
        print("Voiture la plus ancienne: ")
        return self.liste_voitures[0]
        
    def ajouter_voiture(self, voiture):
        self.liste_voitures.append(voiture)
        
    
        
        
        
    