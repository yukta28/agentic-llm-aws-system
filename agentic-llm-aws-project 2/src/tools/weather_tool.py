from typing import Any, Dict
from urllib.parse import urlencode
from urllib.request import urlopen
import json


def _get_json(url: str, timeout: int = 8) -> Dict[str, Any]:
    with urlopen(url, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def get_current_weather(city: str, country_code: str | None = None) -> Dict[str, Any]:
    """
    Real external API tool using Open-Meteo.

    Why this is a good demo tool:
    - No API key required
    - Has a geocoding step + forecast step
    - Forces the agent to call a real service instead of relying on memorized data

    Example:
        get_current_weather(city="Seattle")
    """
    if not city or not city.strip():
        return {"error": "city is required"}

    geo_params = {"name": city.strip(), "count": 1, "language": "en", "format": "json"}
    if country_code:
        geo_params["countryCode"] = country_code.upper()

    geo_url = "https://geocoding-api.open-meteo.com/v1/search?" + urlencode(geo_params)
    geo = _get_json(geo_url)

    results = geo.get("results") or []
    if not results:
        return {"error": f"Could not geocode city: {city}"}

    location = results[0]
    latitude = location["latitude"]
    longitude = location["longitude"]

    forecast_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "timezone": "auto",
    }
    forecast_url = "https://api.open-meteo.com/v1/forecast?" + urlencode(forecast_params)
    forecast = _get_json(forecast_url)

    current = forecast.get("current", {})
    units = forecast.get("current_units", {})

    return {
        "city": location.get("name"),
        "region": location.get("admin1"),
        "country": location.get("country"),
        "latitude": latitude,
        "longitude": longitude,
        "temperature": current.get("temperature_2m"),
        "temperature_unit": units.get("temperature_2m"),
        "humidity": current.get("relative_humidity_2m"),
        "humidity_unit": units.get("relative_humidity_2m"),
        "wind_speed": current.get("wind_speed_10m"),
        "wind_speed_unit": units.get("wind_speed_10m"),
        "time": current.get("time"),
        "source": "Open-Meteo",
    }
