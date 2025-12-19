# ¿Cómo agregar una entidad al motor de sincronización?

Esta guía detalla los pasos para incorporar una nueva entidad de negocio (ej. Usuarios, Almacenes, Proyectos) al pipeline de sincronización.

---

## Estructura de la URL de la API

La **URL** de **API** personalizada de **Business Central** tiene la siguiente estructura:

> [https://api.businesscentral.dynamics.com/v2.0/{entorno}/api/{publisher}/{grupo}/{version}/companies({id_empresa})/entitySet](https://api.businesscentral.dynamics.com/v2.0/{entorno}/api/{publisher}/{grupo}/{version}/companies%28{id_empresa}%29/entitySet)

Los parámetros *publisher*, *group* y *version* se definen dentro del objeto **AL** que define un endpoint específico.

En el caso particular de la [extensión](https://dev.azure.com/dkt-devops/business-central-datawarehouse-api-ext) para sincronizar el **Data Warehouse**, se espera que los endpoints tengan esta estructura:

> [https://api.businesscentral.dynamics.com/v2.0/{entorno}/api/dkt/sql/beta/companies({id_empresa})/entitySet](https://api.businesscentral.dynamics.com/v2.0/{entorno}/api/dkt/sql/beta/companies%28{id_empresa}%29/entitySet)

El **entitySet** hace referencia al endpoint que se está consultando, por ejemplo:

* El entitySet de Clientes es `customers`
* El entitySet de Líneas de facturas de venta es `salesInvoiceLines`

Siguiendo esta convención del código **AL**, si agregamos una tabla al **Data Warehouse** que representa un *entitySet* específico de la **API**, diremos que estamos agregando una nueva **entidad**.

---

## Proceso para agregar una nueva entidad

### 1. Crear el endpoint en Business Central

Crea el *endpoint* correspondiente a la entidad.

Por ejemplo, si se añade una entidad llamada **usuarios**, el endpoint sería:

> [https://api.businesscentral.dynamics.com/v2.0/{entorno}/api/dkt/sql/beta/companies({id_empresa})/users](https://api.businesscentral.dynamics.com/v2.0/{entorno}/api/dkt/sql/beta/companies%28{id_empresa}%29/users)

> Consulta el repositorio de la extensión [aquí](https://dev.azure.com/dkt-devops/business-central-datawarehouse-api-ext) para ver las instrucciones detalladas de cómo agregar nuevos endpoints.

---

### 2. Agregar los componentes en `bcsync`

Una vez confirmada la existencia del endpoint, se deben añadir los siguientes elementos al paquete `bcsync`, respetando la estructura y convenciones existentes:

* **Modelo validador de la API**

  Dentro del módulo `bcsync/api/schemas`, crea una clase que herede de `bcsync.api.schemas.base.BCEntityBase`, con el mapeo correcto de los tipos de datos del *JSON* a tipos de *Python*:

  ```python
  class User(BCEntityBase):
      code: str = Field(alias="code")
      name: BCString = Field(alias="description")
  ```

* **Modelo ORM de staging**

  Dentro del módulo `bcsync/db/models/staging`, crea una clase que herede de `bcsync.db.models.base.StagingBase`, que representará la tabla SQL `staging.user`:

  ```python
  class User(StagingBase):
      __tablename__ = "user"

      code: Mapped[str] = mapped_column(String(10), nullable=False)
      name: Mapped[str] = mapped_column(String(100), nullable=True)
  ```

* **Modelo ORM de core**

  Dentro del módulo `bcsync/db/models/core`, crea una clase que herede de `bcsync.db.models.base.CoreBase`, que representará la tabla SQL `core.user`:

  ```python
  class User(CoreBase):
      __tablename__ = "user"

      code: Mapped[str] = mapped_column(String(10), nullable=False)
      name: Mapped[str] = mapped_column(String(100), nullable=True)
  ```

---

### 3. Crear las plantillas SQL

Crea los siguientes elementos en el directorio `sql/procedures/`:

* Un *stored procedure* de carga a la capa **core** (*loader*) que contenga la lógica de transformación (*merge*) de los registros de *staging* a *core*.
* Un *stored procedure* de limpieza (*fixer*) para resolver dimensiones de llegada tardía, en caso de que la entidad tenga dependencias con otras entidades.

> Los procedimientos contienen la misma lógica de transformación para todas las entidades. Utiliza las plantillas existentes en `sql/procedures/loaders` y `sql/procedures/fixers` como referencia.

---

### 4. Crear vistas semánticas

Crea los objetos *view* que definen la capa **semantic** del **Data Warehouse**, dentro del directorio:

```
sql/views/
```

---

### 5. Registrar la entidad en el motor de sincronización

Crea un objeto que herede de `bcsync.core.types.EntitySyncConfig` asociado a la nueva entidad:

```python
EntitySyncConfig(
    endpoint="users",
    validator_model=schemas.User,
    staging_model=staging.User,
    core_model=core.User,
)
```

> `EntitySyncConfig` es el punto de unión entre la **API**, los modelos **ORM** y la lógica **SQL** del motor de sincronización.

> Mantén la convención de nombres de las propiedades de `EntitySyncConfig` al crear las plantillas **SQL** para permitir su descubrimiento automático.

---

### 6. Actualizar el enum de entidades

Agrega la nueva entidad al enum `bcsync.core.types.BCEntity`:

```python
class BCEntity(str, Enum):
    CUSTOMER = "customer"
    ITEM = "item"
    USER = "user"  # Nuevo registro
```

---

### 7. Registrar la entidad

Registra la entidad en `bcsync.core.registry.SYNC_TARGETS`:

```python
SYNC_TARGETS = {
    BCEntity.USER: EntitySyncConfig(
        endpoint="users",
        validator_model=schemas.User,
        staging_model=staging.User,
        core_model=core.User,
    )
}
```

---

### 8. Desplegar el esquema de base de datos

Actualiza el esquema de la base de datos para reflejar la nueva entidad ejecutando:

```bash
bcsync deploy-db
```

Al completar estos pasos, la entidad quedará registrada automáticamente tanto en la **CLI** como en los flujos de **Prefect**.

> No es necesario modificar los flujos de Prefect al agregar una nueva entidad. El motor de sincronización descubre automáticamente las entidades registradas.

---

## Checklist de entidad

Antes de ejecutar el flujo de sincronización, verifica que se hayan completado los siguientes pasos:

* [ ] Endpoint disponible en Business Central
* [ ] modelo de validación API creado (`bcsync/api/schemas`)
* [ ] Modelo ORM de staging creado (`bcsync/db/models/staging`)
* [ ] Modelo ORM de core creado (`bcsync/db/models/core`)
* [ ] Stored procedure *loader* creado
* [ ] Stored procedure *fixer* creado (si aplica)
* [ ] Vistas semánticas creadas
* [ ] `EntitySyncConfig` registrado
* [ ] Enum `BCEntity` actualizado
* [ ] Registry `SYNC_TARGETS` actualizado
* [ ] Esquema de base de datos desplegado (`bcsync deploy-db`)

---

## Ejecución inicial

Para realizar una carga inicial de la entidad, puedes ejecutar el siguiente comando:

```bash
bcsync sync user
```
