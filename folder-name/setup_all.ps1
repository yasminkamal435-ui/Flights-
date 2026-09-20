<#
  Egypt Aviation Network — one-command setup
  1) Finds a local SQL Server instance
  2) Creates EgyptAviationDB + dbo.Routes
  3) Imports data/egypt_routes.csv (573 real routes)
  4) Writes connection.txt for Python & Power BI to read
#>

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$csvPath = Join-Path $root "data\egypt_routes.csv"
$sqlPath = Join-Path $PSScriptRoot "setup_egypt_routes_database.sql"

Write-Host "== Egypt Aviation Network setup ==" -ForegroundColor Cyan

# 1) Detect a local SQL Server instance
$instances = @(".\SQLEXPRESS", "localhost", "(localdb)\MSSQLLocalDB")
$server = $null
foreach ($inst in $instances) {
    try {
        sqlcmd -S $inst -Q "SELECT 1" -b | Out-Null
        $server = $inst
        Write-Host "Found SQL Server instance: $server" -ForegroundColor Green
        break
    } catch { continue }
}
if (-not $server) {
    Write-Error "No local SQL Server instance found. Install SQL Server Express or LocalDB first."
    exit 1
}

# 2) Create database + table
Write-Host "Creating database and table..." -ForegroundColor Cyan
sqlcmd -S $server -i $sqlPath -b

# 3) Import CSV with bcp
Write-Host "Importing egypt_routes.csv (573 real routes)..." -ForegroundColor Cyan
bcp dbo.Routes in $csvPath -S $server -d EgyptAviationDB -c -t "," -r "0x0a" -F 2 -T

# 4) Write connection.txt for Python / Power BI
$connText = "Server=$server;Database=EgyptAviationDB;Trusted_Connection=True;"
Set-Content -Path (Join-Path $root "connection.txt") -Value $connText
Write-Host "connection.txt written -> $connText" -ForegroundColor Green

Write-Host "Done. Open Power BI Desktop -> Get Data -> SQL Server -> $server / EgyptAviationDB" -ForegroundColor Yellow
