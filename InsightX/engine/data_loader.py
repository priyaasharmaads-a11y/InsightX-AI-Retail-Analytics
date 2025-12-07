import pandas as pd
import os

def load_data(file_path = "../data/sales.csv"):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    df = pd.read_csv(file_path)
    
    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    
    # Parse date column
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], dayfirst=True)

    
    return df

def basic_info(df):
    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": df.isnull().sum().to_dict(),
        "dtypes": df.dtypes.astype(str).to_dict()
    }

if __name__ == "__main__":
    df = load_data()
    print(df.head())
    print(basic_info(df))
