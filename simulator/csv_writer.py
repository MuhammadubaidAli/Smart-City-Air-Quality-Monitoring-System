# csv_writer.py

import csv
import os


FILE_NAME = "iot_readings.csv"


def save_to_csv(reading):
    """
    Save one sensor reading to the CSV file.

    Args:
        reading (dict): Sensor reading dictionary.
    """

    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(file, fieldnames=reading.keys())

        if not file_exists:
            writer.writeheader()

        writer.writerow(reading)