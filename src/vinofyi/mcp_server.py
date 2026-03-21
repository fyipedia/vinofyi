"""MCP server for vinofyi — AI assistant tools for vinofyi.com.

Run: uvx --from "vinofyi[mcp]" python -m vinofyi.mcp_server
"""
from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("VinoFYI")


@mcp.tool()
def list_grapes(limit: int = 20, offset: int = 0) -> str:
    """List grapes from vinofyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from vinofyi.api import VinoFYI

    with VinoFYI() as api:
        data = api.list_grapes(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No grapes found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def get_grape(slug: str) -> str:
    """Get detailed information about a specific grape.

    Args:
        slug: URL slug identifier for the grape.
    """
    from vinofyi.api import VinoFYI

    with VinoFYI() as api:
        data = api.get_grape(slug)
        return str(data)


@mcp.tool()
def list_regions(limit: int = 20, offset: int = 0) -> str:
    """List regions from vinofyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from vinofyi.api import VinoFYI

    with VinoFYI() as api:
        data = api.list_regions(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No regions found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def search_vino(query: str) -> str:
    """Search vinofyi.com for wines, grapes, regions, and food pairings.

    Args:
        query: Search query string.
    """
    from vinofyi.api import VinoFYI

    with VinoFYI() as api:
        data = api.search(query)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return f"No results found for \"{query}\"."
        items = results[:10] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


def main() -> None:
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
