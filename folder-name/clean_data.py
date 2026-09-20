"""
clean_data.py — validation & cleaning rules for the real Egypt routes dataset.
"""
import pandas as pd

EGYPT_AIRPORTS = {"CAI", "HRG", "HBE", "SSH", "LXR", "HMB", "RMF", "ATZ", "ASW", "ABS"}


def clean(df: pd.DataFrame) -> pd.DataFrame:
    before = len(df)

    # Every row must actually touch a known Egyptian airport
    df = df[df["Egypt_Airport"].isin(EGYPT_AIRPORTS)]

    # IATA codes must be exactly 3 letters
    df = df[df["Origin_IATA"].str.len() == 3]
    df = df[df["Destination_IATA"].str.len() == 3]

    # Drop exact duplicate routes (same airline + same city pair)
    df = df.drop_duplicates(subset=["Airline_Name", "Origin_IATA", "Destination_IATA"])

    # Fill missing equipment codes
    df["Equipment"] = df["Equipment"].fillna("Unknown")

    after = len(df)
    print(f"Cleaned: {before:,} -> {after:,} rows ({before - after} removed).")
    return df.reset_index(drop=True)


if __name__ == "__main__":
    from extract_from_sql import load_routes
    df = clean(load_routes())
    print(df.describe(include="all").T.head(10))
