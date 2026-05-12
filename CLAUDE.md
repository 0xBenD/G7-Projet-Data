# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Academic data science project (ISEP 2025–2026, group of 3). Goal: perform PCA and Linear Regression on the Tetuan city power consumption dataset (Morocco, summer 2017). Output: a PDF presentation answering all [graded question] items in `project.md`.

## Dataset

`data/Tetuan PC Courrier.csv` — 7 columns:
- **DateTime**: timestamp (10-minute intervals, summer 2017)
- **Temperature** (°C), **Humidity** (%), **WindSpeed** (Km/h)
- **PCZone1**, **PCZone2**, **PCZone3** (KW) — power consumption of 3 distribution zones

PCA and regression use only: `Temperature`, `Humidity`, `WindSpeed`, `PCZone1`, `PCZone2`, `PCZone3` (no DateTime).

## Environment

```bash
# Activate venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt

# Launch notebook
jupyter notebook                # opens project.ipynb in browser
```

Key libraries: `pandas`, `numpy`, `scikit-learn`, `statsmodels`, `matplotlib`, `seaborn`, `scipy`.

## Architecture

All analysis lives in `project.ipynb`. The notebook follows four stages matching `project.md`:

1. **Descriptive statistics** (§2.2) — shape, missing values, `df.describe()`, boxplots, scatter plots
2. **PCA** (§2.3) — standardize with `StandardScaler` (units differ wildly), correlation matrix, `sklearn.decomposition.PCA`, scree plot, correlation circle (biplot)
3. **Simple linear regression** (§2.4.1) — target: `PCZone1`; identify most correlated predictor, fit with `statsmodels.OLS`, report β̂, 95% CI, t-test, R²
4. **Multiple linear regression / feature selection** (§2.4.2) — Best Subset Selection via `itertools.combinations`, compare models on adjusted R², fit final model, hypothesis tests on all coefficients, predict at T=26°C, H=65%, WS=4.2 Km/h, PCZone2=18840 KW, PCZone3=25700 KW

## Key constraints

- Standardize before PCA — PCZone values are in the tens of thousands vs single-digit WindSpeed
- Use `statsmodels.OLS` (not sklearn) for regression — it provides p-values, CIs, and full summary out of the box
- Numerical results: up to 3 significant digits
- Use `%matplotlib inline` at the top of the notebook so plots render inline
- `display()` for DataFrames in notebook cells, `print()` for plain text
