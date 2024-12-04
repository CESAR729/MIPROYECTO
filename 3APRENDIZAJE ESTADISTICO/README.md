rimeros registros del dataset:
  DEPARTAMENTO PROVINCIA DISTRITO  ... TOTAL FECHA_CORTE   UBIGEO
0        CUSCO       NaN      NaN  ...     1    20230630      NaN
1        CUSCO       NaN      NaN  ...     1    20230630      NaN
2        CUSCO   ACOMAYO  ACOMAYO  ...     1    20230630  80201.0
3        CUSCO   ACOMAYO  ACOMAYO  ...     6    20230630  80201.0
4        CUSCO   ACOMAYO  ACOMAYO  ...    24    20230630  80201.0

[5 rows x 14 columns]

Nombres de las columnas:
Index(['DEPARTAMENTO', 'PROVINCIA', 'DISTRITO', 'RED', 'MICRORED', 'COD_EESS',
       'EESS', 'EDAD', 'ANIO', 'CASOS', 'NORMAL', 'TOTAL', 'FECHA_CORTE',
       'UBIGEO'],
      dtype='object')

Informaci�n general del dataset:
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
None

Estad�sticas descriptivas del dataset:
           COD_EESS          EDAD  ...  FECHA_CORTE        UBIGEO
count  56624.000000  83412.000000  ...      83412.0  83383.000000
mean    3876.395998     26.651681  ...   20230630.0  80706.155643
std     3529.290055     15.316684  ...          0.0    356.363623
min     2290.000000      0.000000  ...   20230630.0  80101.000000
25%     2356.000000     13.000000  ...   20230630.0  80405.000000
50%     2441.000000     25.000000  ...   20230630.0  80801.000000
75%     2534.000000     38.000000  ...   20230630.0  80910.000000
max    27016.000000     59.000000  ...   20230630.0  81307.000000

[8 rows x 8 columns]

Valores nulos en el dataset:
DEPARTAMENTO        0
PROVINCIA          12
DISTRITO           29
RED                 0
MICRORED            0
COD_EESS        26788
EESS                0
EDAD                0
ANIO                0
CASOS               0
NORMAL              0
TOTAL               0
FECHA_CORTE         0
UBIGEO             29
dtype: int64

Columnas num�ricas para la matriz de correlaci�n: Index(['COD_EESS', 'EDAD', 'ANIO', 'CASOS', 'NORMAL', 'TOTAL', 'FECHA_CORTE',
       'UBIGEO'],
      dtype='object')

Matriz de correlaci�n:
             COD_EESS      EDAD      ANIO  ...     TOTAL  FECHA_CORTE    UBIGEO
COD_EESS     1.000000 -0.007068  0.022099  ... -0.081884          NaN  0.105781
EDAD        -0.007068  1.000000  0.086282  ... -0.150340          NaN -0.011671
ANIO         0.022099  0.086282  1.000000  ...  0.074060          NaN -0.003159
CASOS       -0.062743 -0.164934  0.049874  ...  0.861607          NaN -0.082730
NORMAL      -0.080034 -0.089287  0.077232  ...  0.843251          NaN -0.118298
TOTAL       -0.081884 -0.150340  0.074060  ...  1.000000          NaN -0.117286
FECHA_CORTE       NaN       NaN       NaN  ...       NaN          NaN       NaN
UBIGEO       0.105781 -0.011671 -0.003159  ... -0.117286          NaN  1.000000

[8 rows x 8 columns]
![Matriz de Correlación](![alt text](image.png))
