# Paso 3. Limpieza y transformación

## Reglas implementadas
- Retirar duplicados exactos sin convertir incidentes distintos en un único evento.
- Estandarizar etiquetas categóricas con eliminación de espacios externos y normalización a mayúsculas.
- Convertir fechas con `dayfirst=True`; los valores imposibles no se interpretan como fechas válidas.
- Convertir kilometraje, heridos y fallecidos a numérico.
- Tratar cifras negativas como desconocidas, no como cero.
- Crear año y mes para agregaciones temporales.
- Crear `EVENTO_FATAL` solo cuando se conoce la cantidad de fallecidos.

## Consideraciones de calidad
El script actual detiene la ejecución ante fechas no interpretables. Esa decisión evita incorporar periodos falsos, pero requiere revisión manual de los registros afectados.

Los valores extremos de heridos o fallecidos no se eliminan automáticamente: podrían representar siniestros reales. Debe documentarse si se consideran plausibles con apoyo de la fuente.

## Evidencia requerida
Captura del número de filas originales, registros duplicados, tasas de nulos y salida `datos/dataset_limpio.csv`, sin revelar información personal.
