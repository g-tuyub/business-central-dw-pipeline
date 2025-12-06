import logging
import requests
import urllib.parse
from typing import Generator, List, Dict, Any
from datetime import datetime
from msal import ConfidentialClientApplication
from bcsync.config.config import APIConfig

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BusinessCentralClient:
    def __init__(self, config: APIConfig) -> None:
        self.config = config
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
        self.base_url = self.config.base_url
        self.company_id = self.config.company_id
        self.authority = self.config.authority
        self.scopes = ["https://api.businesscentral.dynamics.com/.default"]
        self.access_token = None
        self._refresh_token()

    def _refresh_token(self):

        try:
            app = ConfidentialClientApplication(
                client_id=self.config.client_id,
                client_credential=self.config.client_secret,
                authority=self.config.authority,
            )

            result = app.acquire_token_for_client(self.scopes)

            if "access_token" in result:
                self.access_token = result["access_token"]
                self.session.headers.update({
                    "Authorization": f"Bearer {self.access_token}"
                })
            else:
                error_description = result.get("error_description")
                raise Exception(f"Error al obtener token : {error_description}")

        except Exception as e:
            logger.error(f"Error de autenticacion con la API de BC : {e}")
            raise

    def _make_request(self, method: str, url: str, params=None, data=None) -> requests.Response:

        parsed = urllib.parse.urlparse(url)

        if parsed.scheme:
            full_url = url
        else:
            full_url = urllib.parse.urljoin(self.base_url, url)

        try:
            response = self.session.request(method, full_url, params=params, json=data)

            if response.status_code == 401:
                logger.warning("Token expirado (401). Renovando...")
                self._refresh_token()
                response = self.session.request(method, full_url, params=params, json=data)

            response.raise_for_status()
            return response

        except Exception as e:
            logger.error(f"Error al hacer request a URL : {full_url}: {e}")
            raise

    @staticmethod
    def create_query_parameters(
            last_created_at: datetime = None,
            last_modified_at: datetime = None,
            order_by: str = None,
            select: List[str] = None,
            offset: int = None,
            top: int = None,
            custom_filter: str = None
    ) -> Dict[str, str]:

        params = {"$schemaversion": "1.0"}
        filters = []

        fmt = '%Y-%m-%dT%H:%M:%S.%fZ'

        if last_created_at:
            filters.append(f"systemCreatedAt gt {last_created_at.strftime(fmt)}")

        if last_modified_at:
            filters.append(f"systemModifiedAt gt {last_modified_at.strftime(fmt)}")

        if custom_filter:
            filters.append(custom_filter)

        if filters:
            params["$filter"] = " and ".join(filters)

        if order_by:
            params["$orderby"] = order_by

        if select:
            params["$select"] = ",".join(select)

        if offset:
            params["$skip"] = str(offset)

        if top:
            params["$top"] = str(top)

        return params

    def _get_pages(self, endpoint: str, params: dict = None) -> Generator[List[Dict[str, Any]], None, None]:

        url = endpoint
        current_params = params
        page_counter = 0

        while url:
            page_counter += 1
            logger.info(f"Descargando página {page_counter} de '{endpoint}'...")

            response = self._make_request("GET", url, params=current_params)
            data = response.json()
            items = data.get("value", [])
            if items:
                yield items
            else:
                break

            url = data.get("@odata.nextLink")
            current_params = None

    def iter_records(self, endpoint: str, **kwargs) -> Generator[Dict[str, Any], None, None]:

        params = self.create_query_parameters(**kwargs)

        for page in self._get_pages(endpoint, params):
            for record in page:
                record['companyId'] = str(self.company_id)
                yield record

    def iter_pages(self, endpoint: str, **kwargs) -> Generator[List[Dict[str, Any]], None, None]:

        params = self.create_query_parameters(**kwargs)

        for page in self._get_pages(endpoint, params):
            for record in page:
                record['companyId'] = str(self.company_id)

            yield page
