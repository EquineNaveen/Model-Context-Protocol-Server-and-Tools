from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Adds two integers together."""
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtracts the second integer from the first."""
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:    
    """Multiplies two integers together."""
    return a * b

@mcp.tool()
def divide(a: int, b: int) -> float:    
    """Divides the first integer by the second. Returns a float."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    mcp.run(transport="stdio")