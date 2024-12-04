# Regresión Lineal Múltiple con Datos de Anemia

Este proyecto implementa un modelo de regresión lineal múltiple utilizando Python y `scikit-learn` para analizar datos relacionados con casos de anemia. A continuación, se describen los pasos, resultados y métricas del modelo.

---

## Columnas Numéricas del Dataset

Las siguientes son las columnas numéricas identificadas en el dataset:

- **COD_EESS**: Código del establecimiento de salud.
- **EDAD**: Edad del paciente.
- **ANIO**: Año del registro.
- **CASOS**: Número de casos reportados (variable dependiente).
- **NORMAL**: Indicador de resultados normales.
- **TOTAL**: Total de registros.
- **FECHA_CORTE**: Fecha del corte de datos.
- **UBIGEO**: Código único de ubicación geográfica.

---

## Resultados del Modelo de Regresión

1. **Coeficientes del Modelo**:
   - **EDAD**: -0.0458
   - **ANIO**: 0.0514
   - **NORMAL**: 0.4649

   Estos coeficientes representan el impacto de cada variable independiente en la predicción de los casos de anemia.

2. **Intercepto**:
   - Valor: **-101.7055**
   - Representa el valor base de la variable dependiente cuando las variables independientes son cero.

3. **Métricas de Evaluación**:
   - **Error Cuadrático Medio (MSE)**: **19.9455**
     - Indica el promedio del cuadrado de los errores entre valores reales y predichos.
   - **R² Score**: **0.2517**
     - Indica qué tan bien los datos se ajustan al modelo. Un valor cercano a 1 indica un buen ajuste.

4. **Ejemplo de Predicciones**:
   - Resultados comparativos entre valores reales y predicciones del modelo:

| Real  | Predicción |
|-------|------------|
| 0     | 4.151980   |
| 0     | 1.277729   |
| 0     | 1.533334   |
| 0     | 2.331482   |
| 2     | 1.337788   |

---

## Requisitos

Para ejecutar el proyecto, necesitas instalar las siguientes bibliotecas:

```bash
pip install pandas scikit-learn matplotlib
