Primeros registros:
  DEPARTAMENTO PROVINCIA DISTRITO                        RED      MICRORED  \
0        CUSCO       NaN      NaN  CANAS - CANCHIS - ESPINAR  TECHO OBRERO   
1        CUSCO       NaN      NaN                  CUSCO SUR    HUANCARANI   
2        CUSCO   ACOMAYO  ACOMAYO                  CUSCO SUR       ACOMAYO   
3        CUSCO   ACOMAYO  ACOMAYO                  CUSCO SUR       ACOMAYO   
4        CUSCO   ACOMAYO  ACOMAYO                  CUSCO SUR       ACOMAYO   

   COD_EESS             EESS  EDAD  ANIO  CASOS  NORMAL  TOTAL  FECHA_CORTE  \
0    2390.0       P.S. CCUYO     4  2017      0       1      1     20230630   
1       NaN  C.S. HUANCARANI    41  2010      0       1      1     20230630   
2       NaN     C.S. ACOMAYO     5  2010      1       0      1     20230630   
3       NaN     C.S. ACOMAYO     5  2013      5       1      6     20230630   
4       NaN     C.S. ACOMAYO     6  2010      3      21     24     20230630   

    UBIGEO  
0      NaN  
1      NaN  
2  80201.0  
3  80201.0  
4  80201.0  

Nombres de columnas:
Index(['DEPARTAMENTO', 'PROVINCIA', 'DISTRITO', 'RED', 'MICRORED', 'COD_EESS',
       'EESS', 'EDAD', 'ANIO', 'CASOS', 'NORMAL', 'TOTAL', 'FECHA_CORTE',
       'UBIGEO'],
      dtype='object')

Información general del dataset:
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

Valor esperado de 'CASOS': 1.85