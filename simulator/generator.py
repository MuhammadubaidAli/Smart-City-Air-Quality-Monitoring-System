# generator.py

"""
Reading Generator Module

Generates realistic IoT sensor readings.

Features:
- Base values by zone
- ±15% random noise
- Time-based pollution adjustment
- 15% anomaly spike
- AQI calculation
- Severity calculation
"""

import random
from datetime import datetime

from sensor_config import BASE_VALUES, SENSORS
from aqi import calculate_aqi, get_severity


# ==========================================================
# RANDOM NOISE
# ==========================================================

def apply_noise(value, percentage=15):
    """
    Apply ±15% random noise.
    """

    factor = random.uniform(
        1 - percentage / 100,
        1 + percentage / 100
    )

    return value * factor


# ==========================================================
# TIME EFFECT
# ==========================================================

def apply_time_effect(pm25, pm10):
    """
    Apply time-based pollution changes.
    """

    hour = datetime.now().hour

    # Morning Rush
    if 7 <= hour <= 9:
        pm25 *= 1.25
        pm10 *= 1.20

    # Afternoon
    elif 13 <= hour <= 15:
        pm25 *= 1.10
        pm10 *= 1.08

    # Evening Rush
    elif 17 <= hour <= 19:
        pm25 *= 1.30
        pm10 *= 1.25

    # Night
    elif 0 <= hour <= 5:
        pm25 *= 0.80
        pm10 *= 0.80

    return pm25, pm10


# ==========================================================
# ANOMALY SPIKE
# ==========================================================

def apply_anomaly(pm25):
    """
    15% chance of pollution spike.
    """

    if random.random() < 0.15:
        pm25 *= random.uniform(2.5, 4.0)

    return pm25


# ==========================================================
# WEATHER GENERATORS
# ==========================================================

def generate_humidity():

    return round(random.uniform(30, 80), 2)


def generate_wind_speed():

    return round(random.uniform(2, 15), 2)


# ==========================================================
# MAIN READING GENERATOR
# ==========================================================

def generate_reading(sensor):
    """
    Generate one sensor reading.
    """

    zone = sensor["zone_type"]

    base = BASE_VALUES[zone]

    # Base values from ranges
    pm25 = random.uniform(*base["pm25"])

    # PM10 generated relative to PM2.5
    pm10 = pm25 * random.uniform(1.6, 2.2)

    co2_ppm = random.uniform(*base["co2_ppm"])

    temperature = random.uniform(*base["temperature"])

    # Random noise
    pm25 = apply_noise(pm25)
    pm10 = apply_noise(pm10)
    co2_ppm = apply_noise(co2_ppm)

    # Time Effect
    pm25, pm10 = apply_time_effect(pm25, pm10)

    # Anomaly
    pm25 = apply_anomaly(pm25)

    # Weather
    humidity = generate_humidity()
    wind_speed = generate_wind_speed()

    # AQI
    aqi = calculate_aqi(pm25)

    # Severity
    severity = get_severity(aqi)

    # Timestamp
    recorded_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Final Reading
    reading = {

        "sensor_id": sensor["sensor_id"],
        "city": sensor["city"],
        "zone_type": zone,

        "pm25": round(pm25, 2),
        "pm10": round(pm10, 2),
        "co2_ppm": round(co2_ppm, 2),

        "temperature": round(temperature, 2),
        "humidity": humidity,
        "wind_speed": wind_speed,

        "aqi": aqi,
        "severity": severity,

        "recorded_at": recorded_at

    }

    return reading


# ==========================================================
# TESTING
# ==========================================================

if __name__ == "__main__":

    print("=" * 80)
    print("SMART CITY AQI SENSOR SIMULATOR")
    print("=" * 80)

    for sensor in SENSORS:

        reading = generate_reading(sensor)

        print("\n" + "-" * 80)

        for key, value in reading.items():

            print(f"{key:<18}: {value}")