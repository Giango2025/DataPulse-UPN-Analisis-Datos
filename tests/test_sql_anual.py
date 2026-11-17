"""Los registros anuales no deben mezclarse."""
import unittest
from sql_fixtures import db_prueba

class Anual(unittest.TestCase):
    def test_por_anio(self):
        with db_prueba() as db:
            rows=db.execute("""SELECT t.anio,COUNT(*)
            FROM hecho_accidentes h JOIN dim_tiempo t ON h.fecha_id=t.fecha_id
            GROUP BY t.anio ORDER BY t.anio""").fetchall()
            self.assertEqual(rows,[(2020,2),(2021,2)])

if __name__=="__main__":
    unittest.main()
