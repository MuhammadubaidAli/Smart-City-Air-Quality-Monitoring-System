USE DATABASE SMART_CITY_AQI;

-- ==========================================================
-- LOAD DATA INTO CLEAN LAYER
-- ==========================================================

INSERT INTO CLEAN.AQI_CLEAN
(
    source,
    city,
    sensor_id,
    pm25,
    pm10,
    co2_ppm,
    aqi,
    severity,
    latitude,
    longitude,
    recorded_at
)

SELECT
    'Simulator',
    city,
    sensor_id,
    pm25,
    pm10,
    co2_ppm,
    aqi,
    severity,
    NULL,
    NULL,
    recorded_at

FROM RAW.IOT_READINGS;


-- ==========================================================
-- LOAD DATA INTO ANALYTICS LAYER
-- ==========================================================

INSERT INTO ANALYTICS.CITY_DAILY
(
    city,
    report_date,
    avg_aqi,
    max_aqi,
    min_aqi,
    avg_pm25,
    avg_co2,
    dominant_risk,
    reading_count
)

SELECT
    city,
    CURRENT_DATE(),
    ROUND(AVG(aqi), 2),
    MAX(aqi),
    MIN(aqi),
    ROUND(AVG(pm25), 2),
    ROUND(AVG(co2_ppm), 2),
    MODE(severity),
    COUNT(*)

FROM CLEAN.AQI_CLEAN

GROUP BY city;