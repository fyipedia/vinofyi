# vinofyi

Wine knowledge API client for developers -- search wines, grapes, regions, and wine terminology from [VinoFYI](https://vinofyi.com).

<p align="center">
  <img src="demo.gif" alt="vinofyi demo — wine API search and lookup" width="800">
</p>

## Install

```bash
pip install vinofyi[api]     # API client (httpx)
pip install vinofyi[cli]     # + CLI (typer, rich)
pip install vinofyi[mcp]     # + MCP server
pip install vinofyi[all]     # Everything
```

## Quick Start

```python
from vinofyi.api import VinoFYI

with VinoFYI() as api:
    # Search wines, grapes, regions, terms
    results = api.search("pinot noir")
    print(results)

    # Look up a glossary term
    term = api.glossary_term("terroir")
    print(term)
```

## CLI

```bash
vinofyi search "pinot noir"
vinofyi term "terroir"
```

## MCP Server

```bash
# Add to Claude Desktop config
python -m vinofyi.mcp_server
```

Tools: `wine_search`, `wine_glossary_term`

## API Client

```python
from vinofyi.api import VinoFYI

with VinoFYI() as api:
    results = api.search("cabernet sauvignon")
    term = api.glossary_term("malolactic-fermentation")
```

## Links

- [VinoFYI](https://vinofyi.com) -- Wine encyclopedia with wines, grapes, regions, wineries, and more
- [PyPI](https://pypi.org/project/vinofyi/)
- [GitHub](https://github.com/fyipedia/vinofyi)
- [FYIPedia](https://fyipedia.com) -- Open-source developer tools ecosystem
