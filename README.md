# Projet Data Science — ACP & Régression Linéaire

Projet académique ISEP 2025–2026 (groupe de 3).  
Analyse de la consommation électrique de la ville de Tétouan (Maroc, été 2017) via ACP et régression linéaire.

---

## Installation

Commence par cloner le dépôt :

```bash
git clone <url-du-repo>
cd G7-Projet-Data
```

Ensuite, choisis **une** des deux méthodes ci-dessous selon ce que tu as installé.

---

### Option A — `venv` (Python standard)

```bash
# Créer et activer l'environnement virtuel
python3 -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# Installer les dépendances
pip install -r requirements.txt
```

Pour désactiver l'environnement quand tu as fini :
```bash
deactivate
```

---

### Option B — `conda` (Anaconda / Miniconda)

Si tu as installé [Anaconda](https://www.anaconda.com/) ou [Miniconda](https://docs.conda.io/en/latest/miniconda.html), utilise conda à la place.

```bash
# Créer un environnement dédié au projet
conda create -n g7-data python=3.13

# Activer l'environnement
conda activate g7-data

# Installer les dépendances
pip install -r requirements.txt
```

> **Pourquoi `pip` et pas `conda install` ?** Certaines librairies du `requirements.txt` sont plus à jour sur PyPI que sur les dépôts conda. `pip` dans un environnement conda fonctionne très bien.

Pour désactiver l'environnement quand tu as fini :
```bash
conda deactivate
```

**Avantage de conda** : Jupyter Notebook est souvent déjà inclus avec Anaconda — pas besoin de l'installer séparément. Lance directement :
```bash
jupyter notebook
```

---

## Lancer l'analyse

Le projet utilise un **Jupyter Notebook** (`project.ipynb`). Deux façons de l'ouvrir :

### Option A — Terminal (navigateur)

```bash
jupyter notebook
```

Une page s'ouvre dans ton navigateur. Clique sur `project.ipynb` pour l'ouvrir.

### Option B — VS Code (recommandé si tu l'as déjà)

Ouvre directement le fichier `project.ipynb` dans VS Code. Pas besoin de commande.

---

## Jupyter Notebook — Guide pour débutants

### C'est quoi un Jupyter Notebook ?

Un Jupyter Notebook (`.ipynb`) est un document interactif qui mélange du **code Python**, des **résultats** (tableaux, graphiques) et du **texte explicatif**, tout dans la même page.  
C'est l'outil standard en data science : tu exécutes le code bloc par bloc, tu vois le résultat immédiatement en dessous, et tu peux modifier et relancer sans tout réexécuter.

### Pourquoi Jupyter plutôt qu'un script Python classique ?

| | Script `.py` | Jupyter Notebook `.ipynb` |
|---|---|---|
| Exécution | Tout d'un coup | Bloc par bloc |
| Résultats | Terminal texte | Affiché directement sous le code |
| Graphiques | Fenêtre séparée | Intégrés dans la page |
| Exploration | Peu pratique | Idéal |
| Débogage | Tout relancer | Relancer seulement le bloc bugué |
| Présentation | — | Peut servir de brouillon de rapport |

En résumé : pour un projet d'analyse de données comme le nôtre, le notebook est bien supérieur. Tu peux tester une idée, voir le résultat, corriger, sans jamais perdre le fil.

---

### Utiliser Jupyter en terminal

```bash
# 1. Activer l'environnement virtuel (si pas déjà fait)
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# 2. Lancer Jupyter
jupyter notebook
```

Une page s'ouvre dans ton navigateur sur `http://localhost:8888`.  
Clique sur `project.ipynb` pour l'ouvrir.

**Raccourcis essentiels dans le notebook :**

| Action | Raccourci |
|---|---|
| Exécuter le bloc actuel | `Shift + Entrée` |
| Exécuter sans passer au suivant | `Ctrl + Entrée` |
| Nouveau bloc en dessous | `B` (en mode commande) |
| Supprimer un bloc | `DD` (deux fois D, en mode commande) |
| Passer en mode commande | `Échap` |
| Passer en mode édition | `Entrée` |

---

### Utiliser Jupyter dans VS Code

VS Code supporte nativement les fichiers `.ipynb` sans avoir à lancer de commande.

**Étapes :**

1. Installer l'extension **Python** dans VS Code (si pas déjà là)  
   → Chercher "Python" dans l'onglet Extensions (`Ctrl+Shift+X`)

2. Ouvrir ou créer un fichier `.ipynb` dans VS Code

3. En haut à droite, cliquer sur **"Select Kernel"** → choisir l'interpréteur Python de ton `venv`  
   (il doit apparaître comme `Python 3.x.x ('venv')`)

4. Chaque bloc de code a un bouton ▶ sur la gauche pour l'exécuter

> **Astuce VS Code** : tu peux aussi convertir un `.py` en notebook via `Ctrl+Shift+P` → "Jupyter: Export Current Python File as Jupyter Notebook".

---

### `display` vs `print` — quelle différence ?

C'est une des premières confusions qu'on rencontre en passant de Python à Jupyter.

**`print()`** — fonctionne partout (script `.py` et notebook)
```python
print(df.head())
```
Affiche le résultat en texte brut, comme dans un terminal. Pas très lisible pour les tableaux.

**`display()`** — spécifique à Jupyter
```python
display(df.head())
```
Affiche un tableau HTML bien formaté, avec les colonnes alignées, les types colorés, etc. Bien plus lisible.

**La règle simple :**
- Dans un notebook `.ipynb` → utilise `display()` pour les DataFrames et tableaux, `print()` pour les messages texte simples
- Dans un script `.py` → utilise uniquement `print()` (`display` n'existe pas par défaut)
- Si tu mets un DataFrame **tout seul sur la dernière ligne d'un bloc**, Jupyter l'affiche automatiquement avec `display` sans que tu aies à l'appeler

```python
# Ces trois blocs donnent le même résultat dans Jupyter :
df.head()           # dernière ligne du bloc = affichage auto
display(df.head())  # explicite
print(df.head())    # version texte brut (moins joli)
```

---

### Autres différences à connaître entre script et notebook

**Les variables persistent entre les blocs**  
Si tu définis `df` dans le bloc 1, il est disponible dans le bloc 5. Attention : si tu réexécutes les blocs dans le désordre, tu peux avoir des comportements inattendus. En cas de doute → **Kernel → Restart & Run All** pour tout réexécuter proprement depuis le début.

**Les graphiques s'affichent dans la page**  
Avec `matplotlib`, ajoute cette ligne au début de ton notebook :
```python
%matplotlib inline
```
Sans ça, les graphiques peuvent s'ouvrir dans une fenêtre séparée ou ne pas s'afficher du tout.

**Les lignes magiques `%`**  
Jupyter supporte des commandes spéciales qui commencent par `%` :
```python
%matplotlib inline   # graphiques dans la page
%timeit mon_code()   # mesure le temps d'exécution
%who                 # liste les variables définies
```
Ces commandes ne fonctionnent **pas** dans un script `.py` classique.

**L'ordre d'exécution compte**  
Dans un script `.py`, le code s'exécute toujours de haut en bas. Dans un notebook, tu peux exécuter les blocs dans n'importe quel ordre — ce qui est puissant mais peut créer des bugs difficiles à trouver si on ne fait pas attention.

---

## Structure du projet

```
G7-Projet-Data/
├── data/
│   └── Tetuan PC Courrier.csv   # Dataset brut
├── project.ipynb                # Notebook principal (tout le code ici)
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
- [ ] Sélection de variables par *Best Subset Selection* (`itertools.combinations`, R² ajusté)
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
