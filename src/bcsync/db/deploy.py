import logging
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from sqlalchemy import text
from bcsync.db.constants import SQL_CONTEXT
from bcsync.db.models.base import Base
from bcsync.db.events import register_all_listeners
from bcsync.db.engine import get_engine
from bcsync.config.config import Config
from bcsync.db.models import staging, core

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
TEMPLATES_DIR = PROJECT_ROOT / "sql" / "templates"
PROCEDURES_DIR = TEMPLATES_DIR / "procedures"
logger = logging.getLogger(__name__)


def create_tables_and_schema(engine):
    logger.info('Creating tables and schema.')
    register_all_listeners(Base.metadata)
    Base.metadata.create_all(engine)
    logger.info(f'Successfully created tables and schema.')


def deploy_procedures(engine):
    if not TEMPLATES_DIR.exists():
        logger.error(f"Template directory at {TEMPLATES_DIR} is required to exist")
        raise FileNotFoundError('Could not find SQL_TEMPLATES_DIR')
    files = sorted(PROCEDURES_DIR.rglob('*.sql.j2'))
    if not files:
        logger.info(f'No procedures will be created since {PROCEDURES_DIR} is empty')
        return

    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)))

    with engine.begin() as conn:
        for file_path in files:
            relative_path = file_path.relative_to(TEMPLATES_DIR).as_posix()

            try:
                template = env.get_template(relative_path)
                sql_text = template.render(**SQL_CONTEXT).replace('GO', '')

                conn.execute(text(sql_text))
                logger.info(f'Successfully created procedure {file_path.name}.')

            except Exception as e:
                logger.error(f'Failed to create procedure {relative_path}. Error: {e}')
                raise e


def deploy_db()-> None:
    config = Config()
    engine = get_engine(config.db.connection_string)
    create_tables_and_schema(engine)
    deploy_procedures(engine)
