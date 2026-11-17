"""Cada registro sintético debe producir exactamente un hecho."""
import unittest
from sql_fixtures import db_prueba

class Hechos(unittest.TestCase):
    def test_numero_hechos(self):
        with db_prueba() as db:
            self.assertEqual(db.execute("SELECT COUNT(*) FROM hecho_accidentes").fetchone()[0], 4)

    def test_eventos_con_fallecidos(self):
        with db_prueba() as db:
            self.assertEqual(db.execute("SELECT SUM(evento_fatal) FROM hecho_accidentes").fetchone()[0], 2)

if __name__ == "__main__":
    unittest.main()
