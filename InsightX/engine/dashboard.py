import streamlit as st
import pandas as pd
import plotly.express as px
from qa_engine import answer_question
from report_generator import generate_pdf_report
import os


from data_loader import load_data
from analyze import calculate_kpis, calculate_monthly_trend

# -----------------------
# Load Data
# -----------------------
df = load_data()

st.set_page_config(page_title="InsightX Retail Dashboard", layout="wide")

# -----------------------
# Sidebar Filters
# -----------------------
st.sidebar.header("Filters")

gender_filter = st.sidebar.multiselect(
    "Select Gender",
    options=df["gender"].unique(),
    default=df["gender"].unique()
)

category_filter = st.sidebar.multiselect(
    "Select Category",
    options=df["product_category"].unique(),
    default=df["product_category"].unique()
)

filtered_df = df[
    (df["gender"].isin(gender_filter)) &
    (df["product_category"].isin(category_filter))
]

# -----------------------
# KPI Cards
# -----------------------
kpis = calculate_kpis(filtered_df)

st.title("🛍️ Retail Sales Dashboard — InsightX")

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"₹ {kpis['total_revenue']:,}")
col2.metric("Orders", kpis["total_transactions"])
col3.metric("Avg Order Value", f"₹ {kpis['average_order_value']:.2f}")

st.markdown("---")

# ---------------------------------
# A) TOP 5 PRODUCTS (CATEGORY-WISE)
# ---------------------------------

st.subheader("🏆 Top 5 Product Categories by Revenue")

top5_rev = (
    filtered_df.groupby("product_category")["total_amount"]
    .sum()
    .reset_index()
    .sort_values("total_amount", ascending=False)
    .head(5)
)

fig_top5_rev = px.bar(
    top5_rev,
    x="product_category",
    y="total_amount",
    title="Top 5 Categories by Revenue",
    labels={"product_category": "Category", "total_amount": "Revenue"},
    color="total_amount",
)
st.plotly_chart(fig_top5_rev, use_container_width=True)


st.subheader("📦 Top 5 Categories by Quantity Sold")

top5_qty = (
    filtered_df.groupby("product_category")["quantity"]
    .sum()
    .reset_index()
    .sort_values("quantity", ascending=False)
    .head(5)
)

fig_top5_qty = px.bar(
    top5_qty,
    x="product_category",
    y="quantity",
    title="Top 5 Categories by Quantity Sold",
    labels={"product_category": "Category", "quantity": "Units Sold"},
    color="quantity",
)
st.plotly_chart(fig_top5_qty, use_container_width=True)

st.markdown("---")

# ---------------------------------
# B) AUTO-GENERATED TEXT INSIGHTS
# ---------------------------------

st.subheader("💡 Automatically Generated Insights")

insights = []

# Best performing category
best_cat = top5_rev.iloc[0]
insights.append(
    f"• **{best_cat['product_category']}** is the highest revenue generator with **₹ {best_cat['total_amount']:,}**."
)

# Gender comparison
rev_gender = kpis["revenue_by_gender"]
if len(rev_gender) == 2:
    g1, g2 = list(rev_gender.items())
    diff = abs(g1[1] - g2[1])
    leader = g1[0] if g1[1] > g2[1] else g2[0]
    insights.append(
        f"• **{leader} customers** contribute more revenue by **₹ {diff:,}**."
    )

# Best month
monthly = calculate_monthly_trend(filtered_df)
best_month = monthly.sort_values("monthly_revenue", ascending=False).iloc[0]
insights.append(
    f"• **{best_month['month']}** recorded the highest monthly revenue of **₹ {best_month['monthly_revenue']:,}**."
)

# Slowest month
worst_month = monthly.sort_values("monthly_revenue").iloc[0]
insights.append(
    f"• **{worst_month['month']}** had the lowest monthly revenue (**₹ {worst_month['monthly_revenue']:,}**)."
)

# Display insights
for point in insights:
    st.write(point)
    # PDF report download
pdf_bytes = generate_pdf_report(kpis, insights)

st.download_button(
    label="📄 Download PDF Insight Report",
    data=pdf_bytes,
    file_name="insightx_report.pdf",
    mime="application/pdf",
)


st.markdown("---")

# ---------------------------------
# C) DOWNLOAD BUTTONS
# ---------------------------------

st.subheader("⬇️ Download Data")

colA, colB = st.columns(2)

# 1. Download filtered data CSV
colA.download_button(
    label="Download Filtered Dataset as CSV",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_sales_data.csv",
    mime="text/csv",
)

# 2. Download KPI summary
kpi_df = pd.DataFrame({
    "Metric": ["Total Revenue", "Orders", "Avg Order Value"],
    "Value": [
        kpis["total_revenue"],
        kpis["total_transactions"],
        kpis["average_order_value"]
    ]
})

colB.download_button(
    label="Download KPIs as CSV",
    data=kpi_df.to_csv(index=False),
    file_name="kpis.csv",
    mime="text/csv",
)

st.markdown("---")
st.caption("Built with ❤️ using Python, Streamlit & InsightX Engine")
st.markdown("---")
st.subheader("🤖 Ask Questions About Your Data")

user_question = st.text_input("Type your question in plain English:")

if st.button("Ask"):
    monthly = calculate_monthly_trend(filtered_df)
    response = answer_question(user_question, filtered_df, kpis, monthly)
    st.success(response)
