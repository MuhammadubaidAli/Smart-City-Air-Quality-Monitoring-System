# main.py

"""
Smart City AQI Simulator

Main Program

Workflow:
1. Generate sensor readings
2. Save readings to CSV
3. Insert readings into Snowflake
4. Repeat every 10 seconds
"""

import time

from sensor_config import SENSORS
from generator import generate_reading
from csv_writer import save_to_csv
from snowflake_loader import load_to_snowflake


# ==========================================================
# MAIN LOOP
# ==========================================================

def main():

    print("=" * 80)
    print("SMART CITY AQI SIMULATOR STARTED")
    print("=" * 80)

    while True:

        for sensor in SENSORS:

            try:

                # Generate Reading
                reading = generate_reading(sensor)

                # Save to CSV
                save_to_csv(reading)

                # Insert into Snowflake
                load_to_snowflake(reading)

                # Console Output
                print(
                    f"[✓] {reading['sensor_id']} | "
                    f"{reading['city']} | "
                    f"AQI: {reading['aqi']} | "
                    f"{reading['severity']}"
                )

            except Exception as error:

                print(f"[ERROR] {sensor['sensor_id']} -> {error}")

        print("-" * 80)
        print("Waiting 10 seconds for next cycle...\n")

        time.sleep(10)


# ==========================================================
# PROGRAM ENTRY POINT
# ==========================================================

if __name__ == "__main__":
    main()
