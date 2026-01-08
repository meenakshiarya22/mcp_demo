# MCP Demo Project

A collection of example MCP (Model Context Protocol) servers demonstrating different use cases and implementations.

## Overview

This project contains sample MCP server implementations that showcase how to build tools that can be used by AI assistants like Claude. Each server exposes specific functionality through the MCP protocol.

## MCP Servers

### Weather Demo Server (`mcp_weather.py`)

A simple weather information MCP server that provides simulated weather data.

**Features:**
- `get_weather(city: str)` - Returns simulated weather information for a given city
- Returns temperature, conditions, and observation timestamp

**Usage:**
```bash
python mcp_weather.py
```

**Example Tool Response:**
```
City: New York
Temperature: 28°C
Condition: Cloudy
Observed At: 2024-01-08T10:30:00Z
```

### Calculator Server (`mcp_calculator.py`)

A mathematical calculator MCP server that safely evaluates mathematical expressions.

**Features:**
- `calculate(expression: str)` - Evaluates mathematical expressions safely
- Supports basic arithmetic operations, functions like `sqrt`, `pow`, etc.
- Uses a restricted evaluation environment for security

**Supported Operations:**
- Basic arithmetic: `+`, `-`, `*`, `/`
- Functions: `abs()`, `round()`, `min()`, `max()`, `pow()`, `sqrt()`
- Safe evaluation with limited globals

**Usage:**
```bash
python mcp_calculator.py
```

**Example Usage:**
- Expression: `"2 + 3 * 4"`
- Result: `"Result: 14"`

## Getting Started

### Prerequisites

- Python 3.10+
- MCP SDK (`pip install mcp`)

### Running a Server

1. Choose which server to run (weather or calculator)
2. Execute the Python file directly:
   ```bash
   python mcp_weather.py
   # or
   python mcp_calculator.py
   ```

### Connecting to Claude Desktop

To use these servers with Claude Desktop:

1. Open Claude Desktop configuration
2. Add the server to `mcpServers` in `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "weather-demo": {
      "command": "python",
      "args": ["path/to/mcp_weather.py"]
    },
    "calculator": {
      "command": "python",
      "args": ["path/to/mcp_calculator.py"]
    }
  }
}
```

3. Restart Claude Desktop
4. The tools will be available for Claude to use

## Project Structure

```
mcp_demo/
├── mcp_weather.py      # Weather demo MCP server
├── mcp_calculator.py   # Calculator MCP server
├── main.py            # Basic demo script
├── pyproject.toml     # Project configuration
└── README.md          # This file
```

## Learning Objectives

These examples demonstrate:

- **MCP Server Creation**: How to build MCP servers using FastMCP
- **Tool Definition**: Creating tools with proper type hints and documentation
- **Safe Execution**: Implementing secure evaluation (calculator example)
- **Real-world Integration**: Connecting MCP servers to AI assistants
- **Protocol Usage**: Understanding STDIO transport and MCP communication

## Development

### Adding New MCP Servers

To add a new MCP server:

1. Create a new Python file (e.g., `mcp_newtool.py`)
2. Import FastMCP: `from mcp.server.fastmcp import FastMCP`
3. Initialize server: `mcp = FastMCP("server_name")`
4. Define tools using `@mcp.tool()` decorator
5. Run with: `mcp.run(transport="stdio")`

### Best Practices

- Use descriptive tool names and docstrings
- Implement proper error handling
- Consider security implications (especially for evaluation-like tools)
- Test tools independently before integration

## Related Exercises

This project complements the hands-on MCP exercises in the parent directory, providing concrete implementations of concepts learned in:

- Exercise 3: Building MCP Servers
- Exercise 4: MCP Client Integration

## License

Educational project for learning MCP concepts.