"""Valores nulos geográficos se etiquetan, no se asignan a otra región."""
import unittest
from sql_fixtures import db_prueba

class SinDepartamento(unittest.TestCase):
    def test_no_informado(self):
        with db_prueba() as db:
            count=db.execute("""SELECT COUNT(*) FROM hecho_accidentes
            WHERE departamento_id='NO INFORMADO'""").fetchone()[0]
            self.assertEqual(count,1)

if __name__=="__main__":
    unittest.main()
