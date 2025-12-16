import typer

from bcsync.cli.commands import deploy_db
from bcsync.cli.commands import sync

app = typer.Typer(
    name="bcsync",
    help="Motor de sincronización Business Central → SQL Server"
)

app.add_typer(deploy_db.app, name="deploy-db")
app.add_typer(sync.app, name="sync")

def main():
    app()

if __name__ == "__main__":
    main()