# Real API Tool: Current Weather

This project includes a real external tool:

```python
get_current_weather(city: str, country_code: str | None = None)
```

It calls the Open-Meteo geocoding API to resolve a city, then calls the Open-Meteo forecast API for current weather.

## Why this matters

Mock tools are useful for unit tests, but recruiters and engineers want to see that you understand the real boundary between an LLM and the outside world.

This tool demonstrates:

- Input validation
- Network I/O
- A two-step API workflow
- Error handling
- Structured observations returned to the agent loop

## Example agent action

```json
{
  "type": "tool_call",
  "tool_name": "get_current_weather",
  "tool_input": {
    "city": "Seattle"
  }
}
```

## Example observation

```json
{
  "city": "Seattle",
  "temperature": 13.2,
  "temperature_unit": "°C",
  "humidity": 74,
  "wind_speed": 9.1,
  "source": "Open-Meteo"
}
```

## Local test

```bash
python - <<'PY'
from src.tools.weather_tool import get_current_weather
print(get_current_weather("Seattle"))
PY
```
