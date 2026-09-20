"""
extract_from_sql.py — pulls dbo.Routes into a pandas DataFrame.
Falls back to the raw CSV if SQL Server isn't reachable, so the
pipeline still runs end-to-end without a database.
"""
import pandas as pd
from config import get_engine, CSV_FALLBACK


def load_routes() -> pd.DataFrame:
    try:
        engine = get_engine()
        df = pd.read_sql("SELECT * FROM dbo.Routes", engine)
        print(f"Loaded {len(df):,} rows from SQL Server (dbo.Routes).")
    except Exception as e:
        print(f"[info] SQL Server not available ({e}); using CSV fallback.")
        df = pd.read_csv(CSV_FALLBACK)
        print(f"Loaded {len(df):,} rows from {CSV_FALLBACK}.")
    return df


if __name__ == "__main__":
    df = load_routes()
    print(df.head())
