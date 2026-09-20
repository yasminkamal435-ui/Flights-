# Power BI Setup Guide — Egypt Aviation Network

## 1. Connect to the data source
Open Power BI Desktop → **Get Data** → **SQL Server database**.
Server: `localhost` (or your machine name, see `connection.txt`).
Database: `EgyptAviationDB`. Select `dbo.Routes` → Transform Data.

No SQL Server available? Get Data → Text/CSV → select `data/egypt_routes.csv` directly.

## 2. Clean the data in Power Query
- Keep `Origin_IATA` / `Destination_IATA` at exactly 3 characters
- Remove exact duplicate (Airline_Name, Origin_IATA, Destination_IATA) rows
- Replace blank `Equipment` with "Unknown"

## 3. DAX measures
```
Total Routes = COUNTROWS(Routes)
Airlines Operating = DISTINCTCOUNT(Routes[Airline_Name])
Countries Connected =
DISTINCTCOUNT(
    UNION(
        SELECTCOLUMNS(Routes, "C", Routes[Origin_Country]),
        SELECTCOLUMNS(Routes, "C", Routes[Destination_Country])
    )
)
Cities Connected =
DISTINCTCOUNT(
    UNION(
        SELECTCOLUMNS(Routes, "City", Routes[Origin_City]),
        SELECTCOLUMNS(Routes, "City", Routes[Destination_City])
    )
)
Domestic Egypt Routes =
CALCULATE(COUNTROWS(Routes), Routes[Origin_Country]="Egypt", Routes[Destination_Country]="Egypt")

/* If dbo.Routes_Extra is populated with real scheduling/price data: */
Avg Weekly Frequency = AVERAGE(Routes_Extra[Weekly_Frequency])
Avg Ticket Price = AVERAGE(Routes_Extra[Avg_Ticket_Price])
```

## 4. Apply the theme
**View** → **Themes** → Browse for themes... → select `Black_Gray_PowerBI_Theme.json`.

## 5. Build the visuals
Match the layout in `dashboard_preview/Egypt_Aviation_Network_Dashboard.html`:
- KPI cards: Total Routes, Airlines Operating, Countries Connected, Cities Connected, Domestic Egypt Routes
- Bar chart: Routes by Egyptian Airport (CAI, HRG, HBE, SSH, LXR, HMB, RMF, ATZ, ASW, ABS)
- Horizontal bar: Top 10 Airlines by Route Count
- Horizontal bar: Top 12 Countries Connected
- Pie chart with data labels: Top Cities Connected
- Table: full route list (Airline, Origin, Destination, Direction, Equipment), filterable by Egyptian airport slicer

## 6. Refresh
Any time new rows are added to SQL Server, click **Refresh** in Power BI — no manual re-import needed.
