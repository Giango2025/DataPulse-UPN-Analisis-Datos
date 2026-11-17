"""El notebook debe ser JSON con celdas de ingesta y limpieza."""
import unittest
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class Notebook(unittest.TestCase):
    def test_es_notebook(self):
        data=json.loads((ROOT/"DataPulse_hasta_paso6.ipynb").read_text(encoding="utf-8"))
        self.assertEqual(data["nbformat"],4)
        self.assertTrue(any(c["cell_type"]=="code" for c in data["cells"]))

    def test_sin_resultados_fingidos(self):
        data=json.loads((ROOT/"DataPulse_hasta_paso6.ipynb").read_text(encoding="utf-8"))
        for c in data["cells"]:
            if c["cell_type"]=="code":
                self.assertIsNone(c["execution_count"])
                self.assertEqual(c["outputs"],[])

if __name__ == "__main__":
    unittest.main()
