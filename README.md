Nombre del Proyecto:
EcoReporte-Comunitario

Descripcion del Proyecto:
EcoReporte Comunitario es una iniciativa orientada a identificar y gestionar reportes sobre problemáticas ambientales (gestión de desechos sólidos, contaminación de ríos y fuentes de agua) en el cantón Potrero Grande, caserío El Tule (Municipio de El Paisnal, Departamento de San Salvador).

Integrantes:
Jhimy Isaac Landaverde Gutiérrez,
Ana Guadalupe Echeverría Guillén,
Joel Esaú Méndez Segura,
Estiven Edgardo Alvarenga Henriquez, 
Justin Adonai Lemus Hernández.

Requisitos Funcionales
1.	Gestión de Usuarios: El sistema permitirá el registro e inicio de sesión seguro para ciudadanos y administradores de la ADESCO El Tule con contraseñas cifradas.
2.	Creación de Reporte Ambiental: El ciudadano podrá registrar un reporte especificando la categoría de contaminación (desechos sólidos, vertedero clandestino, escombros, etc.) y una descripción textual. 
3.	Carga de Evidencia Fotográfica: El sistema permitirá adjuntar entre 1 y 5 fotografías como evidencia del problema ambiental. 
4.	Captura de Ubicación Geográfica: El sistema permitirá registrar la ubicación precisa del caso mediante coordenadas GPS o marcación en un mapa interactivo. 
5.	Visualización y Filtrado de Casos: El sistema ofrecerá un listado y mapa interactivo con filtros por estado, categoría, fecha y zona. 
6.	Gestión y Cambio de Estados: El administrador de la ADESCO podrá modificar el estado del caso (Pendiente, En proceso, Resuelto, Rechazado con motivo).
7.	Sistema de Notificaciones: El sistema notificará al ciudadano cuando su reporte cambie de estado y alertará al administrador ante nuevos registros. 
8.	Dashboard Estadístico: El sistema mostrará un panel gráfico con métricas consolidadas de reportes totales, resueltos y pendientes. 

Requisitos No Funcionales
1.	Usabilidad y Adaptabilidad: La interfaz web será intuitiva y adaptable a dispositivos móviles (teléfonos/tabletas) y computadoras de escritorio. 
2.	Rendimiento y Optimización: El tiempo de carga de las páginas principales no excederá los 3 segundos y las fotografías subidas serán comprimidas automáticamente. 
3.	Seguridad y Protección de Datos: El sistema protegerá la información personal de los denunciantes, almacenará contraseñas mediante algoritmos hash y prevendrá inyecciones SQL y XSS. 
4.	Arquitectura y Compatibilidad Tecnológica: El sistema se desarrollará con el framework Django, base de datos SQL Server, versionado en GitHub y compatible con los navegadores web principales. 
