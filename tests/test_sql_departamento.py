"""Validación del filtro regional contra datos de prueba."""
import unittest
from sql_fixtures import db_prueba

class Departamento(unittest.TestCase):
    def test_filtro_cajamarca(self):
        with db_prueba() as db:
            rows=db.execute("SELECT COUNT(*) FROM hecho_accidentes WHERE departamento_id=?",
                            ("CAJAMARCA",)).fetchone()[0]
            self.assertEqual(rows,1)

if __name__=="__main__":
    unittest.main()
