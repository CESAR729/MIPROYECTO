# Clasificación de Regiones por Temporada usando SVM

Este proyecto utiliza un conjunto de datos aleatorio con cinco características (columnas) para clasificar regiones en tres categorías de temporada: `bajo`, `medio`, y `alto`. El modelo implementado es un **Máquina de Soporte Vectorial (SVM)** con un kernel lineal.

## Descripción del Dataset

El dataset tiene 1000 muestras y 7 columnas, que incluyen cinco características numéricas (`columna1` a `columna5`), la columna objetivo (`columna_objetivo`) que es una etiqueta de clasificación, y una columna adicional (`temporada`) que representa la clasificación de la temporada de cada región:

| columna1  | columna2  | columna3  | columna4  | columna5  | columna_objetivo | temporada |
|-----------|-----------|-----------|-----------|-----------|------------------|-----------|
| 0.789678  | 0.875056  | -0.524088 | 1.108592  | -1.402916 | 0                | medio     |
| -1.686931 | 3.324227  | -0.190503 | 3.101080  | -3.083091 | 2                | bajo      |
| -1.070137 | 2.950171  | 0.508269  | 2.853285  | -2.940819 | 2                | bajo      |
| 0.103687  | -1.319036 | -1.352670 | -1.364504 | 1.494486  | 1                | medio     |
| -1.309502 | 1.750843  | -0.557423 | 1.533576  | -1.422048 | 2                | bajo      |

- `columna1` a `columna5`: Características numéricas utilizadas para la clasificación.
- `columna_objetivo`: Etiquetas de clase para entrenamiento del modelo (tres clases posibles).
- `temporada`: Categoría asignada que representa la clasificación de la región por temporada (`bajo`, `medio`, `alto`).

## Preprocesamiento

- **Estandarización**: Las características numéricas se estandarizan para mejorar el rendimiento del modelo SVM.
- **Clasificación de Temporada**: Utilizando la columna `columna1`, se crea una categoría de temporada para cada registro (`alto`, `medio`, `bajo`), basándose en un rango de valores.

## Modelo de Clasificación

Se utilizó un **SVM con kernel lineal** para clasificar las regiones en las categorías de temporada. El modelo se entrenó utilizando el 80% de los datos y se probó con el 20% restante.

## Resultados

### Reporte de Clasificación

El reporte de clasificación muestra las métricas de desempeño del modelo (precisión, recall y F1-score) para cada clase de temporada:

