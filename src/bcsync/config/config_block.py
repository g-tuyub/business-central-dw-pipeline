from prefect.blocks.core import Block
from pydantic import SecretStr, Field
from pathlib import Path
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from bcsync.config.config import Config


class ConfigBlock(Block):
    _block_type_name = "Configuración Ejecución Pipeline Business Central."

    tenant_id : str = Field(title="ID tenant",description="ID del tenant de Azure en el que se encuentra la empresa de BC.")
    client_id : str = Field(title="client ID", description="ID del registro de aplicación de Azure con los permisos para consultar la API de BC.")
    client_secret : SecretStr = Field(title="client secret", description="secreto del cliente de la aplicación de Azure.")
    company_id : str = Field(title="ID empresa BC", description="ID de la empresa de BC.")
    environment : str = Field(title="entorno BC", description="Entorno en donde se encuentra la empresa de BC.")
    api_publisher : str = Field(title="API publisher", description="parametro API publisher de la extensión instalada en BC que expone la API de sincronización.")
    api_group : str = Field(title="API group", description="parametro API group de la extensión instalada en BC que expone la API.")
    api_version : str = Field(title="API version", description="versión de la API.")
    db_username : str = Field(title="Usuario SQL Server")
    db_password : Optional[SecretStr] = Field(title="Contraseña SQL Server")
    db_host : str = Field(title = "Host BD", description="Dirección del servidor en donde se encuentra alojada la BD.")
    db_port : int = Field(title="Puerto BD", description="Puerto de la BD, para SQL Server tradicionalmente es : 1433.")
    db_name : str = Field(title="Nombre BD")

    @classmethod
    def from_config(cls, config : "Config") -> 'ConfigBlock':
        return cls(
            tenant_id = config.api.tenant_id,
            client_id = config.api.client_id,
            client_secret = SecretStr(config.api.client_secret),
            company_id = config.api.company_id,
            environment = config.api.environment,
            api_publisher = config.api.publisher,
            api_group = config.api.group,
            api_version = config.api.version,
            db_username = config.db.username,
            db_password = config.db.password,
            db_host = config.db.host,
            db_port = config.db.port,
            db_name = config.db.database
        )

