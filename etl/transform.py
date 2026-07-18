# transform.py

"""
Transform Module

Convert raw OpenAQ JSON into a clean format
for loading into Snowflake.
"""


# ==========================================================
# TRANSFORM DATA
# ==========================================================

def transform_data(raw_data):
    """
    Transform raw OpenAQ response into a clean list.

    Args:
        raw_data (dict): Raw JSON returned by OpenAQ API

    Returns:
        list: Clean records
    """

    if not raw_data:
        return []

    results = raw_data.get("results", [])

    transformed_data = []

    for location in results:

        coordinates = location.get("coordinates") or {}

        record = {
            "location_id": location.get("id"),
            "station_name": location.get("name"),
            "city": location.get("locality"),
            "country": location.get("country", {}).get("code"),
            "latitude": coordinates.get("latitude"),
            "longitude": coordinates.get("longitude"),
            "timezone": location.get("timezone"),
            "owner": location.get("owner", {}).get("name")
        }

        transformed_data.append(record)

    return transformed_data


# ==========================================================
# TESTING
# ==========================================================

if __name__ == "__main__":

    from extract import extract_data

    raw_data = extract_data()

    clean_data = transform_data(raw_data)

    print("=" * 70)
    print("TRANSFORM SUCCESSFUL")
    print("=" * 70)

    print(f"Total Records: {len(clean_data)}")

    if clean_data:

        print("\nFirst Record:\n")

        for key, value in clean_data[0].items():
            print(f"{key:<15}: {value}")