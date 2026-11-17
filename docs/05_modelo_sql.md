# Paso 3. Modelo ligero de hechos y dimensiones

La base SQLite local `sutran_analisis.sqlite` se genera a partir del dataset limpio. El archivo `analisis_corregido.sql` construye:

- **dim_departamento**: categoría geográfica, con `NO INFORMADO` cuando el dato es desconocido.
- **dim_tiempo**: fecha única y atributos año/mes.
- **hecho_accidentes**: una fila por registro del dataset limpio, con claves foráneas y medidas.

## Comprobación técnica
Ejecutar `python -m unittest discover -s tests -v`. Las pruebas SQL incorporan una muestra **sintética**, sin datos del dataset original, y comprueban dimensiones, integridad, filtros, agregaciones e idempotencia.

En la base real, registrar las salidas de:
```sql
SELECT COUNT(*) FROM hecho_accidentes;
PRAGMA foreign_key_check;
SELECT departamento, SUM(accidentes) FROM vw_concentracion
GROUP BY departamento ORDER BY 2 DESC LIMIT 10;
```

No presentar las pruebas sintéticas como sustituto de las capturas del análisis real.
