# aqi.py

"""
AQI Calculator Module

This module provides:
1. PM2.5 → AQI conversion (US EPA Standard)
2. AQI → Severity category
"""


# ==========================================================
# AQI BREAKPOINTS (US EPA)
# ==========================================================

AQI_BREAKPOINTS = [
    (0.0, 12.0, 0, 50),
    (12.1, 35.4, 51, 100),
    (35.5, 55.4, 101, 150),
    (55.5, 150.4, 151, 200),
    (150.5, 250.4, 201, 300),
    (250.5, 350.4, 301, 400),
    (350.5, 500.4, 401, 500)
]


# ==========================================================
# PM2.5 → AQI
# ==========================================================

def calculate_aqi(pm25):
    """
    Convert PM2.5 concentration (µg/m³) into AQI.

    Args:
        pm25 (float): PM2.5 concentration

    Returns:
        int: AQI value
    """

    if pm25 < 0:
        pm25 = 0

    for bp_low, bp_high, aqi_low, aqi_high in AQI_BREAKPOINTS:

        if bp_low <= pm25 <= bp_high:

            aqi = (
                ((aqi_high - aqi_low) / (bp_high - bp_low))
                * (pm25 - bp_low)
            ) + aqi_low

            return round(aqi)

    return 500


# ==========================================================
# AQI → Severity
# ==========================================================

def get_severity(aqi):
    """
    Return AQI severity category.

    Args:
        aqi (int)

    Returns:
        str
    """

    if aqi <= 50:
        return "Good"

    elif aqi <= 100:
        return "Moderate"

    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups"

    elif aqi <= 200:
        return "Unhealthy"

    elif aqi <= 300:
        return "Very Unhealthy"

    return "Hazardous"


# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    sample_pm25 = [8, 20, 40, 80, 180, 320]

    print("=" * 65)
    print("AQI CALCULATOR TEST")
    print("=" * 65)

    print(f"{'PM2.5':<10}{'AQI':<10}{'Severity'}")
    print("-" * 65)

    for value in sample_pm25:

        aqi = calculate_aqi(value)
        severity = get_severity(aqi)

        print(f"{value:<10}{aqi:<10}{severity}")

    print("=" * 65)