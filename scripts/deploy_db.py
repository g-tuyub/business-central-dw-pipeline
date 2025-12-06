from bcsync.db.engine import create_engine
from bcsync.config.config import  Config
from bcsync.db.models.base import Base
from bcsync.db.models import staging, core
import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def deploy_db() -> None:
    try:
        config = Config.from_env()
        engine = create_engine(config.db.connection_string)
        logger.info(f"Connected to {config.db.connection_string}")

        Base.metadata.create_all(engine)

        logger.info(f"SUCCESFUL db deployment!")

    except Exception as e:
        logger.error(f"FAILED db deployment!, error : {e}")
        sys.exit(1)


if __name__ == "__main__":
    deploy_db()