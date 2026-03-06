---
name: wine-tools
description: Search wines, grape varieties, regions, wineries, and wine terminology from VinoFYI. Use when answering questions about wine types, grape profiles, terroir, food pairings, or winemaking.
license: MIT
metadata:
  author: fyipedia
  version: "0.1.1"
  homepage: "https://vinofyi.com/"
---

# VinoFYI -- Wine Tools for AI Agents

Wine knowledge API client for Python. Search 777 grape varieties, wine regions, wineries, and 230 expert guides from VinoFYI -- the comprehensive wine encyclopedia with 741K records covering terroir, appellation systems, and food pairing principles.

**Install**: `pip install vinofyi[api]` -- **Web**: [vinofyi.com](https://vinofyi.com/) -- **API**: [REST API](https://vinofyi.com/developers/) -- **PyPI**: [vinofyi](https://pypi.org/project/vinofyi/)

## When to Use

- User asks about wine types, grape varieties, or wine regions
- User needs grape variety profiles (flavor, climate, origin)
- User wants wine terminology definitions (terroir, tannins, malolactic fermentation)
- User asks about food and wine pairings
- User needs to search or compare wines

## Tools

### `VinoFYI` API Client

HTTP client for the vinofyi.com REST API. Requires `pip install vinofyi[api]`.

```python
from vinofyi.api import VinoFYI

with VinoFYI() as api:
    results = api.search("pinot noir")       # Search wines, grapes, regions, glossary
    term = api.glossary_term("terroir")      # Get glossary term by slug
```

**Methods:**
- `search(query: str) -> dict` -- Search wines, grapes, regions, and glossary terms
- `glossary_term(slug: str) -> dict` -- Get a glossary term by slug (e.g. `"terroir"`, `"malolactic-fermentation"`)

## REST API (No Auth Required)

```bash
# Search
curl "https://vinofyi.com/api/v1/search/?q=pinot+noir"

# Grape variety detail
curl "https://vinofyi.com/api/v1/grapes/pinot-noir/"

# Glossary term
curl "https://vinofyi.com/api/v1/glossary/terroir/"

# Compare two grapes
curl "https://vinofyi.com/api/v1/compare/pinot-noir/cabernet-sauvignon/"
```

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/wines/` | List all wines |
| GET | `/api/v1/wines/{slug}/` | Wine detail with full profile |
| GET | `/api/v1/grapes/` | List all 777 grape varieties |
| GET | `/api/v1/grapes/{slug}/` | Grape variety detail |
| GET | `/api/v1/regions/` | List wine regions |
| GET | `/api/v1/regions/{slug}/` | Region detail with climate, soils |
| GET | `/api/v1/wineries/` | List wineries |
| GET | `/api/v1/glossary/{slug}/` | Glossary term definition |
| GET | `/api/v1/search/?q={query}` | Search across all content |
| GET | `/api/v1/compare/{slug1}/{slug2}/` | Compare two wines or grapes |
| GET | `/api/v1/random/` | Random wine or grape |
| GET | `/api/v1/openapi.json` | OpenAPI 3.1.0 specification |

Full spec: [OpenAPI 3.1.0](https://vinofyi.com/api/v1/openapi.json)

## Wine Types Reference

| Type | Description | Key Characteristics |
|------|-------------|---------------------|
| Red | Extended skin contact during fermentation | Tannins, body, aging potential |
| White | Pressed before fermentation, minimal skin contact | Acidity, aromatics, freshness |
| Rose | Brief skin contact produces pink hue | Light body, versatile food pairing |
| Sparkling | Secondary fermentation creates carbonation | Methode champenoise, Charmat method |
| Fortified | Spirit added during or after fermentation | Higher ABV (15-22%), Port, Sherry |
| Dessert | Late harvest or dried grapes concentrate sugars | Residual sugar, Sauternes, Ice Wine |

## Major Grape Varieties

| Variety | Color | Origin | Notable Regions |
|---------|-------|--------|-----------------|
| Cabernet Sauvignon | Red | Bordeaux | Napa, Bordeaux, Coonawarra |
| Pinot Noir | Red | Burgundy | Burgundy, Willamette Valley, Central Otago |
| Merlot | Red | Bordeaux | Bordeaux, Washington State |
| Chardonnay | White | Burgundy | Burgundy, Napa, Margaret River |
| Sauvignon Blanc | White | Loire | Marlborough, Sancerre |
| Riesling | White | Germany | Mosel, Alsace, Clare Valley |
| Nebbiolo | Red | Piedmont | Barolo, Barbaresco |
| Tempranillo | Red | Spain | Rioja, Ribera del Duero |

## Demo

![VinoFYI demo](https://raw.githubusercontent.com/fyipedia/vinofyi/main/demo.gif)

## Beverage FYI Family

Part of the [FYIPedia](https://fyipedia.com) ecosystem: [CocktailFYI](https://cocktailfyi.com), [VinoFYI](https://vinofyi.com), [BeerFYI](https://beerfyi.com), [BrewFYI](https://brewfyi.com), [WhiskeyFYI](https://whiskeyfyi.com), [TeaFYI](https://teafyi.com), [NihonshuFYI](https://nihonshufyi.com).
