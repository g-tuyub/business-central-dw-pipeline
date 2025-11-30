import os
from dataclasses import dataclass
from typing import Optional
from pathlib import Path
from dotenv import load_dotenv
from bcsync.config.config_block import ConfigBlock
from sqlalchemy.engine import URL

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

    host : str
    database : str
    port : int = 1433
    username : Optional[str] = None
    password : Optional[str] = None
    driver : Optional[str] = "ODBC Driver 17 for SQL Server"
    trusted_connection : Optional[bool] = False

    @property
    def connection_string(self) -> URL:
        # Argumentos comunes
        query_params = {"driver": self.driver,
                        "TrustServerCertificate": "yes"}

        if self.trusted_connection:
            query_params["Trusted_Connection"] = "yes"

            return URL.create(
                drivername="mssql+pyodbc",
                host=self.host,
                port=self.port,
                database=self.database,
                query=query_params
            )

        else:

            return URL.create(
                drivername="mssql+pyodbc",
                username=self.username,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database,
                query=query_params
            )


@dataclass
class Config:

    api : APIConfig
    db : DBConfig

    @classmethod
    def from_env(cls, env_path : Optional[Path] = None, override : bool = False) -> 'Config':

        if env_path is None:
            load_dotenv(override=override)

        else:
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
            trusted_connection=(os.getenv('TRUSTED_CONNECTION', "0") == "1")
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
