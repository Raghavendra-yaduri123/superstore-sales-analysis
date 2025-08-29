# Superstore Sales Data Analysis

A ready-to-upload, portfolio-quality **Data Analysis + Visualization** project.

## 🚀 What’s inside
- `superstore_sales.csv` — synthetic but realistic retail dataset
- `Superstore_Sales_Analysis.ipynb` — Jupyter notebook (EDA + charts)
- `analysis.py` — runnable Python script that generates and saves plots
- `figures/` — output charts saved as PNG
- `requirements.txt` — minimal dependencies

## 📦 Quick Start
```bash
# 1) Create & activate a virtual environment (optional)
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

# 2) Install deps
pip install -r requirements.txt

# 3) Run the analysis script
python analysis.py

# Or open the notebook
jupyter notebook Superstore_Sales_Analysis.ipynb
```

## 📈 Visuals Included
- Monthly Sales Trend (line)
- Top 10 States by Sales (bar)
- Profit by Category & Region (heatmap)
- Segment-wise Sales Distribution (pie)

## 🧹 Data Cleaning
- Parse dates for `Order Date` and `Ship Date`
- Drop invalid/missing rows for core metrics
- Aggregate by month, state, category, region, and segment

## 📝 Notes
- Dataset is synthetic (no real PII), safe for public portfolio.
- All plots use **matplotlib** only.
