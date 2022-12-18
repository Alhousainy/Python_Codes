print('='*30)
import numpy as np
m=np.random.randint(5,20,size=12).reshape(2,6)
m_1=np.random.randint(5,20,size=12).reshape(2,6)
print('Matrix M is => ',m)
'''
Matrix M is =>  
[[ 8 10  7 15 19 11]
[17  9  8  5  7  6]]
'''
print('Matrix M_1 Is => ',m_1)
'''
Matrix M_1 Is =>  
[[ 8 10 19  6 13  5]
[15  5 11 18  5 15]]
'''
print('The Summation Matrix m +m_1 Is => ',m+m_1)
'''
The Summation Matrix m +m_1 Is =>  
[[16 20 26 21 32 16]
[32 14 19 23 12 21]]
'''
print('The Subtraction m-m_1 Is => ',m-m_1)
'''
The Subtraction m-m_1 Is =>  
[[  0   0 -12   9   6   6]
[  2   4  -3 -13   2  -9]]
'''
m1_2=m*m_1
print('='*20)
print('The Type one From Multiplication Is => ', m1_2)
'''
The Type one From Multiplication Is =>  
[[117 114 168 323  96  70]
[110  30 182 224 168 143]]
'''
print('='*30)
m1_3=m/m_1
print('The Division Matrix m on Matrix m_1 is => ',m1_3)
print('='*30)
'''
The Division Matrix m on Matrix m_1 is => 
[[1.   3.    0.92  0.85  0.76  1.28]
[0.68  0.470 1.1   1.2   1.4   0.57]]
'''
print('the matrix m *3 is => ',m*3)
'''
the matrix m *3 is =>  
[[39 15 30 24 57 51]
[36 57 39 54 18 21]]
'''
print('='*30)
print('the division matrix m on 5 is =>  ',m/5)
'''
the division matrix m on 5 is =>   
[[2.6 1.  2.  1.6 3.8 3.4]  
[2.4  3.8 2.6 3.6 1.2 1.4]]
'''
print('='*30)
print('the sin matrix m is => ',np.sin(m))
'''
[[ 0.99060736  0.6569866  -0.75098725  0.41211849  0.98935825  0.98935825]
[ 0.42016704  0.41211849  0.14987721  0.6569866  -0.2794155  -0.99999021]]
'''
print('='*10)
print('the power 2 of matrix m is => ',np.power(m,2))
'''
[[196  49 324  81  64  64]      
[169  81 361  49  36 121]]
'''
print('='*10)
print('the log matrix m is => ',np.log(m))
'''
[[2.63905733 1.94591015 2.89037176 2.19722458 2.07944154 2.07944154]
[2.56494936 2.19722458 2.94443898 1.94591015 1.79175947 2.39789527]]
'''
print('='*30)
m2=np.random.randint(1,20,size=18).reshape(6,3)
m2_1=np.random.randint(2,16,size=21).reshape(3,7)
print('the matrix m2 is => ',m2)
'''
the matrix m2 is =>  
[[19 15  4]
[ 5  8  4]
[ 7 18 17]
[12 11  4]
[ 5 15 15]
[ 3 14  5]]
'''
print('='*10)
print('the matrix m2_1 is => ',m2_1)
'''
the matrix m2_1 is =>  
[[ 5  6 15  4 14  5 11]
[ 5  2  8 13  2 15  9]
[ 7  5 15 12  7  9  4]]
'''
print('='*10)
print('the multiplicatiom matrcies (m2*m2_1) is => ',np.dot(m2,m2_1))
'''
the multiplicatiom matrcies (m2*m2_1) is =>  
[[198 164 465 319 324 356 360]
[ 93  66 199 172 114 181 143]
[244 163 504 466 253 458 307]
[143 114 328 239 218 261 247]
[205 135 420 395 205 385 250]
[120  71 232 254 105 270 179]]
'''
print('='*30)
m2_2=np.random.randint(5,25,size=16).reshape(4,4)
print('Matrix M2_2 IS => ',m2_2)
'''
Matrix M2_2 IS =>  
[[ 5 18 19 21]
[10 23  9 21]
[11 19  6  5]
[21 15 20 14]]
'''
print('='*10)
print('the summation matrix m2_2 is => ',np.sum(m2_2))
#the summation matrix m2_2 is =>  237
print('the summation matrix m2_2 is => ',m2_2.sum())
#the summation matrix m2_2 is =>  237
print('the summation all columns in matrix m2_2 is => ',np.sum(m2_2,axis=0))
#the summation all columns in matrix m2_2 is =>  [47 75 54 61]  
print('the summation all columns in matrix m2_2 is => ',m2_2.sum(axis=0))
#the summation all columns in matrix m2_2 is =>  [47 75 54 61]  
print('the summation all rows in matrix m2_2 is => ',np.sum(m2_2,axis=1))
#the summation all rows in matrix m2_2 is =>  [63 63 41 70]     
print('the summation all rows in matrix m2_2 is => ',m2_2.sum(axis=1))
#the summation all rows in matrix m2_2 is =>  [63 63 41 70]     
print('The Mean Of Matrix m2_2 is => ',m2_2.mean())
#The Mean Of Matrix m2_2 is =>  12.625
print('The standard Division Of Matrix m2_2 Is => ',m2_2.std())
#The standard Division Of Matrix m2_2 Is =>  4.211220131980754  
print('The Variance Of Matrix m2_2 Is => ',m2_2.var())
#The Variance Of Matrix m2_2 Is =>  17.734375
print('The Correlation Coefficient Of Matrix m2_2 Is => ',np.corrcoef(m2_2))
'''
The Correlation Coefficient Of Matrix m2_2 Is =>  
[[ 1.         0.54806588 -0.32295531 -0.44335501]
[ 0.54806588  1.         -0.94098212  0.5000168 ]
[-0.32295531 -0.94098212  1.         -0.69787335]
[-0.44335501  0.5000168  -0.69787335  1.        ]]
'''
print('='*30)
print('The Sortin Of Matrix M2_2 Is => ',np.sort(m2_2))
'''
The Sortin Of Matrix M2_2 Is =>  
[[ 8 22 23 23]
[ 8 10 12 13]
[ 7 11 13 17]
[ 7  7 16 24]]
'''
print('='*10)
print('the sorting matrix m2_2 for cols is => ',np.sort(m2_2,axis=0))
'''
the sorting matrix m2_2 for cols is =>  
[[ 7  7  7  8]
[12 13 10  8]
[13 23 17 11]
[23 24 22 16]]
'''
print('='*10)
print('the sorting matrix m2_2 for rows is => ',np.sort(m2_2,axis=1))
'''
the sorting matrix m2_2 for rows is =>  
[[ 8 22 23 23]
[ 8 10 12 13]
[ 7 11 13 17]
[ 7  7 16 24]]
'''
print('='*30)
m2_4=np.linalg.inv(m2_2)
print('the inverse matrim m2_2 is => ',m2_4)
print('='*10)
'''
the inverse matrim m2_2 is =>  
[[-0.13586452  0.08953838 -0.12231631  0.11794592]
[ 0.0274242  -0.0305381   0.1698443  -0.15127014]
[ 0.02310844  0.055941   -0.06604753 -0.00196668]
[ 0.07921333 -0.06828735  0.0005463   0.05708823]]
'''
print('the identity matrix from mult (m2_2*m2_4) is => ',np.dot(m2_2,m2_4))
print('='*30)
'''
the identity matrix from mult (m2_2*m2_4) is =>  
[[1.  0.  0.  0.]
[ 0.  1.  0.  0.]
[ 0.  0.  1.  0.]
[ 0.  0.  0.  1.]]
'''
