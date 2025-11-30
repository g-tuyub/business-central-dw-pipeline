import os
from pathlib import Path
from sqlalchemy import text
from src.db.engine import create_engine
from src.db.models.base import Base
from src.db.models import core, staging
from src.db.engine import create_engine
from src.config.config import Config


def deploy_db() -> None:
    config = Config.from_env()
    engine = create_engine(config.db.connection_string)
