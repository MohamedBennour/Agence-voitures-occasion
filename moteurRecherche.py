from transformations import Transformation
import pandas as pd


def voitureToDF(voiture):
    df = pd.DataFrame(columns=['matricule', 'marque', 'date_ciruclation', 'kilometrage', 'cylindre', 'couleur', 'vitesse'])
    df.loc[0] = [voiture.matricule, voiture.marque, voiture.date_circulation, voiture.kilometrage, voiture.cylindre, voiture.couleur, voiture.vitesse]
    t = Transformation("annee")
    t.fit(df)
    df = t.transformer(df)
    return df

def liste_voituresToDF(voitures):
    df = pd.DataFrame(columns=['matricule', 'marque', 'date_ciruclation', 'kilometrage', 'cylindre', 'couleur', 'vitesse'])
    for i in range(len(voitures)):
        df.loc[i] = [voitures[i].matricule, voitures[i].marque, voitures[i].date_circulation, voitures[i].kilometrage, voitures[i].cylindre, voitures[i].couleur, voitures[i].vitesse]
    t = Transformation("annee")
    t.fit(df)
    df = t.transformer(df)
    return df




