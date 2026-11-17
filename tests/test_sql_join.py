"""Las relaciones no deben multiplicar accidentes."""
import unittest
from sql_fixtures import db_prueba

class Relaciones(unittest.TestCase):
    def test_joins_sin_duplicaciones(self):
        with db_prueba() as db:
            count=db.execute("""SELECT COUNT(*) FROM hecho_accidentes h
            INNER JOIN dim_tiempo t ON h.fecha_id=t.fecha_id
            INNER JOIN dim_departamento d ON h.departamento_id=d.departamento_id""").fetchone()[0]
            self.assertEqual(count,4)

if __name__=="__main__":
    unittest.main()
