print('='*30)
import pandas as pd
import numpy as np
D=pd.DataFrame(np.random.rand(3,2),columns=['Food','Drink'],index=['A','B','C'])
print(D)
print('='*20)
'''
   Food     Drink
A  0.277246  0.716236
B  0.186033  0.456101
C  0.550240  0.304779
'''
D_1=pd.Series({'a':1,'b':2,'c':3,'d':4,'e':5})
D_2=pd.Series({'a':6,'b':7,'c':8,'d':9,'e':10})
D_3=pd.Series({'a':11,'b':12,'c':13,'d':14,'e':15})
D_4=pd.Series({'a':16,'b':17,'c':18,'d':19,'e':20})
DF=pd.DataFrame({'Math':D_1,'French':D_2,'Chemistry':D_3,'Physics':D_4})
print('The Original Data Is => ',DF)
'''
The Original Data Is =>     
     Math  French  Chemistry  Physics
a     1       6         11       16
b     2       7         12       17
c     3       8         13       18
d     4       9         14       19
e     5      10         15       20
'''
print('='*20)
DF['Total']=(DF['Math']+DF['French']+DF['Chemistry']+DF['Physics'])/100
print('The Data And Precentage Is => ',DF)
print('='*30)
'''
The Data And Precentage Is =>     
     Math  French  Chemistry  Physics  Total
a     1       6         11       16   0.34
b     2       7         12       17   0.38
c     3       8         13       18   0.42
d     4       9         14       19   0.46
e     5      10         15       20   0.50
'''
DF['Power']=np.power((DF['Math']+DF['French']+DF['Chemistry']+DF['Physics']),3)
print('The Data And Precentage And Power 3  Is => ',DF)
print('='*30)
'''
The Data And Precentage And Power 3  Is =>     
     Math  French  Chemistry  Physics   Total    Power
a     1       6         11       16    0.34     39304
b     2       7         12       17    0.38     54872
c     3       8         13       18    0.42     74088
d     4       9         14       19    0.46     97336
e     5      10         15       20    0.50    125000
'''
D_5=pd.DataFrame(np.random.rand(5,4),columns=['A','B','C','D'],index=['One','Two','Three','Four','Five'])
print('The Orignal Data Is ==> ',D_5)
'''
The Orignal Data Is ==>                
          A         B         C         D
One    0.556652  0.379637  0.750491  0.530015
Two    0.859041  0.501184  0.962533  0.779450
Three  0.814265  0.314709  0.689378  0.993475
Four   0.442715  0.353601  0.000909  0.329574
Five   0.097148  0.177346  0.248310  0.196040
'''
print('='*20)
D_5['Result']=(D_5['A']+D_5['B']+D_5['C']/D_5['D']-1)
print('The Result D_5 Is => ',D_5)
print('='*30)
'''
The Result D_5 Is =>                
          A         B         C         D       Result
One    0.556652  0.379637  0.750491  0.530015  1.352270
Two    0.859041  0.501184  0.962533  0.779450  1.595113
Three  0.814265  0.314709  0.689378  0.993475  0.822880
Four   0.442715  0.353601  0.000909  0.329574 -0.200925
Five   0.097148  0.177346  0.248310  0.196040  0.541124
'''
Result=(D_5['A']+D_5['B']+D_5['C']/D_5['D']-1)
print('The Result Only Is => ',Result)
'''
The Result Only Is =>  
One      1.440616
Two      0.894765
Three    1.902928
Four     0.842089
Five     0.499300
dtype: float64
'''
print('='*20)
Result_1=pd.eval('(D_5.A+D_5.B+D_5.C)/(D_5.D-1)')
print('The Result_1 Is => ',Result_1)
'''
The Result_1 Is =>  
One     -6.314756
Two     -1.473998
Three   -2.265661
Four    -3.236598
Five    -9.663370
dtype: float64
'''
print('='*20)
Result_2=D_5.query('A<0.5 and B<0.5')
print('The Result When A & B Is Lower Than From 0.5 Is => ',Result_2)
print('='*20)
'''
The Result When A & B Is Lower Than From 0.5 Is =>              
          A         B         C         D    Result
One  0.416672  0.390809  0.065547  0.338650  0.001035
Two  0.091829  0.120102  0.133270  0.181061 -0.052018
'''
tmp1=D_5.A<0.4
tmp2=D_5.B<0.2
tmp3=tmp1 & tmp2
Result_3=D_5[tmp3]
print('The Query Using Another Way Is => ',Result_3)
print('='*20)
'''
he Query Using Another Way Is =>               
         A        B        C         D    Result 
Four  0.066267  0.14328  0.88792  0.647112  0.581674
'''
Result_4=D_5[(D_5.A<0.6)&(D_5.B<0.6)]
print('The Result Is => ',Result_4)
print('='*20)
'''
The Result Is =>                
            A         B         C         D    Result
Two    0.382467  0.473889  0.443749  0.489340  0.763187
Three  0.458654  0.060823  0.854829  0.499385  1.231240
Five   0.350928  0.291591  0.762675  0.188749  3.683193
'''
Result_5=D_5[(D_5.A<0.5)| (D_5.B<0.5)]
print('The Result Is => ',Result_5)
'''
The Result Is =>                
          A         B         C         D    Result
Two    0.487304  0.424038  0.901386  0.171750  5.159573
Three  0.481809  0.631652  0.268098  0.466661  0.687964
Four   0.871175  0.468776  0.851831  0.206902  4.457020
Five   0.705292  0.014587  0.420802  0.803974  0.243281
'''
print('='*20)
def make_df(cols,ind):
    data={c:[str(c)+str(i) for i in ind]for c in cols}
    return pd.DataFrame(data,ind)
