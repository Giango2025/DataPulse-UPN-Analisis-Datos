# DataPulse Ingeniería — Análisis de Datos UPN

Proyecto académico del curso **UAIN1008R**, aplicado al análisis de accidentes de tránsito en Perú y relacionado con el **ODS 3, meta 3.6**.

## Alcance
El desarrollo documenta los pasos 1 a 6. El video y las diapositivas de sustentación corresponden exclusivamente a los pasos 1 a 5.

## Archivos técnicos
- `pipeline.py`: ingesta, limpieza, análisis estadístico y generación de gráficos.
- `analisis_corregido.sql`: modelo de hechos y dimensiones y consultas de análisis.
- `dashboard_local.py`: prototipo local con acceso diferenciado ADMIN y CAJAMARCA.
- `requirements.txt`: dependencias de Python.

## Ejecución
1. Instalar Python y ejecutar `python -m pip install -r requirements.txt`.
2. Guardar una copia autorizada del CSV fuente en `datos/dataset_fuente.csv`.
3. Ejecutar `python pipeline.py` para obtener resultados y el CSV limpio.
4. Definir las variables de entorno `DATAPULSE_ADMIN_PASSWORD` y `DATAPULSE_CAJAMARCA_PASSWORD` con contraseñas diferentes.
5. Ejecutar `python dashboard_local.py` y visitar `http://127.0.0.1:8765`.

## Limitaciones
El dataset y los documentos académicos con nombres/códigos de estudiantes no se publican aquí porque este repositorio es público y la licencia del archivo fuente requiere confirmación. La ejecución depende de contar con el dataset autorizado. La validación con usuario real y las capturas deben registrarse por separado; no se declaran realizadas sin evidencia.

Repositorio de trabajo y evidencia de cambios reales. Los commits no representan por sí solos las contribuciones individuales de todo el grupo.
