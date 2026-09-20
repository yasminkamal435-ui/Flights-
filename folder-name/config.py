"""
config.py — reads connection.txt (written by sql/setup_all.ps1)
so the rest of the pipeline never hard-codes a server name.

Open this whole `python/` folder in Visual Studio Code to work on the
pipeline — it's a normal VS Code Python project (create a venv, install
requirements.txt, and run main.py or debug it with F5).
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONN_FILE = os.path.join(ROOT, "connection.txt")
CSV_FALLBACK = os.path.join(ROOT, "data", "egypt_routes.csv")


def get_connection_string() -> str:
    """Read the SQL Server connection string written during setup."""
    if os.path.exists(CONN_FILE):
        with open(CONN_FILE, encoding="utf-8") as f:
            return f.read().strip()
    raise FileNotFoundError(
        "connection.txt not found. Run sql/setup_all.ps1 first, "
        "or just use extract_from_sql.py, which falls back to "
        f"{CSV_FALLBACK} automatically."
    )


def get_engine():
    """Return a SQLAlchemy engine for EgyptAviationDB."""
    import sqlalchemy as sa
    conn_str = get_connection_string()
    odbc = f"mssql+pyodbc:///?odbc_connect={conn_str}&driver=ODBC+Driver+17+for+SQL+Server"
    return sa.create_engine(odbc)


CHARTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "charts")
os.makedirs(CHARTS_DIR, exist_ok=True)
