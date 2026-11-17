"""Comprobación estructural de código sin requerir publicar el dataset."""
from pathlib import Path
import ast
import unittest

ROOT = Path(__file__).resolve().parents[1]

class EstructuraProyecto(unittest.TestCase):
    def test_archivos(self):
        for archivo in ("pipeline.py", "dashboard_local.py", "analisis_corregido.sql", "requirements.txt"):
            with self.subTest(archivo=archivo):
                self.assertTrue((ROOT / archivo).is_file())

    def test_sintaxis_python(self):
        for archivo in ("pipeline.py", "dashboard_local.py"):
            with self.subTest(archivo=archivo):
                ast.parse((ROOT / archivo).read_text(encoding="utf-8"))

    def test_modelo_sql(self):
        sql = (ROOT / "analisis_corregido.sql").read_text(encoding="utf-8").upper()
        for termino in ("CREATE TABLE DIM_TIEMPO", "CREATE TABLE DIM_DEPARTAMENTO",
                        "CREATE TABLE HECHO_ACCIDENTES", "GROUP BY", "HAVING", "JOIN"):
            self.assertIn(termino, sql)

if __name__ == "__main__":
    unittest.main()
