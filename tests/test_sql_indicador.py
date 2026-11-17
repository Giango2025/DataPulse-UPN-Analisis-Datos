"""No incluir registros sin dato de fallecidos en el denominador."""
import unittest
from sql_fixtures import db_prueba

class Indicador(unittest.TestCase):
    def test_indicador_registros_conocidos(self):
        with db_prueba() as db:
            n,f=db.execute("SELECT COUNT(evento_fatal),SUM(evento_fatal) FROM hecho_accidentes").fetchone()
            self.assertEqual(n,4)
            self.assertEqual(f,2)
            self.assertEqual(100*f/n,50)

if __name__=="__main__":
    unittest.main()
