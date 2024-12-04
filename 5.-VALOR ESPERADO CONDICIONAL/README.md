# Análisis del Dataset de Animia

Este proyecto está diseñado para analizar un dataset que contiene información sobre casos de animia en diferentes regiones. Se realiza una clasificación de los casos en dos categorías ("Alto" y "Bajo"), y se calcula el valor esperado condicional para cada clasificación.

## Descripción del Dataset

El dataset contiene información sobre casos de animia en varias regiones. Las columnas incluyen detalles sobre la ubicación, el establecimiento de salud, la edad, el año, el número de casos, entre otros. El dataset es de gran tamaño, con 83,412 registros.

### Primeros Registros del Dataset

Los primeros registros del dataset contienen la siguiente información:

| DEPARTAMENTO | PROVINCIA | DISTRITO | RED | MICRORED | COD_EESS | EESS          | EDAD | ANIO | CASOS | NORMAL | TOTAL | FECHA_CORTE | UBIGEO |
|--------------|-----------|----------|-----|----------|----------|---------------|------|------|-------|--------|-------|-------------|--------|
| CUSCO        | NaN       | NaN      | CANAS - CANCHIS - ESPINAR | TECHO OBRERO | 2390.0 | P.S. CCUYO     | 4    | 2017 | 0     | 1      | 1     | 20230630     | NaN    |
| CUSCO        | NaN       | NaN      | CUSCO SUR    | HUANCARANI | NaN    | C.S. HUANCARANI | 41   | 2010 | 0     | 1      | 1     | 20230630     | NaN    |
| CUSCO        | ACOMAYO   | ACOMAYO  | CUSCO SUR    | ACOMAYO    | NaN    | C.S. ACOMAYO   | 5    | 2010 | 1     | 0      | 1     | 20230630     | 80201.0|
| CUSCO        | ACOMAYO   | ACOMAYO  | CUSCO SUR    | ACOMAYO    | NaN    | C.S. ACOMAYO   | 5    | 2013 | 5     | 1      | 6     | 20230630     | 80201.0|
| CUSCO        | ACOMAYO   | ACOMAYO  | CUSCO SUR    | ACOMAYO    | NaN    | C.S. ACOMAYO   | 6    | 2010 | 3     | 21     | 24    | 20230630     | 80201.0|

### Columnas del Dataset

El dataset tiene 14 columnas que contienen diferentes tipos de información. Estas son:

- **DEPARTAMENTO**: Departamento donde se reporta el caso.
- **PROVINCIA**: Provincia del caso.
- **DISTRITO**: Distrito del caso.
- **RED**: Red de salud.
- **MICRORED**: Microred de salud.
- **COD_EESS**: Código del establecimiento de salud.
- **EESS**: Nombre del establecimiento de salud.
- **EDAD**: Edad del paciente.
- **ANIO**: Año del reporte.
- **CASOS**: Número de casos reportados.
- **NORMAL**: Valor relacionado con el estado de los casos.
- **TOTAL**: Total de casos registrados.
- **FECHA_CORTE**: Fecha del corte de los datos.
- **UBIGEO**: Código geográfico de la región.

### Información General del Dataset

El dataset tiene un total de **83,412 registros**. A continuación, se muestra el tipo de datos de cada columna:

