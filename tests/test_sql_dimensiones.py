"""Comprobar dimensiones del modelo estrella con filas sintéticas."""
import unittest
from sql_fixtures import db_prueba

class Dimensiones(unittest.TestCase):
    def test_departamentos(self):
        with db_prueba() as db:
            rows = {r[0] for r in db.execute("SELECT departamento FROM dim_departamento")}
            self.assertEqual(rows, {"LIMA", "CAJAMARCA", "NO INFORMADO"})

    def test_fecha_unica(self):
        with db_prueba() as db:
            fechas = db.execute("SELECT fecha_id FROM dim_tiempo").fetchall()
            self.assertEqual(len(fechas), 3)
            self.assertEqual(len(fechas), len(set(fechas)))

if __name__ == "__main__":
    unittest.main()
