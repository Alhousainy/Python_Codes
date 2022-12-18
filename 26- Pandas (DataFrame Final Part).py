print('='*30)
from heapq import merge
import pandas as pd
import numpy as np
D1=pd.DataFrame({'Employee':['Alhousainy','Ahmed','Mostafa','Dina','Bahaa'],'Group':['Student','Engineer','Accountant',
'HR','Doctor']},index=['One','Two','Three','Four','Five'])
print(D1)
'''
         Employee       Group
One    Alhousainy     Student
Two         Ahmed    Engineer
Three     Mostafa  Accountant
Four         Dina          HR
Five        Bahaa      Doctor
'''
print('='*20)
D1_1=pd.DataFrame({'Employee':['Alhousainy','Ahmed','Mostafa','Dina','Bahaa'],'Hire_Date':[2004,2008,
2012,2016,2020]},index=['One','Two','Three','Four','Five'])
print(D1_1)
'''
          Employee  Hire_Date
One    Alhousainy       2004
Two         Ahmed       2008
Three     Mostafa       2012
Four         Dina       2016
Five        Bahaa       2020
'''
print('='*20)
DF_Merge=pd.merge(D1,D1_1)
print(DF_Merge)
'''
        Employee       Group  Hire_Date
0  Alhousainy     Student       2004
1       Ahmed    Engineer       2008
2     Mostafa  Accountant       2012
3        Dina          HR       2016
4       Bahaa      Doctor       2020
'''
print('='*30)
D1_3=pd.DataFrame({'Employee1':['Alhousainy','Ahmed','Mostafa','Dina','Bahaa'],
'Group':['Engineer','Lawyer','Accountant','HR','Doctor']})
D1_4=pd.DataFrame({'Employee1':['Alhousainy','Ahmed','Mostafa','Dina','Bahaa'],
'Hire_Date':[2004,2008,2012,2016,2020]})
D1_5=pd.DataFrame({'Group':['Engineer','Lawyer','Accountant','HR','Doctor'],
'Supervisior':['Ahmed','Seddik','Mohammed','Mostafa','Khalad']})
D1_6=pd.DataFrame({'Employee1':['Alhousainy','Ahmed','Mostafa','Dina','Bahaa'],
'Country':['Egypt','Syria','USA','UAE','KSA']})
D1_7=pd.DataFrame({'Employee1':['Alhousainy','Ahmed','Mostafa','Dina','Bahaa'],
'Job':['ML Eng','Judge','Kashir','ISFP HR','Dentist']})
DF_1=pd.merge(D1_3,D1_4)
print(DF_1)
'''
      Employee       Group       Hire_Date
0  Alhousainy       Engineer       2004
1       Ahmed       Engineer       2008
2     Mostafa       Accountant     2012
3        Dina          HR          2016
4       Bahaa        Doctor        2020
'''
print('='*15)
DF_2=pd.merge(D1_5,DF_1)
print(DF_2)
'''
       Group       Supervisior    Employee     Hire_Date
0    Engineer       Ahmed        Alhousainy      2004
1    Engineer       Ahmed        Ahmed           2008
2    Engineer      Seddik       Alhousainy       2004
3    Engineer      Seddik       Ahmed            2008
4  Accountant    Mohammed       Mostafa          2012
5          HR     Mostafa        Dina            2016
6      Doctor      Khalad       Bahaa            2020
'''
print('='*30)
DF_3=pd.merge(DF_2,D1_6)
print(DF_3)
'''
       Group      Supervisior    Employee      Hire_Date    Country
0    Engineer       Ahmed       Alhousainy       2004       Egypt
1    Engineer      Seddik       Alhousainy       2004       Egypt
2    Engineer       Ahmed       Ahmed            2008       Syria
3    Engineer      Seddik       Ahmed            2008       Syria
4  Accountant    Mohammed       Mostafa          2012       USA
5          HR     Mostafa        Dina            2016       UAE
6      Doctor      Khalad        Bahaa           2020       KSA

'''
print('='*30)
DF_4=pd.merge(DF_3,D1_7)
print(DF_4)
'''
        Group      Supervisior   Employee1    Hire_Date   Country      Job
0    Engineer       Ahmed        Alhousainy      2004     Egypt      ML Eng
1      Lawyer      Seddik        Ahmed           2008     Syria      Judge
2  Accountant    Mohammed        Mostafa         2012     USA        Kashir
3          HR     Mostafa        Dina            2016     UAE        ISFP HR
4      Doctor      Khalad        Bahaa           2020     KSA        Dentist
'''
print('='*30)
D2=pd.DataFrame({'Employee':['Alhousainy','Ahmed','Mostafa','Dina','Bahaa'],
'Group':['Engineer','Lawyer','Accountant','HR','Doctor']})
D2_1=pd.DataFrame({'Employee':['Alhousainy','Ahmed','Mostafa','Dina','Bahaa'],
'Hire_Date':[2004,2008,2012,2016,2020]})
D2_2=pd.DataFrame({'Name':['Alhousainy','Ahmed','Mostafa','Dina','Bahaa'],
'Salary':[6000,5000,7000,10000,70000]})
print('The Merge Is => ',pd.merge(D2,D2_2,left_on='Employee',right_on='Name'))
''' 
        Employee        Group         Name       Salary
0       Alhousainy     Engineer     Alhousainy    6000
1       Ahmed          Lawyer       Ahmed         5000
2       Mostafa       Accountant    Mostafa       7000
3        Dina          HR           Dina          10000
4        Bahaa         Doctor       Bahaa         70000
'''
print('='*30)
print('The Merge Data After Drop Name Column Is => ',pd.merge(D2,D2_2,left_on='Employee',
right_on='Name').drop('Name',axis=1))
'''
The Merge Data After Drop Name Column Is =>      
      Employee       Group  Salary
0  Alhousainy    Engineer    6000
1       Ahmed      Lawyer    5000
2     Mostafa  Accountant    7000
3        Dina          HR   10000
4       Bahaa      Doctor   70000
'''
print('='*30)
DF_5=D2.set_index('Employee')
print('The Keys After Change Is => ',DF_5)
'''
he Keys After Change Is =>                   
Employee        Group
Alhousainy     Engineer
Ahmed          Lawyer
Mostafa        Accountant
Dina           HR
Bahaa          Doctor
'''
print('='*30)
D2_3=pd.DataFrame({'Name':['Ahmed','Mostafa','Mona'],'Food':['Fish','Beans','Bread']},
columns=['Name','Food'])
D2_4=pd.DataFrame({'Name':['Mostafa','Marwa'],'Drink':['Cola','Tea']},
columns=['Name','Drink'])
print(D2_3)
'''
  Name   Food
0    Ahmed   Fish
1  Mostafa  Beans
2     Mona  Bread
'''
print('='*10)
print(D2_4)
'''
   Name Drink
0  Mostafa  Cola
1    Marwa   Tea
'''
print('='*10)
print('Mearge Is => ',pd.merge(D2_3,D2_4))
'''
Mearge Is =>        
     Name   Food   Drink
0  Mostafa  Beans  Cola
'''
print('='*10)
print('The Merge Using Inner Method => ',pd.merge(D2_3,D2_4,how='inner'))
'''
The Merge Using Inner Method =>       
     Name   Food Drink
0  Mostafa  Beans  Cola
'''
print('='*30)
print('The All Data Is => ',pd.merge(D2_3,D2_4,how='outer'))
'''
      Name   Food   Drink
0    Ahmed   Fish   NaN
1  Mostafa  Beans  Cola
2     Mona  Bread   NaN
3    Marwa    NaN   Tea
'''
print('='*10)
print('The All Data In D2_4 Is => ',pd.merge(D2_3,D2_4,how='right'))
'''
   Name      Food   Drink
0  Mostafa  Beans   Cola
1    Marwa   NaN    Tea
'''
print('='*10)
print('The All Data In D2_3 Is => ',pd.merge(D2_3,D2_4,how='left'))
'''
    Name     Food   Drink
0    Ahmed   Fish    NaN
1  Mostafa  Beans    Cola
2     Mona  Bread    NaN
'''
print('='*10)
D2_5=pd.DataFrame({'A':np.random.rand(10),'B':np.random.rand(10),'C':np.random.rand(10)})
print(D2_5)
'''
   A         B         C
0  0.402297  0.386654  0.824529
1  0.771907  0.045312  0.587070
2  0.671903  0.477360  0.063772
3  0.297403  0.213931  0.768612
4  0.513746  0.427687  0.840732
5  0.346199  0.363498  0.045558
6  0.081024  0.189701  0.018563
7  0.353776  0.000285  0.136009
8  0.973711  0.977013  0.143021
9  0.723175  0.753988  0.749291
'''
print('='*10)
print('The Sum For Columns Is => ',D2_5.sum())
'''
A    5.135139
B    3.835428
C    4.177156
dtype: float64
'''
print('='*10)
print('The Multiplication For Any Columns Is => ',D2_5.prod())
'''
A    2.227687e-04
B    1.106509e-08
C    2.458723e-07
dtype: float64
'''
print('='*10)
print('The Varince For Any Columns Is => ',D2_5.var())
'''
A    0.071914
B    0.092025
C    0.131568
dtype: float64
'''
print('='*10)
print('The Summation Of Column A Is => ',D2_5['A'].sum())
#The Summation Of Column A Is =>  6.293949716452368
print('The Mean For Columns B Is => ',D2_5['B'].mean())
#The Mean For Columns B Is =>  0.5546772727089214
print('The Production For Columns C Is => ',D2_5['C'].prod())
#The Production For Columns C Is =>  7.520885128980154e-07
print('='*20)
print('The Means For Any Rows Is => ',D2_5.mean(axis='columns'))
'''
0    0.481360
1    0.372760
2    0.246271
3    0.536216
4    0.236614
5    0.545539
6    0.842729
7    0.618382
8    0.578278
9    0.707103
dtype: float64
'''
print('='*30)
print('The Mean For Any Columns Is => ',D2_5.mean(axis='rows'))
'''
A    0.429113
B    0.520318
C    0.460452
dtype: float64
'''
print('='*20)
D2_6=pd.DataFrame({'Keys':['A','B','C','A','B','C'],'Data':range(6)},
columns=['Keys','Data'])
print(D2_6)
'''
     Keys  Data
0    A     0
1    B     1
2    C     2
3    A     3
4    B     4
5    C     5
'''
print('='*30)
print('The Summation Is => ',D2_6.groupby('Keys').sum())
'''
Keys    Data
A        3
B        5
C        7
'''
print('='*30)
print('The Describe Of D2_6 Is => ',D2_6.describe())
'''
         Data
count  6.000000
mean   2.500000
std    1.870829
min    0.000000
25%    1.250000
50%    2.500000
75%    3.750000
max    5.000000
'''
print('='*20)
print('The Groupby With Describe Is => ',D2_6.groupby('Keys').describe())
'''
        count mean      std  min   25%  50%   75%  max
Keys
A      2.0  1.5  2.12132  0.0  0.75  1.5  2.25  3.0
B      2.0  2.5  2.12132  1.0  1.75  2.5  3.25  4.0
C      2.0  3.5  2.12132  2.0  2.75  3.5  4.25  5.0
'''
print('='*30)
print('The Data Using Unstack with Describe Is => ',D2_6.groupby('Keys').describe().unstack())
'''
Data  count  A       2.00000
             B       2.00000
             C       2.00000
      mean   A       1.50000
             B       2.50000
             C       3.50000
      std    A       2.12132
             B       2.12132
             C       2.12132
      min    A       0.00000
             B       1.00000
             C       2.00000
      25%    A       0.75000
             B       1.75000
             C       2.75000
      50%    A       1.50000
             B       2.50000
             C       3.50000
      75%    A       2.25000
             B       3.25000
             C       4.25000
      max    A       3.00000
             B       4.00000
             C       5.00000
dtype: float64
'''
print('='*30)
D2_7=pd.DataFrame({'Key':['A','B','C','A','B','C'],'data1':range(6),
'data2':np.random.randint(0,10,size=6)},columns=['Key','data1','data2'])
print(D2_7)
'''
    Key  data1  data2
0   A      0      7
1   B      1      2
2   C      2      8
3   A      3      4
4   B      4      6
5   C      5      9 
'''
print('='*20)
print(D2_7.groupby('Key').aggregate({'data1':'min','data2':'max'}))
'''
Key     data1  data2
A        0      7
B        1      6
C        2      9
'''
print('='*20)
def filter_func(x):
      return x['data2'].std()>4
df=D2_7.groupby('Key').filter(filter_func)
print(D2_7)
'''
    Key  data1  data2
0   A      0      6
1   B      1      3
2   C      2      6
3   A      3      0
4   B      4      0
5   C      5      0
'''
print('='*20)
print(df)
'''
    Key  data1  data2
0   A      0      6
2   C      2      6
3   A      3      0
5   C      5      0
'''
print('='*20)
df1=D2_7.groupby('Key').transform(lambda x:np.power(x,3))
print(df1)
'''
     data1  data2
0      0      8
1      1    512
2      8    729
3     27    125
4     64      8
5    125     64
'''
print('='*20)
