"""Validación temporal contra fechas sintéticas."""
import unittest
from sql_fixtures import db_prueba

class Tiempo(unittest.TestCase):
    def test_meses(self):
        with db_prueba() as db:
            vals=db.execute("SELECT fecha_id,anio,mes FROM dim_tiempo ORDER BY fecha_id").fetchall()
            self.assertEqual(vals,[("2020-01-02",2020,1),("2020-02-03",2020,2),("2021-03-04",2021,3)])

if __name__ == "__main__":
    unittest.main()
