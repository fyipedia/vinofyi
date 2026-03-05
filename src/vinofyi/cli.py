"""Command-line interface for vinofyi.

Requires the ``cli`` extra: ``pip install vinofyi[cli]``

Usage::

    vinofyi search "pinot noir"
    vinofyi term "terroir"
"""

from __future__ import annotations

import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(
    name="vinofyi",
    help="Wine knowledge API client — search wines, grapes, regions, and wine terms.",
    no_args_is_help=True,
)
console = Console()


@app.command()
def search(
    query: str = typer.Argument(help="Search term (e.g. 'pinot noir', 'bordeaux', 'tannin')"),
) -> None:
    """Search wines, grapes, regions, and glossary terms."""
    from vinofyi.api import VinoFYI

    with VinoFYI() as api:
        data = api.search(query)

    table = Table(title=f"Search: {query}")
    table.add_column("Type", style="cyan", no_wrap=True)
    table.add_column("Name")
    table.add_column("URL")

    results = data.get("results", [])
    if not results:
        console.print(f"[yellow]No results found for '{query}'[/yellow]")
        return

    for item in results:
        table.add_row(
            str(item.get("type", "")),
            str(item.get("name", "")),
            str(item.get("url", "")),
        )

    console.print(table)
    console.print(f"[dim]{len(results)} result(s)[/dim]")


@app.command()
def term(
    slug: str = typer.Argument(
        help="Glossary term slug (e.g. 'terroir', 'malolactic-fermentation')"
    ),
) -> None:
    """Look up a wine glossary term by slug."""
    from vinofyi.api import VinoFYI

    with VinoFYI() as api:
        data = api.glossary_term(slug)

    table = Table(title=f"Term: {slug}")
    table.add_column("Property", style="cyan", no_wrap=True)
    table.add_column("Value")

    table.add_row("Name", str(data.get("name", "")))
    table.add_row("Slug", str(data.get("slug", slug)))
    table.add_row("Definition", str(data.get("definition", "")))

    if data.get("category"):
        table.add_row("Category", str(data["category"]))
    if data.get("related_terms"):
        table.add_row("Related", ", ".join(str(t) for t in data["related_terms"]))

    console.print(table)


if __name__ == "__main__":
    app()
