import pandas as pd
import datetime
from sklearn.preprocessing import OneHotEncoder

# definir class transformation
class transformation:
    def __init__(self, dateCirculationTo = "age"):
        self.dateCirculationTo = dateCirculationTo
    
    def fit(self, df):
        df_ = df.copy()
        marquecouleur = pd.DataFrame()
        self.OHE = OneHotEncoder()
        self.OHE.fit(df_[['marque']])
        self.OHE1 = OneHotEncoder()
        self.OHE1.fit(df_[['couleur']])
        
    
    def transformer(self, df):
        df_transformer = df.copy()
        # suppression de colonne matricule
        df_transformer.drop(columns=['matricule'], axis=1, inplace=True)
        
        if self.dateCirculationTo == "age":
            # transformation de la colonne date_circulation en age
            df_transformer['date_ciruclation'] = pd.to_datetime(df_transformer['date_ciruclation'], format='%d/%m/%Y')
            df_transformer['age'] = datetime.datetime.now().year - df_transformer['date_ciruclation'].dt.year
        elif self.dateCirculationTo == "annee":
            # transformation de la colonne date_circulation en année
            df_transformer['date_ciruclation'] = pd.to_datetime(df_transformer['date_ciruclation'], format='%d/%m/%Y')
            df_transformer['annee'] = df_transformer['date_ciruclation'].dt.year
            
        # suppression de la colonne date_circulation
        df_transformer = df_transformer.drop(columns=['date_ciruclation'], axis=1)
        
        # transformation de la colonne marque en one hot encoding
        transformedMarque = self.OHE.transform(df_transformer[['marque']]).toarray()
        df_transformer["Marque_"+self.OHE.categories_[0]] = transformedMarque
        
        # transformation de la colonne couleur en one hot encoding
        transformedCouleur = self.OHE1.transform(df_transformer[['couleur']]).toarray()
        df_transformer["Couleur_"+self.OHE1.categories_[0]] = transformedCouleur
        
        # suppression de la colonne marque
        df_transformer.drop(columns=['marque'], axis=1, inplace=True)
        
        # suppression de la colonne couleur
        df_transformer.drop(columns=['couleur'], axis=1, inplace=True)
        
        return df_transformer
    
if __name__ == '__main__' :
    df = pd.read_csv("voitures.csv",sep=';')
    trans = transformation("annee")
    trans.fit(df)
    
    df_transformer = trans.transformer(df)
    print(df_transformer)