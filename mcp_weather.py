from mcp.server.fastmcp import FastMCP
from datetime import datetime

# Initialize FastMCP server
mcp = FastMCP("weather_demo")

@mcp.tool()
async def get_weather(city: str) -> str:
    """
    Get current weather for a city (simulated).

    Args:
        city: Name of the city
    """
    return f"""
City: {city}
Temperature: 28°C
Condition: Cloudy
Observed At: {datetime.utcnow().isoformat()}Z
"""

if __name__ == "__main__":
    mcp.run(transport="stdio")
