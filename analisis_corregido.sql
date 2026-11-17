-- Modelo ligero en SQLite; la tabla accidentes_limpios se genera en pipeline.py
PRAGMA foreign_keys=OFF;
DROP VIEW IF EXISTS vw_concentracion;
DROP TABLE IF EXISTS hecho_accidentes;
DROP TABLE IF EXISTS dim_tiempo;
DROP TABLE IF EXISTS dim_departamento;
CREATE TABLE dim_departamento (departamento_id TEXT PRIMARY KEY, departamento TEXT NOT NULL);
INSERT INTO dim_departamento SELECT DISTINCT COALESCE(DEPARTAMENTO,'NO INFORMADO'),COALESCE(DEPARTAMENTO,'NO INFORMADO') FROM accidentes_limpios;
CREATE TABLE dim_tiempo (fecha_id TEXT PRIMARY KEY, anio INTEGER, mes INTEGER);
INSERT INTO dim_tiempo SELECT FECHA,MIN(AÑO),MIN(MES) FROM accidentes_limpios GROUP BY FECHA;
CREATE TABLE hecho_accidentes (
 accidente_id INTEGER PRIMARY KEY,
 departamento_id TEXT NOT NULL,
 fecha_id TEXT NOT NULL,
 modalidad TEXT,
 fallecidos REAL,
 heridos REAL,
 total_victimas REAL,
 evento_fatal INTEGER,
 FOREIGN KEY(departamento_id) REFERENCES dim_departamento(departamento_id),
 FOREIGN KEY(fecha_id) REFERENCES dim_tiempo(fecha_id)
);
INSERT INTO hecho_accidentes SELECT rowid,COALESCE(DEPARTAMENTO,'NO INFORMADO'),FECHA,MODALIDAD,FALLECIDOS,HERIDOS,TOTAL_VICTIMAS,EVENTO_FATAL FROM accidentes_limpios;
CREATE INDEX idx_hecho_dep ON hecho_accidentes(departamento_id);
CREATE INDEX idx_hecho_fecha ON hecho_accidentes(fecha_id);
CREATE VIEW vw_concentracion AS
SELECT d.departamento,t.anio,COUNT(*) AS accidentes,SUM(h.fallecidos) AS fallecidos
FROM hecho_accidentes h JOIN dim_departamento d ON h.departamento_id=d.departamento_id
JOIN dim_tiempo t ON h.fecha_id=t.fecha_id
WHERE t.anio BETWEEN 2020 AND 2021 GROUP BY d.departamento,t.anio HAVING COUNT(*)>=1;
PRAGMA foreign_keys=ON;
