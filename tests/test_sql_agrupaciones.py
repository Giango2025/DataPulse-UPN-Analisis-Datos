"""Agrupaciones deben contar registros, no confundirlos con personas."""
import unittest
from sql_fixtures import db_prueba

class Agregaciones(unittest.TestCase):
    def test_lima_tiene_dos_eventos(self):
        with db_prueba() as db:
            n=db.execute("SELECT COUNT(*) FROM hecho_accidentes WHERE departamento_id='LIMA'").fetchone()[0]
            self.assertEqual(n, 2)

    def test_mortalidad_registrada(self):
        with db_prueba() as db:
            deaths=db.execute("SELECT SUM(fallecidos) FROM hecho_accidentes").fetchone()[0]
            self.assertEqual(deaths, 3)

if __name__ == "__main__":
    unittest.main()
