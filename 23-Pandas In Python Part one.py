print('='*30)
import pandas as pd
p=pd.Series([0.25,0.50,0.75,1.0,1.25,1.50,1.75])
print('The Data Is => ',p)
'''
The Data Is =>  
0    0.25
1    0.50
2    0.75
3    1.00
4    1.25
5    1.50
6    1.75
dtype: float64
'''
print('='*20)
p_1=pd.Series((0.25,0.50,0.75,1.0,1.25,1.50,1.75))
print('The Data Is => ',p_1)
'''
The Data Is =>  
0    0.25
1    0.50
2    0.75
3    1.00
4    1.25
5    1.50
6    1.75
dtype: float64
'''
print('='*20)
print('The Values Only From Data Is => ',p_1.values)
#The Values Only From Data Is =>  [0.25 0.5  0.75 1.   1.25 1.5  1.75]
print('The Index Only From Data Is => ',p_1.index)
#The Index Only From Data Is =>  RangeIndex(start=0, stop=7, step=1)
print('The All Data Is => ',p_1.keys)
'''
The All Data Is =>  <bound method Series.keys of
0    0.25
1    0.50
2    0.75
3    1.00
4    1.25
5    1.50
6    1.75
dtype: float64>
'''
print('='*20)
p_2=pd.Series((3,6,9,8,5,4,2,6,3,5,8))
print('The Describe Of Data From P_2 Is => ',p_2.describe())
print('='*20)
'''
The Describe Of Data From P_2 Is =>  
count    11.000000
mean      5.363636
std       2.292280
min       2.000000
25%       3.500000
50%       5.000000
75%       7.000000
max       9.000000
dtype: float64
'''
print('The Aggregate Of Data From P_2 Is => ',p_2.agg(['max','min','sum','mean','std']))
print('='*20)
'''
The Aggregate Of Data From P_2 Is => 
max      9.000000        
min      2.000000
sum     59.000000
mean     5.363636
std      2.292280
dtype: float64
'''
print('The Second Element In P_1 Is => ',p_1[1])
#The Second Element In P_1 Is =>  0.5
print('The Second Element And Three Element In P_1 => ',p_1[1:3])
'''
The Second Element And Three Element In P_1 =>  
1    0.50      
2    0.75
dtype: float64
'''
print('The Second Element And Three Element Step 2 In P_1 => ',p_1[1:3:2])
#The Second Element And Three Element Step 2 In P_1 =>  1    0.5        dtype: float64
print('='*20)
p_3=pd.Series([1,2,3,4,5,6,7,8,9], index=['a','b','c','d','e','f','g','h','e'])
p_4=pd.Series({'a':'Alhousainy','b':'26 Years Old','c':'ML_ENG','d':90})
print('The Data P_3 Is => ',p_3)
'''
The Data P_3 Is =>  
a    1
b    2
c    3
d    4
e    5
f    6
g    7
h    8
e    9
dtype: int64
'''
print('The Data From Dictionary Is => ',p_4)
'''
The Data From Dictionary Is =>  
a      Alhousainy
b    26 Years Old
c          ML_ENG
d              90
dtype: object
'''
print('The Value Of Key A in p_3 Is => ',p_3['a'])
#The Value Of Key A in p_3 Is =>  1
print('The Value Of Key c in Dictionary Is => ',p_4['c'])
#The Value Of Key c in Dictionary Is =>  ML_ENG
print('='*20)
#=======================================================================================================
data=pd.Series((3,6,9,8,5,4,2,6,3,5,8))
data.plot()
print('='*20)
data.plot(kind='line')
print('='*20)
data.plot(kind='pie')
import matplotlib
print(matplotlib.__version__)