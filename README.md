# 🛍️ InsightX — AI-Powered Retail Analytics Dashboard

InsightX is a complete **interactive retail analytics dashboard** built using **Python, Streamlit, Plotly**, and a custom **AI-style Q&A engine**.  
It allows users to explore sales data, generate insights, ask questions in plain English, and download reports.

This project demonstrates end-to-end skills in:
- Data analysis
- Dashboard development
- Business insight generation
- AI-style natural language querying

---

## 🚀 Features

### ✅ Interactive Dashboard
- Dynamic filters for **Gender** and **Product Category**
- KPI Cards:
  - Total Revenue  
  - Total Orders  
  - Average Order Value  
- Visualizations:
  - Revenue by Gender (Bar Chart)
  - Revenue by Category (Bar Chart)
  - Monthly Revenue Trend (Line Chart)

---

### ✅ Top 5 Insights
- Top 5 product categories by **Revenue**
- Top 5 product categories by **Quantity Sold**

---

### ✅ AI-Style Q&A System
Users can ask questions like:
- *What is the best category?*
- *Which month had the highest revenue?*
- *Compare male and female revenue*
- *How many total orders are there?*

The system answers instantly using rule-based NLP logic.

---

### ✅ Automatic Business Insights
The dashboard automatically generates text-based insights such as:
- Best-performing category
- Best and worst revenue months
- Gender-wise revenue comparison

---

### ✅ PDF Report Generator
Users can download a clean business-style **PDF report** that includes:
- KPI summary
- Key business insights

---

### ✅ CSV Download Options
Users can download:
- Filtered dataset
- KPI summary

---

## 🧠 Tech Stack

| Layer | Tools |
|--------|--------|
| Dashboard | Streamlit |
| Charts | Plotly |
| Data Processing | Python, Pandas |
| Reporting | FPDF |
| AI Logic | Rule-based NLP |

---

## 📁 Project Structure

InsightX/
├── data/ # Sample dataset (CSV)
├── engine/ # Core analytics & dashboard engine
├── outputs/ # Generated files (PDF, CSV)
├── requirements.txt
└── README.md

---

## ▶️ How to Run the Project Locally

### 1️⃣ Install dependencies
pip install -r requirements.txt

### 2️⃣ Run the dashboard
cd InsightX/engine
streamlit run dashboard.py

The app will open in your browser at:http://localhost:8501/

---

## 📸 Screenshots
(Add screenshots of your dashboard here)
![alt text](<Screenshot 2025-12-07 212941.png>)
![alt text](<Screenshot 2025-12-07 213000.png>) ![alt text](<Screenshot 2025-12-07 213013.png>) ![alt text](<Screenshot 2025-12-07 213025.png>) ![alt text](<Screenshot 2025-12-07 213036.png>)

---

## 🎯 Project Highlights
- Real-world retail analytics use case
- End-to-end data pipeline
- AI-powered Q&A without machine learning
- Business-ready reporting and exports
- Resume and portfolio ready

---

## ❤️ Built With Passion for Data & Analytics

