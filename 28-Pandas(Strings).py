print('='*30)
import numpy as np 
import pandas as pd
names=['Alhousainy','ahmed','MARAH','Mona','Khalad','Raouf','20',' ']
print(pd.Series(names).str.len())
'''
0    10
1     5
2     5
3     4
4     6
5     5
6     2
7     0
dtype: int64
'''
print('='*10)
print(pd.Series(names).str.startswith('A'))
'''
0     True
1    False
2    False
3    False
4    False
5    False
6    False
7    False
dtype: bool
'''
print('='*10)
print(pd.Series(names).str.endswith('H'))
'''
0    False
1    False
2     True
3    False
4    False
5    False
6    False
7    False
dtype: bool
'''
print('='*10)
print(pd.Series(names).str.find('A'))
'''
0    0
1   -1
2    1
3   -1
4   -1
5   -1
6   -1
7   -1
dtype: int64
'''
print('='*10)
print(pd.Series(names).str.rfind('A'))
'''
0    0
1   -1
2    3
3   -1
4   -1
5   -1
6   -1
7   -1
dtype: int64
'''
print('='*10)
print(pd.Series(names).str.rjust(20))
'''
0              Alhousainy
1                   ahmed
2                   MARAH
3                    Mona
4                  Khalad
5                   Raouf
6                      20
7
dtype: object
'''
print('='*10)
print(pd.Series(names).str.ljust(50))
'''
0    Alhousainy                                    ...
1    ahmed                                         ...
2    MARAH                                         ...
3    Mona                                          ...
4    Khalad                                        ...
5    Raouf                                         ...
6    20                                            ...
7                                                  ...
dtype: object
'''
print('='*10)
print(pd.Series(names).str.center(15))
'''
0       Alhousainy
1         ahmed
2         MARAH
3          Mona
4         Khalad
5         Raouf
6           20
7
dtype: object
'''
print('='*10)
print(pd.Series(names).str.zfill(12))
'''
0    00Alhousainy
1    0000000ahmed
2    0000000MARAH
3    00000000Mona
4    000000Khalad
5    0000000Raouf
6    000000000020
7    000000000000
dtype: object
'''
print('='*10)
print(pd.Series(names).str.lower())
'''
0    alhousainy
1         ahmed
2         marah
3          mona
4        khalad
5         raouf
6            20
7
dtype: object
'''
print('='*10)
print(pd.Series(names).str.upper())
'''
0    ALHOUSAINY
1         AHMED
2         MARAH
3          MONA
4        KHALAD
5         RAOUF
6            20
7
dtype: object
'''
print('='*10)
print(pd.Series(names).str.title())
'''
0    Alhousainy
1         Ahmed
2         Marah
3          Mona
4        Khalad
5         Raouf
6            20
7
dtype: object
'''
print('='*10)
print(pd.Series(names).str.islower())
'''
0    False
1     True
2    False
3    False
4    False
5    False
6    False
7    False
dtype: bool
'''
print('='*10)
print(pd.Series(names).str.isupper())
'''
0    False
1    False
2     True
3    False
4    False
5    False
6    False
7    False
dtype: bool
'''
print('='*10)
print(pd.Series(names).str.istitle())
'''
0     True
1    False
2    False
3     True
4     True
5     True
6    False
7    False
dtype: bool
'''
print('='*10)
print(pd.Series(names).str.isspace())
'''
0    False
1    False
2    False
3    False
4    False
5    False
6    False
7    False
dtype: bool
'''
print('='*10)
print(pd.Series(names).str.isdigit())
'''
0    False
1    False
2    False
3    False
4    False
5    False
6     True
7    False
dtype: bool
'''
print('='*10)
print(pd.Series(names).str.isalpha())
'''
0     True
1     True
2     True
3     True
4     True
5     True
6    False
7    False
dtype: bool
'''
print('='*10)
