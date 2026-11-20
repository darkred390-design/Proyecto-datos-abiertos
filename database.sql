
IF DB_ID('DatosAbiertosDB') IS NULL
BEGIN
    CREATE DATABASE DatosAbiertosDB;
END;
GO

USE DatosAbiertosDB;
GO

IF OBJECT_ID('dbo.RegistrosAPI', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.RegistrosAPI (
        id INT IDENTITY(1,1) PRIMARY KEY,
        id_api NVARCHAR(64) NOT NULL UNIQUE,
        fecha_toma_muestra NVARCHAR(50) NULL,
        codigo_muestra NVARCHAR(100) NULL,
        tipo_muestra NVARCHAR(100) NULL,
        color_aparente NVARCHAR(50) NULL,
        turbiedad NVARCHAR(50) NULL,
        ph NVARCHAR(50) NULL,
        cloro_residual_libre NVARCHAR(50) NULL,
        dureza_total NVARCHAR(50) NULL,
        json_original NVARCHAR(MAX) NULL,
        fecha_captura DATETIME2 NOT NULL DEFAULT SYSDATETIME()
    );
END;
GO

SELECT COUNT(*) AS TotalRegistros
FROM dbo.RegistrosAPI;
GO
