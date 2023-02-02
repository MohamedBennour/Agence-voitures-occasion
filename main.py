from voitures import Voiture
from agence import Agence
from datetime import date


v1 = Voiture("145", "BMW", date(2019, 1, 1), 1000, 2000, "bleu", 200)
#v1.saisi_voiture()

#v1.afficher_voiture()

v2 = Voiture("123456", "Toyota", date(2019, 1, 1), 1000, 2000, "Rouge", 200)

ag1 = Agence("Agence 1", "Adresse 1", "12345678")
ag1.ajouter_voiture(v1)
ag1.ajouter_voiture(v2)

ag1.afficher_agence()



