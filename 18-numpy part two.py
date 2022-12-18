print('='*30)
from turtle import rt
import numpy as np
v1=np.random.randint(0,10,(5,5))
v2=np.count_nonzero(v1)
v3=np.count_nonzero(v1>4)
v4=np.count_nonzero(v1<8)
print('The Matrix Random Integer 5*5 Is=> ',v1)
print('='*30)
'''
The Matrix Random Integer 5*5 Is=>  
[[5 4 1 8 2]
[7 2 0 7 5]
[8 4 2 1 9]
[7 3 3 1 8]
[1 6 9 5 3]]
'''
print('The Count Number Not Equal Zero In Matrix Is => ',v2)
#The Count Number Not Equal Zero In Matrix Is =>  24
print('The Count Number In Matrix Is Greater Than 4 Is => ',v3)
#The Count Number In Matrix Is Greater Than 4 Is =>  13
print('The Count Number In Matrix Is Lower Than 8 Is => ',v4)
#The Count Number In Matrix Is Lower Than 8 Is =>  19
print('='*30)
v5=np.count_nonzero(v1>4,axis=1)
print('The Count Number In Matrix Is Greater Than 4 In Rows Is =>',v5)
#The Count Number In Matrix Is Greater Than 4 In Rwos Is => [1 2 0 1 3]
v6=np.count_nonzero(v1<8,axis=1)
print('The Count Number In Matrix Is Lower Than 8  in Rows Is => ',v6)
#The Count Number In Matrix Is Lower Than 8  in Rows Is =>  [5 4 5 5 5]
print('='*30)
v7=np.any(v1>4)
v8=np.any(v1<8)
print('IS The Matrix It Is Number Is Graeter Than From 4 => ',v7)#True
print('Is The Matrix It Is Any Number Is Lower Than From 8 => ',v8)#True
print('='*30)
v9=np.any(v1>4,axis=1)
v9_1=np.any(v1<8,axis=1)
print('The Result In The Matrix Number Is Greater Than From 4 ',v9)
#The Result In The Matrix Number Is Greater Than From 4  [ True  True  True  True  True]
print('The End Result in Matrix Number Is Lower Than From 8 Is => ',v9_1)
#The End Result in Matrix Number Is Lower Than From 8 Is =>  [ True  True  True  True  True]
print('='*30)
print('It is All Numbers In Matrix Is Graeter Than From 4 => ',np.all(v1>4))
#It is All Numbers In Matrix Is Graeter Than From 4 =>  False
print('It Is All Numbers In Matrix Is Lower Than From 8 => ',np.all(v1<8))
#It Is All Numbers In Matrix Is Lower Than From 8 =>  False
print('='*30)
m1=np.random.randint(1,20,size=25).reshape(5,5)
m1_0=m1>10
m1_1=m1<15
m1_2=m1[m1_0]
m1_3=m1[m1_1]
print('The Original Matrix Is => ',m1)
'''
The Original Matrix Is =>  
[[19 11 12 14  5]
[16  6 15 18 15]
[18 15 13  5 10]
[11 13 16 13 18]
[ 4 13  9 18  6]]
'''
print('='*30)
print('The Boolean Matrix Numbers Is Greater Than From 10 Is => ',m1_0)
'''
The Boolean Matrix Numbers Is Greater Than From 10 Is =>  
[[ True  True  True  True False]
[ True False  True  True  True]
[ True  True  True False False]
[ True  True  True  True  True]
[False  True False  True False]]
'''
print('='*30)
print('The Boolean Matrix Is Numbers Is Lower Than From 15 Is => ',m1_1)
print('='*30)
'''
The Boolean Matrix Is Numbers Is Lower Than From 15 Is =>  
[[False  True  True  True  True]
[False  True False False False]
[False False  True  True  True]
[ True  True False  True False]
[ True  True  True False  True]]
'''
print('The Numbers Is Greater Than From 10 Is => ',m1_2)
#The Numbers Is Greater Than From 10 Is=>[19 11 12 14 16 15 18 15 18 15 13 11 13 16 13 18 13 18]
print('The Numbers Is Lower Than From 15 Is => ',m1_3)
#The Numbers Is Lower Than From 15 Is=>[11 12 14  5  6 13  5 10 11 13 13  4 13  9  6]
print('='*30)
k1=np.arange(25).reshape(5,5)
k2=np.arange(25).reshape(5,5)
k2_1=2*k2
k3=np.isclose(k1,k2,rtol=2)
k4=np.isclose(k1,k2_1,rtol=0.1)
print('The Original Matrix K1 Is => ',k1)
print('='*30)
'''
The Original Matrix K1 Is =>  
[[ 0  1  2  3  4]
[ 5  6  7  8  9]
[10 11 12 13 14]
[15 16 17 18 19]
[20 21 22 23 24]]
'''
print('The Original Matrix K2 Is => ',k2)
print('='*30)
'''
The Original Matrix K2 Is =>  
[[ 0  1  2  3  4]
[ 5  6  7  8  9]
[10 11 12 13 14]
[15 16 17 18 19]
[20 21 22 23 24]]
'''
print('The Matrix K2 Is Mult In 2 Is => ',k2_1)
print('='*30)
'''
The Matrix K2 Is Mult In 2 Is =>  
[[ 0  2  4  6  8]
[10 12 14 16 18]
[20 22 24 26 28]
[30 32 34 36 38]
[40 42 44 46 48]]
'''
print('The Compare Between Two Matrix K1 & K2 Is => ',k3)
print('='*30)
'''
The Compare Between Two Matrix K1 & K2 Is =>  
[[ True  True  True  True  True]
[ True  True  True  True  True]
[ True  True  True  True  True]
[ True  True  True  True  True]
[ True  True  True  True  True]]
'''
print('The Compare Between Two Matrix K1 & K1_2 Is => ',k4)
print('='*30)
'''
The Compare Between Two Matrix K1 & K1_2 Is => 
[[ True False False False False]
[False False False False False]
[False False False False False]
[False False False False False]
[False False False False False]]
'''
M1=np.arange(10)
print('The Matrix M1 Is => ',M1)
#The Matrix M1 Is =>  [0 1 2 3 4 5 6 7 8 9]
M2=np.empty(10)
print('The Matrix M2 Before Multiply Is => ',M2)
'''
The Matrix M2 Before Multiply Is =>  
[6.95167599e-310 3.56043053e-307 1.60219306e-306 1.11261095e-306
3.22651328e-307 1.11260755e-306 1.24606309e-306 1.33512173e-306       
4.45058486e-308 1.06811422e-306]
'''
np.multiply(M1,5,out=M2)
print('The Matrix M2 After Multiply Is => ',M2)
#The Matrix M2 After Multiply Is =>  [ 0.  5. 10. 15. 20. 25. 30. 35. 40. 45.]
M_comp=np.isclose(M1,M2,rtol=2)
print('The Compare Between Two After Multiply ',M_comp)
#The Compare Between Two After Multiply 
#[ True  True  True  True  True  True  True  True  True  True]
print('='*30)
np.power(M1,4,out=M2)
print('The Matrix M2 After Power 5 For Numbers Is => ',M2)
#The Matrix M2 After Power 5 For Numbers Is =>  
#[0.000e+00 1.000e+00 1.600e+01 8.100e+01 2.560e+02 
#6.250e+02 1.296e+03 2.401e+03 4.096e+03 6.561e+03]
print('='*30)
M3=np.arange(20)
print('The Matrix Is => ',M3)
#The Matrix Is =>  [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
print('The Summation All Numbers In Matrix Is => ',np.add.reduce(M3))
#The Summation All Numbers In Matrix Is =>  190
print('='*30)
M4=np.arange(2,15)
print('The Matrix Is => ',M4)
#The Matrix Is =>  [ 2  3  4  5  6  7  8  9 10 11 12 13 14]
print('The Multiplcation All Numbers In Matrix Is => ',np.multiply.reduce(M4))
#The Multiplcation All Numbers In Matrix Is =>  1278945280
print('='*30)
print('The Matrix After Multiply Outer => ',np.multiply.outer(M4,M4))
print('='*30)
'''
The Matrix Is =>  [ 2  3  4  5  6  7  8  9 10 11 12 13 14]
The Matrix After Multiply Outer =>  
[[  4   6   8  10  12  14  16  18  20  22  24  26  28]
[  6   9  12  15  18  21  24  27  30  33  36  39  42]
[  8  12  16  20  24  28  32  36  40  44  48  52  56]
[ 10  15  20  25  30  35  40  45  50  55  60  65  70]
[ 12  18  24  30  36  42  48  54  60  66  72  78  84]
[ 14  21  28  35  42  49  56  63  70  77  84  91  98]
[ 16  24  32  40  48  56  64  72  80  88  96 104 112]
[ 18  27  36  45  54  63  72  81  90  99 108 117 126]
[ 20  30  40  50  60  70  80  90 100 110 120 130 140]
[ 22  33  44  55  66  77  88  99 110 121 132 143 154]
[ 24  36  48  60  72  84  96 108 120 132 144 156 168]
[ 26  39  52  65  78  91 104 117 130 143 156 169 182]
[ 28  42  56  70  84  98 112 126 140 154 168 182 196]]
'''
print('The Matrix Is => ',M4)
#The Matrix Is =>  [ 2  3  4  5  6  7  8  9 10 11 12 13 14]
print('The Matrix After Accumulate Process Is => ',np.add.accumulate(M4))
#The Matrix After Accumulate Process Is =>  [  2   5   9  14  20  27  35  44  54  65  77  90 104]
print('='*30)
print('The Matrix Is => ',M4)
#The Matrix Is =>  [ 2  3  4  5  6  7  8  9 10 11 12 13 14]
print('The Matrix After Multiply Accumulate Process Is => ',np.multiply.accumulate(M4))
#The Matrix After Multiply Accumulate Process Is=>
#[2 6 24 120 720 5040 40320 362880 3628800 39916800 479001600 1932053504 1278945280]
print('='*30)
a=np.arange(15)
b=len(a)
c=a.reshape(5,3)
d=len(c)
print('The Matrix A => ',a)
#The Matrix A =>  [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]        
print('The Length Matrix A Is => ',b)
#The Length Matrix A Is =>  15
print('The Length Of Matrix All elements Is => ',np.size(a))
#The Length Of Matrix All elements Is =>  15
print('The Number Of Dimensions Of Array Is => ',a.ndim)
#The Number Of Dimensions Of Array Is =>  1
print('The Dimensions Matrix Before Reshape Is => ',np.shape(a))
#The Dimensions Matrix Before Reshape Is =>  (15,)
print('The Matrix A After Reshape Is => ',c)
'''
The Matrix A After Reshape Is =>  
[[ 0  1  2]
[ 3  4  5]
[ 6  7  8]
[ 9 10 11]
[12 13 14]]
'''
print('The Length Of Matrix A After Reshape Is => ',d)
#The Length Of Matrix A After Reshape Is =>  5 Rows 
print('The Length Of Matrix All elements After Reshape Is => ',np.size(c))
#The Length Of Matrix All elements After Reshape Is =>  15
f=c.shape
print('The Dimensions Matrix After Reshape Is => ',f)
#The Dimensions Matrix After Reshape Is =>  (5, 3)
print('The Number of Dimensions Of Matrix After Reshape Is => ',c.ndim)
#The Number of Dimensions Of Matrix After Reshape Is =>  2
print('='*30)
print('The Type Of Data In Matrix Is => ',c.dtype)
#The Type Of Data In Matrix Is =>  int32
print('='*30)
L=np.array(['Alhousainy','Mostafa','Ahmed','Ali'])
L_Type=L.dtype
L1=np.array(['GNM','H','M','N','B'])
L1_Type=L1.dtype
print('The Type Of Array In List (L) Is => ',L_Type)
#The Type Of Array In List (L) Is =>  <U10
print('The Data Type In Array In List (L1) Is => ',L1_Type)
#The Data Type In Array In List (L1) Is =>  <U3
print('='*30)
m2=np.matrix('{} {};{} {} '.format(1,2,3,4))
print('The Matrix 2*2 Is => ',m2)
'''
The Matrix 2*2 Is =>
[[1 2]
[3 4]]
'''
m2_1=np.matrix('{} {} {};{} {} {} '.format(1,2,3,4,5,6))
print('The Matrix 2*3 Is => ',m2_1)
'''
The Matrix 2*3 Is =>  
[[1 2 3]
[4 5 6]]
'''
print('='*30)
m3=np.matrix('{} {} {} ;{} {} {} ;{} {} {} ;{} {} {} '.format(1,2,3,4,5,6,7,8,9,10,11,12))
print('The Matrix 4*3 Is => ',m3)
'''
The Matrix 4*3 Is =>  
[[ 1  2  3]
[ 4  5  6]
[ 7  8  9]
[10 11 12]]
'''
print('='*30)
m3_1=np.matrix('{} {} {} {} {} ; {} {} {} {} {} ; {} {} {} {} {} ; {} {} {} {} {} ; {} {} {} {} {}'
.format(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24))
print('The Matrix 5*5 Is => ',m3_1)
print('='*30)
'''
The Matrix 5*5 Is =>  
[[ 0  1  2  3  4]
[ 5  6  7  8  9]
[10 11 12 13 14]
[15 16 17 18 19]
[20 21 22 23 24]]
'''
m4=np.arange(25)
m4_1=m4.reshape(5,5)
m4_2=np.trace(m4_1)
print('The Orignal Matrix Is => ',m4)
#The Orignal Matrix Is=>[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
print('The Matrix After Reshape Is => ',m4_1)
'''
The Matrix After Reshape Is =>  
[[ 0  1  2  3  4]
[ 5  6  7  8  9]
[10 11 12 13 14]
[15 16 17 18 19]
[20 21 22 23 24]]
'''
print('The Summation Of Diagonal Is Equal => ',m4_2)
#The Summation Of Diagonal Is Equal =>  60
print('='*30)
m5=np.linalg.det(m4_1)
m5_1=np.linalg.eig(m4_1)
print('The Orignal Matrix Is => ',m4_1)
'''
The Orignal Matrix Is =>  
[[ 0  1  2  3  4]
[ 5  6  7  8  9]
[10 11 12 13 14]
[15 16 17 18 19]
[20 21 22 23 24]]
'''
print('The Determined Of The Matrix Is => ',m5)
#The Determined Of The Matrix Is =>  0.0
print('The Eigan Value Of Matrix Is => ',m5_1)
'''
The Eigan Value Of Matrix Is =>  
(array([ 6.39116499e+01+0.00000000e+00j, -3.91164992e+00+0.00000000e+00j,
-3.22069971e-15+0.00000000e+00j,2.58587115e-16+7.36422729e-16j, 2.58587115e-16-7.36422729e-16j]),
array([[-0.0851802+0.j ,0.67779864+0.j,0.24109755+0.j,
0.23152795-0.12469177j,0.23152795+0.12469177j],
[-0.23825372+0.j,0.36348873+0.j, -0.54061326+0.j ,-0.21054131-0.10215471j,-0.21054131+0.10215471j],
[-0.39132723+0.j , 0.04917881+0.j , -0.02551006+0.j ,  0.18426328+0.4026156j ,
0.18426328-0.4026156j ],
[-0.54440074+0.j , -0.2651311 +0.j ,0.70846967+0.j , -0.66301443+0.j , -0.66301443-0.j],
[-0.69747425+0.j , -0.57944101+0.j ,-0.38344391+0.j , 0.45776451-0.17576912j,
0.45776451+0.17576912j]]))
'''
print('='*30)
m6=np.arange(15)
m6_1=m6.reshape(5,3)
m6_2=m6[3]
m6_3=m6[3:14]
m6_4=m6[3:14:2]
m6_5=m6[-1]
m6_6=m6[-5]
print('The Orignal Matrix Is => ',m6)
#The Orignal Matrix Is =>  [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
print('The Matrix After Reshape Is => ',m6_1)
'''
The Matrix After Reshape Is =>  
[[ 0  1  2]
[ 3  4  5]
[ 6  7  8]
[ 9 10 11]
[12 13 14]]
'''
print('The Element 4 In The Matrix Is => ',m6_2)
#The Element 4 In The Matrix Is =>  3
print('The Elements From 3 To 14 In Matrix Is => ',m6_3)
#The Elements From 3 To 14 In Matrix Is =>  [ 3  4  5  6  7  8  9 10 11 12 13]
print('The Elements In The Matrix From 3 To 14 But 2 Step Is => ',m6_4)
#The Elements In The Matrix From 3 To 14 But 2 Step Is =>  [ 3  5  7  9 11 13]
print('The First Element From The End Is => ',m6_5)
#The First Element From The End Is =>  14
print('The Element Number 5 From The End In The Matrix Is => ',m6_6)
#The Element Number 5 From The End In The Matrix Is =>  10
print('='*30)
m7=np.arange(81).reshape(9,9)
m7_1=m7[3]
m7_2=m7[3:8]
m7_3=m7[3:8:2]
m7_4=m7[-1]
m7_5=m7[-5]
print('The Orignal Matrix Is => ',m7)
'''
The Orignal Matrix Is =>  
[[ 0  1  2  3  4  5  6  7  8]
[ 9 10 11 12 13 14 15 16 17]
[18 19 20 21 22 23 24 25 26]
[27 28 29 30 31 32 33 34 35]
[36 37 38 39 40 41 42 43 44]
[45 46 47 48 49 50 51 52 53]
[54 55 56 57 58 59 60 61 62]
[63 64 65 66 67 68 69 70 71]
[72 73 74 75 76 77 78 79 80]]
'''
print('The Matrix Is Row 4 Is => ',m7_1)
#The Matrix Is Row 4 Is =>  [27 28 29 30 31 32 33 34 35]
print('The Matrix From Row 4 To Row 7 Is => ',m7_2)
'''
The Matrix From Row 4 To Row 7 Is =>  
[[27 28 29 30 31 32 33 34 35]    
[36 37 38 39 40 41 42 43 44]
[45 46 47 48 49 50 51 52 53]
[54 55 56 57 58 59 60 61 62]
[63 64 65 66 67 68 69 70 71]]
'''
print('='*20)
print('The Matrix From Row 4 To Row 7 But Step 2 Is => ',m7_3)
'''
The Matrix From Row 4 To Row 7 But Step 2 Is =>  
[[27 28 29 30 31 32 33 34 35]
[45 46 47 48 49 50 51 52 53]
[63 64 65 66 67 68 69 70 71]]
'''
print('='*20)
print('The Matrix From Row 1  But From The End Is => ',m7_4)
#The Matrix From Row 1  But From The End Is =>  [72 73 74 75 76 77 78 79 80]
print('='*20)
print('The Matrix Is The Row 5 From The End Is => ',m7_5)
#The Matrix Is The Row 5 From The End Is =>  [36 37 38 39 40 41 42 43 44]
print('='*40)
m9=np.arange(100).reshape(10,10)
m9_1=m9[5,5]
m9_2=m9[5,:]
m9_3=m9[8,:]
m9_4=m9[:,2]
m9_5=m9[:,2:8]
m9_6=m9[1:9,]
print('The Origanl Matrix Is => ',m9)
'''
The Origanl Matrix Is =>  
[[ 0  1  2  3  4  5  6  7  8  9]
[10 11 12 13 14 15 16 17 18 19]
[20 21 22 23 24 25 26 27 28 29]
[30 31 32 33 34 35 36 37 38 39]
[40 41 42 43 44 45 46 47 48 49]
[50 51 52 53 54 55 56 57 58 59]
[60 61 62 63 64 65 66 67 68 69]
[70 71 72 73 74 75 76 77 78 79]
[80 81 82 83 84 85 86 87 88 89]
[90 91 92 93 94 95 96 97 98 99]]
'''
print('='*30)
print('The Element In The Row 6 and Column 6 Is => ',m9_1)
#The Element In The Row 6 and Column 6 Is =>  55
print('The All Elements In Row 6 Is => ',m9_2)
#The All Elements In Row 6 Is =>  [50 51 52 53 54 55 56 57 58 59]       
print('The All Elements In Row 9 Is => ',m9_3)
#The All Elements In Row 9 Is =>  [80 81 82 83 84 85 86 87 88 89]       
print('The All Elements In Column Three Is => ',m9_4)
#The All Elements In Column Three Is =>  [ 2 12 22 32 42 52 62 72 82 92]
print('='*30)
print('The All Elements From Column 3 To Column 7 Is => ',m9_5)
'''
The All Elements From Column 3 To Column 7 Is =>  
[[ 2  3  4  5  6  7] 
[12 13 14 15 16 17]
[22 23 24 25 26 27]
[32 33 34 35 36 37]
[42 43 44 45 46 47]
[52 53 54 55 56 57]
[62 63 64 65 66 67]
[72 73 74 75 76 77]
[82 83 84 85 86 87]
[92 93 94 95 96 97]]
'''
print('='*30)
print('The All Elements From Row 2 To Row 8 Is => ',m9_6)
'''
The All Elements From Row 2 To Row 8 Is =>  
[[10 11 12 13 14 15 16 17 18 19]
[20 21 22 23 24 25 26 27 28 29]
[30 31 32 33 34 35 36 37 38 39]
[40 41 42 43 44 45 46 47 48 49]
[50 51 52 53 54 55 56 57 58 59]
[60 61 62 63 64 65 66 67 68 69]
[70 71 72 73 74 75 76 77 78 79]
[80 81 82 83 84 85 86 87 88 89]]
'''
print('='*30)
g1=m9[3:4,1:5]
g1_1=m9[2:,3:]
g1_2=m9[:2,:3]
g1_3=m9[:,-1]
g1_4=m9[-1,:]
print('The Orignal Matrix Is => ',m9)
'''
The Orignal Matrix Is =>  
[[ 0  1  2  3  4  5  6  7  8  9]
[10 11 12 13 14 15 16 17 18 19]
[20 21 22 23 24 25 26 27 28 29]
[30 31 32 33 34 35 36 37 38 39]
[40 41 42 43 44 45 46 47 48 49]
[50 51 52 53 54 55 56 57 58 59]
[60 61 62 63 64 65 66 67 68 69]
[70 71 72 73 74 75 76 77 78 79]
[80 81 82 83 84 85 86 87 88 89]
[90 91 92 93 94 95 96 97 98 99]]
'''
print('='*10)
print('The Matrix Is Row 4 And From Column 1 To Column 4 Is => ',g1)
#The Matrix Is Row 4 And From Column 1 To Column 4 Is =>  [[31 32 33 34]]
print('='*10)
print('The Matrix From Row 2 To The End and From Column 3 To The End Is => ',g1_1)
'''
The Matrix From Row 2 To The End and From Column 3 To The End Is =>  
[[23 24 25 26 27 28 29]
[33 34 35 36 37 38 39]
[43 44 45 46 47 48 49]
[53 54 55 56 57 58 59]
[63 64 65 66 67 68 69]
[73 74 75 76 77 78 79]
[83 84 85 86 87 88 89]
[93 94 95 96 97 98 99]]
'''
print('='*10)
print('The Matrix From Row 0 To Row 1 and From Column 0 To Column 2 Is => ',g1_2)
'''
The Matrix From Row 0 To Row 1 and From Column 0 To Column 2 Is =>  
[[ 0  1  2]
[10 11 12]]
'''
print('='*10)
print('The Matrix From Row 0 To The End and The First Column From End Is => ',g1_3)
#The Matrix From Row 0 To The End and The First Column From End Is=>[ 9 19 29 39 49 59 69 79 89 99]
print('='*10)
print('The Matrix From Row One From The End and The All Columns Is => ',g1_4)
#The Matrix From Row One From The End and The All Columns Is=>[90 91 92 93 94 95 96 97 98 99]
print('='*30)
g2=m9[::2,::3]
g2_1=m9[::-1,::-1]
g2_2=m9[:2:-1,:3:-1]
g2_3=m9[2::2,3::3]
g2_4=m9[-1::,-1::]
print('The Original Matrix Is => ',m9)
print('='*10)
'''
The Original Matrix Is =>  
[[ 0  1  2  3  4  5  6  7  8  9]
[10 11 12 13 14 15 16 17 18 19]
[20 21 22 23 24 25 26 27 28 29]
[30 31 32 33 34 35 36 37 38 39]
[40 41 42 43 44 45 46 47 48 49]
[50 51 52 53 54 55 56 57 58 59]
[60 61 62 63 64 65 66 67 68 69]
[70 71 72 73 74 75 76 77 78 79]
[80 81 82 83 84 85 86 87 88 89]
[90 91 92 93 94 95 96 97 98 99]]
'''
print('The matrix From Row 0 To The End But Step 2 and From Column 0 To The end but step 3 => ',g2)
'''
The matrix From Row 0 To The End But Step 2 and From Column 0 To The end but step 3 =>  
[[ 0  3  6  9]
[20 23 26 29]
[40 43 46 49]
[60 63 66 69]
[80 83 86 89]]
'''
print('='*10)
print('The Matrix From Row One To The End But From The End and The Columns Like That => ',g2_1)
'''
The Matrix From Row One To The End But From The End and The Columns Like That =>  
[[99 98 97 96 95 94 93 92 91 90]
[89 88 87 86 85 84 83 82 81 80]
[79 78 77 76 75 74 73 72 71 70]
[69 68 67 66 65 64 63 62 61 60]
[59 58 57 56 55 54 53 52 51 50]
[49 48 47 46 45 44 43 42 41 40]
[39 38 37 36 35 34 33 32 31 30]
[29 28 27 26 25 24 23 22 21 20]
[19 18 17 16 15 14 13 12 11 10]
[ 9  8  7  6  5  4  3  2  1  0]]
'''
print('='*10)
print('The Matrix From Row 0 To Row 2 But From The End and From Column o To 3 But The End => ',g2_2)
'''
The Matrix From Row 0 To Row 2 But From The End and From Column o To 3 But The End =>  
[[99 98 97 96 95 94]
[89 88 87 86 85 84]
[79 78 77 76 75 74]
[69 68 67 66 65 64]
[59 58 57 56 55 54]
[49 48 47 46 45 44]
[39 38 37 36 35 34]]
'''
print('='*10)
print('The Matrix From Row 2 To The End Step 2 , The Column 3 to the end Step 3 => ',g2_3)
'''
he Matrix From Row 2 To The End Step 2 , The Column 3 to the end Step 3 =>  
[[23 26 29]
[43 46 49]
[63 66 69]
[83 86 89]]
'''
print('='*10)
print('The Matrix From The Row From The End and Columns As Like That => ',g2_4)
#The Matrix From The Row From The End and Columns As Like That =>  [[99]]
print('='*30)
g3=np.arange(20).reshape(5,4)
print('The Original Matrix Is => ',g3)
'''
The Original Matrix Is =>  
[[ 0  1  2  3]
[ 4  5  6  7]
[ 8  9 10 11]
[12 13 14 15]
[16 17 18 19]]
'''
print('='*10)
g3_1=g3[2,3]=0
print('The Row 3 And The Columns 4 The Elements Is = 0 , Is => ',g3)
'''
The Row 3 And The Columns 4 The Elements Is = 0 , Is =>  
[[ 0  1  2  3]
[ 4  5  6  7]
[ 8  9 10  0]
[12 13 14 15]
[16 17 18 19]]
'''
print('='*10)
g3_2=g3[:,3]=0
print('The All Rows and The Column 4 In The Matrix Is = 0 , Is => ',g3)
'''
The All Rows and The Column 4 In The Matrix Is = 0 , Is =>  
[[ 0  1  2  0]
[ 4  5  6  0]
[ 8  9 10  0]
[12 13 14  0]
[16 17 18  0]]
'''
print('='*10)
g3_3=g3[2,:]=0
print('The Row Three and all columns In The Row Is = 0  , => ',g3)
'''
The Row Three and all columns In The Row Is = 0  , =>  
[[ 0  1  2  0]  
[ 4  5  6  0]
[ 0  0  0  0]
[12 13 14  0]
[16 17 18  0]]
'''
print('='*10)
g3_4=g3[:,:]=0
print('The All Elements In The Matrix Is Equal Zero , is => ',g3)
'''
The All Elements In The Matrix Is Equal Zero , is =>  
[[0 0 0 0]       
[0 0 0 0]
[0 0 0 0]
[0 0 0 0]
[0 0 0 0]]
'''
print('='*30)
g4=np.arange(25).reshape(5,5)
print('The original Matrix Is => ',g4)
print('='*10)
'''
The original Matrix Is =>  
[[ 0  1  2  3  4]
[ 5  6  7  8  9]
[10 11 12 13 14]
[15 16 17 18 19]
[20 21 22 23 24]]
'''
g4_1=g4[:,1:4]
print('The Matrix g4_1 Is => ',g4_1)
print('='*10)
'''
The Matrix g4_1 Is =>  
[[ 1  2  3]
[ 6  7  8]
[11 12 13]
[16 17 18]
[21 22 23]]
'''
g4_1[:,:]=10
print('The Matrix g4_1 After Change Value => ',g4_1)
print('='*10)
'''
The Matrix g4_1 After Change Value =>  
[[10 10 10]
[10 10 10]
[10 10 10]
[10 10 10]
[10 10 10]]
'''
print('The Matrix g4 After Change Value In Matrix g4_1 Is => ',g4)
print('='*10)
'''
The Matrix g4 After Change Value In Matrix g4_1 Is =>  
[[ 0 10 10 10  4]
[ 5 10 10 10  9]
[10 10 10 10 14]
[15 10 10 10 19]
[20 10 10 10 24]]
'''
g4[:,:]=8
print('The Matrix G4 After Change Value Is => ',g4)
print('='*10)
'''
The Matrix G4 After Change Value Is =>  
[[8 8 8 8 8]
[8 8 8 8 8]
[8 8 8 8 8]
[8 8 8 8 8]
[8 8 8 8 8]]
'''
print('The Matrix G4_1 After Change Value Matrix g4 Is => ',g4_1)
print('='*30)
'''
The Matrix G4_1 After Change Value Matrix g4 Is =>  
[[8 8 8]
[8 8 8]
[8 8 8]
[8 8 8]
[8 8 8]]
'''
g4_5=g4[:,1:3].copy()
g4[:,:]=12
print('The Matrix G4 Is => ',g4)
print('='*10)
'''
The Matrix G4 Is => 
[[12 12 12 12 12]
[12 12 12 12 12]
[12 12 12 12 12]
[12 12 12 12 12]
[12 12 12 12 12]]
'''
print('The Matrix G4_5 After Change Value In Matrix G4 Is => ',g4_5)
print('='*10)
'''
The Matrix G4_5 After Change Value In Matrix G4 Is =>  
[[8 8]
[8 8]
[8 8]
[8 8]
[8 8]]
'''
g4_5[:,:]=26
print('The Matrix G4_5 Is => ',g4_5)
print('='*10)
'''
The Matrix G4_5 Is =>  
[[26 26]
[26 26]
[26 26]
[26 26]
[26 26]]
'''
print('The Matrix G4 After Change Value Matrix G4_5 Is => ',g4)
print('='*30)
'''
The Matrix G4 After Change Value Matrix G4_5 Is =>  
[[12 12 12 12 12]  
[12 12 12 12 12]
[12 12 12 12 12]
[12 12 12 12 12]
[12 12 12 12 12]]
'''
g5=np.arange(18).reshape(3,3,2)
print('The Original Matrix Is => ',g5)
print('='*10)
'''
The Original Matrix Is =>  
[[[ 0  1]
[ 2  3]
[ 4  5]]

[[ 6  7]
[ 8  9]
[10 11]]

[[12 13]
[14 15]
[16 17]]]
'''
g5_1=g5[0]
print('The Matrix 0 In The Original Matrix Is => ',g5_1)
print('='*10)
'''
The Matrix 0 In The Original Matrix Is =>  
[[0 1]
[2 3]
[4 5]]
'''
g5_2=g5[1,2]
print('The Matrix one In The Original Matrix and Row Three Is => ',g5_2)
#The Matrix one In The Original Matrix and Row Three Is =>  [10 11]     
g5_3=g5[2,2,1]
print('The Matrix Three In The Original Matrix and Row 3 And Column Two Is => ',g5_3)
#The Matrix Three In The Original Matrix and Row 3 And Column Two Is =>  17
print('='*30)
x=[11,22,33,44,55,66,77,88,99,100]
x1,x2,x3=np.split(x,(3,6))
print('The Matrices Is => ',x1,x2,x3)
#The Matrices Is =>  [11 22 33] [44 55 66] [ 77  88  99 100]
x1,x2,x3=np.split(x,(1,5))
print('The Matrices Is => ',x1,x2,x3)
#The Matrices Is =>  [11] [22 33 44 55] [ 66  77  88  99 100]
x1,x2,x3=np.split(x,(6,3))
print('The Matrices Is => ',x1,x2,x3)
#The Matrices Is =>  [11 22 33 44 55 66] [] [ 44  55  66  77  88  99 100]
x1,x2,x3=np.split(x,(0,3))
print('The Matrices Is => ',x1,x2,x3)
#The Matrices Is =>  [] [11 22 33] [ 44  55  66  77  88  99 100]        
x1,x2,x3=np.split(x,(4,0))
print('The Matrices Is => ',x1,x2,x3)
#The Matrices Is =>  [11 22 33 44] [] [ 11  22  33  44  55  66  77  88  99 100]
print('='*30)
g7=np.arange(25).reshape(5,5)
g4_6=g7[2][1]
g4_7=g7[2,1]
print('The original matrix is => ',g7)
print('The Element In The Row 3 and Column 2 Is => ',g4_6)
#The Element In The Row 3 and Column 2 Is =>  11
print('The Element In The Row 3 and Column 2 Is => ',g4_7)
#The Element In The Row 3 and Column 2 Is =>  11
print('='*30)
G1=np.arange(16).reshape(4,4)
G2=2*np.arange(24).reshape(6,4)
G3=np.vstack((G1,G2))
print('The Matrix G1 Is => ',G1)
'''
The Matrix G1 Is =>  
[[ 0  1  2  3]
[ 4  5  6  7]
[ 8  9 10 11]
[12 13 14 15]]
'''
print('='*10)
print('The Matrix G2 Is => ',G2)
print('='*10)
'''
The Matrix G2 Is =>  
[[ 0  2  4  6]
[ 8 10 12 14]
[16 18 20 22]
[24 26 28 30]
[32 34 36 38]
[40 42 44 46]]
'''
print('The Matrix G3 Is => ',G3)
'''
The Matrix G3 Is =>  
[[ 0  1  2  3]
[ 4  5  6  7]
[ 8  9 10 11]
[12 13 14 15]
[ 0  2  4  6]
[ 8 10 12 14]
[16 18 20 22]
[24 26 28 30]
[32 34 36 38]
[40 42 44 46]]
'''
print('='*30)
G4=np.arange(25).reshape(5,5)
G5=np.arange(35).reshape(5,7)
print('The Matrix G4 Is => ',G4)
print('='*30)
'''
The Matrix G4 Is =>  
[[ 0  1  2  3  4]
[ 5  6  7  8  9]
[10 11 12 13 14]
[15 16 17 18 19]
[20 21 22 23 24]]
'''
print('The Matrix G5 Is => ',G5)
print('='*10)
'''
The Matrix G5 Is =>  
[[ 0  1  2  3  4  5  6]
[ 7  8  9 10 11 12 13]
[14 15 16 17 18 19 20]
[21 22 23 24 25 26 27]
[28 29 30 31 32 33 34]]
'''
G6=np.hstack((G4,G5))
print('The Matrix G6 Is => ',G6)
'''
The Matrix G6 Is =>  
[[ 0  1  2  3  4  0  1  2  3  4  5  6]
[ 5  6  7  8  9  7  8  9 10 11 12 13]
[10 11 12 13 14 14 15 16 17 18 19 20]
[15 16 17 18 19 21 22 23 24 25 26 27]
[20 21 22 23 24 28 29 30 31 32 33 34]]
'''
print('='*30)
y=np.random.randint(5,35,size=20).reshape(4,5)
print('The Matrix Y Is => ',y)
print('='*10)
'''
The Matrix Y Is =>  
[[ 5 34 12 15 34]
[18  7 10 27  7]
[21 13  9 31 21]
[24 30 14 29 23]]
'''
y_1=np.random.randint(5,40,size=25).reshape(5,5)
print('The Matrix Y Is => ',y_1)
print('='*10)
'''
The Matrix Y Is =>  
[[23 34 35 18 27]
[25 31 25 13 31]
[ 9 14 11 25 30]
[26 23 21 12 11]
[24 19  9 35 12]]
'''
y_2=np.concatenate([y,y_1],axis=0)
print('The Matrix Y Is => ',y_2)
print('='*30)
'''
The Matrix Y Is =>  
[[ 5 34 12 15 34]
[18  7 10 27  7]
[21 13  9 31 21]
[24 30 14 29 23]
[23 34 35 18 27]
[25 31 25 13 31]
[ 9 14 11 25 30]
[26 23 21 12 11]
[24 19  9 35 12]]
'''
y2=np.random.randint(10,30,size=15).reshape(3,5)
print('The Matrix Y2 Is => ',y2)
print('='*10)
'''
The Matrix Y2 Is =>  
[[29 25 16 13 18]
[27 17 29 28 25]
[23 19 19 19 22]]
'''
y2_1=np.random.randint(10,30,size=18).reshape(3,6)
print('The Matrix Y2 Is => ',y2_1)
print('='*10)
'''
The Matrix Y2 Is =>  
[[20 18 27 25 28 25]
[11 10 22 24 25 23]
[28 14 23 24 17 21]]
'''
y2_2=np.concatenate([y2,y2_1],axis=1)
print('The Matrix Y2 Is => ',y2_2)
print('='*30)
'''
The Matrix Y2 Is =>  
[[29 25 16 13 18 20 18 27 25 28 25]
[27 17 29 28 25 11 10 22 24 25 23]
[23 19 19 19 22 28 14 23 24 17 21]]
'''
print('The maximum Value In Matrix y2 Is => ',np.max(y2))
#The maximum Value In Matrix y2 Is =>  28
print('The minimum Value In Matrix y2 Is => ',np.min(y2))
#The minimum Value In Matrix y2 Is =>  12
print('The Place maximum Value In Matrix Y2 Is => ',np.argmax(y2))
#The Place maximum Value In Matrix Y2 Is =>  1
print('The Place minimum Value In Matrix y2 Is => ',np.argmin(y2))
#The Place minimum Value In Matrix y2 Is =>  9
print('='*30)
print('The Varinace Of Matrix Y2 Is => ',np.var(y2))
#The Varinace Of Matrix Y2 Is =>  27.928888888888885
print('The Covariance Of Matrix Y2 Is => ',np.cov(y2))
'''
The Covariance Of Matrix Y2 Is =>  
[[ 20.3    9.95  -6.65]
[  9.95  32.3  -12.1 ]
[ -6.65 -12.1   19.7 ]]
'''
print('='*30)