"""Prueba de integridad referencial del esquema estrella."""
import unittest
from sql_fixtures import db_prueba

class Integridad(unittest.TestCase):
    def test_foreign_key_check(self):
        with db_prueba() as db:
            self.assertEqual(db.execute("PRAGMA foreign_key_check").fetchall(), [])

    def test_cada_hecho_tiene_departamento(self):
        with db_prueba() as db:
            faltantes = db.execute("""SELECT COUNT(*) FROM hecho_accidentes h
              LEFT JOIN dim_departamento d ON h.departamento_id=d.departamento_id
              WHERE d.departamento_id IS NULL""").fetchone()[0]
            self.assertEqual(faltantes, 0)

if __name__ == "__main__":
    unittest.main()
