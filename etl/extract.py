# extract.py

"""
Extract Module

Fetch raw air quality data from the OpenAQ API.
"""

import os
import requests
from dotenv import load_dotenv


# ==========================================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================================

load_dotenv("../config/.env")

API_KEY = os.getenv("OPENAQ_API_KEY")

BASE_URL = "https://api.openaq.org/v3"

HEADERS = {
    "X-API-Key": API_KEY
}


# ==========================================================
# EXTRACT DATA
# ==========================================================

def extract_data(country="PK", limit=100):
    """
    Fetch raw location data from OpenAQ.

    Args:
        country (str): Country code (default: PK)
        limit (int): Number of records

    Returns:
        dict: Raw JSON response
    """

    endpoint = "/locations"

    params = {
        "country_id": country,
        "limit": limit
    }

    try:

        response = requests.get(
            BASE_URL + endpoint,
            headers=HEADERS,
            params=params,
            timeout=30
        )

        response.raise_for_status()

        print("Data extracted successfully.")

        return response.json()

    except requests.exceptions.RequestException as error:

        print(f"Extraction Error: {error}")

        return None


# ==========================================================
# TESTING
# ==========================================================

if __name__ == "__main__":

    data = extract_data()

    if data:

        print("=" * 60)
        print("EXTRACT SUCCESSFUL")
        print("=" * 60)

        print(f"Total Locations: {len(data.get('results', []))}")

        if data.get("results"):

            print("\nFirst Record:\n")
            print(data["results"][0])