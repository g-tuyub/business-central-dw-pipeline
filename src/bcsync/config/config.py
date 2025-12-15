from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, SecretStr
from typing import Optional, TYPE_CHECKING
from sqlalchemy.engine import URL
from dotenv import load_dotenv

load_dotenv()

if TYPE_CHECKING:
    from bcsync.config.config_block import ConfigBlock


class APIConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="API_", env_file=".env", extra='ignore')

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
        return f"https://api.businesscentral.dynamics.com/v2.0/{self.environment}/api/{self.publisher}/{self.group}/{self.version}/companies({self.company_id})"

    @property
    def authority(self) -> str:
        return f"https://login.microsoftonline.com/{self.tenant_id}"

class DBConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='DB_', env_file='.env', extra='ignore')

    host : str
    database : str
    port : int = 1433
    username : Optional[str] = None
    password : Optional[SecretStr] = None
    driver : Optional[str] = "ODBC Driver 17 for SQL Server"
    trusted_connection : Optional[bool] = False

    @property
    def connection_string(self) -> URL:
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
                password=self.password.get_secret_value(),
                host=self.host,
                port=self.port,
                database=self.database,
                query=query_params
            )

class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    api : APIConfig = Field(default_factory=APIConfig)
    db : DBConfig = Field(default_factory=DBConfig)

    @classmethod
    def from_prefect_block(cls, block_name : str) -> 'Config':
        from bcsync.config.config_block import ConfigBlock

        block = ConfigBlock.load(block_name)

        api_config = APIConfig(
            tenant_id = block.tenant_id,
            client_id = block.client_id,
            client_secret = block.client_secret.get_secret_value(),
            company_id = block.company_id,
            environment = block.environment,
            publisher = block.api_publisher,
            group = block.api_group,
            version = block.api_version,
        )

        db_config = DBConfig(
            username = block.db_username,
            password = block.db_password.get_secret_value(),
            host = block.db_host,
            database = block.db_name,
            port = block.db_port,
        )

        return cls(api=api_config, db=db_config)
