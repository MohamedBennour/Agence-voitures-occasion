import numpy as np
from voitures import Voiture

# definir class aggence
class Agence:
    def __init__(self, nom="", adresse="", telephone="", email="", liste_voitures=[]):
        self.nom = nom
        self.adresse = adresse
        self.telephone = telephone
        self.email = email
        self.liste_voitures = liste_voitures

    # fonction affiche agence      
    def afficher_agence(self):
        print("Nom: ", self.nom)
        print("Adresse: ", self.adresse)
        print("Telephone: ", self.telephone)
        print("Email: ", self.email)
        print("Liste des voitures: ")
        for voiture in self.liste_voitures:
            voiture.afficher_voiture()
    
    # fonction supprimer voiture    
    def supp_voiture(self, voiture):
        self.liste_voitures.remove(voiture)
    
    # fonction rechercher voiture
    def rechercher_voiture(self, matricule):
        for voiture in self.liste_voitures:
            if voiture.matricule == matricule:
                return voiture
        return None
    
    # fonction trier voiture selon date de circulation
    def trier_selon_dateCirculation(self):
        self.liste_voitures.sort(key=lambda voiture: voiture.date_circulation)
    
    # fonction retourner voiture la plus recente
    def get_voiture_plusRecente(self):
        print("Voiture la plus recente: ")
        return self.liste_voitures[-1]
    
    # fonction retourner voiture la plus ancienne
    def get_voiture_plusAncienne(self):
        print("Voiture la plus ancienne: ")
        return self.liste_voitures[0]
     
    # fonction ajouter voiture   
    def ajouter_voiture(self, voiture):
        self.liste_voitures.append(voiture)
    
    # fonnction transformer liste de voiture en matrice    
    def liste_voituresToMatrix(self):
        normalised_list = []
        for v in self.liste_voitures:
            normalised_list.append(Voiture.normaliser_voiture(v))
        return np.array(normalised_list)

    # fonction calculer distance entre une nouvelle voiture et les voitures de l'agence
    def calcule_distance(self, vecteur_normaliser, matrice_normaliser):
        distances = []
        for ligne in matrice_normaliser:
            distance = np.sqrt(sum((vecteur_normaliser - ligne)**2))
            distances.append(distance)
        return distances
    
    # fonction trier distance
    def trier_distance(self, distances):
        distances_triees = sorted(distances)
        return distances_triees
    
    # fonction afficher voiture similaire
    def afficher_voiture_similaire(self, nouvelle_voiture):
        nouvelle_voiture_normalisee = Voiture.normaliser_voiture(nouvelle_voiture)
        distance = self.calcule_distance(nouvelle_voiture_normalisee, self.liste_voituresToMatrix())
        distances_triees = self.trier_distance(distance)
        index = distance.index(distances_triees[0])
        print("\nLa voiture la plus similaire est : ")
        print(self.liste_voitures[index].afficher_voiture())
        

        
        