"""Los índices de departamento y fecha deben existir."""
import unittest
from sql_fixtures import db_prueba

class Indices(unittest.TestCase):
    def test_indices(self):
        with db_prueba() as db:
            indices={r[1] for r in db.execute("PRAGMA index_list('hecho_accidentes')")}
            self.assertTrue({"idx_hecho_dep","idx_hecho_fecha"}.issubset(indices))

if __name__=="__main__":
    unittest.main()
