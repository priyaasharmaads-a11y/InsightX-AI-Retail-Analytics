import matplotlib.pyplot as plt
import pandas as pd

from .data_loader import load_data
from .analyze import calculate_kpis, calculate_monthly_trend



# Load data
df = load_data()

# Calculate analytics
kpis = calculate_kpis(df)
monthly_trend = calculate_monthly_trend(df)

# 1️⃣ Revenue by Gender
plt.figure()
gender = kpis["revenue_by_gender"]
plt.bar(gender.keys(), gender.values())
plt.title("Revenue by Gender")
plt.xlabel("Gender")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

# 2️⃣ Revenue by Category
plt.figure()
category = kpis["revenue_by_category"]
plt.bar(category.keys(), category.values())
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

# 3️⃣ Monthly Revenue Trend
plt.figure()
plt.plot(monthly_trend["month"], monthly_trend["monthly_revenue"], marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

