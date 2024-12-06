# Árbol de Decisión sobre el Dataset de Museo

Este proyecto utiliza un **Árbol de Decisión** para analizar y predecir el valor objetivo basado en varias características del dataset de museos. El dataset contiene información sobre visitas a museos, con variables relacionadas a la ubicación, tipo de museo, y el número de visitantes categorizado por género y otros factores.

## Dataset

El dataset utilizado tiene 1815 registros y 18 columnas con la siguiente información:

- **FECHA_CORTE**: Fecha de corte de la información.
- **anio**: Año de la observación.
- **idmes**: Identificador del mes.
- **Mes**: Nombre del mes.
- **Ubigeo**: Código de ubicación geográfica.
- **Departamento**: Departamento de la ubicación.
- **Provincia**: Provincia de la ubicación.
- **Distrito**: Distrito de la ubicación.
- **Idmuseo**: Identificador del museo.
- **NombreMuseo**: Nombre del museo.
- **Tipo**: Tipo de museo (Sala o Museo).
- **VaronAdulto**: Número de adultos varones visitantes.
- **VaronEstudiante**: Número de estudiantes varones visitantes.
- **VaronNino**: Número de niños varones visitantes.
- **MujerAdulto**: Número de adultas mujeres visitantes.
- **Militares**: Número de visitantes militares.
- **Discapacitado**: Número de visitantes discapacitados.
- **Total**: Total de visitantes.

## Preprocesamiento

El dataset fue preprocesado para seleccionar las características relevantes y la variable objetivo. En este caso, **Total** es la variable objetivo que indica el número total de visitantes, y las características incluyen las demás columnas.

## Código de Árbol de Decisión

A continuación se muestra el código para entrenar y evaluar un modelo de árbol de decisión utilizando el dataset de museos.

```python
# Importar librerías necesarias
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

# Cargar el dataset desde el archivo CSV
df = pd.read_csv('/content/DatosMuseo.csv', encoding='latin-1', delimiter=';')

# Asumiendo que 'Total' es la variable objetivo y el resto son características
X = df.drop(columns=['Total'])  # Variable de características
y = df['Total']  # Variable objetivo

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de árbol de decisión y entrenarlo
dt_classifier = DecisionTreeClassifier(random_state=42)
dt_classifier.fit(X_train, y_train)

# Realizar predicciones y calcular la precisión
y_pred = dt_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Clasificar la precisión en alto, medio y bajo
if accuracy >= 0.80:
    performance = "Alto"
elif accuracy >= 0.60:
    performance = "Medio"
else:
    performance = "Bajo"

# Mostrar el resultado final
print(f"Precisión del Árbol de Decisión: {accuracy:.2f} ({performance})")
