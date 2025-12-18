import typer
from bcsync.core.types import BCEntity
from bcsync.config.config import Config
from bcsync.flows import sync_entities
from typing import Optional, List

app = typer.Typer(help="Ejecuta sincronizaciones de entidades de Business Central que se encuentran registradas.",
                  invoke_without_command=True)

@app.callback()
def sync(
    entities: List[BCEntity] = typer.Argument(
        None,
        help="Entidades a sincronizar (ej: customer item vendor)"
    ),
    all_entities: bool = typer.Option(
        False,
        "--all",
        help="Sincroniza todas las entidades disponibles"
    ),
):
    """
    Ejecuta la sincronización de una o más entidades.
    """

    if all_entities:
        entities = None
    elif not entities:
        typer.echo("Debes especificar al menos una entidad o usar --all")
        raise typer.Exit(code=1)

    sync_entities(entities_to_sync=entities)