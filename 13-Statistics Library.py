print('='*60)
import statistics as st
L=[i for i in range(11)]
v=st.mean(L)
print(L)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(v)#5
T=([i for i in range(20)])
v1=st.mean(T)
print(T)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(v1)#9.5
S={k for k in range(16)}
v3=st.mean(S)
print(S)#{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
print(v3)#7.5
h=[7,6,5,3,2,4,1]
x=st.harmonic_mean(h)
print('The Harmonic Mean Is => ',x)#The Harmonic Mean Is =>  2.6997245179063363
h1=[7,6,5,1]
x1=st.harmonic_mean(h1)
print('The Harmonic Mean Is => ',x1)#The Harmonic Mean Is =>  2.6498422712933754
h3=[k for k in range(7)]
x2=st.harmonic_mean(h3)
print('The Harmonic Mean Is => ',x2)#The Harmonic Mean Is =>  0
h4={k for k in range(1,7)}
x3=st.harmonic_mean(h4)
print('The Harmonic Mean Is => ',x3)#The Harmonic Mean Is =>  2.4489795918367347
m=[7,5,2,3,1,9,8]
m1=sorted(m)
m2=sorted(m,reverse=True)
y=st.median(m1)
print('The Median Number is ==> ',y)#The Median Number is ==>  5
y2=st.median(m2)
print('The Median Number is ==> ',y2)#The Median Number is ==>  5
m3=[k for k in range(1,10)]
y3=st.median(m3)
print('The Median Number is ==> ',y3)#The Median Number is ==>  5
m3=[k for k in range(10)]
y4=st.median(m3)
print('The Median Number is ==> ',y4)#The Median Number is ==>  4.5
m4={k for k in range(10)}
m5=sorted(m4,reverse=True)
y5=st.median(m5)
print('The Median Number is ==> ',y5)#The Median Number is ==>  4.5
L=[1,2,3,4,5,6,7,8,9]
M=st.median_low(L)
print('The Median Low Is ==> ',M)#The Median Low Is ==>  5
L1=[1,2,3,4,5,6,7,8]
M1=st.median_low(L1)
print('The Median Low Is ==> ',M1)#The Median Low Is ==>  4
M2=st.median_high(L)
M3=st.median_high(L1)
print('The Median High Is ==> ',M2)#The Median High Is ==>  5
print('The Median High Is ==> ',M3)#The Median High Is ==>  5
T=[1,1,2,3,4,5,6,2,2,2,4,4,4,4,6,7,8,9]
T1=(1,1,2,3,4,5,6,2,2,2,4,4,4,4,6,7,8,9)
X=st.mode(T)
X1=st.mode(T1)
print('The Mode Is ==> ',X)#The Mode Is ==>  4
print('The Mode Is ==> ',X1)#The Mode Is ==>  4
Standard_Devision=[3.2,6.9,8.1,-9.3,66]
S=st.stdev(Standard_Devision)
print('The Standard Division Is ==> ',S)#The Standard Division Is ==>  29.342579981998853
S1=st.variance(Standard_Devision)
print('The Variance Is ==> ',S1)#The Variance Is ==>  860.9869999999999