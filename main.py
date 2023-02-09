from datetime import date
from agences import Agence
from voitures import Voiture

# créer des objets voitures
voiture1 = Voiture("123abc", "Toyota", date(2021, 1, 1), 100000, 1500, "rouge", 140)
voiture2 = Voiture("456def", "BMW", date(2020, 12, 12), 80000, 2000, "noir", 150)
voiture3 = Voiture("789ghi", "Mercedes", date(2022, 11, 11), 50000, 1600, "blanc", 160)
voiture4 = Voiture("246ujk", "Audi", date(2022, 5, 5), 60000, 1700, "gris", 170)

# ajouter des voitures à une liste
liste_voitures = [voiture1, voiture2, voiture3, voiture4]

# créer une instance de la classe Agence
agence1 = Agence("Agence1", "adresse1", "telephone1", "email1", liste_voitures)

# creation d'une nouvelle voiture pour la recherche
nouvelle_voiture = Voiture("154ikj", "Audi", date(2021, 1, 1), 70000, 1500, "rouge", 140)

# Recherche de la voiture la plus similaire a la nouvelle voiture
agence1.afficher_voiture_similaire(nouvelle_voiture)