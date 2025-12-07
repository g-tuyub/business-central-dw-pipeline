import logging
from bcsync.config.config import Config
from bcsync.db.deploy import create_tables_and_schema, deploy_procedures
from bcsync.db.engine import get_engine

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
    datefmt='%H:%M:%S'
)


def main()-> None:
    config = Config.from_env()
    engine = get_engine(config.db.connection_string)
    create_tables_and_schema(engine)
    deploy_procedures(engine)


if __name__ == '__main__':
    main()
