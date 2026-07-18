# sensor_config.py

# ==========================================================
# SENSOR CONFIGURATION
# ==========================================================

SENSORS = [
    {
        "sensor_id": "PKS_KHI_IND_01",
        "city": "Karachi",
        "zone_type": "Industrial"
    },
    {
        "sensor_id": "PKS_KHI_TRF_02",
        "city": "Karachi",
        "zone_type": "Traffic"
    },
    {
        "sensor_id": "PKS_LHR_RES_01",
        "city": "Lahore",
        "zone_type": "Residential"
    },
    {
        "sensor_id": "PKS_LHR_IND_02",
        "city": "Lahore",
        "zone_type": "Industrial"
    },
    {
        "sensor_id": "PKS_ISB_PRK_01",
        "city": "Islamabad",
        "zone_type": "Park"
    },
    {
        "sensor_id": "PKS_ISB_TRF_02",
        "city": "Islamabad",
        "zone_type": "Traffic"
    },
    {
        "sensor_id": "PKS_PEW_IND_01",
        "city": "Peshawar",
        "zone_type": "Industrial"
    },
    {
        "sensor_id": "PKS_PEW_RES_02",
        "city": "Peshawar",
        "zone_type": "Residential"
    },
    {
        "sensor_id": "PKS_MUL_TRF_01",
        "city": "Multan",
        "zone_type": "Traffic"
    },
    {
        "sensor_id": "PKS_MUL_PRK_02",
        "city": "Multan",
        "zone_type": "Park"
    }
]

# ==========================================================
# BASE VALUES FOR EACH ZONE
# (Ranges taken from project specification)
# ==========================================================

BASE_VALUES = {

    "Industrial": {
        "pm25": (80, 120),
        "co2_ppm": (600, 900),
        "temperature": (30, 42)
    },

    "Traffic": {
        "pm25": (55, 80),
        "co2_ppm": (500, 700),
        "temperature": (28, 40)
    },

    "Residential": {
        "pm25": (25, 50),
        "co2_ppm": (420, 500),
        "temperature": (25, 38)
    },

    "Park": {
        "pm25": (8, 20),
        "co2_ppm": (400, 430),
        "temperature": (22, 35)
    }

}