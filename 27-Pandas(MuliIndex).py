print('='*30)
import numpy as np
import pandas as pd
index=[('Qena',2010),('Qena',2015),('Alex',2010),('Alex',2015),
('Cairo',2010),('Cairo',2015),('Aswan',2010),('Aswan',2015),('Luxor',2010),('Luxor',2015)]
Populations=[1000000,2000000,1000000,2000000,1000000,2000000,
1000000,5000000,1000000,3000000]
I=pd.MultiIndex.from_tuples(index)
D=pd.Series(Populations,index=I)
D1=D.reindex(I)
print(D1)
'''
Qena   2010    1000000
       2015    2000000
Alex   2010    1000000
       2015    2000000
Cairo  2010    1000000
       2015    2000000
Aswan  2010    1000000
       2015    5000000
Luxor  2010    1000000
       2015    3000000
dtype: int64
'''
print('='*30)
print(D1[:,2015])
'''
Qena     2000000
Alex     2000000
Cairo    2000000
Aswan    5000000
Luxor    3000000
dtype: int64
'''
print('='*30)
print(D1.unstack())
'''
        2010     2015
Alex   1000000  2000000
Aswan  1000000  5000000
Cairo  1000000  2000000
Luxor  1000000  3000000
Qena   1000000  2000000
'''
'''
I=pd.MultiIndex.from_tuples(index)
D=pd.Series(Populations,index=I)
D1=D.reindex(I)
print(D1)
'''
print('='*30)
D2=pd.DataFrame({'Total':D1,'Under18':[98535,45632,54136,78923,21523,54782,14638,14568,
21222,20546],'Male':[10535,24783,54364,25489,14230,14789,25432,14832,54368,47320],
'Female':[14730,2456,78930,25476,36547,248965,24432,4756,3217,10543]})
print(D2)
'''
             Total    Under18   Male  Female
Qena  2010  1000000    98535   10535   14730
      2015  2000000    45632   24783    2456
Alex  2010  1000000    54136   54364   78930
      2015  2000000    78923   25489   25476
Cairo 2010  1000000    21523   14230   36547
      2015  2000000    54782   14789  248965
Aswan 2010  1000000    14638   25432   24432
      2015  5000000    14568   14832    4756
Luxor 2010  1000000    21222   54368    3217
      2015  3000000    20546   47320   10543
'''
print('='*30)
df=pd.DataFrame(np.random.rand(4,2),index=[['a','a','b','b'],[1,2,1,2]],
columns=['income','profit'])
print(df)
'''
       income    profit
a 1  0.890875  0.757494
  2  0.917932  0.284459
b 1  0.974565  0.707888
  2  0.543666  0.179649
'''
print('='*30)
'''
Dict=pd.Series({'Alhousainy':5000,'Alhousainy':8000,'Ahmed':6000,'Ahmed':4000,
'Mona':8000,'Mona':7000,'Mostafa':4000,'Mostafa':4500,
'Mohammed':2000,'Mohammed':3000,'Khalad':1000,'Khalad':2400})
'''
L=[('Alhousainy',5000),('Alhousainy',8000),('Ahmed',6000),('Ahmed',4000),('Mona',8000)
,('Mona',4000),('Mostafa',4000),('Mostafa',4500),('Khalad',1000),('Khalad',2400)]
df1=pd.DataFrame(L,index=[['One','Two','One','Two','One','Two','One','Two','One','Two']
,['a','b','a','b','a','b','a','b','a','b']],columns=['Name','Salary'])
print(df1)
'''
              Name          Salary
One   a    Alhousainy       5000
Two   b    Alhousainy       8000
One   a       Ahmed         6000
Two   b       Ahmed         4000
One   a        Mona         8000
Two   b        Mona         4000
One   a     Mostafa         4000
Two   b     Mostafa         4500
One   a      Khalad         1000
Two   b      Khalad         2400
'''
print('='*30)
data1={('Cairo',2010):20000,('Cairo',2015):150000,('Alex',2010):120000,('Alex',2015):
150000,('Qena',2010):140000,('Qena',2015):160000,('Luxor',2010):170000,
('Luxor',2015):15420}
df_2=pd.Series(data1)
print(df_2)
'''
Cairo  2010     20000
       2015    150000
Alex   2010    120000
       2015    150000
Qena   2010    140000
       2015    160000
Luxor  2010    170000
       2015     15420
dtype: int64
'''
print('='*30)
data={('Alhousainy',2014):'Student',('Alhousainy',2018):'Graduated',('Alhousainy',2020):'ML_Eng',('Ahmed',2014):'Student',
('Ahmed',2018):'Engineer',('Ahmed',2020):'Doctor',('Mostafa',2014):'Teacher',('Mostafa',2018):'First Teacher',
('Mostafa',2020):'Manager',('Arwa',2014):'Student',('Arwa',2018):'Graduated',('Arwa',2020):'Developper'}
df1_1=pd.Series(data)
print(df1_1)
'''
Alhousainy  2014          Student
            2018        Graduated
            2020           ML_Eng
Ahmed       2014          Student
            2018         Engineer
            2020           Doctor
Mostafa     2014          Teacher
            2018    First Teacher
            2020          Manager
Arwa        2014          Student
            2018        Graduated
            2020       Developper
dtype: object
'''
print('='*30)
index1=pd.MultiIndex.from_product([[2013,2014],[1,2]],names=['Year','Visit'])
columns1=pd.MultiIndex.from_product([['Bob','Guido','Sue'],['HR','Eng']],
names=['Subject','Type'])
data1_1=np.random.randn(4,6)
df1_3=pd.DataFrame(data1_1,index=index1,columns=columns1)
print(df1_3)
'''
Subject          Bob               Guido                 Sue
Type              HR       Eng        HR       Eng        HR       Eng   
Year Visit
2013 1      0.092361  0.314666  1.252546 -0.351495  0.086717  0.225323   
     2     -0.905224 -2.044547  1.235056 -0.394199 -1.158760 -1.209294   
2014 1      0.183798 -0.626389 -1.526319  0.050832 -0.907418  0.850181   
     2      0.444967 -0.685780  0.959466  0.804541  0.630031 -0.856868 
'''
print('='*30)
print(df1_3['Sue','Eng'])
'''
Year  Visit
2013  1       -0.240849
      2       -0.365287
2014  1       -1.263106
      2       -1.812932
Name: (Sue, Eng), dtype: float64
'''
print('='*30)
print(df1_3.loc[:,('Bob','HR')])
'''
Year  Visit
2013  1        0.571634
      2        1.151320
2014  1       -1.211343
      2        0.444846
Name: (Bob, HR), dtype: float64
'''
print('='*30)
idx=pd.IndexSlice
print(df1_3.loc[idx[:,1],idx[:,'HR']])
'''
Subject          Bob     Guido       Sue
Type              HR        HR        HR
Year Visit
2013 1     -0.740400 -0.860338 -0.443725
2014 1      0.090635  0.087854  0.918686
'''
print('='*30)

