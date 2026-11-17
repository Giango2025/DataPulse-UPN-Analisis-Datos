"""Las víctimas se interpretan como cantidades registradas."""
import unittest
from sql_fixtures import db_prueba

class Victimas(unittest.TestCase):
    def test_total(self):
        with db_prueba() as db:
            total=db.execute("SELECT SUM(total_victimas) FROM hecho_accidentes").fetchone()[0]
            self.assertEqual(total,9)

    def test_heridos(self):
        with db_prueba() as db:
            heridos=db.execute("SELECT SUM(heridos) FROM hecho_accidentes").fetchone()[0]
            self.assertEqual(heridos,6)

if __name__ == "__main__":
    unittest.main()
