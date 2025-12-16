# Motor de sincronización de Business Central a Data Warehouse en SQL Server
#
Solución empresarial que sincroniza datos de **Microsoft Dynamics 365 Business Central** a un **Data Warehouse** multiempresa
implementado en **SQL Server**.

La solución incluye:

- Extracción incremental de datos mediante APIs avanzadas de Business Central.
- Patrón de arquitectura ELT con cargas a tablas de staging.
- Transformación y carga de datos directamente en **SQL Server** mediante stored procedures.
- Implementación de **Slowly Changing Dimensions – Type 1 (SCD1)**
- Resolución de referencias y dimensiones de llegada tardía (*late arriving dimensions*)
- Creación automática del esquema de la base de datos, incluyendo *stored procedures*, *vistas*
- Orquestación completa del pipeline mediante **Prefect 3**
- Ejecución de flujos de sincronización en contenedores **Docker**.



La solución está diseñada para ser **reproducible, extensible y automatizada**, 
cubriendo todo el ciclo de integración de datos desde el ERP en múltiples empresas, hasta el Data Warehouse.


[Diagrama de arquitectura general](docs/diagrams/architecture-diagram.png)

## *Stack* tecnológico

- **Python 3.12+**
- **Prefect 3.4.5** (orquestación de workflows)
- **SQLAlchemy** (modelado y conexión a SQL Server)
- **Pydantic** (modelos de datos y configuración)
- **Microsoft SQL Server**
- **Microsoft Dynamics 365 Business Central Custom APIs**
- **Docker** (ejecución de flujos)
- **Azure DevOps** (repositorio y CI/CD)


## ¿Cómo instalar para desarrollo local?

### 1. Prerrequisitos

#### Software y Herramientas:

* Python 3.12 o superior
* Git
* Docker Desktop (opcional para desarrollo, requerido para simular el entorno de producción)

#### Permisos y accesos:

* **Azure:** Se requiere un **App Registration** en Azure con permiso *API.ReadWrite.All* y Admin Consent otorgado.
* **Business Central:** La extensión (.app) que expone la API, debe estar instalada y activa en el entorno de Business Central.
* **SQL Server:** Usuario con permisos elevados en la base de datos, ya que se gestionan y modifican esquemas. (db_owner)
### 2. Instalación
Clona el repositorio e instala las dependencias:



```bash
git clone [https://dev.azure.com/{myorg}/{myrepo}](https://dev.azure.com/{myorg}/{myrepo})
cd myrepo
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -e .
```
### 3. Configuración
Copia el archivo .env de ejemplo: 

```bash
cp .env.example .env
```
Reemplaza las credenciales del registro de aplicación y los accesos de SQL Server:
```bash
API_CLIENT_ID=mi_id_registro_aplicacion
API_CLIENT_SECRET=mi_secreto_de_cliente
API_TENANT_ID=id_mi_tenant
API_COMPANY_ID=id_mi_empresa
API_PUBLISHER=publicante_api
API_GROUP=grupo_api
API_VERSION=version_api
API_ENVIRONMENT=mi_entorno_de_bc
DB_TRUSTED_CONNECTION=0 # Usar 1 para Windows Auth, 0 para SQL Auth
DB_HOST=server_ip
DB_DATABASE=nombre_base_de_datos
DB_USERNAME=mi_usuario
DB_PASSWORD=mi_contraseña
```
### 4. Preparación Base de datos

#### Entorno Local o Nuevo:
Si estás levantando el proyecto desde cero en local o en un servidor nuevo, primero asegúrate de crear la base de datos nueva (debe coincidir con el nombre en tu .env):

```tsql
CREATE DATABASE mi_bd
```

Posteriormente, ejecuta el script de inicialización para crear el esquema de la base de datos:

```bash
python scripts/deploy_db.py
```

#### Entorno Existente:
Si tu archivo .env apunta a un servidor compartido donde el Data Warehouse ya está implementado, no necesitas ejecutar este paso inicial, salvo que hayas agregado nuevas tablas o modificado procedimientos y necesites aplicar los cambios.

**Nota**: El script de inicialización es idempotente. Si los objetos ya existen, verificará su estado o los actualizará sin borrar datos, aún así, se recomienda precaución en entorno productivo.

### 5. Configuración del orquestador (Prefect)

Antes de ejecutar, para visualizar los flujos tienes dos opciones:

#### Modo Servidor:

Conecta tu entorno local a un servidor de prefect ya existente.

Ejecuta en tu terminal:

```bash
prefect config set PREFECT_API_URL=http://localhost:4200/api
```
Si utilizas un servidor remoto, reemplaza localhost por la IP o dominio correspondiente.

#### Modo Efímero:
Si no tienes el servidor de Prefect corriendo, puedes ejecutar los flujos en modo "offline", sin necesidad de configurar el orquestador.

### 6. Ejecución:
Una vez asegurada la conexión a SQL, la existencia del esquema y la configuración del orquestador, para confirmar el funcionamiento del motor de sincronización sin
ejecutar una carga masiva, ejecuta el siguiente script de verificación:

```bash
python scripts/run_customer_sync.py
```
Este script ejecuta una sincronización de la tabla: customer.

Si este flujo se ejecuta con éxito, confirma que:

* La extensión de Business Central está correctamente instalada en tu entorno.
* Tu conexión a la API de Business Central esta correctamente configurada.
* Tu usuario de SQL Server tiene los permisos adecuados en la BD.
* El esquema de la BD se creó y funciona correctamente.

Ya puedes proceder a ejecutar o desplegar flujos completos desde tu entorno.