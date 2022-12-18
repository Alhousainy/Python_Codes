print('='*30)
import numpy as np
'''
#fname='D:\\Programming\Machine learning Python\\Files\\1.text'
fname='D:\\1.text'
dtype1=np.dtype([('gender', '|S1'), ('height', 'f8')])
a=np.loadtxt(fname, dtype=dtype1, skiprows=9, usecols=(1,3))
print(a)
'''
fname = 'D:\\1.txt'
dtype1 = np.dtype([('gender', '|S1'), ('height', 'f8')])
a = np.loadtxt(fname, dtype=dtype1, skiprows=8, usecols=(1,3))
print(a)
'''
[(b'F', 1.68) (b'M', 1.72) (b'F', 1.78) (b'F', 1.6 ) (b'M', 1.72)
(b'M', 1.83) (b'F', 1.56) (b'F', 1.64) (b'M', 1.63) (b'M', 1.67)
(b'M', 1.66) (b'F', 1.59) (b'F', 1.7 ) (b'M', 1.97) (b'F', 1.66)
(b'F', 1.63) (b'M', 1.69)]
'''
print('='*30)
b= np.array(a)
print(b)
'''
[(b'M', 1.77) (b'F', 1.68) (b'M', 1.72) (b'F', 1.78) (b'F', 1.6 )
 (b'M', 1.72) (b'M', 1.83) (b'F', 1.56) (b'F', 1.64) (b'M', 1.63)
 (b'M', 1.67) (b'M', 1.66) (b'F', 1.59) (b'F', 1.7 ) (b'M', 1.97)
 (b'F', 1.66) (b'F', 1.63) (b'M', 1.69)]
'''
c=b.reshape(6,3)
print(c)
'''
[[(b'M', 1.77) (b'F', 1.68) (b'M', 1.72)]
[(b'F', 1.78) (b'F', 1.6 ) (b'M', 1.72)]
[(b'M', 1.83) (b'F', 1.56) (b'F', 1.64)]
[(b'M', 1.63) (b'M', 1.67) (b'M', 1.66)]
[(b'F', 1.59) (b'F', 1.7 ) (b'M', 1.97)]
[(b'F', 1.66) (b'F', 1.63) (b'M', 1.69)]]
'''
print('='*30)
m1,m2,m3=np.loadtxt('D:\\2.text' , unpack=True,skiprows=3)
print('The Years Is => ',m1)
#The Years Is =>  [1890. 1900. 1910. 1920. 1930.]
print('The Male Is => ',m2)
#The Male Is =>  [26.1 25.9 25.1 24.6 24.3]
print('The Women Is => ',m3)
#The Women Is =>  [22.  21.9 21.6 21.2 21.3]
print('='*30)
print('convert m1 to matrix is => ',np.array(m1).reshape(1,5))
#convert m1 to matrix is =>  [[1890. 1900. 1910. 1920. 1930.]]
print('the variance of m1 is => ',np.var(m1))
#the variance of m1 is =>  200.0
print('the sin of m1 all elements is => ',np.sin(m1))
#the sin of m1 all elements is =>  [-0.94538622  0.61592173 -0.08821855 -0.46787837  0.8733854 ]
print('the covariance of m1 is => ',np.cov(m1))
#the covariance of m1 is =>  250.0
print('the standard devision m1 is => ',np.std(m1))
#the standard devision m1 is =>  14.142135623730951
print('='*30)
'''
data =np.genfromtxt('D:\\3.txt', skip_header=1,
dtype=[('student','u8'),
('gender','S1'),('black','f8'),
('colour','f8')],delimiter=',',
missing_values='X')
print(data)
print('='*30)
'''
m4=np.genfromtxt('D:\\3.txt',skip_header=1,dtype=[('student','u8'),('gender','S1'),('black','f8'),
('colour','f8')],delimiter=',',missing_values='X')
print('M4 Is => ',m4)
#M4 Is =>  [(1, b'F', 18.72, 31.11) (2, b'F', 21.14, 52.47) (3, b'F', 19.38, 33.9 )]
print('='*30)
print('convert m4 to matrix is => ',np.array(m4))
#convert m4 to matrix is =>  [(1, b'F', 18.72, 31.11) (2, b'F', 21.14, 52.47) (3, b'F', 19.38, 33.9 )]
print('the m4 after reshape is => ',np.array(m4).reshape(3,1))
'''
the m4 after reshape is =>  
[[(1, b'F', 18.72, 31.11)]
[(2, b'F', 21.14, 52.47)]
[(3, b'F', 19.38, 33.9 )]]
'''
print('='*30)
