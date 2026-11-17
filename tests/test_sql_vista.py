"""La vista agregada mantiene departamentos y años."""
import unittest
from sql_fixtures import db_prueba

class Vista(unittest.TestCase):
    def test_concentracion_lima_2020(self):
        with db_prueba() as db:
            n=db.execute("""SELECT accidentes FROM vw_concentracion
                WHERE departamento='LIMA' AND anio=2020""").fetchone()[0]
            self.assertEqual(n,2)

    def test_total_vista(self):
        with db_prueba() as db:
            total=db.execute("SELECT SUM(accidentes) FROM vw_concentracion").fetchone()[0]
            self.assertEqual(total,4)

if __name__ == "__main__":
    unittest.main()
