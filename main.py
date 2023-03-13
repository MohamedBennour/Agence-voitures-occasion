from datetime import date
from agences import Agence
from voitures import Voiture
from transformations import Transformation
import pandas as pd
import moteurRecherche as mr

df = pd.read_csv("voitures.csv",sep=';')
liste_voitures = df.copy()
trans = Transformation("annee")
trans.fit(liste_voitures)
df_transforme = trans.transformer(liste_voitures)

#print(df_transforme)


# créer des objets voitures
voiture1 = Voiture("123abc", "Toyota", "12/12/2020", 100000, 1500, "rouge", 140)

voiture2 = Voiture("456def", "BMW", "01/02/2023", 80000, 2000, "noir", 150)
voiture3 = Voiture("789ghi", "Mercedes", "03/02/2022", 50000, 1600, "blanc", 160)
voiture4 = Voiture("246ujk", "Audi", "20/05/2021", 60000, 1700, "gris", 170)

df = mr.PCA_voitures([voiture1, voiture2, voiture3, voiture4])
print(df)


"""""

# ajouter des voitures à une liste
#liste_voitures = [voiture1, voiture2, voiture3, voiture4]

# créer une instance de la classe Agence
agence1 = Agence("Agence1", "adresse1", "telephone1", "email1", liste_voitures)

# creation d'une nouvelle voiture pour la recherche
nouvelle_voiture = Voiture("154ikj", "Audi", date(2021, 1, 1), 70000, 1500, "rouge", 140)

# Recherche de la voiture la plus similaire a la nouvelle voiture
#agence1.afficher_voiture_similaire(nouvelle_voiture)
"""