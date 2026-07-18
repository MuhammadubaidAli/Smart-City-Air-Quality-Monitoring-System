# etl_pipeline.py

"""
ETL Pipeline

Workflow:
1. Extract data from OpenAQ API
2. Transform raw JSON into clean records
3. Load records into Snowflake
"""

from extract import extract_data
from transform import transform_data
from load import load_data


# ==========================================================
# ETL PIPELINE
# ==========================================================

def run_etl():
    """
    Execute the complete ETL pipeline.
    """

    print("=" * 70)
    print("STARTING OPENAQ ETL PIPELINE")
    print("=" * 70)

    # ------------------------------------------------------
    # Extract
    # ------------------------------------------------------

    raw_data = extract_data()

    if raw_data is None:
        print("ETL Failed: Unable to extract data.")
        return

    print("Extract Step Completed.")

    # ------------------------------------------------------
    # Transform
    # ------------------------------------------------------

    transformed_data = transform_data(raw_data)

    if not transformed_data:
        print("ETL Failed: No data available after transformation.")
        return

    print(f"Transform Step Completed. Records: {len(transformed_data)}")

    # ------------------------------------------------------
    # Load
    # ------------------------------------------------------

    load_data(transformed_data)

    print("Load Step Completed.")

    print("=" * 70)
    print("ETL PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 70)


# ==========================================================
# PROGRAM ENTRY POINT
# ==========================================================

if __name__ == "__main__":
    run_etl()