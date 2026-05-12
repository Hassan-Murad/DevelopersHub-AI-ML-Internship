# Task 6: House Price Prediction

**Name:** Muhammad Hassan Murad  
**DHC ID:** DHC-2360  
**Internship:** DevelopersHub Corporation — AI/ML Engineering Internship

---

## Objective

Predict house prices using property features such as size, bedrooms, location, and income level.

---

## Dataset

| Detail | Value |
|---|---|
| **Name** | California Housing Dataset |
| **Source** | Loaded via `scikit-learn` (no download needed) |
| **Samples** | 20,640 census blocks |
| **Features** | 8 original + 3 engineered = 11 total |
| **Target** | Median house value (in $100,000s) |

---

## Models Applied

| Model | Notes |
|---|---|
| **Linear Regression** | Baseline — fast, interpretable |
| **Gradient Boosting Regressor** | 300 estimators, captures non-linear patterns |

---

## Feature Engineering

| Feature | Description |
|---|---|
| `RoomsPerPerson` | AveRooms / AveOccup — space per occupant |
| `BedroomRatio` | AveBedrms / AveRooms — bedroom proportion |
| `PopDensity` | Population / AveOccup — household density |

---

## Key Results

- **Gradient Boosting significantly outperforms Linear Regression**
- `MedInc` (median income) is the #1 predictor of house price
- Location (Latitude/Longitude) is a strong signal — coastal areas command higher prices
- Engineered features improve model performance beyond raw inputs

---

## Visualizations Produced

- House price distribution (histogram + log-transformed)
- Feature vs price scatter plots with trend lines
- Geographic price map (California heatmap)
- Correlation heatmap
- Actual vs predicted scatter plots (both models)
- Residual analysis
- Feature importance chart (Gradient Boosting)
- Metrics comparison bar chart

---

## Project Structure

```
Task6-House-Price-Prediction/
├── house_price_prediction.ipynb   # Full Jupyter Notebook
└── README.md
```

---

## How to Run

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
jupyter notebook house_price_prediction.ipynb
```

No dataset download needed — loads directly from scikit-learn.

---

## Skills Demonstrated

- ✅ Regression modeling (Linear Regression + Gradient Boosting)
- ✅ Feature engineering from raw property data
- ✅ Outlier detection and treatment
- ✅ Model evaluation: MAE, RMSE, R²
- ✅ Geographic data visualization
- ✅ Actual vs predicted price comparison plots
- ✅ Feature importance analysis
