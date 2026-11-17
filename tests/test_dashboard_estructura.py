"""Revisión estructural sin conexión ni contraseñas reales."""
import ast
from pathlib import Path
import unittest

PATH=Path(__file__).resolve().parents[1]/"dashboard_local.py"

class Dashboard(unittest.TestCase):
    def test_codigo_valido(self):
        ast.parse(PATH.read_text(encoding="utf-8"))

    def test_restriccion_precede_kpis(self):
        source=PATH.read_text(encoding="utf-8")
        self.assertLess(source.index('if role == "CAJAMARCA"'), source.index('n = len(df)'))

    def test_solo_localhost(self):
        self.assertIn('("127.0.0.1", 8765)',PATH.read_text(encoding="utf-8"))

if __name__=="__main__":
    unittest.main()
