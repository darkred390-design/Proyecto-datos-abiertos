# Sistema Web de Consulta y Análisis de Datos de Calidad del Agua

## 1. Integrantes del grupo

**Integrantes:**

1. Vicente Ortega
2. Jafet Villarreal


**Asignatura:** Desarrollo de Aplicaciones con Acceso a Datos

## 2. Descripción del proyecto

Este proyecto consiste en el desarrollo de una aplicación web que permite consultar y analizar información relacionada con la calidad del agua, obtenida desde un conjunto de datos abiertos publicado en el portal de datos.gov.co.

La aplicación utiliza Python para consumir una API REST, almacenar la información en una base de datos SQL Server y presentar los registros mediante una interfaz web desarrollada con Flask, HTML y CSS.

## 3. Objetivo general

Desarrollar un sistema web que permita consultar, almacenar y visualizar datos relacionados con la calidad del agua, utilizando una API de datos abiertos y una base de datos relacional.

## 4. Tecnologías utilizadas

- Python.
- Flask.
- SQL Server.
- SQL Server Management Studio (SSMS).
- API REST de datos.gov.co.
- HTML.
- CSS.
- Requests.
- PyODBC.
- Python-dotenv.

## 5. Fuente de datos

Los datos utilizados provienen del conjunto de datos **CALIDAD DEL AGUA**, publicado en el portal de datos abiertos del Gobierno de Colombia.

- Portal: https://www.datos.gov.co/
- Recurso de datos: `jq38-dwmj`
- API: https://www.datos.gov.co/resource/jq38-dwmj.json

La información contiene registros relacionados con muestras de calidad del agua.

## 6. Funcionamiento del sistema

El funcionamiento se desarrolla mediante los siguientes pasos:

1. Python realiza una solicitud a la API REST de datos.gov.co.
2. La aplicación recibe los registros en formato JSON.
3. Los datos son procesados y almacenados en SQL Server.
4. Se evita insertar registros duplicados mediante una identificación única.
5. Flask consulta la información almacenada en la base de datos.
6. Los registros y estadísticas se presentan en una interfaz web.

## 7. Funcionalidades

- Consulta de datos desde una API REST.
- Sincronización de registros con SQL Server.
- Almacenamiento de información evitando duplicados.
- Consulta de registros almacenados.
- Búsqueda por código o tipo de muestra.
- Visualización de estadísticas generales.
- Cálculo de valores mínimos, máximos y promedios de los indicadores.
- Interfaz web para consultar la información.

## 8. Arquitectura del proyecto

El proyecto utiliza una organización basada en el patrón MVC (Modelo-Vista-Controlador).

- **Modelo:** administra la conexión con SQL Server, el almacenamiento, las consultas y las estadísticas.
- **Vista:** presenta la información mediante archivos HTML y CSS.
- **Controlador:** administra las rutas y coordina las operaciones de la aplicación mediante Flask.

## 9. Estructura de carpetas

```text
proyecto_datos_abiertos/
│
├── api/
│   ├── __init__.py
│   └── api_client.py
│
├── models/
│   ├── __init__.py
│   └── datos_model.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── estilos.css
│
├── evidencias/
│
├── app.py
├── database.sql
├── requirements.txt
├── .env.example
└── README.md
```

## 10. Requisitos para ejecutar el proyecto

Para ejecutar la aplicación en otro equipo se necesita:

- Python 3 instalado.
- Microsoft SQL Server.
- SQL Server Management Studio (SSMS), para ejecutar el script de la base de datos.
- Microsoft ODBC Driver 18 for SQL Server.
- Visual Studio Code (opcional, para editar el proyecto).

## 11. Configuración e instalación

### Paso 1. Crear la base de datos

Abrir SQL Server Management Studio y ejecutar el archivo `database.sql`.

Este script crea la base de datos `DatosAbiertosDB` y la tabla `RegistrosAPI` si todavía no existen.

### Paso 2. Configurar la conexión

Copiar el archivo `.env.example` y crear una copia con el nombre `.env`.

Editar los datos de conexión para que correspondan al servidor SQL Server del equipo donde se ejecutará el proyecto.

### Paso 3. Crear el entorno virtual

Abrir una terminal en la carpeta principal del proyecto y ejecutar:

```powershell
python -m venv venv
```

### Paso 4. Activar el entorno virtual

```powershell
.\venv\Scripts\Activate
```

### Paso 5. Instalar las dependencias

```powershell
pip install -r requirements.txt
```

### Paso 6. Ejecutar la aplicación

```powershell
python app.py
```

### Paso 7. Abrir el sistema

Abrir el navegador y acceder a:

http://127.0.0.1:5000

## 12. Sincronización de datos

Una vez iniciada la aplicación, se puede utilizar el botón de sincronización para consultar nuevos registros desde la API y almacenarlos en SQL Server.

La aplicación evita insertar nuevamente los registros que ya se encuentran almacenados.

La base de datos de una instalación nueva comienza sin registros. Estos se obtienen al realizar la sincronización desde la aplicación.

## 13. Evidencias

En la carpeta `evidencias` se incluyen capturas de pantalla que muestran:

- Consulta de información desde la API.
- Base de datos creada en SQL Server.
- Registros almacenados.
- Aplicación web funcionando.
- Búsqueda de registros.
- Sincronización de información.

## 14. Conclusión

Con el desarrollo de este proyecto pude integrar diferentes tecnologías para consultar, almacenar y visualizar información proveniente de una fuente de datos abiertos.

También pude aplicar el consumo de servicios API REST, la conexión de Python con SQL Server, la organización del código mediante el patrón MVC y la creación de una interfaz web para facilitar la consulta de información sobre la calidad del agua.