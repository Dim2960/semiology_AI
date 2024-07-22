# Manipulation des données
import pandas as pd
import numpy as np
import joblib



# Charger le modèle depuis le fichier
loaded_model = joblib.load('random_forest_model.pkl')

# Utiliser le modèle chargé pour faire des prédictions
predictions = loaded_model.predict(X_test)