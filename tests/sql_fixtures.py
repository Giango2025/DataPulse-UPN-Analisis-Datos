"""Datos sintéticos no derivados del archivo real: pruebas del modelo SQL."""
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SQL = (ROOT / "analisis_corregido.sql").read_text(encoding="utf-8")

def db_prueba():
    db = sqlite3.connect(":memory:")
    db.execute("""CREATE TABLE accidentes_limpios
    (DEPARTAMENTO TEXT, FECHA TEXT, AÑO INTEGER, MES INTEGER,
     MODALIDAD TEXT, FALLECIDOS REAL, HERIDOS REAL,
     TOTAL_VICTIMAS REAL, EVENTO_FATAL INTEGER)""")
    rows = [
      ("LIMA", "2020-01-02", 2020, 1, "CHOQUE", 0, 2, 2, 0),
      ("LIMA", "2020-02-03", 2020, 2, "DESPISTE", 1, 1, 2, 1),
      ("CAJAMARCA", "2021-03-04", 2021, 3, "CHOQUE", 0, 3, 3, 0),
      (None, "2021-03-04", 2021, 3, "CHOQUE", 2, 0, 2, 1),
    ]
    db.executemany("INSERT INTO accidentes_limpios VALUES (?,?,?,?,?,?,?,?,?)", rows)
    db.executescript(SQL)
    return db
