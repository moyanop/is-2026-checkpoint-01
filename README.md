# TeamBoard App

## Integrantes del equipo

| Nombre                          | Legajo | Feature    | Servicio                       |
| ------------------------------- | ------ | ---------- | ------------------------------ |
| Moyano Amaya, Pedro             | 31411  | Feature 01 | Coordinación e Infraestructura |
| Reale Bortone, Milagros Ailen   | 32856  | Feature 02 | Frontend                       |
| Jiménez, Franco                 | 31848  | Feature 03 | Backend                        |
| Portillo Colinas, Franco Javier | 31089  | Feature 04 | Base de Datos                  |
| Calvo, Bautista                 | 32156  | Feature 05 | Panel Portainer                |

Stack

- Frontend: HTML, JavaScript y CSS estáticos, servidos con `http.server` de Python.
- Backend: Flask sobre Gunicorn, Python 3.12.
- Base de datos: PostgreSQL 16 (Alpine).
- Orquestación: Docker Compose.
- Administración: Portainer CE.

Requisitos

- Docker 24 o superior.
- Docker Compose v2.
- Puertos libres en el host: 5000, 8080 y 9000.
  Configuración
  Las credenciales de Postgres se leen desde un archivo `.env` en la raíz del repositorio. Ese archivo no se versiona. Antes del primer arranque, crearlo con el siguiente contenido:

```env
POSTGRES_HOST=database
POSTGRES_PORT=5432
POSTGRES_DB=teamboard
POSTGRES_USER=teamboard
POSTGRES_PASSWORD=cambiar
```

`POSTGRES_HOST=database` apunta al nombre del servicio definido en `docker-compose.yml`, no al hostname del equipo donde se ejecuta Docker.
Levantar el entorno

```sh
docker compose up -d --build
```

Servicios disponibles:
Frontend: http://localhost:8080
Backend: http://localhost:5000
Portainer: http://localhost:9000
Para detener los contenedores manteniendo los datos:

```sh
docker compose down
```

Para detener y eliminar también los volúmenes (borra el contenido de la base):

```sh
docker compose down -v
```

Endpoints del backend
`GET /api/health` — estado del servicio.
`GET /api/info` — nombre, versión y lista de endpoints.
`GET /api/team` — lista de integrantes leídos desde la tabla `members`.
Base de datos
La tabla `members` se crea y se siembra al primer arranque del contenedor de Postgres a partir de `database/init.sql`. El script solo se ejecuta cuando el datadir está vacío; si se modifica el SQL después del primer `up`, hace falta `docker compose down -v` para que vuelva a aplicarse.

```sql
CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    legajo VARCHAR(20) NOT NULL,
    feature VARCHAR(50) NOT NULL,
    servicio VARCHAR(50) NOT NULL,
    estado VARCHAR(20) NOT NULL
);
```

Comandos útiles

```sh
docker compose logs -f backend
docker compose ps
docker compose exec database psql -U "$POSTGRES_USER" -d "$POSTGRES_DB"
docker compose config > /dev/null
```
