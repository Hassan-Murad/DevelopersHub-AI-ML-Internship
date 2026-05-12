# Task 1: Exploring and Visualizing the Iris Dataset

**Name:** Muhammad Hassan Murad  
**DHC ID:** DHC-2360  
**Internship:** DevelopersHub Corporation — AI/ML Engineering Internship

---

## Objective

Learn how to load, inspect, and visualize a dataset to understand data trends and distributions.

---

## Dataset

| Detail | Value |
|---|---|
| **Name** | Iris Dataset |
| **Source** | Loaded via `seaborn` (no download needed) |
| **Samples** | 150 (50 per species) |
| **Features** | sepal_length, sepal_width, petal_length, petal_width |
| **Target** | Species: Setosa, Versicolor, Virginica |
| **Missing Values** | None |

---

## What Was Done

- Loaded dataset using pandas + seaborn
- Printed shape, column names, `.head()`, `.info()`, `.describe()`
- Created 5 visualizations:
  - **Pairplot** — all feature combinations coloured by species
  - **Scatter plots** — petal and sepal dimensions by species
  - **Histograms** — value distributions per feature per species
  - **Box plots** — outlier detection per feature per species
  - **Violin plots** — distribution shape for petal features
  - **Correlation heatmap** — feature relationships

---

## Key Findings

- Petal length and petal width are the best features for separating species
- Setosa is clearly distinct; Versicolor and Virginica overlap more
- Petal length and width are highly correlated (r = 0.96)
- Dataset is perfectly balanced and clean — ideal for beginner ML

---

## Project Structure

```
Task1-Iris-Dataset-Exploration/
├── iris_exploration.ipynb   # Full Jupyter Notebook
└── README.md
```

---

## How to Run

```bash
pip install pandas numpy matplotlib seaborn
jupyter notebook iris_exploration.ipynb
```

---

## Skills Demonstrated

- ✅ Data loading and inspection using pandas
- ✅ Descriptive statistics and data exploration
- ✅ Basic plotting and visualization with seaborn and matplotlib
- ✅ Scatter plots, histograms, box plots, heatmaps
