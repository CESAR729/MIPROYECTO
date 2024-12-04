# Proyecto: Predicción de Casos Médicos con KNN

## Descripción del Proyecto

Este proyecto tiene como objetivo predecir los casos médicos utilizando el algoritmo K-Nearest Neighbors (KNN). El modelo se ha entrenado con un conjunto de datos que contiene información sobre establecimientos de salud, pacientes y los casos reportados, con el fin de hacer predicciones sobre el número de casos para cada registro.

## Primeros Registros del Dataset

A continuación, se muestran algunos registros del dataset utilizado en este proyecto:

| DEPARTAMENTO | PROVINCIA | DISTRITO | RED        | MICRORED  | COD_EESS | EESS        | EDAD | ANIO | CASOS | NORMAL | TOTAL | FECHA_CORTE | UBIGEO |
|--------------|-----------|----------|------------|-----------|----------|-------------|------|------|-------|--------|-------|-------------|--------|
| CUSCO        | ACOMAYO   | ACOMAYO  | CUSCO SUR  | ACOMAYO   | 2317.0   | C.S. ACOMAYO| 0    | 2019 | 1     | 0      | 1     | 20230630    | 80201.0 |
| CUSCO        | ACOMAYO   | ACOMAYO  | CUSCO SUR  | ACOMAYO   | 2317.0   | C.S. ACOMAYO| 4    | 2015 | 1     | 0      | 1     | 20230630    | 80201.0 |
| CUSCO        | ACOMAYO   | ACOMAYO  | CUSCO SUR  | ACOMAYO   | 2317.0   | C.S. ACOMAYO| 5    | 2015 | 5     | 1      | 6     | 20230630    | 80201.0 |
| CUSCO        | ACOMAYO   | ACOMAYO  | CUSCO SUR  | ACOMAYO   | 2317.0   | C.S. ACOMAYO| 6    | 2015 | 17    | 5      | 22    | 20230630    | 80201.0 |
| CUSCO        | ACOMAYO   | ACOMAYO  | CUSCO SUR  | ACOMAYO   | 2317.0   | C.S. ACOMAYO| 8    | 2020 | 4     | 0      | 4     | 20230630    | 80201.0 |

## Columnas del Dataset

El dataset contiene las siguientes columnas:

1. **DEPARTAMENTO**: Nombre del departamento.
2. **PROVINCIA**: Nombre de la provincia.
3. **DISTRITO**: Nombre del distrito.
4. **RED**: Red sanitaria asociada.
5. **MICRORED**: Microred de salud asociada.
6. **COD_EESS**: Código del establecimiento de salud.
7. **EESS**: Nombre del establecimiento de salud.
8. **EDAD**: Edad del paciente.
9. **ANIO**: Año del registro.
10. **CASOS**: Número de casos reportados.
11. **NORMAL**: Número de casos normales.
12. **TOTAL**: Total de casos registrados.
13. **FECHA_CORTE**: Fecha de corte de los datos.
14. **UBIGEO**: Código UBIGEO (código geográfico único de localización).

## Información General del Dataset

El dataset contiene 56,619 registros, con 14 columnas. Las columnas de tipo `float64` son `COD_EESS` y `UBIGEO`, mientras que las columnas de tipo `int64` incluyen la edad del paciente, el año del registro, y el número de casos. Las demás columnas son de tipo `object`, y contienen información categórica como nombres de departamentos, provincias, y establecimientos de salud.

### Resumen de las columnas:

- **DEPARTAMENTO**: 56,619 entradas no nulas.
- **PROVINCIA**: 56,619 entradas no nulas.
- **DISTRITO**: 56,619 entradas no nulas.
- **RED**: 56,619 entradas no nulas.
- **MICRORED**: 56,619 entradas no nulas.
- **COD_EESS**: 56,619 entradas no nulas.
- **EESS**: 56,619 entradas no nulas.
- **EDAD**: 56,619 entradas no nulas.
- **ANIO**: 56,619 entradas no nulas.
- **CASOS**: 56,619 entradas no nulas.
- **NORMAL**: 56,619 entradas no nulas.
- **TOTAL**: 56,619 entradas no nulas.
- **FECHA_CORTE**: 56,619 entradas no nulas.
- **UBIGEO**: 56,619 entradas no nulas.

## Precisión del Modelo KNN

El modelo de K-Nearest Neighbors (KNN) entrenado con este dataset ha alcanzado una **precisión del 44.21%**. Este valor indica la proporción de predicciones correctas realizadas por el modelo en relación con el total de predicciones realizadas.

## Primeras Predicciones

Las primeras predicciones del modelo son:

