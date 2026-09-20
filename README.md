# Egypt Aviation Network Project

An end-to-end aviation data pipeline and interactive business intelligence dashboard analyzing flight route connections, airline operations, and network density across Egyptian airports.

---

##  Project Overview

The **Egypt Aviation Network Project** processes and visualizes real-world flight route datasets across major Egyptian airports. The system unifies raw aviation data into a structured pipeline using **SQL Server**, **Python**, and dynamic web dashboards (**HTML/CSS/JS** & **Power BI**), allowing aviation analysts and decision-makers to explore network connectivity, carrier dominance, and route distributions.

---

## Dashboard Preview & Features

The project includes an interactive dashboard with the following features:

* **Executive Network Overview:** High-level KPIs showing total active routes, operating airlines, connected countries, and destination cities.
* **Airport Selection & Filtering:** Interactive slice-and-dice functionality across major Egyptian airports (Cairo, Hurghada, Alexandria, Sharm El Sheikh, Luxor, Sohag, Marsa Alam, Assiut).
* **Carrier Dominance Analysis:** Visual breakdown of top airlines by route volume per airport.
* **Geographic Connectivity:** Top connected countries and destination city distribution charts.
* **Interactive Routes Explorer:** Searchable and filterable route matrix providing detailed route direction, origin/destination codes, operating airline, and aircraft type.

---

##  System Architecture & Data Pipeline

The project follows a clean 3-tier data engineering architecture:

1. **Database Layer (SQL Server):**
   * Stores structured relational route and airport datasets.
   * Managed via automated T-SQL deployment scripts (`setup_egypt_routes_database.sql`).

2. **Data Pipeline Layer (Python ETL):**
   * **Extraction:** Connects to SQL database to extract raw records (`extract_from_sql.py`).
   * **Transformation:** Cleans missing values, normalizes airport IATA codes, and validates route directions (`clean_data.py`).
   * **Analytics Engine:** Generates network density stats and airline market share metrics (`analyze.py`).

3. **Visualization & Reporting Layer:**
   * **Web-Based Dashboard:** Interactive HTML preview dashboard (`Egypt_Aviation_Network_Dashboard.html`).
   * **Power BI Integration:** Custom dark-theme analytics report (`Black_Gray_PowerBI_Theme.json`).

---

##  Repository Structure

```text
Egypt_Aviation_Network_Project/
│
├── sql/
│   ├── setup_egypt_routes_database.sql   # SQL database creation and table schemas
│   └── setup_all.ps1                     # PowerShell automation script for SQL setup
│
├── python/
│   ├── main.py                           # Main execution entry point for the ETL pipeline
│   ├── extract_from_sql.py               # SQL database connection and extraction module
│   ├── clean_data.py                     # Data cleaning, wrangling, and missing-value handling
│   ├── analyze.py                        # Statistical calculations and route metrics engine
│   ├── config.py                         # Environment configurations and DB connection strings
│   └── requirements.txt                  # Python dependency list
│
├── data/
│   └── egypt_routes.csv                  # Processed route dataset
│
├── powerbi/
│   ├── Black_Gray_PowerBI_Theme.json     # Custom executive Power BI theme file
│   └── PowerBI_Setup_Guide.md            # Step-by-step setup guide for Power BI
│
└── dashboard_preview/
    └── Egypt_Aviation_Network_Dashboard.html  # Interactive HTML web dashboard
