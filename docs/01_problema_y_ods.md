# Paso 1. Problema de ingeniería y relación con los ODS

**Pregunta analítica:** ¿En qué departamentos, periodos y modalidades se concentran los accidentes registrados, y qué hallazgos ayudan a priorizar la revisión de seguridad vial?

**Usuario de decisión propuesto:** responsable de planificación vial que debe decidir dónde revisar causas, infraestructura o intervenciones preventivas.

**ODS principal:** ODS 3, salud y bienestar. La meta 3.6 se refiere a muertes y lesiones por siniestros de tránsito. El indicador oficial 3.6.1 es una tasa de mortalidad por 100 000 habitantes; **no** se estima directamente con este archivo.

**Indicadores internos del proyecto:** número de accidentes registrados por zona/mes; proporción de registros con fallecidos dentro del subconjunto con dato conocido. Se explicita que ambas métricas son descriptivas del conjunto analizado y no tasas poblacionales de riesgo.

**Alcance:** registros de la fuente SUTRAN disponibles en el dataset que se incorpore localmente. No atribuir causas ni extrapolar sin analizar cobertura, subregistro y denominadores adecuados.

**Criterio de aceptación:** el usuario identifica la región y el periodo de mayor número de registros, distingue conteos de tasas y puede explicar al menos una limitación antes de recomendar una acción.
