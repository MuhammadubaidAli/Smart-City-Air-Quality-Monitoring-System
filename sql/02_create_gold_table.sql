USE DATABASE SMART_CITY_AQI;
USE SCHEMA CLEAN;

CREATE OR REPLACE TABLE AQI_CLEAN
(
    clean_id NUMBER AUTOINCREAMENT PRIMARY KEY,

    source VARCHAR(20),

    city VARCHAR(100),

    sensor_id VARCHAR(30),

    pm25 FLOAT,

    pm10 FLOAT,

    co2_ppm FLOAT,

    aqi_value FLOAT,

    aqi_category VARCHAR(40),

    health_risk VARCHAR(20),

    latitude FLOAT,

    longitude FLOAT,

    recorded_at TIMESTAMP_NTZ,

    processed_At TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
);

USE SCHEMA ANALYTICS;

CREATE OR REPLACE TABLE CITY_DAILY
(
    daily_id NUMBER AUTOINCREAMENT PRIMARY KEY,

    city VARCHAR(100),

    report_date DATE,

    avg_aqi FLOAT,

    max_aqi FLOAT,

    min_aqi FLOAT,

    avg_pm25 FLOAT,

    avg_co2 FLOAT,

    dominant_risk VARCHAR(20),

    readign_count NUMBER,

    created_at TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
);