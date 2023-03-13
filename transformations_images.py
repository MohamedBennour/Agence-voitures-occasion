import cv2
import numpy as np
from imutils import paths
from sklearn.base import BaseEstimator, TransformerMixin
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array

class TransformationImageVoiture(BaseEstimator, TransformerMixin):
    
    def __init__(self, color_mode='grayscale', target_size=(224, 224)):
        self.color_mode = color_mode
        self.target_size = target_size
        
    def fit(self, X, y=None):
        # On ne calcule pas de modèle de transformation, cette méthode ne fait rien
        return self
    
    def transform(self, X, y=None):
        # On transforme chaque image en un vecteur
        data = []
        for imagePath in X:
            image = load_img(imagePath, color_mode=self.color_mode, target_size=self.target_size)
            vector = img_to_array(image)
            vector = vector.reshape(1, -1)
            data.append(vector)
        
        # On retourne une matrice dont les lignes sont les vecteurs des images obtenus
        return np.concatenate(data, axis=0)

if __name__ == '__main__' :
    PATH = "C:\\Users\\Bennour\\Desktop\\Python_data_science\\voitures_images"
    imagePaths = list(paths.list_images(PATH))

    # Créer une instance de la classe de transformation
    transformation = TransformationImageVoiture()

    # Transformer les images de l'agence en vecteurs
    data = transformation.transform(imagePaths)

    # Transformer l'image target en vecteur
    target_image_path = "C:\\Users\\Bennour\\Desktop\\Python_data_science\\target.jpeg"
    target_vector = transformation.transform([target_image_path])

    print("Data shape:", data.shape)
    print("Target vector shape:", target_vector.shape)
