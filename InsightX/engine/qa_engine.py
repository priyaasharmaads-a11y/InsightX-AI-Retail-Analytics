import pandas as pd

def answer_question(question, df, kpis, monthly_trend):
    q = question.lower()

    if "best category" in q or "top category" in q:
        top_cat = max(kpis["revenue_by_category"], key=kpis["revenue_by_category"].get)
        value = kpis["revenue_by_category"][top_cat]
        return f"The best performing category is {top_cat} with revenue ₹ {value:,}."

    elif "worst category" in q:
        worst_cat = min(kpis["revenue_by_category"], key=kpis["revenue_by_category"].get)
        value = kpis["revenue_by_category"][worst_cat]
        return f"The worst performing category is {worst_cat} with revenue ₹ {value:,}."

    elif "male" in q and "female" in q:
        male_rev = kpis["revenue_by_gender"].get("Male", 0)
        female_rev = kpis["revenue_by_gender"].get("Female", 0)
        return f"Male Revenue: ₹ {male_rev:,} | Female Revenue: ₹ {female_rev:,}"

    elif "best month" in q or "highest month" in q:
        best = monthly_trend.sort_values("monthly_revenue", ascending=False).iloc[0]
        return f"The best month was {best['month']} with revenue ₹ {best['monthly_revenue']:,}."

    elif "worst month" in q:
        worst = monthly_trend.sort_values("monthly_revenue").iloc[0]
        return f"The worst month was {worst['month']} with revenue ₹ {worst['monthly_revenue']:,}."

    elif "total revenue" in q:
        return f"Total Revenue is ₹ {kpis['total_revenue']:,}."

    elif "average order" in q:
        return f"Average Order Value is ₹ {kpis['average_order_value']:.2f}."

    elif "orders" in q:
        return f"Total number of orders is {kpis['total_transactions']}."

    else:
        return "Sorry, I couldn't understand the question. Try asking about revenue, category, gender, or month."
