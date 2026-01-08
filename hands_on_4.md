# Exercise 4: Build an MCP Client (Python)

## Objective

By the end of this exercise, participants will:

- Understand the **role of an MCP client**
- Build a **Python-based MCP client**
- Connect the client to **any MCP server**
- Enable **Claude to dynamically call MCP tools**
- Observe the full **client ⇄ Claude ⇄ server ⇄ tool** loop

This exercise completes the MCP lifecycle:
> **Client → Claude → MCP Server → Tools → Claude → Client**

---

## ⏱Time

**30-40 minutes**

---

## Context

So far, you have:

- **Exercise 1** – Connected a local MCP server  
- **Exercise 2** – Connected a remote MCP server  
- **Exercise 3** – Built your own MCP server  

In this exercise, you will **build the client itself**.

An MCP client:
- Discovers tools exposed by MCP servers
- Sends tool metadata to the LLM
- Executes tool calls requested by the LLM
- Returns results back to the LLM
- Displays final responses to the user

This is the foundation for **agent frameworks**.

---

## Prerequisites

Before starting, ensure:

- Python **3.10+**
- `uv` installed [https://docs.astral.sh/uv/getting-started/installation/#standalone-installer]
- An MCP server available (Exercise 3 weather server works)
- Anthropic API key (Claude)

---

## Step 1: Create the Client Project

```bash
uv init mcp-client
cd mcp-client

uv venv
source .venv/bin/activate     # macOS/Linux
.venv\Scripts\activate        # Windows

uv add mcp anthropic python-dotenv

rm main.py
touch client.py
````

---

## Step 2: Configure API Key

Create a `.env` file:

```bash
ANTHROPIC_API_KEY=your-api-key-here
```

Add to `.gitignore`:

```bash
.env
```

**Never commit API keys**

---

## Step 3: Create the MCP Client Skeleton

Open `client.py` and add:

```python
import asyncio
from typing import Optional
from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
```

```python
class MCPClient:
    def __init__(self):
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.anthropic = Anthropic()
```

---

## Step 4: Connect to an MCP Server

Add this method inside `MCPClient`:

```python
async def connect_to_server(self, server_script_path: str):
    """Connect to an MCP server via stdio"""
    is_python = server_script_path.endswith(".py")
    is_js = server_script_path.endswith(".js")

    if not (is_python or is_js):
        raise ValueError("Server must be a .py or .js file")

    command = "python" if is_python else "node"

    params = StdioServerParameters(
        command=command,
        args=[server_script_path],
        env=None
    )

    stdio_transport = await self.exit_stack.enter_async_context(
        stdio_client(params)
    )
    self.stdio, self.write = stdio_transport

    self.session = await self.exit_stack.enter_async_context(
        ClientSession(self.stdio, self.write)
    )

    await self.session.initialize()

    tools = (await self.session.list_tools()).tools
    print("Connected to server with tools:", [t.name for t in tools])
```

---

## Step 5: Process Queries & Tool Calls

Add the core orchestration logic:

```python
async def process_query(self, query: str) -> str:
    messages = [{"role": "user", "content": query}]

    tool_response = await self.session.list_tools()
    available_tools = [
        {
            "name": tool.name,
            "description": tool.description,
            "input_schema": tool.inputSchema,
        }
        for tool in tool_response.tools
    ]

    response = self.anthropic.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=messages,
        tools=available_tools,
    )

    final_output = []

    for content in response.content:
        if content.type == "text":
            final_output.append(content.text)

        elif content.type == "tool_use":
            tool_name = content.name
            tool_args = content.input

            result = await self.session.call_tool(tool_name, tool_args)

            messages.extend([
                {"role": "assistant", "content": response.content},
                {
                    "role": "user",
                    "content": [{
                        "type": "tool_result",
                        "tool_use_id": content.id,
                        "content": result.content
                    }]
                }
            ])

            followup = self.anthropic.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1000,
                messages=messages,
            )

            final_output.append(followup.content[0].text)

    return "\n".join(final_output)
```

---

## Step 6: Interactive Chat Loop

```python
async def chat_loop(self):
    print("\nMCP Client Started")
    print("Type 'quit' to exit")

    while True:
        query = input("\nQuery: ").strip()
        if query.lower() == "quit":
            break

        response = await self.process_query(query)
        print("\n" + response)
```

---

## Step 7: Cleanup Resources

```python
async def cleanup(self):
    await self.exit_stack.aclose()
```

---

## Step 8: Main Entry Point

```python
import sys

async def main():
    if len(sys.argv) < 2:
        print("Usage: python client.py <path_to_server>")
        sys.exit(1)

    client = MCPClient()
    try:
        await client.connect_to_server(sys.argv[1])
        await client.chat_loop()
    finally:
        await client.cleanup()

if __name__ == "__main__":
    asyncio.run(main())
```

---

## Run the Client

Connect to your **Exercise 3 weather server**:

```bash
uv run client.py ../weather/weather.py
```

---

## Test Prompts

Try:

* *“What is the weather forecast for Sacramento?”*
* *“Are there any weather alerts in Texas?”*

Observe:

* Claude choosing tools
* Client executing tool calls
* Results flowing back into Claude’s response

---

## How It Works (Mental Model)

1. Client fetches available tools
2. Query + tool schemas sent to Claude
3. Claude decides whether to call tools
4. Client executes tool via MCP server
5. Results returned to Claude
6. Claude generates final response

---

## Completion Checklist

* [ ] Client connects to MCP server
* [ ] Tools are listed successfully
* [ ] Claude invokes tools automatically
* [ ] Tool results appear in responses
* [ ] Client exits cleanly

---

## Reflection Questions

1. Why is the client responsible for tool execution?
2. What happens if the client refuses a tool call?
3. How does MCP differ from function calling alone?
4. Where would memory or state live in this architecture?

---

## Wrap-Up

You have now built:

✔ MCP Server
✔ MCP Client
✔ Claude-integrated Tool Execution Loop

You are ready to:

* Build **agent frameworks**
* Orchestrate **multi-tool systems**
* Integrate MCP into real products


