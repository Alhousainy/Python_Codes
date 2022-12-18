print('='*30)
import numpy as np
x=np.array('1996-03-24',dtype=np.datetime64)
print('The Date Is => ',x)#The Date Is =>  1996-03-24
x_1=np.array('2021-08-12',dtype=np.datetime64)
print('The Date Is => ',x_1)#The Date Is =>  2021-08-12
x_2=np.datetime64('1996-03-24')
x_3=np.datetime64('2021-08-12')
print('The Date Is => ',x_2)#The Date Is =>  1996-03-24
print('The Date Is => ',x_3)#The Date Is =>  2021-08-12
x_4=x_3+np.arange(12)
print('The X_4 After Plus 12 Numbers is => ',x_4)
'''
The X_4 After Plus 12 Numbers is =>  
['2021-08-12' '2021-08-13' '2021-08-14' '2021-08-15' '2021-08-16'
'2021-08-17' '2021-08-18' '2021-08-19' '2021-08-20' '2021-08-21'
'2021-08-22' '2021-08-23']
'''
x_5=x_4.reshape(3,4)
print('The Matrix x_5 Is => ',x_5)
'''
The Matrix x_5 Is =>  
[['2021-08-12' '2021-08-13' '2021-08-14' '2021-08-15']
['2021-08-16' '2021-08-17' '2021-08-18' '2021-08-19']
['2021-08-20' '2021-08-21' '2021-08-22' '2021-08-23']]
'''
x_6=np.datetime64('2015-02-26')
x_7=x_6+np.arange(6)
print('Matrix X_7 Is => ',x_7.reshape(2,3))
'''
Matrix X_7 Is =>  
[['2015-02-26' '2015-02-27' '2015-02-28']    
['2015-03-01' '2015-03-02' '2015-03-03']]
'''
print('='*30)
x_8=np.datetime64('2015-01-04')
x_9=x_8-np.arange(12)
print('The Matrix x_9 Is => ',x_9)
'''
The Matrix x_9 Is =>  
['2015-01-04' '2015-01-03' '2015-01-02' '2015-01-01' '2014-12-31'
'2014-12-30' '2014-12-29' '2014-12-28' '2014-12-27' '2014-12-26'
'2014-12-25' '2014-12-24']
'''
print('='*30)
print('The Reshape Matrix X_9 Is => ',x_9.reshape(3,4))
'''
The Reshape Matrix X_9 Is =>  
[['2015-01-04' '2015-01-03' '2015-01-02' '2015-01-01']
['2014-12-31' '2014-12-30' '2014-12-29' '2014-12-28']
['2014-12-27' '2014-12-26' '2014-12-25' '2014-12-24']] 
'''
print('='*30)
x_10=x_1-x_8
print('The Number Of Days Between Two Dates Is => ',x_10,' Days')
#The Number Of Days Between Two Dates Is =>  2412 days  Days    
print('='*20)
m=np.fromfunction(lambda i:np.power(i,3),(10,))
print('The Matrix Is Cube From 0=> 9 Is => ',m)
#The Matrix Is Cube From 0=> 9 Is =>  [  0.   1.   8.  27.  64. 125. 216. 343. 512. 729.]
print('='*10)
m_1=np.fromfunction(lambda i: 3*np.power(i+5,3),(10,))
print('The Matrix Is => ',m_1)
#The Matrix Is =>  [ 375.  648. 1029. 1536. 2187. 3000. 3993. 5184. 6591. 8232.]
print('='*10)
m_2=np.fromfunction(lambda i,j:(i+j),(4,5))
print('The Matrix 2D Is => ',m_2)
'''
The Matrix 2D Is =>  
[[0. 1. 2. 3. 4.]
[1. 2. 3. 4. 5.]
[2. 3. 4. 5. 6.]
[3. 4. 5. 6. 7.]]
'''
print('='*20)
m_3=np.fromfunction(lambda i,j:3*i*j ,(4,5))
print('The Matrix 3D Is => ',m_3)
'''
The Matrix 3D Is =>  
[[ 0.  0.  0.  0.  0.]
[ 0.  3.  6.  9. 12.]
[ 0.  6. 12. 18. 24.]
[ 0.  9. 18. 27. 36.]]
'''
print('='*20)
m_4=np.fromfunction(lambda i,j,k:i+j+k,(2,3,4))
print('The Matrix 3D Is => ',m_4)
'''
The Matrix 3D Is =>  
[[[0. 1. 2. 3.]
[1. 2. 3. 4.]
[2. 3. 4. 5.]]

[[1. 2. 3. 4.]
[2. 3. 4. 5.]
[3. 4. 5. 6.]]]
'''
print('='*20)
m_5=np.fromfunction(lambda i,j,k:(2*i)+np.power(j,2)*k,(2,3,4))
print('The Matrix 3D Is => ',m_5)
'''
The Matrix 3D Is =>  
[[[ 0.  0.  0.  0.]
[ 0.  1.  2.  3.]
[ 0.  4.  8. 12.]]

[[ 2.  2.  2.  2.]
[ 2.  3.  4.  5.]
[ 2.  6. 10. 14.]]]
'''
print('='*30)
def powers(i):
    i=i**2
    return i
m_6=np.fromfunction(powers,(10,),dtype=int)
print('The Matrix Power 2 From 0=>9 Is => ',m_6)
#The Matrix Power 2 From 0=>9 Is =>  [ 0  1  4  9 16 25 36 49 64 81]
print('='*20)
def power(i,j):
    i=i**j
    return i
m_7=np.fromfunction(power,(4,5),dtype=int)
print('The Matrix m_7 is power j => ',m_7)
'''
The Matrix m_7 is power j =>  
[[ 1  0  0  0  0]
[ 1  1  1  1  1]
[ 1  2  4  8 16]
[ 1  3  9 27 81]]
'''
print('='*10)
u,l=40,5
def f(i):
    return(i%l==0)
m_8=np.fromfunction(f,(u,),dtype=int)
print('The Matrix Boolean Value Is => ',m_8)
'''
The Matrix Boolean Value Is =>  
[ True False False False False  True False False False False  True False
False False False  True False False False False  True False False False
False  True False False False False  True False False False False  True
False False False False]
'''
print('='*30)