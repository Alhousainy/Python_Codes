print('='*30)
import pandas as pd
import numpy as np 
myarray=np.array([[6,9,8,5,4,2],[0,2,5,6,3,9],[8,5,4,1,2,3],
[6,9,8,5,4,2],[0,5,3,6,9,8],[8,7,4,5,2,3]])
rownames=['A','B','C','D','E','F']
colnames=['One','Two','Three','Four','Five','Six']
DF=pd.DataFrame(myarray,index=rownames,columns=colnames)
print('The Data Is ')
print(DF)
'''
The Data Is 
   One  Two  Three  Four  Five  Six
A    6    9      8     5     4    2
B    0    2      5     6     3    9
C    8    5      4     1     2    3
D    6    9      8     5     4    2
E    0    5      3     6     9    8
F    8    7      4     5     2    3
'''
print('='*20)
D=pd.Series({'a':1,'b':2,'c':3,'d':4,'e':5})
D_1=pd.Series({'a':6,'b':7,'c':8,'d':9,'e':10})
D_2=pd.Series({'a':11,'b':12,'c':13,'d':14,'e':15})
D_3=pd.Series({'a':16,'b':17,'c':18,'d':19,'e':20})
DF_1=pd.DataFrame({'Math':D,'French':D_1,'Physics':D_2,'Germany':D_3})
print('The Data Is => ',DF_1)
print('='*30)
'''
The Data Is =>     
    Math    French  Physics   Germany
a     1       6       11       16
b     2       7       12       17
c     3       8       13       18
d     4       9       14       19
e     5      10       15       20
'''
print('The Columns Of Math Is => ',DF_1['Math'])
'''
The Columns Of Math Is =>  
a    1
b    2
c    3
d    4
e    5
Name: Math, dtype: int64
'''
print('='*20)
print('The Transpose Data Is => ',DF_1.T)
'''
The Transpose Data Is =>            
          a   b   c   d   e
Math      1   2   3   4   5
French    6   7   8   9  10
Physics  11  12  13  14  15
Germany  16  17  18  19  20
'''
print('='*20)
print('The Keys In Dictionary Is => ',DF_1.keys())
#The Keys In Dictionary Is =>  Index(['Math', 'French', 'Physics', 'Germany'], dtype='object')
print('The Keys In Dictionary Is => ',DF_1.keys)
'''
The Keys In Dictionary Is =>  <bound method NDFrame.keys of    
     Math  French  Physics  Germany
a     1       6       11       16
b     2       7       12       17
c     3       8       13       18
d     4       9       14       19
e     5      10       15       20>
'''
print('The Values Of Dictionary Is => ',DF_1.values)
'''
The Values Of Dictionary Is =>  
[[ 1  6 11 16]
[ 2  7 12 17]
[ 3  8 13 18]
[ 4  9 14 19]
[ 5 10 15 20]]
'''
print('='*20)
print('The Index Only In The Dictionary Is => ',DF_1.index)
#The Index Only In The Dictionary Is =>  Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
print('='*20)
print('The Math In Keys Of Data Frame 1 => ','Math' in DF_1.keys())
#The Math In Keys Of Data Frame 1 =>  True
print('Science In Keys Of Data Frame 1 => ','Science' in DF_1.keys())
#Science In Keys Of Data Frame 1 =>  False
print('The Value Of 12 In DF_1 => ',12 in DF_1.values)
#The Value Of 12 In DF_1 =>  True
print('The Value 25 In DF_1 => ',25 in DF_1.values)
#The Value 25 In DF_1 =>  False
print('='*30)
print('The SubList Of Data  1 After Using .Stack Is => ',DF_1.stack())
'''
he SubList Of Data  1 After Using .Stack Is =>  
a  Math        1 
   French      6
   Physics    11
   Germany    16
b  Math        2
   French      7
   Physics    12
   Germany    17
c  Math        3
   French      8
   Physics    13
   Germany    18
d  Math        4
   French      9
   Physics    14
   Germany    19
e  Math        5
   French     10
   Physics    15
   Germany    20
dtype: int64
'''
print('='*30)
print('The Data From Row 0 To Row 2 And From Col 0 To 1 Is => ',DF_1.iloc[:3,:2])
'''
The Data From Row 0 To Row 2 And From Col 0 To 1 Is =>    
     Math  French
a     1       6
b     2       7
c     3       8
'''
print('='*30)
print('The Row 1 Is => ',DF_1.iloc[0,:])
#The Row 1 Is =>  Math  French  Physics   Germany      
#                  1      6       11        16   
print('The Row 2 Is => ',DF_1.iloc[1,:])
#The Row 2 Is =>  Math  French  Physics   Germany      
#                  2      7       12        17
print('The Row 3 Is => ',DF_1.iloc[2,:])
#The Row 2 Is =>  Math  French  Physics   Germany      
#                  3      8       13        18
print('='*30)
print('The Data From Row 0 and Row 2 and From Math To Physics' ,DF_1.loc['a':'c','Math':'Physics'])
'''
The Data From Row 0 and Row 2 and From Math To Physics    
     Math  French  Physics
a     1       6       11
b     2       7       12
c     3       8       13
'''
print('='*30)
print('The Grades Of Studen But Math Is Greater Than From 3 Is => ',DF_1.loc[DF_1.Math>3])
'''
The Grades Of Studen But Math Is Greater Than From 3 Is =>     
     Math  French  Physics  Germany
d     4       9       14       19
e     5      10       15       20
'''
print('='*30)
print('The Grades Of Studen But French Is Greater Than From 7 Is => ',DF_1.loc[DF_1.French>7])
'''
The Grades Of Studen But French Is Greater Than From 7 Is =>    
     Math  French  Physics  Germany
c     3       8       13       18
d     4       9       14       19
e     5      10       15       20
'''
print('='*20)
print('The Data of Math And Germany But Is Math> 3 Is => ',DF_1.loc[DF_1.Math>3,['Math','Germany']])
print('='*20)
'''
The Data of Math And Germany But Is Math> 3 Is =>     
     Math  Germany
d     4       19
e     5       20
'''
#print(DF_1.loc[DF_1.Math>2 and  DF_1.French>7])
#print(DF_1[(DF_1['Math']>3) and (DF_1['Physics']>13)])
#print(DF_1.loc[DF_1.Math>2 or DF_1.Physics>12])
#print(DF_1.loc[DF_1.Math > 3 , DF_1.Physics>13])
#print(  grades.loc [ (grades.Math>3)  &  (grades.French>5) ] )
print(DF_1.loc[(DF_1.Math>3) & (DF_1.Physics>13) ])
'''
     Math  French  Physics  Germany
d     4       9       14       19
e     5      10       15       20
'''
print('The Data Is => ',DF_1.loc[(DF_1.Math>3) | (DF_1.Physics>13) ])
'''
The Data Is =>     
   Math  French  Physics  Germany
d     4       9       14       19
e     5      10       15       20
'''
print('='*20)
print('The Name Of Columns Is => ',DF_1.columns)
#The Name Of Columns Is =>  Index(['Math', 'French', 'Physics', 'Germany'], dtype='object')
print('The Name Of Rows Is => ',DF_1.index)
#The Name Of Rows Is =>  Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
print('The All Grade But Math Only Is => ',DF_1['Math'])
'''
The All Grade But Math Only Is =>  
a    1
b    2
c    3
d    4
e    5
Name: Math, dtype: int64
'''
print('The All Data But Arange Is Descending About Values Of Math Is => ',DF_1.sort_values(['Math'],
ascending=False))
'''
The All Data But Arange Is Descending About Values Of Math Is =>     
     Math  French  Physics  Germany
e     5      10       15       20
d     4       9       14       19
c     3       8       13       18
b     2       7       12       17
a     1       6       11       16
'''
print('='*20)
print('The Arnage Data Ascending For Values Of French Is => ',DF_1.sort_values(['French'],ascending=True))
'''
The Arnage Data Ascending For Values Of French Is =>     
     Math  French  Physics  Germany
a     1       6       11       16
b     2       7       12       17
c     3       8       13       18
d     4       9       14       19
e     5      10       15       20
'''
print('='*20)
print('The Descibe Of Dataframe Is => ',DF_1.describe())
'''
The Descibe Of Dataframe Is =>             
         Math     French    Physics    Germany
count  5.000000   5.000000   5.000000   5.000000
mean   3.000000   8.000000  13.000000  18.000000
std    1.581139   1.581139   1.581139   1.581139
min    1.000000   6.000000  11.000000  16.000000
25%    2.000000   7.000000  12.000000  17.000000
50%    3.000000   8.000000  13.000000  18.000000
75%    4.000000   9.000000  14.000000  19.000000
max    5.000000  10.000000  15.000000  20.000000
'''
print('='*30)
print('The Max Value In All Columns Is => ',DF_1.max())
'''
The Max Value In All Columns Is =>  
Math        5
French     10
Physics    15
Germany    20
dtype: int64
'''
print('='*20)
print('The Min Value In All Columns Is => ',DF_1.min())
'''
The Min Value In All Columns Is =>  
Math        1
French      6
Physics    11
Germany    16
dtype: int64
'''
print('='*20)
print('The Mean Value In All Columns Is =>  ',DF_1.mean())
'''
The Mean Value In All Columns Is =>   
Math        3.0
French      8.0
Physics    13.0
Germany    18.0
dtype: float64
'''
print('='*20)
print('The standard deviation For All Columns Is => ',DF_1.std())
'''
The standard deviation For All Columns Is =>  
Math       1.581139 
French     1.581139
Physics    1.581139
Germany    1.581139
dtype: float64
'''
print('='*20)
print('The Aggregate Values Is => ',DF_1.agg(['sum','count','max','min','var','std','mean','median']))
'''
The Aggregate Values Is =>               
          Math     French    Physics    Germany
sum     15.000000  40.000000  65.000000  90.000000
count    5.000000   5.000000   5.000000   5.000000
max      5.000000  10.000000  15.000000  20.000000
min      1.000000   6.000000  11.000000  16.000000
var      2.500000   2.500000   2.500000   2.500000
std      1.581139   1.581139   1.581139   1.581139
mean     3.000000   8.000000  13.000000  18.000000
median   3.000000   8.000000  13.000000  18.000000
'''
print('='*20)
print('The Max Value For Mathmatics Is => ',DF_1['Math'].max())
#The Max Value For Mathmatics Is =>  5
print('The minimum Value For Mathmatics Is => ',DF_1['Math'].min())
#The minimum Value For Mathmatics Is =>  1
print('The Describe All Value For Mathmatics Is => ',DF_1['Math'].describe())
'''
The Describe All Value For Mathmatics Is =>  
count    5.000000    
mean     3.000000
std      1.581139
min      1.000000
25%      2.000000
50%      3.000000
75%      4.000000
max      5.000000
Name: Math, dtype: float64
'''
print('The Aggregate Values For Mathmatics Is => ',DF_1['Math'].agg(['max','min','count','sum','var']))
'''
The Aggregate Values For Mathmatics Is =>  
max       5.0
min       1.0
count     5.0
sum      15.0
var       2.5
Name: Math, dtype: float64
'''
print('='*20)
DF_2=pd.DataFrame(np.random.rand(7,5),columns=['A','B','C','D','E'])
print('The Data Is => ',DF_2)
'''
The Data Is =>           
       A         B         C         D         E
0  0.660989  0.782472  0.695480  0.604662  0.199086
1  0.887303  0.321313  0.208181  0.782739  0.143335
2  0.661092  0.655815  0.051252  0.155536  0.004132
3  0.315523  0.940351  0.546101  0.497173  0.506895
4  0.070725  0.340350  0.213594  0.710887  0.923051
5  0.904006  0.667543  0.535448  0.440866  0.603644
6  0.800635  0.165220  0.142850  0.904470  0.897671
'''
print('='*30)
print('The Correlation Cofficient For Data Is => ',DF_2.corr())
'''
The Correlation Cofficient For Data Is =>            
      A         B         C         D         E
A  1.000000 -0.165197 -0.012800  0.022374 -0.383544
B -0.165197  1.000000  0.693392 -0.682966 -0.431557
C -0.012800  0.693392  1.000000 -0.055233 -0.049178
D  0.022374 -0.682966 -0.055233  1.000000  0.552033
E -0.383544 -0.431557 -0.049178  0.552033  1.000000
'''
print('='*30)
print('The Skew Of Data Is => ',DF_2.skew())
'''
The Skew Of Data Is => 
A    0.488324
B   -1.560599
C    0.435424
D    1.169119
E    0.050619
dtype: float64
'''
print('='*20)
Row_Names=['A','B','C','D','E','F','G','H','O','M']
D1=[{'Cube':np.power(i,3)} for i in range(10)]
DF_3=pd.DataFrame(D1,index=Row_Names)
print(DF_3)
'''
  Cube
A     0
B     1
C     8
D    27
E    64
F   125
G   216
H   343
O   512
M   729
'''
print('='*30)
D2=[{'Number':i,'Square':np.power(i,2),'Cube':np.power(i,3),'Roots':i*0.5} for i in range(10)]
DF_4=pd.DataFrame(D2,index=Row_Names)
print(DF_4)
'''
       Number  Square  Cube  Roots
A       0       0     0    0.0
B       1       1     1    0.5
C       2       4     8    1.0
D       3       9    27    1.5
E       4      16    64    2.0
F       5      25   125    2.5
G       6      36   216    3.0
H       7      49   343    3.5
O       8      64   512    4.0
M       9      81   729    4.5
'''
print('='*30)
D3=[{'a':1,'b':2},{'a':3,'b':4},{'a':5,'b':6},{'a':7,'b':8}]
DF_5=pd.DataFrame(D3)
print(DF_5)
'''
  a  b
0  1  2
1  3  4
2  5  6
3  7  8
'''
print('='*30)
D4=[{'a':1,'b':2},{'b':3,'c':4},{'c':5,'d':6},{'e':7,'f':8}]
DF_6=pd.DataFrame(D4)
print(DF_6)
'''
    a    b    c    d    e    f
0  1.0  2.0  NaN  NaN  NaN  NaN
1  NaN  3.0  4.0  NaN  NaN  NaN
2  NaN  NaN  5.0  6.0  NaN  NaN
3  NaN  NaN  NaN  NaN  7.0  8.0
'''
print('='*30)