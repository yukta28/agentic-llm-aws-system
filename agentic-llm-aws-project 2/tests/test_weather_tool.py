from src.tools.weather_tool import get_current_weather


def test_weather_tool_validates_city():
    result = get_current_weather("")
    assert result["error"] == "city is required"
