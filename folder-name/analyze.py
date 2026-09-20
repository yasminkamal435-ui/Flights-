"""
analyze.py — KPIs, insights, and charts for the Egypt Aviation Network project.
Saves PNG charts to python/charts/ and prints a summary to the console.
"""
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from config import CHARTS_DIR
import os


def compute_kpis(df: pd.DataFrame) -> dict:
    other_country = df.apply(
        lambda r: r["Destination_Country"] if r["Direction"] == "Departure" else r["Origin_Country"], axis=1
    )
    other_city = df.apply(
        lambda r: r["Destination_City"] if r["Direction"] == "Departure" else r["Origin_City"], axis=1
    )
    domestic = ((df["Origin_Country"] == "Egypt") & (df["Destination_Country"] == "Egypt")).sum()
    return {
        "total_routes": len(df),
        "airlines_operating": df["Airline_Name"].nunique(),
        "countries_connected": other_country.nunique(),
        "cities_connected": other_city.nunique(),
        "egyptian_airports_served": df["Egypt_Airport"].nunique(),
        "domestic_routes": int(domestic),
    }


def routes_by_airport(df: pd.DataFrame) -> pd.Series:
    return df["Egypt_Airport"].value_counts()


def top_airlines(df: pd.DataFrame, n=10) -> pd.Series:
    return df["Airline_Name"].value_counts().head(n)


def top_countries(df: pd.DataFrame, n=12) -> pd.Series:
    other_country = df.apply(
        lambda r: r["Destination_Country"] if r["Direction"] == "Departure" else r["Origin_Country"], axis=1
    )
    return other_country.value_counts().head(n)


def save_charts(df: pd.DataFrame):
    routes_by_airport(df).plot(kind="bar", color="#222222", figsize=(7, 4), title="Routes by Egyptian Airport")
    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS_DIR, "routes_by_airport.png"))
    plt.close()

    top_airlines(df).plot(kind="barh", color="#555555", figsize=(7, 4), title="Top 10 Airlines")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS_DIR, "top_airlines.png"))
    plt.close()

    top_countries(df).plot(kind="barh", color="#222222", figsize=(7, 5), title="Top 12 Countries Connected")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS_DIR, "top_countries.png"))
    plt.close()

    print(f"Charts saved to {CHARTS_DIR}")


def print_insights(df: pd.DataFrame):
    kpis = compute_kpis(df)
    print("\n=== KPIs ===")
    for k, v in kpis.items():
        print(f"{k}: {v:,}")

    print("\n=== Routes by Egyptian airport ===")
    print(routes_by_airport(df).to_string())

    print("\n=== Top 10 airlines ===")
    print(top_airlines(df).to_string())

    top = routes_by_airport(df).idxmax()
    print(f"\nInsight: {top} is Egypt's most internationally connected airport "
          f"in this dataset, with {routes_by_airport(df).max()} real routes.")


if __name__ == "__main__":
    from extract_from_sql import load_routes
    from clean_data import clean

    df = clean(load_routes())
    print_insights(df)
    save_charts(df)
