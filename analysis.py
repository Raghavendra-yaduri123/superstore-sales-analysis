# Superstore Sales Data Analysis (Portfolio-Ready)
# Author: You
# How to run:
#   pip install -r requirements.txt
#   python analysis.py
#
# This script loads the dataset, cleans data, performs analysis, saves figures,
# and prints key KPIs. Plots use matplotlib only (no seaborn).

import pandas as pd
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(__file__)
FIG_DIR = os.path.join(BASE_DIR, "figures")
os.makedirs(FIG_DIR, exist_ok=True)

# Load data
df = pd.read_csv(os.path.join(BASE_DIR, "superstore_sales.csv"))

# Basic cleaning
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')
df = df.dropna(subset=['Order Date', 'Ship Date', 'Sales', 'Profit'])

# KPIs
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
avg_discount = df['Discount'].mean()
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Average Discount: {avg_discount:.2%}")

# Monthly Sales Trend
monthly = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum().sort_index()
plt.figure(figsize=(10,5))
monthly.index = monthly.index.astype(str)
plt.plot(monthly.index, monthly.values, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "monthly_sales_trend.png"))
plt.close()

# Top 10 States by Sales
top_states = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
plt.bar(top_states.index, top_states.values)
plt.title("Top 10 States by Sales")
plt.xlabel("State")
plt.ylabel("Sales")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "top_states_sales.png"))
plt.close()

# Profit by Category & Region (as a matrix using pcolor to avoid seaborn)
pivot = df.pivot_table(values='Profit', index='Category', columns='Region', aggfunc='sum').fillna(0)
plt.figure(figsize=(8,5))
plt.pcolor(pivot.values)
plt.title("Profit by Category & Region")
plt.xlabel("Region")
plt.ylabel("Category")
plt.xticks(range(len(pivot.columns)), pivot.columns, rotation=0)
plt.yticks([i+0.5 for i in range(len(pivot.index))], pivot.index)
plt.colorbar(label='Profit')
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "profit_category_region_heatmap.png"))
plt.close()

# Segment-wise Sales Distribution (Pie Chart)
segment_sales = df.groupby('Segment')['Sales'].sum()
plt.figure(figsize=(6,6))
plt.pie(segment_sales.values, labels=segment_sales.index, autopct="%1.1f%%", startangle=90)
plt.title("Segment-wise Sales Distribution")
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "segment_sales_pie.png"))
plt.close()

print("Figures saved to ./figures")
