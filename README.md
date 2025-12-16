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
Clona el repositorio e instala el proyecto en modo desarrollo:
```bash
git clone <url-repositorio>
cd <nombre-repositorio>
python -m venv .venv
source .venv/bin/activate   # Linux / Mac
# .venv\Scripts\activate    # Windows
pip install -e .
```
### 3. Configuración
Copia el archivo .env.example a .env y reemplaza los valores con las credenciales correspondientes a tu entorno:

```bash
cp .env.example .env
```
### 4. Preparación Base de datos

#### Entorno Local o Nuevo:
Si estás levantando el proyecto desde cero en local o en un servidor nuevo, primero asegúrate de crear la base de datos nueva (debe coincidir con el nombre en tu .env):

```tsql
CREATE DATABASE example_db
```

Posteriormente, ejecuta el comando de inicialización para crear el esquema de la base de datos:

```bash
bcsync deploy-db
```

#### Entorno Existente:
Si tu archivo .env apunta a un servidor compartido donde el Data Warehouse ya está implementado, no necesitas ejecutar este paso inicial, salvo que hayas agregado nuevas tablas o modificado procedimientos y necesites aplicar los cambios.

**Nota**: El script de inicialización es idempotente. Si los objetos ya existen, verificará su estado o los actualizará sin borrar datos, aún así, se recomienda precaución en entorno productivo.

### 5. Ejecución:

Si deseas visualizar y monitorear las ejecuciones en un servidor de Prefect ya existente, configura la URL de la API:
```bash
prefect config set PREFECT_API_URL=http://localhost:4200/api
```
Si utilizas un servidor remoto, reemplaza localhost por la IP o dominio correspondiente.

Si no se configura esta variable, los flujos se ejecutarán en modo efímero.

Una vez asegurada la conexión a SQL Server y la existencia del esquema, puedes ejecutar una sincronización de prueba con el siguiente comando:

```bash
bcsync sync customer
```
Este comando ejecuta una sincronización de la tabla: customer.

Si la ejecución finaliza correctamente, confirma que el entorno está correctamente configurado y que el motor está listo para ejecutar sincronizaciones completas o programadas.