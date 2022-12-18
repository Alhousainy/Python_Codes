print('='*30)
import numpy as np 
import pandas as pd 
F=pd.read_csv('D:\\Programming\\Machine learning Python\\Files\\iris.csv')
print(F.head())
'''
        sepal.length   sepal.width  petal.length   petal.width     variety
0           5.1          3.5           1.4          0.2           Setosa
1           4.9          3.0           1.4          0.2           Setosa
2           4.7          3.2           1.3          0.2           Setosa
3           4.6          3.1           1.5          0.2           Setosa
4           5.0          3.6           1.4          0.2           Setosa
'''
print('='*30)
F1=pd.read_csv('D:\\Programming\\Machine learning Python\\Files\\4.csv')
print(F1.head())
'''
    Id    SepalLengthCm      SepalWidthCm       PetalLengthCm       PetalWidthCm     Species
0   1        5.1                 3.5               1.4                   0.2        Iris-setosa                                                
1   2        4.9                  3                1.4                   0.2        Iris-setosa      
2   3        4.7                 3.2               1.3                   0.2        Iris-setosa                            
3   4        4.6                 3.1               1.5                   0.2        Iris-setosa                                     
'''
print('='*30)
print(F.head(20))
'''
         sepal.length  sepal.width  ...      petal.width      variety
0            5.1          3.5       ...          0.2          Setosa
1            4.9          3.0       ...          0.2          Setosa
2            4.7          3.2       ...          0.2          Setosa
3            4.6          3.1       ...          0.2          Setosa
4            5.0          3.6       ...          0.2          Setosa
5            7.0          3.2       ...          1.4          Versicolor
6            6.4          3.2       ...          1.5          Versicolor
7            6.9          3.1       ...          1.5          Versicolor
8            5.5          2.3       ...          1.3          Versicolor
9            6.5          2.8       ...          1.5          Versicolor
10           5.7          2.8       ...          1.3          Versicolor
11           6.3          3.3       ...          2.5          Virginica
12           5.8          2.7       ...          1.9          Virginica
13           7.1          3.0       ...          2.1          Virginica
14           6.3          2.9       ...          1.8          Virginica
15           6.5          3.0       ...          2.2          Virginica
16           7.6          3.0       ...          2.1          Virginica
17           4.9          2.5       ...          1.7          Virginica
18           5.4          3.9       ...          0.4          Setosa
19           4.6          3.4       ...          0.3          Setosa
[20 rows x 5 columns]
'''
F1_1=pd.read_csv('D:\\Programming\\Machine learning Python\\Files\\iris.csv')
print(F1_1)
'''
  sepal.length  sepal.width  petal.length  petal.width    variety
0            5.1          3.5           1.4          0.2     Setosa 
1            4.9          3.0           1.4          0.2     Setosa 
2            4.7          3.2           1.3          0.2     Setosa 
3            4.6          3.1           1.5          0.2     Setosa 
4            5.0          3.6           1.4          0.2     Setosa 
..           ...          ...           ...          ...        ... 
58           6.0          2.2           5.0          1.5  Virginica 
59           6.9          3.2           5.7          2.3  Virginica 
60           5.6          2.8           4.9          2.0  Virginica 
61           7.7          2.8           6.7          2.0  Virginica 
62           5.7          3.8           1.7          0.3     Setosa
'''
print('='*30)
F1_2=pd.read_csv('D:\\Programming\\Machine learning Python\\Files\\iris.csv',index_col='variety')
print(F1_2.head(20))
'''
                sepal.length    sepal.width    petal.length   petal.width
variety
Setosa               5.1          3.5           1.4          0.2    
Setosa               4.9          3.0           1.4          0.2    
Setosa               4.7          3.2           1.3          0.2    
Setosa               4.6          3.1           1.5          0.2    
Setosa               5.0          3.6           1.4          0.2    
Versicolor           7.0          3.2           4.7          1.4    
Versicolor           6.4          3.2           4.5          1.5    
Versicolor           6.9          3.1           4.9          1.5    
Versicolor           5.5          2.3           4.0          1.3    
Versicolor           6.5          2.8           4.6          1.5    
Versicolor           5.7          2.8           4.5          1.3    
Virginica            6.3          3.3           6.0          2.5    
Virginica            5.8          2.7           5.1          1.9    
Virginica            7.1          3.0           5.9          2.1    
Virginica            6.3          2.9           5.6          1.8    
Virginica            6.5          3.0           5.8          2.2    
Virginica            7.6          3.0           6.6          2.1    
Virginica            4.9          2.5           4.5          1.7    
Setosa               5.4          3.9           1.7          0.4    
Setosa               4.6          3.4           1.4          0.3 
'''
print('='*30)
D1=pd.Series({'a':1,'b':2,'c':3,'d':4,'e':5})
D2=pd.Series({'a':6,'b':7,'c':8,'d':9,'e':10})
D3=pd.Series({'a':11,'b':12,'c':13,'d':14,'e':15})
D4=pd.Series({'a':16,'b':17,'c':18,'d':19,'e':20})
DF=pd.DataFrame({'Math':D1,'Physics':D2,'Science':D3,'Chemistry':D4})
print(DF)
print('='*30)
DF.to_csv('D:\\Programming\\Machine learning Python\\Files\\Subjects.csv')
print(DF.head())
print('='*30)
filename='D:\\Programming\\Machine learning Python\\Files\\Subjects.csv'
names=['One','Two','Three','Four','Five']
data=pd.read_csv(filename,names=names)
print(data)
'''
   One   Two    Three     Four       Five
0  NaN  Math  Physics  Science  Chemistry
1    a     1        6       11         16
2    b     2        7       12         17
3    c     3        8       13         18
4    d     4        9       14         19
5    e     5       10       15         20
'''
print('='*30)
filename1='D:\\Programming\\Machine learning Python\\Files\\diabetes.csv'
names1=['preg','plas','pres','skin','test','mass','pedi','age','class']
data1=pd.read_csv(filename1,names=names1)
print(data1)
'''
  preg     plas  ...  age    class
0  Pregnancies  Glucose  ...  Age  Outcome
1            6      148  ...   50        1
2            1       85  ...   31        0
3            8      183  ...   32        1
4            1       89  ...   21        0
5            0      137  ...   33        1
6            5      116  ...   30        0
7            3       78  ...   26        1
8           10      115  ...   29        0
9            2      197  ...   53        1
'''
from pandas import read_csv
from pandas import set_option
print('='*20)
'''set_option('display.width',50)
set_option('precision',3)
desc=data1.describe()
print(desc)'''

set_option('display.width', 100)
set_option('display.precision', 3)
description = data1.describe()
print(description)
'''
        preg plas pres skin test mass   pedi  age class
count   769  769  769  769  769  769    769  769   769
unique   18  137   48   52  187  249    518   53     3
top       1  100   70    0    0   32  0.254   22     0
freq    135   17   57  227  374   13      6   72   500
'''
print('='*30)
class_counts=data1.groupby('class').size()
print(class_counts)
'''
class
0          500
1          268
Outcome      1
dtype: int64
'''
print('='*15)
corrleations=data1.corr(method='pearson')
print(corrleations)
'''
Empty DataFrame
Columns: []
Index: []
'''
print('='*20)
df=data1.skew()
#print(df)
