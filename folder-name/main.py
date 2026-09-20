"""
main.py — runs the full Egypt Aviation Network pipeline end to end:
extract -> clean -> analyze -> charts.

Open the `python/` folder in Visual Studio Code, select/create a venv,
`pip install -r requirements.txt`, then run or debug this file (F5).

Usage:
    python main.py
"""
from extract_from_sql import load_routes
from clean_data import clean
from analyze import print_insights, save_charts


def run():
    print("=== Egypt Aviation Network Pipeline ===")
    df = load_routes()
    df = clean(df)
    print_insights(df)
    save_charts(df)
    print("\nPipeline complete.")


if __name__ == "__main__":
    run()
