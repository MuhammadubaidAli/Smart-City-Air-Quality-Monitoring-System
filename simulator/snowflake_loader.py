# snowflake_loader.py

import os
import snowflake.connector
from dotenv import load_dotenv

load_dotenv("../config/.env")


def load_to_snowflake(reading):
    """Load one sensor reading into Snowflake."""

    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
    )

    cursor = conn.cursor()

    insert_query = """
    INSERT INTO IOT_READINGS (
        sensor_id,
        city,
        zone_type,
        pm25,
        pm10,
        co2_ppm,
        temperature,
        humidity,
        wind_speed,
        aqi,
        severity,
        recorded_at
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(
        insert_query,
        (
            reading["sensor_id"],
            reading["city"],
            reading["zone_type"],
            reading["pm25"],
            reading["pm10"],
            reading["co2_ppm"],
            reading["temperature"],
            reading["humidity"],
            reading["wind_speed"],
            reading["aqi"],
            reading["severity"],
            reading["recorded_at"],
        ),
    )

    conn.commit()

    cursor.close()
    conn.close()