# Model Context Protocol Server and Tools

This repository contains implementations of Model Context Protocol (MCP) servers and client applications that demonstrate how to use MCP for AI agent interactions.

## Part 1: Math Tools Integration (client.py and mathserver.py)

This part of the codebase demonstrates how to create a simple MCP server that provides math operations and a client that utilizes these operations through a language model.

### mathserver.py

A simple MCP server that provides basic mathematical operations:
- `add`: Adds two integers together
- `subtract`: Subtracts the second integer from the first
- `multiply`: Multiplies two integers together
- `divide`: Divides the first integer by the second, returns a float

The server uses `FastMCP` to easily expose these operations as tools that can be called by MCP clients.

### client.py

A demonstration client that:
1. Sets up a connection to the math server using `MultiServerMCPClient`
2. Uses the Groq API with the "qwen-qwq-32b" model
3. Creates a ReAct agent using LangGraph
4. Executes a simple math problem "(88*(2+3))/5" by having the language model use the math tools

### How to Run

1. Make sure you have all dependencies installed: `pip install -r requirements.txt`
2. Set your Groq API key in a `.env` file: `GROQ_API_KEY=your-api-key`
3. Run the client: `python client.py`

The client will automatically start the math server as a subprocess, communicate with it using stdio transport, and solve the math problem.

## Part 2: Advanced MCP Integration (app.py and mcpconfig.json)

This part demonstrates a more advanced usage of MCP with multiple external tool servers and an interactive chat interface.

### mcpconfig.json

Configuration file that defines external MCP servers:
- `playwright`: For web automation tasks
- `airbnb`: For Airbnb-related operations
- `duckduckgo-search`: For web search functionality

Each server is configured with the command and arguments needed to start it.

### app.py

An interactive chat application that:
1. Connects to all the servers defined in `mcpconfig.json`
2. Sets up a chat interface using the Groq "qwen-qwq-32b" model
3. Creates an `MCPAgent` that can use all available tools from the configured servers
4. Provides a memory-enabled conversation that maintains chat history
5. Allows users to interact with the agent in a continuous conversation

#### Features:
- Persistent conversation history (memory)
- Commands to exit the chat (`exit`, `quit`)
- Command to clear conversation history (`clear`)
- Error handling for agent operations

### How to Run

1. Make sure you have all dependencies installed: `pip install -r requirements.txt`
2. Set your Groq API key in a `.env` file: `GROQ_API_KEY=your-api-key`
3. Run the application: `python app.py`
4. Interact with the chat interface by typing messages

Note: When running `app.py`, the external MCP servers will be started automatically as configured in `mcpconfig.json`.

## Requirements

See `requirements.txt` for the full list of dependencies:
- langchain-groq
- langchain-mcp-adapters
- mcp
- langgraph
- mcp-use