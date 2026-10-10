CREATE DATABASE EcoReporte;
GO

USE EcoReporte;
GO

-- TABLA DE ROLES
CREATE TABLE Roles (
IdRol INT IDENTITY (1,1) NOT NULL,
NombreRol VARCHAR (50) NOT NULL,
Descripcion VARCHAR (250) NOT NULL,
CONSTRAINT PK_Roles PRIMARY KEY (IdRol),
CONSTRAINT UQ_NombreRol UNIQUE (NombreRol)
);
GO

--TABLA DE USUARIOS
CREATE TABLE Usuarios (
IdUsuario INT IDENTITY (1,1) NOT NULL,
Nombre VARCHAR (50) NOT NULL,
Apellido VARCHAR (60) NOT NULL,
Correo VARCHAR (150) NOT NULL,
Contraseña VARCHAR (150) NOT NULL,
Telefono VARCHAR (20) NULL,
FechaRegistro DATETIME DEFAULT GETDATE() NOT NULL,
Activo BIT DEFAULT 1 NOT NULL,
IdRol INT NOT NULL,
CONSTRAINT PK_Usuarios PRIMARY KEY (IdUsuario),
CONSTRAINT UQ_Usuarios_Correo UNIQUE (Correo),
CONSTRAINT FK_Usuarios_Roles FOREIGN KEY (IdRol) REFERENCES Roles(IdRol) ON DELETE NO ACTION ON UPDATE CASCADE
);
GO

--TABLA DE CATEGORIA
CREATE TABLE Categoria (
IdCategoria INT IDENTITY (1,1) NOT NULL,
NombreCategoria VARCHAR (40) NOT NULL,
Descripcion VARCHAR (250) NOT NULL,
CONSTRAINT PK_Categoria PRIMARY KEY (IdCategoria),
CONSTRAINT UQ_Categoria_NombreCategoria UNIQUE (NombreCategoria),
);
GO

--TABLA DE REPORTES AMBIENTAL
CREATE TABLE ReporteAmbiental(
IdReporteAmbiental INT IDENTITY (1,1) NOT NULL,
Titulo VARCHAR (90) NOT NULL,
Descripcion VARCHAR (MAX) NOT NULL,
UbicacionReferencial VARCHAR (200) NOT NULL,
Latitud DECIMAL (10,8) NULL,
Longitud DECIMAL (11,8) NULL,
Estado VARCHAR (20) DEFAULT 'Pendiente' NOT NULL,
FechaCreacion DATETIME DEFAULT GETDATE() NOT NULL,
IdUsuario INT NOT NULL,
IdCategoria INT NOT NULL,
CONSTRAINT PK_ReporteAmbiental PRIMARY KEY (IdReporteAmbiental),
CONSTRAINT CK_Estado CHECK (Estado IN ('Pendiente', 'En progreso', 'Resuelto', 'Rechazado')),
CONSTRAINT FK_ReporteAmbiental_Usuarios FOREIGN KEY (IdUsuario) REFERENCES Usuarios(IdUsuario) ON DELETE NO ACTION ON UPDATE CASCADE,
CONSTRAINT FK_ReporteAmbiental_Categoria FOREIGN KEY (IdCategoria) REFERENCES Categoria(IdCategoria) ON DELETE NO ACTION ON UPDATE CASCADE
);
GO

--TABLA DE EVIDENCIAS DE FOTOGRAFIAS
CREATE TABLE EvidenciaFotografia (
IdEvidenciaFotografia INT IDENTITY(1,1) NOT NULL,
RutaArchivo VARCHAR (255) NOT NULL,
FechaCarga DATETIME DEFAULT GETDATE () NOT NULL,
Tamano BIGINT NULL,
IdReporteAmbiental INT NOT NULL,
CONSTRAINT PK_EvidenciaFotografia PRIMARY KEY (IdEvidenciaFotografia),
CONSTRAINT FK_EvidenciaFotografia_ReporteAmbiental FOREIGN KEY(IdReporteAmbiental) REFERENCES ReporteAmbiental(IdReporteAmbiental) ON DELETE CASCADE ON UPDATE CASCADE
);
GO

--TABLA DE HISTORIAL DEL ESTADO 
CREATE TABLE HistorialEstado (
IdHistorialEstado INT IDENTITY (1,1) NOT NULL,
EstadoAnterior VARCHAR (20) NOT NULL,
EstadoNuevo VARCHAR (20) NOT NULL,
Observacion VARCHAR (255) NULL,
FechaCambio DATETIME DEFAULT GETDATE() NOT NULL,
IdReporteAmbiental INT NOT NULL,
IdUsuarioAdmin INT NOT NULL,
CONSTRAINT PK_HistorialEstado PRIMARY KEY (IdHistorialEstado),
CONSTRAINT FK_HistorialEstado_ReporteAmbiental FOREIGN KEY (IdReporteAmbiental) REFERENCES ReporteAmbiental(IdReporteAmbiental) ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT FK_HistorialEstado_Admin FOREIGN KEY(IdUsuarioAdmin) REFERENCES Usuarios(IdUsuario) ON DELETE NO ACTION
);
GO

SELECT * FROM Roles;
SELECT * FROM Usuarios;
SELECT * FROM Categoria;
SELECT * FROM ReporteAmbiental;
SELECT * FROM EvidenciaFotografia;
SELECT * FROM HistorialEstado;