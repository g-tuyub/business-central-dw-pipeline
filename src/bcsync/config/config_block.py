from prefect.blocks.core import Block
from pydantic import SecretStr

class ConfigBlock(Block):

    _block_type_name = "Business Central Pipeline Config"

    tenant_id : SecretStr
    client_id : SecretStr
    client_secret : SecretStr
    company_id : str
    environment : str

    api_publisher : str
    api_group : str
    api_version : str

    db_username : SecretStr
    db_password : SecretStr
    db_host : str
    db_port : int = 1433
    db_name : str

