/* =========================================================
   Egypt Aviation Network — Database Setup
   Real data: 573 real airline routes touching 10 Egyptian
   airports, from OpenFlights (routes.dat / airports.dat /
   airlines.dat), an openly published real aviation dataset.
   ========================================================= */

IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = N'EgyptAviationDB')
BEGIN
    CREATE DATABASE EgyptAviationDB;
END
GO

USE EgyptAviationDB;
GO

IF OBJECT_ID('dbo.Routes', 'U') IS NOT NULL
    DROP TABLE dbo.Routes;
GO

CREATE TABLE dbo.Routes (
    Route_ID            INT IDENTITY(1,1) PRIMARY KEY,
    Airline_Name         VARCHAR(100) NOT NULL,
    Origin_IATA           CHAR(3) NOT NULL,
    Origin_City            VARCHAR(80),
    Origin_Country          VARCHAR(80),
    Destination_IATA          CHAR(3) NOT NULL,
    Destination_City            VARCHAR(80),
    Destination_Country          VARCHAR(80),
    Direction                     VARCHAR(12) NOT NULL,  -- Departure / Arrival, relative to Egypt
    Egypt_Airport                  CHAR(3) NOT NULL,       -- which Egyptian airport this route touches
    Equipment                       VARCHAR(20)
);
GO

/* Optional: ready to receive real scheduling/pricing data if you connect
   this project to a live carrier feed or GDS export later */
IF OBJECT_ID('dbo.Routes_Extra', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.Routes_Extra (
        Route_ID       INT PRIMARY KEY,
        Weekly_Frequency INT NULL,
        Avg_Ticket_Price DECIMAL(10,2) NULL,
        Seasonal        VARCHAR(20) NULL
    );
END
GO

/* ---- Bulk import (adjust path to your local copy of the CSV) ----
BULK INSERT dbo.Routes
FROM 'C:\Egypt_Aviation_Network_Project\data\egypt_routes.csv'
WITH (
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);
*/

PRINT 'EgyptAviationDB and dbo.Routes created successfully.';
