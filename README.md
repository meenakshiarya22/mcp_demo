# MCP Hands-On Exercises

This repository contains a series of hands-on exercises designed to teach the fundamentals of the **Model Context Protocol (MCP)**. MCP is a protocol that enables AI models like Claude to securely interact with external tools and services through standardized interfaces.

## Overview

The exercises build progressively, starting from connecting existing MCP servers to building your own custom MCP servers and clients. By the end, you'll understand how to integrate AI agents with real-world tools and services.

## Exercises

### Exercise 1: Connect a Local MCP Server (Filesystem)
- **Objective**: Connect a local filesystem MCP server to Claude Desktop.
- **Duration**: 20-25 minutes
- **Key Concepts**: Local tool integration, permission-based access, human-in-the-loop control.
- **Skills Learned**: Configuring MCP servers, understanding security boundaries, basic file operations via AI.

### Exercise 2: Connect a Remote MCP Server (Canva)
- **Objective**: Connect the Canva MCP server to Claude for AI-driven design workflows.
- **Duration**: 20-30 minutes
- **Key Concepts**: Remote MCP servers, OAuth authentication, creative tool integration.
- **Skills Learned**: Connecting third-party services, managing permissions, AI-assisted design creation and editing.

### Exercise 3: Build a Weather MCP Server (Python)
- **Objective**: Build a custom Python MCP server that exposes weather-related tools.
- **Duration**: 30-40 minutes
- **Key Concepts**: MCP server development, tool definition, STDIO transport, real API integration.
- **Skills Learned**: Creating MCP servers with FastMCP, handling external APIs, deploying local MCP servers.

### Exercise 4: Build an MCP Client (Python)
- **Objective**: Build a Python MCP client that connects to MCP servers and orchestrates tool calls with Claude.
- **Duration**: 30-40 minutes
- **Key Concepts**: MCP client development, tool discovery, AI orchestration, client-server communication.
- **Skills Learned**: Implementing MCP clients, integrating with LLMs, managing tool execution loops.

## Prerequisites

- Python 3.10+
- Node.js (for Exercise 1)
- Claude Desktop or Claude web version
- uv package manager
- Anthropic API key (for Exercise 4)
- Canva account (for Exercise 2)

## Getting Started

1. Ensure all prerequisites are installed.
2. Start with Exercise 1 and progress sequentially.
3. Each exercise includes detailed step-by-step instructions.
4. Test your implementations with the provided prompts.

## Learning Outcomes

By completing all exercises, you'll be able to:
- Understand the MCP architecture and protocol
- Connect and configure MCP servers (local and remote)
- Build custom MCP servers for specific use cases
- Develop MCP clients for AI agent frameworks
- Implement secure, permission-based tool execution
- Integrate AI with real-world systems and APIs

## Next Steps

After completing these exercises, you'll be ready to:
- Build agent frameworks using MCP
- Create custom tools for specific domains
- Integrate MCP into production applications
- Contribute to the MCP ecosystem

For more information about MCP, visit the [official documentation](https://modelcontextprotocol.io/).