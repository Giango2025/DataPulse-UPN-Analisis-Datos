"""Ejecutar dos veces no duplica dimensiones ni registros."""
import unittest
from sql_fixtures import db_prueba, SQL

class Repeticion(unittest.TestCase):
    def test_idempotencia(self):
        with db_prueba() as db:
            before=db.execute("SELECT COUNT(*) FROM hecho_accidentes").fetchone()[0]
            db.executescript(SQL)
            after=db.execute("SELECT COUNT(*) FROM hecho_accidentes").fetchone()[0]
            self.assertEqual((before,after),(4,4))

if __name__ == "__main__":
    unittest.main()
