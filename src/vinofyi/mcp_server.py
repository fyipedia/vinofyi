"""MCP server for vinofyi — wine knowledge tools for AI assistants.

Requires the ``mcp`` extra: ``pip install vinofyi[mcp]``

Run as a standalone server::

    python -m vinofyi.mcp_server

Or configure in ``claude_desktop_config.json``::

    {
        "mcpServers": {
            "vinofyi": {
                "command": "python",
                "args": ["-m", "vinofyi.mcp_server"]
            }
        }
    }
"""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("vinofyi")


@mcp.tool()
def wine_search(query: str) -> str:
    """Search wines, grapes, regions, and wine glossary terms from VinoFYI.

    Returns matching results across all wine knowledge categories.

    Args:
        query: Search term (e.g. "pinot noir", "bordeaux", "tannin").
    """
    from vinofyi.api import VinoFYI

    with VinoFYI() as api:
        data = api.search(query)

    results = data.get("results", [])
    if not results:
        return f"No results found for '{query}'."

    lines = [
        f"## Wine Search: {query}",
        "",
        f"Found {len(results)} result(s):",
        "",
        "| Type | Name | URL |",
        "|------|------|-----|",
    ]
    for item in results:
        lines.append(f"| {item.get('type', '')} | {item.get('name', '')} | {item.get('url', '')} |")
    return "\n".join(lines)


@mcp.tool()
def wine_glossary_term(slug: str) -> str:
    """Look up a wine glossary term by slug from VinoFYI.

    Returns the term name, definition, category, and related terms.

    Args:
        slug: Term slug (e.g. "terroir", "malolactic-fermentation", "tannin").
    """
    from vinofyi.api import VinoFYI

    with VinoFYI() as api:
        data = api.glossary_term(slug)

    name = data.get("name", slug)
    definition = data.get("definition", "No definition available.")
    lines = [
        f"## {name}",
        "",
        definition,
    ]
    if data.get("category"):
        lines.extend(["", f"**Category:** {data['category']}"])
    if data.get("related_terms"):
        related = ", ".join(str(t) for t in data["related_terms"])
        lines.extend(["", f"**Related terms:** {related}"])
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run()
