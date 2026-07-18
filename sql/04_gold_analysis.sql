USE DATABASE SMART_CITY_AQI;

-- Total Records
SELECT COUNT(*) AS total_records
FROM CLEAN.AQI_CLEAN;

-- Average AQI by City
SELECT
    city,
    ROUND(AVG(aqi), 2) AS average_aqi
FROM CLEAN.AQI_CLEAN
GROUP BY city
ORDER BY average_aqi DESC;

-- Top 10 Highest AQI
SELECT *
FROM CLEAN.AQI_CLEAN
ORDER BY aqi DESC
LIMIT 10;

-- Top 10 Lowest AQI
SELECT *
FROM CLEAN.AQI_CLEAN
ORDER BY aqi ASC
LIMIT 10;

-- Severity Distribution
SELECT
    severity,
    COUNT(*) AS total
FROM CLEAN.AQI_CLEAN
GROUP BY severity
ORDER BY total DESC;

-- Average PM2.5 by City
SELECT
    city,
    ROUND(AVG(pm25), 2) AS avg_pm25
FROM CLEAN.AQI_CLEAN
GROUP BY city
ORDER BY avg_pm25 DESC;

-- Average CO2 by City
SELECT
    city,
    ROUND(AVG(co2_ppm), 2) AS avg_co2
FROM CLEAN.AQI_CLEAN
GROUP BY city
ORDER BY avg_co2 DESC;

-- Analytics Table
SELECT *
FROM ANALYTICS.CITY_DAILY
ORDER BY avg_aqi DESC;

-- Top 5 Cities by AQI
SELECT
    city,
    ROUND(AVG(aqi), 2) AS avg_aqi
FROM CLEAN.AQI_CLEAN
GROUP BY city
ORDER BY avg_aqi DESC
LIMIT 5;