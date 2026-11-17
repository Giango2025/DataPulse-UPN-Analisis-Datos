# Paso 4. Estadística, KPIs y análisis temporal

## KPI 1: volumen de accidentes
`COUNT(*)` de eventos por departamento y periodo. Describe concentración de reportes, no exposición al tránsito.

## KPI 2: proporción de eventos con fallecidos
Numerador: registros con `FALLECIDOS > 0`. Denominador: registros con dato conocido de fallecidos. No equiparar con la tasa oficial ODS 3.6.1.

## Estadística
El pipeline imprime medidas descriptivas de `KILOMETRO`, `FALLECIDOS` y `HERIDOS`; también calcula una aproximación normal al intervalo del 95 % para la proporción, bajo supuestos estadísticos que deben mencionarse.

La prueba chi-cuadrado en tablas de contingencia es exploratoria. Una diferencia de frecuencias no establece causalidad ni implica por sí misma una intervención efectiva.

## Tiempo
La serie mensual permite observar cambios, pero debe contextualizarse con la cobertura temporal de la fuente y cambios en movilidad o registro.

## Evidencias
Conservar capturas de los resultados numéricos y los cuatro gráficos generados en `visualizaciones/`.
