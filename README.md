# Weather MCP Server

This project is a reference implementation of a **Model Context Protocol (MCP)** server that connects to the **National Weather Service (NWS) API**. It allows MCP-compatible clients, such as **Claude for Desktop**, to fetch real-time weather alerts and forecasts for locations within the United States.

## Features

*   **Real-time Alerts:** Fetch active weather alerts for any US state using two-letter state codes.
*   **Detailed Forecasts:** Get weather forecasts including temperature, wind speed, and direction for specific latitude/longitude coordinates.
*   **Multi-Language Support:** Implementation examples are available for **Python, TypeScript, Java, Kotlin, C#, and Rust**.

## Core MCP Concepts

MCP servers provide three main capabilities to enhance LLM functionality:
1.  **Resources:** File-like data readable by clients.
2.  **Tools:** Functions called by the LLM with user approval (this project's primary focus).
3.  **Prompts:** Pre-written templates for specific tasks.

## ⚠️ Critical Logging Requirements

When building or modifying **STDIO-based** MCP servers, **never write to standard output (stdout)**. Functions like `print()` in Python, `console.log()` in JavaScript, or `println!()` in Rust will **corrupt JSON-RPC messages** and break the server connection. 

**Best Practice:** Always use a logging library that writes to **stderr** or specific log files.

---

## Getting Started

### Prerequisites
*   Familiarity with your chosen programming language and LLMs like Claude.
*   **Claude for Desktop** installed and updated to the latest version.
    https://claude.com/download
*   **System Requirements:**
    *   **Python:** 3.10+ and MCP SDK 1.2.0+.
    https://www.python.org/downloads/


### Installation & Build

#### Python
1.  Install the `uv` package manager: `curl -LsSf https://astral.sh/uv/install.sh | sh`.
Make sure to restart your terminal afterwards to ensure that the uv command gets picked up.
2.  Initialize the project: `uv init weather && cd weather`.
3.  Add dependencies: `uv add "mcp[cli]" httpx`.
4.  Run the server: `uv run weather.py`.

---

## Server Tools

The following tools are exposed by this server:

| Tool Name | Description | Arguments |
| :--- | :--- | :--- |
| `get_alerts` | Get active weather alerts for a US state. | `state` (Two-letter code, e.g., "CA"). |
| `get_forecast` | Get a 5-period weather forecast for a location. | `latitude` (number), `longitude` (number). |

---

## Configuration for Claude for Desktop

To use this server, you must configure the `mcpServers` section of your `claude_desktop_config.json` file.

**Path:** `~/Library/Application Support/Claude/claude_desktop_config.json`.

### Example Configuration (Python)
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
*Note: Always use **absolute paths** for directories and executables.*

---

## Troubleshooting

*   **Server not showing up:** Check the JSON syntax in your config file and ensure paths are absolute.
*   **Restarting Claude:** You must **fully quit** the application (from the system tray or menu bar), not just close the window, for changes to take effect.
*   **Logs:** Check `~/Library/Logs/Claude/mcp.log` for connection issues and `mcp-server-weather.log` for server-specific errors.
*   **NWS API Errors:** The NWS API only supports **US locations**; coordinates outside the US will fail to retrieve grid data.

***

**Analogy for Understanding:** Think of the MCP server as a **translator** standing between a manager (Claude) and a specialist database (National Weather Service). The manager knows what information they need, but they don't speak the database's specific "language" (API calls). The MCP server listens for the manager's request, translates it into a precise command for the database, and then relays the answer back in a format the manager understands.
