"""No deben publicarse contraseñas predeterminadas en el script."""
import unittest
from pathlib import Path

class Credenciales(unittest.TestCase):
    def test_variables_entorno(self):
        code=(Path(__file__).resolve().parents[1]/"dashboard_local.py").read_text(encoding="utf-8")
        for name in ("DATAPULSE_ADMIN_PASSWORD","DATAPULSE_CAJAMARCA_PASSWORD"):
            self.assertIn(name,code)
        self.assertIn("hmac.compare_digest",code)
        self.assertIn("401",code)

if __name__=="__main__":
    unittest.main()
