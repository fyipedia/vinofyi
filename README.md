# vinofyi

[![PyPI](https://img.shields.io/pypi/v/vinofyi)](https://pypi.org/project/vinofyi/)
[![Python](https://img.shields.io/pypi/pyversions/vinofyi)](https://pypi.org/project/vinofyi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Wine knowledge API client for Python. Search wines, grapes, regions, wineries, and wine terminology from [VinoFYI](https://vinofyi.com) -- the comprehensive wine encyclopedia with 777 grape varieties, 741K records, and 230 expert guides covering everything from terroir and appellation systems to food pairing principles.

> **Explore wine at [vinofyi.com](https://vinofyi.com)** -- [Wine Directory](https://vinofyi.com/wines/) | [Grape Varieties](https://vinofyi.com/grapes/) | [Wine Regions](https://vinofyi.com/regions/) | [Wineries](https://vinofyi.com/wineries/) | [Wine Guides](https://vinofyi.com/guides/)

<p align="center">
  <img src="demo.gif" alt="vinofyi demo -- wine API search and lookup" width="800">
</p>

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [What You'll Find on VinoFYI](#what-youll-find-on-vinofyi)
  - [Wine Types](#wine-types)
  - [Grape Varieties](#grape-varieties)
  - [Wine Regions and Terroir](#wine-regions-and-terroir)
  - [Wine Guides](#wine-guides)
- [API Endpoints](#api-endpoints)
- [Command-Line Interface](#command-line-interface)
- [MCP Server (Claude, Cursor, Windsurf)](#mcp-server-claude-cursor-windsurf)
- [API Client](#api-client)
- [Learn More About Wine](#learn-more-about-wine)
- [Beverage FYI Family](#beverage-fyi-family)
- [FYIPedia Developer Tools](#fyipedia-developer-tools)
- [License](#license)

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
    # Search wines, grapes, regions, glossary terms
    results = api.search("pinot noir")
    print(results)

    # Look up a glossary term
    term = api.glossary_term("terroir")
    print(term["definition"])
```

## What You'll Find on VinoFYI

VinoFYI is a comprehensive wine reference with 741K records spanning wines, grape varieties, regions, wineries, and an extensive glossary. Whether you are building a wine recommendation engine, a sommelier study tool, or a food pairing application, the VinoFYI API provides structured data for every aspect of wine knowledge.

### Wine Types

Wine is classified into six major categories based on production method, color, and residual sugar. Each type encompasses distinct winemaking techniques and flavor profiles:

| Type | Description | Key Characteristics |
|------|-------------|---------------------|
| Red | Made with extended skin contact during fermentation | Tannins, body, aging potential |
| White | Pressed before fermentation, minimal skin contact | Acidity, aromatics, freshness |
| Rose | Brief skin contact produces pink hue | Light body, versatile food pairing |
| Sparkling | Secondary fermentation creates carbonation | Methode champenoise, Charmat method |
| Fortified | Spirit added during or after fermentation | Higher ABV (15-22%), Port, Sherry |
| Dessert | Late harvest or dried grapes concentrate sugars | Residual sugar, Sauternes, Ice Wine |

Understanding wine types is essential for proper service temperature, glassware selection, and food pairing decisions.

Learn more: [Wine Types Guide](https://vinofyi.com/type/) · [Wine Encyclopedia](https://vinofyi.com/wine/)

### Grape Varieties

VinoFYI catalogs 777 grape varieties with detailed profiles including origin, flavor descriptors, ideal growing conditions, and notable wine regions. Grapes are the foundation of wine character -- the same variety planted in different terroirs produces dramatically different wines.

Major international varieties include Cabernet Sauvignon, Merlot, Pinot Noir, Chardonnay, Sauvignon Blanc, and Riesling. Indigenous varieties like Nebbiolo (Piedmont), Tempranillo (Rioja), Gruner Veltliner (Austria), and Assyrtiko (Santorini) reflect centuries of regional adaptation and cultural identity.

Key grape attributes tracked in the database:

- **Skin color** -- determines red, white, or rose potential
- **Berry size** -- affects skin-to-juice ratio and tannin extraction
- **Ripening period** -- early, mid, or late season
- **Climate preference** -- cool, moderate, or warm climate suitability
- **Typical flavor profile** -- primary, secondary, and tertiary aromas

Learn more: [Browse 777 Grape Varieties](https://vinofyi.com/grape/) · [Grape Search](https://vinofyi.com/search/)

### Wine Regions and Terroir

Wine regions are organized hierarchically from country to specific appellations. Terroir -- the complete natural environment in which a wine is produced -- encompasses climate, soil composition, altitude, aspect, and local traditions. The concept of terroir explains why a Pinot Noir from Burgundy tastes fundamentally different from one grown in Oregon's Willamette Valley.

Major wine-producing countries include France, Italy, Spain, the United States, Argentina, Chile, Australia, Germany, Portugal, and South Africa. Each country's appellation system (AOC, DOC, AVA, GI) defines quality standards and geographic boundaries.

Learn more: [Explore Wine Regions](https://vinofyi.com/region/) · [Country Profiles](https://vinofyi.com/country/)

### Wine Guides

VinoFYI features 230 expert guides covering wine tasting methodology, food pairing principles, cellar management, and regional deep-dives. Guides range from beginner topics like understanding wine labels to advanced subjects like malolactic fermentation chemistry and barrel aging programs.

Learn more: [Wine Guides Library](https://vinofyi.com/guide/) · [Wine Glossary](https://vinofyi.com/glossary/)

## API Endpoints

All endpoints are free, require no authentication, and return JSON with CORS enabled.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/wines/` | List all wines |
| GET | `/api/v1/wines/{slug}/` | Wine detail with full profile |
| GET | `/api/v1/grapes/` | List all 777 grape varieties |
| GET | `/api/v1/grapes/{slug}/` | Grape variety detail |
| GET | `/api/v1/regions/` | List wine regions |
| GET | `/api/v1/regions/{slug}/` | Region detail with climate, soils |
| GET | `/api/v1/wineries/` | List wineries |
| GET | `/api/v1/wineries/{slug}/` | Winery detail |
| GET | `/api/v1/glossary/` | List all wine terminology |
| GET | `/api/v1/glossary/{slug}/` | Glossary term definition |
| GET | `/api/v1/search/?q={query}` | Search across all content |
| GET | `/api/v1/compare/{slug1}/{slug2}/` | Compare two wines or grapes |
| GET | `/api/v1/random/` | Random wine or grape |
| GET | `/api/v1/guides/` | List all 230 guides |
| GET | `/api/v1/guides/{slug}/` | Guide detail |
| GET | `/api/v1/openapi.json` | OpenAPI 3.1.0 specification |

### Example

```bash
curl -s "https://vinofyi.com/api/v1/grapes/pinot-noir/"
```

```json
{
  "slug": "pinot-noir",
  "name": "Pinot Noir",
  "color": "red",
  "description": "One of the world's most celebrated red grape varieties, known for elegance, complexity, and translucent color.",
  "origin": "Burgundy, France",
  "notable_regions": ["Burgundy", "Willamette Valley", "Central Otago", "Sonoma Coast"],
  "flavor_profile": ["cherry", "raspberry", "earth", "mushroom", "spice"],
  "ideal_climate": "cool",
  "url": "https://vinofyi.com/grapes/pinot-noir/"
}
```

Full API documentation: [vinofyi.com/developers/](https://vinofyi.com/developers/).
OpenAPI 3.1.0 spec: [vinofyi.com/api/v1/openapi.json](https://vinofyi.com/api/v1/openapi.json).

## Command-Line Interface

```bash
# Search wines, grapes, regions, and terms
vinofyi search "pinot noir"
vinofyi search "burgundy"
vinofyi search "malolactic fermentation"

# Look up a specific glossary term
vinofyi term "terroir"
vinofyi term "tannins"

# Get grape variety details
vinofyi search "cabernet sauvignon"
```

The CLI displays results in formatted tables with rich terminal output.

## MCP Server (Claude, Cursor, Windsurf)

Run as an MCP server for AI-assisted wine queries:

```bash
python -m vinofyi.mcp_server
```

**Claude Desktop** (`~/.claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "vinofyi": {
      "command": "uvx",
      "args": ["--from", "vinofyi[mcp]", "python", "-m", "vinofyi.mcp_server"]
    }
  }
}
```

**Tools**: `wine_search`, `wine_glossary_term`

## API Client

```python
from vinofyi.api import VinoFYI

with VinoFYI() as api:
    # Search across wines, grapes, regions, glossary
    results = api.search("cabernet sauvignon")

    # Look up wine terminology
    term = api.glossary_term("malolactic-fermentation")
    print(term["definition"])

    # Compare two grapes
    comparison = api.compare("pinot-noir", "cabernet-sauvignon")

    # Get a random wine
    random_wine = api.random()
```

## Learn More About Wine

- **Reference**: [Wines](https://vinofyi.com/wines/) | [Grape Varieties](https://vinofyi.com/grapes/) | [Wine Regions](https://vinofyi.com/regions/) | [Wineries](https://vinofyi.com/wineries/)
- **Glossary**: [Wine Terminology](https://vinofyi.com/glossary/)
- **Guides**: [Wine Guides](https://vinofyi.com/guides/)
- **Compare**: [Wine Comparisons](https://vinofyi.com/compare/)
- **API**: [Developer Docs](https://vinofyi.com/developers/) | [OpenAPI Spec](https://vinofyi.com/api/v1/openapi.json)

## Beverage FYI Family

| Site | Domain | Focus |
|------|--------|-------|
| CocktailFYI | [cocktailfyi.com](https://cocktailfyi.com) | 636 cocktail recipes, ABV, calories, flavor profiles |
| **VinoFYI** | [vinofyi.com](https://vinofyi.com) | **Wines, grapes, regions, wineries, food pairings** |
| BeerFYI | [beerfyi.com](https://beerfyi.com) | 112 beer styles, hops, malts, yeast, brewing guides |
| BrewFYI | [brewfyi.com](https://brewfyi.com) | 72 coffee varieties, roasting, 21 brew methods |
| WhiskeyFYI | [whiskeyfyi.com](https://whiskeyfyi.com) | 80 whiskey expressions, distilleries, regions |
| TeaFYI | [teafyi.com](https://teafyi.com) | 60 tea varieties, teaware, brewing guides |
| NihonshuFYI | [nihonshufyi.com](https://nihonshufyi.com) | 80 sake, rice varieties, 50 breweries |

## FYIPedia Developer Tools

| Package | PyPI | npm | Description |
|---------|------|-----|-------------|
| colorfyi | [PyPI](https://pypi.org/project/colorfyi/) | [npm](https://www.npmjs.com/package/@fyipedia/colorfyi) | Color conversion, WCAG contrast, harmonies -- [colorfyi.com](https://colorfyi.com) |
| emojifyi | [PyPI](https://pypi.org/project/emojifyi/) | [npm](https://www.npmjs.com/package/emojifyi) | Emoji encoding & metadata for 3,953 emojis -- [emojifyi.com](https://emojifyi.com) |
| symbolfyi | [PyPI](https://pypi.org/project/symbolfyi/) | [npm](https://www.npmjs.com/package/symbolfyi) | Symbol encoding in 11 formats -- [symbolfyi.com](https://symbolfyi.com) |
| unicodefyi | [PyPI](https://pypi.org/project/unicodefyi/) | [npm](https://www.npmjs.com/package/unicodefyi) | Unicode lookup with 17 encodings -- [unicodefyi.com](https://unicodefyi.com) |
| fontfyi | [PyPI](https://pypi.org/project/fontfyi/) | [npm](https://www.npmjs.com/package/fontfyi) | Google Fonts metadata & CSS -- [fontfyi.com](https://fontfyi.com) |
| distancefyi | [PyPI](https://pypi.org/project/distancefyi/) | [npm](https://www.npmjs.com/package/distancefyi) | Haversine distance & travel times -- [distancefyi.com](https://distancefyi.com) |
| timefyi | [PyPI](https://pypi.org/project/timefyi/) | [npm](https://www.npmjs.com/package/timefyi) | Timezone ops & business hours -- [timefyi.com](https://timefyi.com) |
| namefyi | [PyPI](https://pypi.org/project/namefyi/) | [npm](https://www.npmjs.com/package/namefyi) | Korean romanization & Five Elements -- [namefyi.com](https://namefyi.com) |
| unitfyi | [PyPI](https://pypi.org/project/unitfyi/) | [npm](https://www.npmjs.com/package/unitfyi) | Unit conversion, 220 units -- [unitfyi.com](https://unitfyi.com) |
| holidayfyi | [PyPI](https://pypi.org/project/holidayfyi/) | [npm](https://www.npmjs.com/package/holidayfyi) | Holiday dates & Easter calculation -- [holidayfyi.com](https://holidayfyi.com) |
| cocktailfyi | [PyPI](https://pypi.org/project/cocktailfyi/) | -- | Cocktail ABV, calories, flavor -- [cocktailfyi.com](https://cocktailfyi.com) |
| **vinofyi** | [PyPI](https://pypi.org/project/vinofyi/) | -- | **Wine API client -- grapes, regions, wineries -- [vinofyi.com](https://vinofyi.com)** |
| beerfyi | [PyPI](https://pypi.org/project/beerfyi/) | -- | Beer styles, hops, malts API -- [beerfyi.com](https://beerfyi.com) |
| brewfyi | [PyPI](https://pypi.org/project/brewfyi/) | -- | Coffee varieties, brew methods API -- [brewfyi.com](https://brewfyi.com) |
| whiskeyfyi | [PyPI](https://pypi.org/project/whiskeyfyi/) | -- | Whiskey expressions, distilleries API -- [whiskeyfyi.com](https://whiskeyfyi.com) |
| teafyi | [PyPI](https://pypi.org/project/teafyi/) | -- | Tea varieties, teaware API -- [teafyi.com](https://teafyi.com) |
| nihonshufyi | [PyPI](https://pypi.org/project/nihonshufyi/) | -- | Sake grades, breweries API -- [nihonshufyi.com](https://nihonshufyi.com) |
| drinkfyi | [PyPI](https://pypi.org/project/drinkfyi/) | -- | Unified beverage hub -- 7 sites -- [fyipedia.com](https://fyipedia.com) |
| fyipedia | [PyPI](https://pypi.org/project/fyipedia/) | -- | Unified CLI: `fyi color info FF6B35` -- [fyipedia.com](https://fyipedia.com) |
| fyipedia-mcp | [PyPI](https://pypi.org/project/fyipedia-mcp/) | -- | Unified MCP hub for AI assistants -- [fyipedia.com](https://fyipedia.com) |

## License

MIT
