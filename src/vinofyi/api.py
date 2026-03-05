"""HTTP API client for vinofyi.com REST endpoints.

Requires the ``api`` extra: ``pip install vinofyi[api]``

Usage::

    from vinofyi.api import VinoFYI

    with VinoFYI() as api:
        results = api.search("pinot noir")
        print(results)
"""

from __future__ import annotations

from typing import Any

import httpx


class VinoFYI:
    """API client for the vinofyi.com REST API.

    Args:
        base_url: API base URL. Defaults to ``https://vinofyi.com``.
        timeout: Request timeout in seconds. Defaults to ``10.0``.
    """

    def __init__(
        self,
        base_url: str = "https://vinofyi.com",
        timeout: float = 10.0,
    ) -> None:
        self._client = httpx.Client(base_url=base_url, timeout=timeout)

    # -- HTTP helpers ----------------------------------------------------------

    def _get(self, path: str, **params: Any) -> dict[str, Any]:
        resp = self._client.get(path, params={k: v for k, v in params.items() if v is not None})
        resp.raise_for_status()
        result: dict[str, Any] = resp.json()
        return result

    # -- Endpoints -------------------------------------------------------------

    def search(self, query: str) -> dict[str, Any]:
        """Search wines, grapes, regions, and glossary terms.

        Args:
            query: Search term (e.g. ``"pinot noir"``, ``"bordeaux"``).
        """
        return self._get("/api/search/", q=query)

    def glossary_term(self, slug: str) -> dict[str, Any]:
        """Get a glossary term by slug.

        Args:
            slug: Term slug (e.g. ``"terroir"``, ``"malolactic-fermentation"``).
        """
        return self._get(f"/api/term/{slug}/")

    # -- Context manager -------------------------------------------------------

    def close(self) -> None:
        """Close the underlying HTTP connection."""
        self._client.close()

    def __enter__(self) -> VinoFYI:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
