# Task 2: Predict Future Stock Prices (Short-Term)

**Name:** Muhammad Hassan Murad
**DHC ID:** DHC-2360
**Internship:** DevelopersHub Corporation — AI/ML Engineering Internship

---

## Task Objective

Use historical stock market data to predict the **next day's closing price** using machine learning regression models.

---

## Dataset

| Detail | Value |
|---|---|
| **Source** | Yahoo Finance via `yfinance` Python library |
| **Stock** | Apple Inc. (AAPL) |
| **Period** | 2 years of daily OHLCV data |
| **Rows** | ~500 trading days |

---

## Models Applied

| Model | Notes |
|---|---|
| **Linear Regression** | Baseline — fast and interpretable |
| **Random Forest Regressor** | Ensemble — captures non-linear patterns |

---

## Feature Engineering

| Feature | Description |
|---|---|
| `Price_Range` | High − Low (intraday volatility) |
| `Open_Close_Gap` | Open − Previous Close (gap signal) |
| `MA_5`, `MA_10` | 5 and 10-day moving averages |
| `Vol_MA_5` | 5-day average volume |
| `Lag_1`, `Lag_2`, `Lag_3` | Previous 1/2/3 days' closing prices |
| `Pct_Change` | Day-over-day % change |

---

## Key Results

- Random Forest outperforms Linear Regression on all metrics
- `Lag_1` (yesterday's close) is the most important single feature
- Moving averages contribute significant predictive signal
- Chronological 80/20 split used — no shuffling (correct for time series)

---

## Project Structure

```
Task2-Stock-Price-Prediction/
├── stock_prediction.ipynb   # Full Jupyter Notebook
└── README.md
```

---

## How to Run

```bash
pip install yfinance pandas numpy scikit-learn matplotlib seaborn
jupyter notebook stock_prediction.ipynb
```

---

## Skills Demonstrated

- ✅ Time series data handling (no-shuffle split)
- ✅ Regression modeling (Linear Regression + Random Forest)
- ✅ Data fetching via API (yfinance)
- ✅ Feature engineering from OHLCV data
- ✅ Model evaluation: MAE, RMSE, R², MAPE
- ✅ Visualizing predictions vs actual prices
