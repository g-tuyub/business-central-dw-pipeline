from bcsync.db.engine import create_engine
from bcsync.config.config import  Config


def deploy_db() -> None:
    config = Config.from_env()
    engine = create_engine(config.db.connection_string)
