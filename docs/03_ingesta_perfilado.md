# Paso 2. Ingesta y perfilado

## Entrada
CSV con separador punto y coma y codificación compatible con Latin-1. Confirmar con el archivo original antes de cambiar estos parámetros.

## Secuencia
1. Instalar las dependencias del proyecto.
2. Colocar una copia autorizada en `datos/dataset_fuente.csv`.
3. Abrir `DataPulse_hasta_paso6.ipynb` en Jupyter o VS Code.
4. Ejecutar la celda de importación.
5. Guardar evidencia de `df.shape`, `df.dtypes`, porcentaje de nulos, duplicados y `df.head()`.
6. Explicar los rangos y categorías observadas, incluidos valores inusuales.

## Diccionario mínimo
| Variable | Tipo esperado | Unidad o interpretación |
|---|---|---|
| FECHA | fecha | día/mes/año en la fuente |
| DEPARTAMENTO | categoría | ámbito administrativo |
| MODALIDAD | categoría | tipo de accidente |
| FALLECIDOS | numérico | personas registradas |
| HERIDOS | numérico | personas registradas |
| KILOMETRO | numérico | kilómetro vial, si aplica |

Los tipos definitivos y rangos deben verificarse con el CSV ejecutado. No copiar porcentajes históricos sin volver a correr el perfilado.
