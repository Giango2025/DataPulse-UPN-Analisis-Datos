"""La base debe dejar activas las restricciones de claves foráneas."""
import sqlite3
import unittest
from sql_fixtures import db_prueba

class Restricciones(unittest.TestCase):
    def test_restricciones_activas(self):
        with db_prueba() as db:
            self.assertEqual(db.execute("PRAGMA foreign_keys").fetchone()[0],1)
            with self.assertRaises(sqlite3.IntegrityError):
                db.execute("""INSERT INTO hecho_accidentes
                    (departamento_id,fecha_id,modalidad) VALUES (?,?,?)""",
                    ("INEXISTENTE","2020-01-02","PRUEBA"))

if __name__=="__main__":
    unittest.main()
