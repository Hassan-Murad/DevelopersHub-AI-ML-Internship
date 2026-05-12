# Task 3: Heart Disease Prediction

**Name:** Muhammad Hassan Murad
**DHC ID:** DHC-2360
**Internship:** DevelopersHub Corporation — AI/ML Engineering Internship

---

## Task Objective

Build a binary classification model to predict whether a patient is at risk of **heart disease** based on clinical health data.

---

## Dataset

| Detail | Value |
|---|---|
| **Source** | Heart Disease UCI Dataset (Cleveland) — UCI ML Repository |
| **Patients** | 303 |
| **Features** | 13 clinical attributes |
| **Target** | 0 = No disease, 1 = Heart disease present |
| **Missing Values** | 6 rows in `ca` and `thal` — imputed with median |

### Feature Summary

| Feature | Description |
|---|---|
| `age` | Age in years |
| `sex` | 1 = male, 0 = female |
| `cp` | Chest pain type (0–3) |
| `trestbps` | Resting blood pressure (mmHg) |
| `chol` | Serum cholesterol (mg/dl) |
| `fbs` | Fasting blood sugar > 120 mg/dl |
| `restecg` | Resting ECG results |
| `thalach` | Maximum heart rate achieved |
| `exang` | Exercise-induced angina |
| `oldpeak` | ST depression by exercise |
| `slope` | Slope of peak exercise ST segment |
| `ca` | Number of major vessels (fluoroscopy) |
| `thal` | Thalassemia type |

---

## Models Applied

| Model | Notes |
|---|---|
| **Logistic Regression** | Baseline — interpretable, great for binary classification |
| **Decision Tree** | Visual, rule-based — max_depth=4 to prevent overfitting |

---

## Key Results

- Both models achieve **>80% accuracy** on the test set
- `cp`, `thalach`, `exang`, and `oldpeak` are the strongest predictors
- Logistic Regression produces stronger ROC-AUC
- Recall for Disease class is prioritised — missing a true case is more dangerous

---

## Visualizations Produced

- Target class distribution (bar + pie)
- Feature distributions by target class
- Categorical feature disease rates
- Correlation heatmap
- Box plots with outlier detection
- Confusion matrices (both models)
- ROC curves with AUC scores
- Feature importance (both models)
- Decision tree diagram

---

## Project Structure

```
Task3-Heart-Disease-Prediction/
├── heart_disease_prediction.ipynb   # Full Jupyter Notebook
└── README.md
```

---

## How to Run

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
jupyter notebook heart_disease_prediction.ipynb
```

No manual dataset download needed — loads directly from UCI ML Repository.

---

## Skills Demonstrated

- ✅ Binary classification (Logistic Regression + Decision Tree)
- ✅ Medical data understanding and interpretation
- ✅ EDA with clinical context
- ✅ Model evaluation: accuracy, ROC-AUC, confusion matrix, classification report
- ✅ Feature importance analysis
- ✅ Stratified train/test split and 5-fold cross-validation
- ✅ Missing value handling (median imputation)
