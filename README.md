# 🌍 Smart City Air Quality Monitoring System

A complete end-to-end Data Engineering project that simulates IoT air quality sensors, integrates real-world air quality data from the OpenAQ API, stores and processes data in Snowflake, and visualizes insights through an interactive Power BI dashboard.

---

## 📖 Project Overview

Air pollution is one of the biggest challenges faced by modern smart cities. This project demonstrates how air quality data can be collected, processed, analyzed, and visualized using a modern data engineering pipeline.

The project combines simulated IoT sensor data with OpenAQ API data to create a centralized air quality monitoring solution.

---

## 🚀 Features

- IoT Air Quality Sensor Simulator
- Random Air Quality Data Generation
- AQI Calculation
- Air Quality Severity Classification
- OpenAQ API Integration
- ETL Pipeline (Extract, Transform, Load)
- Snowflake Data Warehouse
- SQL Data Processing
- Power BI Interactive Dashboard
- Clean Data Architecture

---

# 🏗 Project Architecture

```
                OpenAQ API
                     │
                     ▼
              Extract Module
                     │
                     ▼
             Transform Module
                     │
                     ▼
               Load to Snowflake
                     │
                     ▼
        RAW → CLEAN → ANALYTICS
                     │
                     ▼
            Power BI Dashboard
```

---

# 📂 Project Structure

```
Smart-City-Air-Quality-Monitoring-System/
│
├── config/
│   ├── .env
│   └── .env.example
│
├── simulator/
│   ├── sensor_config.py
│   ├── generator.py
│   ├── csv_writer.py
│   ├── snowflake_loader.py
│   └── main.py
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── etl_pipeline.py
│
├── sql/
│   ├── 01_database_setup.sql
│   ├── 02_create_gold_table.sql
│   ├── 03_load_gold_data.sql
│   └── 04_gold_analysis.sql
│
├── powerbi/
│   └── Smart_City_AQI_Dashboard.pbix
│
├── screenshots/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🛠 Technologies Used

- Python
- Snowflake
- SQL
- Power BI
- OpenAQ API
- Pandas
- Requests
- Python Dotenv
- Git
- GitHub

---

# 📊 Database Architecture

The project uses a three-layer Snowflake architecture.

## RAW Layer

Stores raw data collected from:

- IoT Simulator
- OpenAQ API

Tables

- RAW.IOT_READINGS
- RAW.OPENAQ_RAW

---

## CLEAN Layer

Contains cleaned and standardized air quality data.

Table

- CLEAN.AQI_CLEAN

---

## ANALYTICS Layer

Contains aggregated city-level reports for dashboards.

Table

- ANALYTICS.CITY_DAILY

---

# ⚙ ETL Workflow

## Extract

Fetch air quality data from the OpenAQ API.

## Transform

Convert raw JSON into a structured dataset.

- Clean data
- Standardize fields
- Prepare records

## Load

Insert transformed data into Snowflake.

---

# 🌫 IoT Simulator Workflow

The simulator generates synthetic air quality data every few seconds.

Generated fields include:

- Sensor ID
- City
- Zone Type
- PM2.5
- PM10
- CO₂
- Temperature
- Humidity
- Wind Speed
- AQI
- Severity
- Timestamp

---

# 📈 Power BI Dashboard

The dashboard provides interactive visualizations including:

- Average AQI
- Highest AQI
- Lowest AQI
- Total Readings
- Total Cities
- Average AQI by City
- AQI Severity Distribution
- Average PM2.5 by City
- Average CO₂ by City

---

# ▶️ How to Run the Project

## 1 Clone Repository

```bash
git clone https://github.com/MuhammadubaidAli/Smart-City-Air-Quality-Monitoring-System.git
```

---

## 2 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3 Create Environment File

Create

```
config/.env
```

using

```
config/.env.example
```

---

## 4 Configure

Add your

- OpenAQ API Key
- Snowflake Credentials

inside `.env`.

---

## 5 Run IoT Simulator

```bash
cd simulator
python main.py
```

---

## 6 Run ETL Pipeline

```bash
cd etl
python etl_pipeline.py
```

---

## 7 Execute SQL Scripts

Run the SQL files inside Snowflake in the following order:

1. 01_database_setup.sql

2. 02_create_gold_table.sql

3. 03_load_gold_data.sql

4. 04_gold_analysis.sql

---

## 8 Open Power BI Dashboard

Open

```
Smart_City_AQI_Dashboard.pbix
```

Refresh the data and explore the dashboard.

---

# 📸 Screenshots



# 🔮 Future Improvements

- Live Streaming Data
- Apache Kafka Integration
- Apache Airflow Scheduling
- Docker Deployment
- Azure Cloud Deployment
- Real-time Dashboard Refresh
- Machine Learning AQI Prediction
- Weather Data Integration

---

# 👨‍💻 Author

**Muhammad Ubaid Ali**
Aspiring Data Engineer | Data Science

GitHub:
https://github.com/MuhammadubaidAli

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
