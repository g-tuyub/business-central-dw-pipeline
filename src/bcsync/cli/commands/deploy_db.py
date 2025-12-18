import typer
from bcsync.config.config import Config
from bcsync.db.deploy import deploy_db
from bcsync.db.engine import get_engine

app = typer.Typer(help="Inicializa o actualiza el esquema del Data Warehouse")

@app.callback()
def deploy():
    """
    Crea o actualiza esquemas, tablas, vistas y stored procedures.
    """
    deploy_db()
    typer.echo("Base de datos desplegada correctamente.")