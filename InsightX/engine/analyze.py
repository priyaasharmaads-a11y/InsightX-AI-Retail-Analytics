import pandas as pd

def calculate_kpis(df):
    """
    Returns a dictionary of basic KPIs:
      - total_revenue
      - total_transactions
      - average_order_value
      - revenue_by_gender (dict)
      - revenue_by_category (dict)
    """
    kpis = {}
    kpis["total_revenue"] = int(df["total_amount"].sum())
    kpis["total_transactions"] = int(df.shape[0])
    kpis["average_order_value"] = float(df["total_amount"].mean())

    kpis["revenue_by_gender"] = (
        df.groupby("gender")["total_amount"].sum().to_dict()
    )

    kpis["revenue_by_category"] = (
        df.groupby("product_category")["total_amount"].sum().to_dict()
    )

    return kpis


def calculate_monthly_trend(df):
    """
    Returns a dataframe with columns: month (YYYY-MM) and monthly_revenue
    This is the function name expected by viz.py
    """
    # Ensure date column is datetime
    if not pd.api.types.is_datetime64_any_dtype(df["date"]):
        df["date"] = pd.to_datetime(df["date"], dayfirst=True)

    df_copy = df.copy()
    df_copy["month"] = df_copy["date"].dt.to_period("M")
    trend = (
        df_copy.groupby("month")["total_amount"]
        .sum()
        .reset_index()
        .rename(columns={"total_amount": "monthly_revenue"})
    )
    trend["month"] = trend["month"].astype(str)
    return trend


# Backwards-compatible alias (in case some code used old name)
monthly_sales_trend = calculate_monthly_trend


if __name__ == "__main__":
    # Quick smoke test when running analyze.py directly
    from .data_loader import load_data  # relative import works when run as package
    df = load_data("data/sales.csv")
    print("KPIs:\n", calculate_kpis(df))
    print("\nMonthly Trend:\n", calculate_monthly_trend(df))

