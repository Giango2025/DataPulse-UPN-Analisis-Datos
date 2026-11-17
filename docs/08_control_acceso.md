# Paso 5. Seguridad por roles y alcance RLS

**ADMIN** puede consultar los departamentos incluidos en el dataset, sujetos a filtros seleccionados.

**CAJAMARCA** aplica una restricción de filas por `DEPARTAMENTO == "CAJAMARCA"` **antes** de calcular cualquier tarjeta o gráfico.

## Ensayo propuesto
1. Abrir una sesión nueva y autenticarse como ADMIN.
2. Registrar número de registros y filtros disponibles.
3. Cerrar completamente esa sesión (la autenticación HTTP Basic puede persistir en el navegador).
4. Abrir un perfil de navegador separado o ventana privada y autenticarse como CAJAMARCA.
5. Verificar que las cifras y categorías se calculan solo con datos regionales.
6. Intentar cambiar manualmente el parámetro de departamento en la URL: no debe devolver otra región.

## Advertencias
HTTP Basic es apto únicamente para una demostración en `127.0.0.1`, no para exponer el servicio a Internet. Usar contraseñas de prueba y no grabarlas en pantalla. Esta restricción en Python es equivalente conceptual de filtrado de filas, no una configuración RLS certificada en Power BI.
