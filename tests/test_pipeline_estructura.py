"""Revisión estática de pasos de ingesta, limpieza y resultados."""
import ast
import unittest
from pathlib import Path

SOURCE=(Path(__file__).resolve().parents[1]/"pipeline.py").read_text(encoding="utf-8")

class Pipeline(unittest.TestCase):
    def test_sintaxis(self):
        ast.parse(SOURCE)

    def test_limpieza(self):
        for token in ("drop_duplicates()","pd.to_datetime","pd.to_numeric","to_csv"):
            self.assertIn(token,SOURCE)

    def test_analisis(self):
        for token in ("crosstab","chi2_contingency","describe()","savefig"):
            self.assertIn(token,SOURCE)

if __name__=="__main__":
    unittest.main()
