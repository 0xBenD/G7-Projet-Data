import pandas as pd

# Chargement des données
# Assurez-vous que le fichier CSV est dans le même dossier que votre script/notebook
# Pandas s'occupe de tout lire automatiquement
df = pd.read_csv('./data/Tetuan PC Courrier.csv')

# Aperçu des 5 premières lignes pour vérifier que les colonnes sont bien lues
print("--- Aperçu des données ---")
print(df.head()) # Remplacez 'display' par 'print' si vous n'utilisez pas Jupyter

# Informations générales (types de données, vérification des valeurs manquantes)
print("\n--- Informations sur le Dataset ---")
df.info()

# Statistiques descriptives (moyenne, écart-type, min, max, etc.)
# C'est ici que vous verrez l'écart-type dont vous parliez !
print("\n--- Statistiques descriptives ---")
print(df.describe())
