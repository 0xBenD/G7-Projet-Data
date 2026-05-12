# Projet Data Science — ACP & Régression Linéaire

Projet académique ISEP 2025–2026 (groupe de 3).  
Analyse de la consommation électrique de la ville de Tétouan (Maroc, été 2017) via ACP et régression linéaire.

---

## Installation

```bash
# Cloner le dépôt
git clone <url-du-repo>
cd G7-Projet-Data

# Créer et activer l'environnement virtuel
python3 -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# Installer les dépendances
pip install -r requirements.txt
```

---

## Lancer l'analyse

```bash
python project.py
```

---

## Structure du projet

```
G7-Projet-Data/
├── data/
│   └── Tetuan PC Courrier.csv   # Dataset brut (52 417 observations)
├── project.py                   # Script principal d'analyse
├── project.md                   # Énoncé du projet (questions notées)
├── requirements.txt             # Dépendances Python
└── README.md
```

---

## Dataset

| Variable    | Description                        | Unité |
|-------------|-----------------------------------|-------|
| DateTime    | Horodatage (intervalles de 10 min) | —     |
| Temperature | Température                        | °C    |
| Humidity    | Humidité                           | %     |
| WindSpeed   | Vitesse du vent                    | Km/h  |
| PCZone1     | Consommation zone 1 (cible)        | KW    |
| PCZone2     | Consommation zone 2                | KW    |
| PCZone3     | Consommation zone 3                | KW    |

---

## Feuille de route

Le projet suit les 3 étapes de l'énoncé (`project.md`) :

### ✅ Étape 1 — Statistiques descriptives (`project.md` §2.2)
- [x] Chargement du dataset
- [x] Aperçu des données et types
- [x] Statistiques descriptives (moyenne, écart-type, min/max)
- [ ] Visualisations : boxplots, scatter plots
- [ ] Vérification et traitement des valeurs manquantes

### 🔲 Étape 2 — ACP (`project.md` §2.3)
- [ ] Calcul des variances → décision de standardisation
- [ ] Matrice de corrélation
- [ ] ACP avec `sklearn.decomposition.PCA` (variables : Temperature, Humidity, WindSpeed, PCZone1, PCZone2, PCZone3)
- [ ] Pourcentage de variance expliquée (PVE) + scree plot
- [ ] Cercle des corrélations (biplot)
- [ ] Interprétation des deux premières composantes principales

### 🔲 Étape 3 — Régression linéaire (`project.md` §2.4)
- [ ] Corrélations target/prédicteurs → choix du meilleur prédicteur simple
- [ ] Régression linéaire simple (PCZone1 ~ meilleur prédicteur)
  - Estimations β̂₀, β̂₁ et interprétation
  - Intervalle de confiance à 95% pour β₁
  - Test de Student (pente nulle)
  - R²
- [ ] Sélection de variables par *Best Subset Selection* (itertools.combinations, R² ajusté)
- [ ] Régression multiple avec le meilleur sous-ensemble
  - Interprétation des coefficients
  - Tests d'hypothèse sur chaque coefficient
  - Prédiction : T=26°C, H=65%, WS=4.2 Km/h, PCZone2=18840 KW, PCZone3=25700 KW

---

## Rendu

- **Format** : présentation PDF (10 min + 5 min questions)
- **Nom du fichier** : `Nom1_Nom2_Nom3.pdf`
- **Dépôt** : Moodle, **3 jours avant** la soutenance
- Une seule remise par groupe

---

## Références

- Salam, A., & El Hibaoui, A. (2018). *Power Consumption of Tetouan City*. UCI ML Repository.
- A. Salam and A. E. Hibaoui, IRSEC 2018, Rabat, Morocco.
