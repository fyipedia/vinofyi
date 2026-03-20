"""HTTP API client for vinofyi.com REST endpoints.

Requires the ``api`` extra: ``pip install vinofyi[api]``

Usage::

    from vinofyi.api import VinoFYI

    with VinoFYI() as api:
        items = api.list_countries()
        detail = api.get_country("example-slug")
        results = api.search("query")
"""

from __future__ import annotations

from typing import Any

import httpx


class VinoFYI:
    """API client for the vinofyi.com REST API.

    Provides typed access to all vinofyi.com endpoints including
    list, detail, and search operations.

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

    def _get(self, path: str, **params: Any) -> dict[str, Any]:
        resp = self._client.get(
            path,
            params={k: v for k, v in params.items() if v is not None},
        )
        resp.raise_for_status()
        result: dict[str, Any] = resp.json()
        return result

    # -- Endpoints -----------------------------------------------------------

    def list_countries(self, **params: Any) -> dict[str, Any]:
        """List all countries."""
        return self._get("/api/v1/countries/", **params)

    def get_country(self, slug: str) -> dict[str, Any]:
        """Get country by slug."""
        return self._get(f"/api/v1/countries/" + slug + "/")

    def list_faqs(self, **params: Any) -> dict[str, Any]:
        """List all faqs."""
        return self._get("/api/v1/faqs/", **params)

    def get_faq(self, slug: str) -> dict[str, Any]:
        """Get faq by slug."""
        return self._get(f"/api/v1/faqs/" + slug + "/")

    def list_faults(self, **params: Any) -> dict[str, Any]:
        """List all faults."""
        return self._get("/api/v1/faults/", **params)

    def get_fault(self, slug: str) -> dict[str, Any]:
        """Get fault by slug."""
        return self._get(f"/api/v1/faults/" + slug + "/")

    def list_flavors(self, **params: Any) -> dict[str, Any]:
        """List all flavors."""
        return self._get("/api/v1/flavors/", **params)

    def get_flavor(self, slug: str) -> dict[str, Any]:
        """Get flavor by slug."""
        return self._get(f"/api/v1/flavors/" + slug + "/")

    def list_foods(self, **params: Any) -> dict[str, Any]:
        """List all foods."""
        return self._get("/api/v1/foods/", **params)

    def get_food(self, slug: str) -> dict[str, Any]:
        """Get food by slug."""
        return self._get(f"/api/v1/foods/" + slug + "/")

    def list_glossary(self, **params: Any) -> dict[str, Any]:
        """List all glossary."""
        return self._get("/api/v1/glossary/", **params)

    def get_term(self, slug: str) -> dict[str, Any]:
        """Get term by slug."""
        return self._get(f"/api/v1/glossary/" + slug + "/")

    def list_grapes(self, **params: Any) -> dict[str, Any]:
        """List all grapes."""
        return self._get("/api/v1/grapes/", **params)

    def get_grape(self, slug: str) -> dict[str, Any]:
        """Get grape by slug."""
        return self._get(f"/api/v1/grapes/" + slug + "/")

    def list_guides(self, **params: Any) -> dict[str, Any]:
        """List all guides."""
        return self._get("/api/v1/guides/", **params)

    def get_guide(self, slug: str) -> dict[str, Any]:
        """Get guide by slug."""
        return self._get(f"/api/v1/guides/" + slug + "/")

    def list_methods(self, **params: Any) -> dict[str, Any]:
        """List all methods."""
        return self._get("/api/v1/methods/", **params)

    def get_method(self, slug: str) -> dict[str, Any]:
        """Get method by slug."""
        return self._get(f"/api/v1/methods/" + slug + "/")

    def list_regions(self, **params: Any) -> dict[str, Any]:
        """List all regions."""
        return self._get("/api/v1/regions/", **params)

    def get_region(self, slug: str) -> dict[str, Any]:
        """Get region by slug."""
        return self._get(f"/api/v1/regions/" + slug + "/")

    def list_styles(self, **params: Any) -> dict[str, Any]:
        """List all styles."""
        return self._get("/api/v1/styles/", **params)

    def get_style(self, slug: str) -> dict[str, Any]:
        """Get style by slug."""
        return self._get(f"/api/v1/styles/" + slug + "/")

    def list_wineries(self, **params: Any) -> dict[str, Any]:
        """List all wineries."""
        return self._get("/api/v1/wineries/", **params)

    def get_winery(self, slug: str) -> dict[str, Any]:
        """Get winery by slug."""
        return self._get(f"/api/v1/wineries/" + slug + "/")

    def list_wines(self, **params: Any) -> dict[str, Any]:
        """List all wines."""
        return self._get("/api/v1/wines/", **params)

    def get_wine(self, slug: str) -> dict[str, Any]:
        """Get wine by slug."""
        return self._get(f"/api/v1/wines/" + slug + "/")

    def search(self, query: str, **params: Any) -> dict[str, Any]:
        """Search across all content."""
        return self._get(f"/api/v1/search/", q=query, **params)

    # -- Lifecycle -----------------------------------------------------------

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> VinoFYI:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
