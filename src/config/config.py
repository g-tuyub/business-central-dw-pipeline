import os
from dataclasses import dataclass
from typing import Optional
from pathlib import Path
from dotenv import load_dotenv
from config.config_block import ConfigBlock


@dataclass
class APIConfig:

    tenant_id : str
    client_id : str
    client_secret : str
    company_id : str
    environment : str

    publisher : str
    group : str
    version : str

    @property
    def base_url(self) -> str:
        return f"https://api.businesscentral.dynamics.com/v2.0/{self.environment}/api/{self.publisher}/{self.group}/{self.version}/"

    @property
    def authority(self) -> str:
        return f"https://login.microsoftonline.com/{self.tenant_id}"

@dataclass
class DBConfig:

    username : str
    password : str
    host : str
    database : str
    port : int = 1433

    @property
    def connection_string(self) -> str:
        return f"mssql+pyodbc://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}?driver=ODBC+Driver+17+for+SQL+Server"



@dataclass
class Config:

    api : APIConfig
    db : DBConfig

    @classmethod
    def from_env(cls, env_path : Optional[Path], override : bool = False) -> 'Config':

        load_dotenv(dotenv_path=env_path,override=override)

        api_config = APIConfig(
            tenant_id =os.getenv("TENANT_ID"),
            client_id = os.getenv("CLIENT_ID"),
            client_secret = os.getenv("CLIENT_SECRET"),
            company_id = os.getenv("COMPANY_ID"),
            environment = os.getenv("ENVIRONMENT"),
            publisher = os.getenv("PUBLISHER"),
            group = os.getenv("GROUP"),
            version = os.getenv("VERSION"),
        )

        db_config = DBConfig(
            username =os.getenv('DATABASE_USERNAME'),
            password =os.getenv('DATABASE_PASSWORD'),
            host =os.getenv('DATABASE_HOST'),
            database =os.getenv('DATABASE'),
            port =int(os.getenv('DATABASE_PORT') or 1433),
        )

        return cls(api=api_config, db=db_config)

    @classmethod
    def from_prefect_block(cls, block_name : str) -> 'Config':

        block = ConfigBlock.load(block_name)

        api_config = APIConfig(
            tenant_id = block.tenant_id.get_secret_value(),
            client_id = block.client_id,
            client_secret = block.client_secret,
            company_id = block.company_id,
            environment = block.environment,
            publisher = block.api_publisher,
            group = block.api_group,
            version = block.api_version,
        )

        db_config = DBConfig(
            username = block.db_username,
            password = block.db_password,
            host = block.db_host,
            database = block.db_name,
            port = block.db_port,
        )

        return cls(api=api_config, db=db_config)
