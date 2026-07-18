import os
import snowflake.connector
from dotenv import load_dotenv

load_dotenv("../config/.env")


def load_data(records):

    if not records:
        print("No records to load.")
        return

    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA")
    )

    cursor = conn.cursor()

    insert_query = """
    INSERT INTO OPENAQ_RAW
    (
        location_id,
        station_name,
        city,
        country,
        latitude,
        longitude,
        timezone,
        owner
    )
    VALUES
    (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    try:

        for record in records:

            cursor.execute(
                insert_query,
                (
                    record["location_id"],
                    record["station_name"],
                    record["city"],
                    record["country"],
                    record["latitude"],
                    record["longitude"],
                    record["timezone"],
                    record["owner"]
                )
            )

        conn.commit()

        print(f"{len(records)} records loaded successfully.")

    except Exception as e:

        conn.rollback()
        print("Load Error:", e)

    finally:

        cursor.close()
        conn.close()


if __name__ == "__main__":

    from extract import extract_data
    from transform import transform_data

    raw = extract_data()
    data = transform_data(raw)

    load_data(data)