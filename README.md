# Nombre del Proyecto:
**EcoReporte-Comunitario**

---

## Descripcion del Proyecto:
EcoReporte Comunitario es una iniciativa orientada a identificar y gestionar reportes sobre problemáticas ambientales (gestión de desechos sólidos, contaminación de ríos y fuentes de agua) en el cantón Potrero Grande, caserío El Tule (Municipio de El Paisnal, Departamento de San Salvador).

---

## Integrantes:
* Jhimy Isaac Landaverde Gutiérrez
* Ana Guadalupe Echeverría Guillén
* Joel Esaú Méndez Segura
* Estiven Edgardo Alvarenga Henriquez
* Justin Adonai Lemus Hernández

---

## Requisitos Funcionales
1. **Gestión de Usuarios:** El sistema permitirá el registro e inicio de sesión seguro para ciudadanos y administradores de la ADESCO El Tule con contraseñas cifradas.
2. **Creación de Reporte Ambiental:** El ciudadano podrá registrar un reporte especificando la categoría de contaminación (desechos sólidos, vertedero clandestino, escombros, etc.) y una descripción textual.
3. **Carga de Evidencia Fotográfica:** El sistema permitirá adjuntar entre 1 y 5 fotografías como evidencia del problema ambiental.
4. **Captura de Ubicación Geográfica:** El sistema permitirá registrar la ubicación precisa del caso mediante coordenadas GPS o marcación en un mapa interactivo.
5. **Visualización y Filtrado de Casos:** El sistema ofrecerá un listado y mapa interactivo con filtros por estado, categoría, fecha y zona.
6. **Gestión y Cambio de Estados:** El administrador de la ADESCO podrá modificar el estado del caso (Pendiente, En proceso, Resuelto, Rechazado con motivo).
7. **Sistema de Notificaciones:** El sistema notificará al ciudadano cuando su reporte cambie de estado y alertará al administrador ante nuevos registros.
8. **Dashboard Estadístico:** El sistema mostrará un panel gráfico con métricas consolidadas de reportes totales, resueltos y pendientes.

---

## Requisitos No Funcionales
1. **Usabilidad y Adaptabilidad:** La interfaz web será intuitiva y adaptable a dispositivos móviles (teléfonos/tabletas) y computadoras de escritorio.
2. **Rendimiento y Optimización:** El tiempo de carga de las páginas principales no excederá los 3 segundos y las fotografías subidas serán comprimidas automáticamente.
3. **Seguridad y Protección de Datos:** El sistema protegerá la información personal de los denunciantes, almacenará contraseñas mediante algoritmos hash y prevendrá inyecciones SQL y XSS.
4. **Arquitectura y Compatibilidad Tecnológica:** El sistema se desarrollará con el framework Django, base de datos SQL Server, versionado en GitHub y compatible con los navegadores web principales.

---

##  Semana 3: Diseño de Clases y Modelado de Base de Datos

En esta etapa se ha establecido la arquitectura técnica del sistema mediante el paradigma Orientado a Objetos (POO) y el diseño de la base de datos relacional.

### 1. Estructura de Clases Principales
El sistema se compone de 6 clases orientadas al dominio del problema:
* **`Usuario`**: Gestiona los datos compartidos de acceso y perfil.
* **`Rol`**: Asigna permisos (`Administrador` / `Ciudadano`).
* **`Categoria`**: Clasifica el tipo de incidente ambiental.
* **`ReporteAmbiental`**: Entidad central del sistema que registra las denuncias.
* **`EvidenciaFotografica`**: Almacena de 1 a 5 imágenes adjuntas por reporte.
* **`HistorialEstado`**: Registra la trazabilidad y auditoría de cambios por parte de la ADESCO.


---

### 2. Diagrama de Clases UML
Representación visual del modelo conceptual del software:

![Diagrama de Clases UML](https://drive.google.com/file/d/17Z780m9CR3pT_q7k00iJHpt5d2T5ZM6P/view?usp=sharing)

---

###  3. Modelo de Base de Datos (SQL Server)
El diseño físico de la base de datos relacional se implementa sobre SQL Server:
* **Script DDL de Creación:** (https://drive.google.com/file/d/1Aapi5XcopRlZ90GUd9g0Ne3_9Kyd1yLz/view?usp=sharing)
* **Diccionario de Datos:**(https://docs.google.com/document/d/12w_iw4Te06-KpKSmeoTp-cwmQV3rrDfu/edit?usp=sharing&ouid=113841504882508374026&rtpof=true&sd=true)

---

### 4. Organización del Repositorio
```text
EcoReporte-Comunitario/
├── docs/
│   ├── diagramas/
│   │   └── diagrama_clases.png
│   └── database/
│       ├── schema_sqlserver.sql
│      
|── README.md