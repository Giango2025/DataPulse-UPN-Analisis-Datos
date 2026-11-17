# Paso 5. Dashboard local: demostración

## Inicio
1. Instalar dependencias según `requirements.txt`.
2. Ejecutar `python pipeline.py` con el CSV autorizado.
3. Configurar contraseñas distintas en variables de entorno:
   `DATAPULSE_ADMIN_PASSWORD` y `DATAPULSE_CAJAMARCA_PASSWORD`.
4. Ejecutar `python dashboard_local.py`.
5. Abrir `http://127.0.0.1:8765`.

## Lo que debe enseñarse
- KPI de accidentes, eventos con fallecidos y proporción conocida.
- Gráficos de departamentos, modalidades, meses y heridos.
- Uso del filtro geográfico y del año.
- Diferencia visible entre la vista general y el alcance restringido.

## Limitaciones
Se trata de un prototipo HTML local, no de un servicio productivo de Power BI. La interfaz contiene barras HTML; no afirmar que equivale a un tablero publicado en workspace.

La captura debe provenir del programa realmente ejecutado; si falla, registrar el error para corregirlo.
