Primeras filas del dataset:
  DEPARTAMENTO PROVINCIA DISTRITO              RED  MICRORED     COD_EESS           EESS  EDAD  ANIO  CASOS  NORMAL  TOTAL  FECHA_CORTE   UBIGEO
0        CUSCO       NaN      NaN  CANAS - CANCHIS - ESPINAR  TECHO OBRERO    2390.0       P.S. CCUYO     4  2017      0       1      1     20230630    NaN
1        CUSCO       NaN      NaN                  CUSCO SUR    HUANCARANI       NaN  C.S. HUANCARANI    41  2010      0       1      1     20230630    NaN
2        CUSCO   ACOMAYO  ACOMAYO                  CUSCO SUR       ACOMAYO      NaN     C.S. ACOMAYO     5  2010      1       0      1     20230630  80201.0

Información del dataset:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 83412 entries, 0 to 83411
Data columns (total 14 columns):
 #   Column        Non-Null Count  Dtype  
 ---  ------        --------------  -----  
  0   DEPARTAMENTO  83412 non-null  object 
  1   PROVINCIA     83400 non-null  object 
  2   DISTRITO      83383 non-null  object 
  3   RED           83412 non-null  object 
  4   MICRORED      83412 non-null  object 
  5   COD_EESS      56624 non-null  float64
  6   EESS          83412 non-null  object 
  7   EDAD          83412 non-null  int64  
  8   ANIO          83412 non-null  int64  
  9   CASOS         83412 non-null  int64  
  10  NORMAL        83412 non-null  int64  
  11  TOTAL         83412 non-null  int64  
  12  FECHA_CORTE   83412 non-null  int64  
  13  UBIGEO        83383 non-null  float64
dtypes: float64(2), int64(6), object(6)
memory usage: 8.9+ MB

Mean Squared Error (MSE): 1.6148464730328802e-07

Coeficientes de Ridge Regression: [ 3.40941045e-06 -5.44634081e+00  9.02988566e+00]
