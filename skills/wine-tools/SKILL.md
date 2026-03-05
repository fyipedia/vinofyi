---
name: wine-tools
description: Search 100,646 wines, look up grape varieties, wine regions, and glossary terms from the world's most comprehensive wine database.
---

# Wine Tools

Wine search and reference powered by [vinofyi](https://vinofyi.com/) -- a comprehensive wine knowledge platform covering 100,646 wines, 30,510 wineries, and 7,184 grape varieties.

## Setup

Install the MCP server:

```bash
pip install "vinofyi[mcp]"
```

Add to your `claude_desktop_config.json`:

```json
{
    "mcpServers": {
        "vinofyi": {
            "command": "python",
            "args": ["-m", "vinofyi.mcp_server"]
        }
    }
}
```

## Available Tools

| Tool | Description |
|------|-------------|
| `wine_search` | Search wines, grapes, regions, wineries, and styles by keyword |
| `wine_glossary_term` | Look up wine terminology definitions and related concepts |

## When to Use

- Searching for wines by name, grape, region, or style
- Looking up wine terminology (malolactic fermentation, terroir, tannin, etc.)
- Finding food pairing suggestions for specific wines
- Researching grape varieties and their characteristics
- Exploring wine regions and appellations

## Links

- [Wine Database](https://vinofyi.com/wines/)
- [Grape Varieties](https://vinofyi.com/grapes/)
- [Wine Regions](https://vinofyi.com/regions/)
- [API Documentation](https://vinofyi.com/developers/)
- [PyPI Package](https://pypi.org/project/vinofyi/)