print(make_df('ABC',range(3)))
print('='*30)
'''
   A   B   C
0  A0  B0  C0
1  A1  B1  C1
2  A2  B2  C2
'''
def make_def2(index,columns):
    Data={j:[str(j)+str(k) for k in index] for j in columns }
    return pd.DataFrame(Data,index,columns)
List=['Egypt','KSA','USA','UAE','France','Germany','Russia','China','Japan','Libya','Sudan','Ghana','Sudan','Iraq','Plastine']
print(make_def2(range(15),List))
'''
   Egypt    KSA    USA      ...    Sudan    Iraq    Plastine
0    Egypt0   KSA0   USA0  ...   Sudan0   Iraq0   Plastine0       
1    Egypt1   KSA1   USA1  ...   Sudan1   Iraq1   Plastine1       
2    Egypt2   KSA2   USA2  ...   Sudan2   Iraq2   Plastine2       
3    Egypt3   KSA3   USA3  ...   Sudan3   Iraq3   Plastine3       
4    Egypt4   KSA4   USA4  ...   Sudan4   Iraq4   Plastine4       
5    Egypt5   KSA5   USA5  ...   Sudan5   Iraq5   Plastine5       
6    Egypt6   KSA6   USA6  ...   Sudan6   Iraq6   Plastine6       
7    Egypt7   KSA7   USA7  ...   Sudan7   Iraq7   Plastine7       
8    Egypt8   KSA8   USA8  ...   Sudan8   Iraq8   Plastine8       
9    Egypt9   KSA9   USA9  ...   Sudan9   Iraq9   Plastine9       
10  Egypt10  KSA10  USA10  ...  Sudan10  Iraq10  Plastine10       
11  Egypt11  KSA11  USA11  ...  Sudan11  Iraq11  Plastine11       
12  Egypt12  KSA12  USA12  ...  Sudan12  Iraq12  Plastine12       
13  Egypt13  KSA13  USA13  ...  Sudan13  Iraq13  Plastine13       
14  Egypt14  KSA14  USA14  ...  Sudan14  Iraq14  Plastine14   
'''
def make_def2(index,columns):
    Data={j:[str(j)+str(k) for k in index] for j in columns }
    return pd.DataFrame(Data,index)
List=['Egypt','KSA','USA','UAE','France','Germany','Russia','China','Japan','Libya','Sudan','Ghana','Sudan','Iraq','Plastine']
print(make_def2(range(15),List))
'''
     Egypt    KSA    USA  ...    Ghana    Iraq    Plastine       
0    Egypt0   KSA0   USA0  ...   Ghana0   Iraq0   Plastine0       
1    Egypt1   KSA1   USA1  ...   Ghana1   Iraq1   Plastine1       
2    Egypt2   KSA2   USA2  ...   Ghana2   Iraq2   Plastine2       
3    Egypt3   KSA3   USA3  ...   Ghana3   Iraq3   Plastine3       
4    Egypt4   KSA4   USA4  ...   Ghana4   Iraq4   Plastine4       
5    Egypt5   KSA5   USA5  ...   Ghana5   Iraq5   Plastine5       
6    Egypt6   KSA6   USA6  ...   Ghana6   Iraq6   Plastine6       
7    Egypt7   KSA7   USA7  ...   Ghana7   Iraq7   Plastine7       
8    Egypt8   KSA8   USA8  ...   Ghana8   Iraq8   Plastine8       
9    Egypt9   KSA9   USA9  ...   Ghana9   Iraq9   Plastine9       
10  Egypt10  KSA10  USA10  ...  Ghana10  Iraq10  Plastine10       
11  Egypt11  KSA11  USA11  ...  Ghana11  Iraq11  Plastine11       
12  Egypt12  KSA12  USA12  ...  Ghana12  Iraq12  Plastine12       
13  Egypt13  KSA13  USA13  ...  Ghana13  Iraq13  Plastine13       
14  Egypt14  KSA14  USA14  ...  Ghana14  Iraq14  Plastine14       

[15 rows x 14 columns]
'''