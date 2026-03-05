"""vinofyi — Wine knowledge API client for developers.

Search wines, grapes, regions, and wine terminology from VinoFYI.

Usage::

    from vinofyi.api import VinoFYI

    with VinoFYI() as api:
        results = api.search("pinot noir")
        print(results)
"""

__version__ = "0.1.0"
