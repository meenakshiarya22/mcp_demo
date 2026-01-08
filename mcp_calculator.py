from mcp.server.fastmcp import FastMCP
import math

# Initialize FastMCP server
mcp = FastMCP("calculator")

SAFE_GLOBALS = {
    "__builtins__": {},
    "abs": abs,
    "round": round,
    "min": min,
    "max": max,
    "pow": pow,
    "sqrt": math.sqrt
}

@mcp.tool()
async def calculate(expression: str) -> str:
    """
    Evaluate a mathematical expression.

    Args:
        expression: Math expression to evaluate
    """
    try:
        result = eval(expression, SAFE_GLOBALS, {})
        return f"Result: {result}"
    except Exception as e:
        return f"Error evaluating expression: {e}"

if __name__ == "__main__":
    mcp.run(transport="stdio")
