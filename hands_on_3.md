# Exercise 3: Build a Weather MCP Server (Python)

## Objective
By the end of this exercise, participants will:

- Build a **Python MCP server** using the FastMCP SDK
- Expose two real tools:
  - `get_alerts` – US weather alerts by state
  - `get_forecast` – weather forecast by latitude & longitude
- Run the server locally using **STDIO transport**
- Connect the server to **Claude for Desktop**
- Invoke MCP tools through natural language

---

## ⏱Time
**30–40 minutes**

---

## Background (Why this matters)

In **Exercise 1**, you connected a local MCP server.  
In **Exercise 2**, you connected a remote MCP server.

In this exercise, you will **build your own MCP server from scratch**.

An MCP server:
- Exposes **tools** the LLM can call
- Executes real code (APIs, logic, systems)
- Runs safely with explicit user approval
- Uses a standard protocol so any MCP client can connect

This is the foundation of **agentic AI systems**.

---

## Prerequisites

Before starting, ensure:

- Python **3.10+**
- Internet access (US National Weather Service API)
- Claude for Desktop (latest version)
- Basic Python familiarity

This exercise uses **STDIO transport** — avoid `print()`.

---

## Logging Rule (Important)

❌ **Never use `print()` in STDIO-based MCP servers**  
✅ Use a logging framework if needed

Reason: MCP uses **JSON-RPC over stdout**. Any extra output will corrupt the protocol.

---

## Step-by-Step Instructions

---

## Step 1: Install `uv` and Set Up Project

### Install `uv` (one-time)

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
````

```powershell
# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Restart your terminal after installation.

---

### Create project and environment

```bash
uv init weather
cd weather

uv venv
source .venv/bin/activate    # macOS/Linux
.venv\Scripts\activate       # Windows

uv add "mcp[cli]" httpx
touch weather.py
```

---

## Step 2: Initialize the MCP Server

Open `weather.py` and add:

```python
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("weather")

# Constants
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"
```

---

## Step 3: Add Helper Functions

```python
async def make_nws_request(url: str) -> dict[str, Any] | None:
    """Make a request to the NWS API with proper error handling."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None


def format_alert(feature: dict) -> str:
    """Format an alert feature into a readable string."""
    props = feature["properties"]
    return f"""
Event: {props.get("event", "Unknown")}
Area: {props.get("areaDesc", "Unknown")}
Severity: {props.get("severity", "Unknown")}
Description: {props.get("description", "No description available")}
Instructions: {props.get("instruction", "No specific instructions provided")}
"""
```

---

## Step 4: Define MCP Tools

### Tool 1: Get Weather Alerts

```python
@mcp.tool()
async def get_alerts(state: str) -> str:
    """Get weather alerts for a US state.

    Args:
        state: Two-letter US state code (e.g. CA, NY)
    """
    url = f"{NWS_API_BASE}/alerts/active/area/{state.upper()}"
    data = await make_nws_request(url)

    if not data or "features" not in data:
        return "Unable to fetch alerts or no alerts found."

    if not data["features"]:
        return "No active alerts for this state."

    alerts = [format_alert(feature) for feature in data["features"]]
    return "\n---\n".join(alerts)
```

---

### Tool 2: Get Weather Forecast

```python
@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    """Get weather forecast for a location.

    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
    """
    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    points_data = await make_nws_request(points_url)

    if not points_data:
        return "Unable to fetch forecast data."

    forecast_url = points_data["properties"]["forecast"]
    forecast_data = await make_nws_request(forecast_url)

    if not forecast_data:
        return "Unable to fetch detailed forecast."

    periods = forecast_data["properties"]["periods"][:5]
    forecasts = []

    for period in periods:
        forecasts.append(f"""
{period["name"]}:
Temperature: {period["temperature"]}°{period["temperatureUnit"]}
Wind: {period["windSpeed"]} {period["windDirection"]}
Forecast: {period["detailedForecast"]}
""")

    return "\n---\n".join(forecasts)
```

---

## Step 5: Run the MCP Server

Add to the bottom of `weather.py`:

```python
def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
```

Run the server:

```bash
uv run weather.py
```

The MCP server is now running.

---

## Step 6: Connect to Claude for Desktop

Open the Claude configuration file:

* **macOS / Linux**

  ```
  ~/Library/Application Support/Claude/claude_desktop_config.json
  ```
* **Windows**

  ```
  %AppData%\Claude\claude_desktop_config.json
  ```

Add the following:

```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/weather",
        "run",
        "weather.py"
      ]
    }
  }
}
```

Use **absolute paths only**.

Fully quit and restart **Claude for Desktop**.

---

## Hands-On Testing

In Claude Desktop, try:

### Test 1

> What’s the weather forecast for Sacramento?

### Test 2

> What are the active weather alerts in Texas?

Claude will:

1. Detect available MCP tools
2. Ask for permission
3. Execute your server code
4. Return real weather data

---

## Completion Criteria

Participants should be able to confirm:

* [ ] MCP server starts without errors
* [ ] Claude detects the weather server
* [ ] `get_alerts` tool works
* [ ] `get_forecast` tool works
* [ ] Tool calls require explicit approval

---

## Reflection Questions

1. How does MCP differ from calling an API directly?
2. Why must STDIO servers avoid stdout logging?
3. What internal systems could you expose using MCP?
4. How would you secure this server in production?

---

## Wrap-Up

You have now:

* Connected a **local MCP server**
* Integrated a **remote MCP server**
* Built and deployed your **own MCP server**

This is the foundation for **agentic AI systems using MCP**.


