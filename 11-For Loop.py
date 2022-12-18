# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 00:07:28 2022

@author: ENG-Alhousainy
"""

print('='*60)
for k in range(6):
    print('The Number Is ',k)
print('End')
# The Number Is  0
# The Number Is  1
# The Number Is  2
# The Number Is  3
# The Number Is  4
# The Number Is  5
#End
for n in range(1,10,2):
    print('The Number Is ',n)
print('End')
# The Number Is  1
# The Number Is  3
# The Number Is  5
# The Number Is  7
# The Number Is  9
# End
f=[(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
print(f)#[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
d=[(x,y) for x in range(3) for y in range(3)]
print(d)#[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
z=[(x,y) for x in range(3) for y in range(3,7) if x!=y]
print(z)#[(0, 3), (0, 4), (0, 5), (0, 6), (1, 3), (1, 4), (1, 5), (1, 6), (2, 3), (2, 4), (2, 5), (2, 6)]
Stat= 'supercalifragilisticexpialidocious'
for x in range(len(Stat)):
    print(Stat[x])
#Line 1 ==>  s     ,Line 2 ==># u , Line 3 ==> # p ,Line 4 ==># e, Line 6 ==># r , Line 7 ==># c , Line 8 ==># a
#Line 9 ==> l , Line 10 ==> i , Line 11 ==># f ,Line 12 ==># r , Line 13 ==># a ,Line 14 ==># g ,Line 15 ==># i
#Line 16 ==> l ,Line 17 ==># i ,Line 18 ==># s ,Line 19 ==># t , Line 20 ==># i , Line 21 ==># c ,Line 22 ==># e
# Stat1 ='My Name Is Alhousainy and Iam a Machine Learning Engineer'
# for y in range(len(Stat1.split())):
#     print(Stat1[y])
S=''
Stat1 ='Alhousainy'
for x in range(len(Stat1)):
   S=S+Stat1[len(Stat1)-x-1]
print(S)#yniasuohlA
for v in Stat1:
    if v =='y':
        continue
    print(v)# 
for v in range(12):
    if v % 5 ==0 :
        continue
    print('The Number Is =',v)
# The Number Is = 1
# The Number Is = 2
# The Number Is = 3
# The Number Is = 4
# The Number Is = 6
# The Number Is = 7
# The Number Is = 8
# The Number Is = 9
# The Number Is = 11
print('='*20)
for v in range(12):
    if v % 5 ==0 or v % 3 ==0 :
        continue
    print('The Number Is =',v)
# The Number Is = 1
# The Number Is = 2
# The Number Is = 4
# The Number Is = 7
# The Number Is = 8
# The Number Is = 11
for num in range (2,10):
    if num % 2 ==0:
        print('Number Is an Even Number==> ' +str(num))
        continue
    print('Number Is an Odd Number ==> ' ,num)
print('='*20)
# Number Is an Even Number==> 2
# Number Is an Odd Number ==>  3
# Number Is an Even Number==> 4
# Number Is an Odd Number ==>  5
# Number Is an Even Number==> 6
# Number Is an Odd Number ==>  7
# Number Is an Even Number==> 8
# Number Is an Odd Number ==>  9
for x in Stat1:
    print('The Character Is ==>',x)
print('='*20)
# The Character Is ==> A
# The Character Is ==> l
# The Character Is ==> h
# The Character Is ==> o
# The Character Is ==> u
# The Character Is ==> s
# The Character Is ==> a
# The Character Is ==> i
# The Character Is ==> n
# The Character Is ==> y
S = 'Hello World'
for x in S:
    print('The Character Is ==>',x)
# The Character Is ==> H
# The Character Is ==> e
# The Character Is ==> l
# The Character Is ==> l
# The Character Is ==> o
# The Character Is ==>  
# The Character Is ==> W
# The Character Is ==> o
# The Character Is ==> r
# The Character Is ==> l
# The Character Is ==> d
print('='*20)
Countries =['Egypt','Japan','France','Germany','USA','KSA','UAE','Libya']
for i in Countries:
    print('The Country is ==> ' ,i)
print('='*20)
# The Country is ==>  Egypt
# The Country is ==>  Japan
# The Country is ==>  France
# The Country is ==>  Germany
# The Country is ==>  USA
# The Country is ==>  KSA
# The Country is ==>  UAE
# The Country is ==>  Libya
Dict={'Name':'Alhousainy' ,'Age':26 ,'Job':'Engineer' ,'Country':'Egypt'}
for j in Dict.items():
    print('The Item Is ==> ' ,j)
# The Item Is ==>  ('Name', 'Alhousainy')
# The Item Is ==>  ('Age', 26)
# The Item Is ==>  ('Job', 'Engineer')
# The Item Is ==>  ('Country', 'Egypt')
print('='*20)
for x in Dict.keys():
    print('The Key Is ==> ',x)
print('='*20)
# The Key Is ==>  Name
# The Key Is ==>  Age
# The Key Is ==>  Job
# The Key Is ==>  Country
for z in Dict.values():
    print('The Value Is ==> ',z)
# The Value Is ==>  Alhousainy
# The Value Is ==>  26
# The Value Is ==>  Engineer
# The Value Is ==>  Egypt
print('='*20)
for x,y in Dict.items():
    print('The Key is ==> ',x)
    print('The Value Is ==> ' ,y)
# The Key is ==>  Name
# The Value Is ==>  Alhousainy
# The Key is ==>  Age
# The Value Is ==>  26
# The Key is ==>  Job
# The Value Is ==>  Engineer
# The Key is ==>  Country
# The Value Is ==>  Egypt
print('='*20)
Dict={'Name':'Alhousainy' ,'Age':26 ,'Job':'Engineer' ,'Country':'Egypt'}
L=['Ahmed','Mostafa','Ali','Mona','Mia','Khalad']
S={'Ahmed','Mostafa','Ali','Mona','Mia','Khalad'}
T=('Ahmed','Mostafa','Ali','Mona','Mia','Khalad')
for i , j in enumerate (L):
    print(i," The Name Is ==>" , j)
# 0  The Name Is ==> Ahmed
# 1  The Name Is ==> Mostafa
# 2  The Name Is ==> Ali
# 3  The Name Is ==> Mona
# 4  The Name Is ==> Mia
# 5  The Name Is ==> Khalad
print('='*20)
for i ,v in enumerate(S):
    print(i," The Name Is ==>" , v)
# 0  The Name Is ==> Ali
# 1  The Name Is ==> Mia
# 2  The Name Is ==> Mostafa
# 3  The Name Is ==> Khalad
# 4  The Name Is ==> Mona
# 5  The Name Is ==> Ahmed
print('='*20)
for i , v in enumerate(T):
    print(i," The Name Is ==>" , v)
# 0  The Name Is ==> Ahmed
# 1  The Name Is ==> Mostafa
# 2  The Name Is ==> Ali
# 3  The Name Is ==> Mona
# 4  The Name Is ==> Mia
# 5  The Name Is ==> Khalad
print('='*20)
Dict={'Name':'Alhousainy' ,'Age':26 ,'Job':'Engineer' ,'Country':'Egypt'}
for j , v in enumerate(Dict):
    print(j," The Name Is ==>" , v)
# 0  The Name Is ==> Name
# 1  The Name Is ==> Age
# 2  The Name Is ==> Job
# 3  The Name Is ==> Country
print('='*20)
for j , v in enumerate(Dict.keys()):
    print(j," The Name Is ==>" , v)
# 0  The Name Is ==> Name
# 1  The Name Is ==> Age
# 2  The Name Is ==> Job
# 3  The Name Is ==> Country
print('='*20)
for x,y in enumerate(Dict.items()):
    print(x," The Item Is ==>" , y)
# 0  The Item Is ==> ('Name', 'Alhousainy')
# 1  The Item Is ==> ('Age', 26)
# 2  The Item Is ==> ('Job', 'Engineer')
# 3  The Item Is ==> ('Country', 'Egypt')    
print('='*20)
for j , v in enumerate(Dict.values()):
    print(j," The Name Is ==>" , v)
# 0  The Name Is ==> Alhousainy
# 1  The Name Is ==> 26
# 2  The Name Is ==> Engineer
# 3  The Name Is ==> Egypt
print('='*20)
L1=['Alhousainy','Mostafa','Ali','Mona','Fairuz']
L2=['Egypt','Libya','USA','KSA','UAE']
L3=['25 Years Old','27 Years Old','18 Years Old','30 Years Old','12 Years Old']
L4=['Is Enginner','Is Doctor','Is Lawyer','Is Teacher','Is Student']
for a,b,c,d in zip(L1,L2,L3,L4):
    print(a,'From ',b,c,d)
print('='*20)
# Alhousainy From  Egypt 25 Years Old Is Enginner
# Mostafa From  Libya 27 Years Old Is Doctor
# Ali From  USA 18 Years Old Is Lawyer
# Mona From  KSA 30 Years Old Is Teacher
# Fairuz From  UAE 12 Years Old Is Student
L=[i for i in range(100) if i%5==0]
print(L)#[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
# T1=(i for i in range(100) if i % 5 !=0)
# print(T1)# Error
S={i for i in range(100) if i % 5 !=0}
print(sorted(S))#[1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33,
# 34, 36, 37, 38, 39, 41, 42, 43, 44, 46, 47, 48, 49, 51, 52, 53, 54, 56, 57, 58, 59, 61, 62, 63, 64, 66, 67, 68, 69,
# 71, 72, 73, 74, 76, 77, 78, 79, 81, 82, 83, 84, 86, 87, 88, 89, 91, 92, 93, 94, 96, 97, 98, 99]
import math as m
L=[m.pow(x, 2) for x in range(11)]
print(L)#[0.0, 1.0, 4.0, 9.0, 16.0, 25.0, 36.0, 49.0, 64.0, 81.0, 100.0]
L1=[(i,j,c) for i in range (2) for j in range(3) for c in range(2)]
print(L1)#[(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (0, 2, 0), (0, 2, 1), (1, 0, 0), (1, 0, 1),
# (1, 1, 0), (1, 1, 1), (1, 2, 0), (1, 2, 1)]
L3=[m.pow(i,2) for i in range(100) if i % 3 ==0 and i %2 == 0]
print(L3)#[0.0, 36.0, 144.0, 324.0, 576.0, 900.0, 1296.0, 1764.0, 2304.0, 2916.0,
#3600.0, 4356.0, 5184.0, 6084.0, 7056.0, 8100.0, 9216.0]
L4=[(i*4,j+5) for i in range(3) for j in range(1 , 6)]
print(L4)#[(0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (4, 6), (4, 7), (4, 8),
#(4, 9), (4, 10), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10)]
for x in range(6):print('More')
else: print('Less')
# More
# More
# More
# More
# More
# More
# Less
print(sum([1.0/k for k in range (1,11,1)]))#2.9289682539682538
print([1.0/k for k in range(1,11)])
#[1.0, 0.5, 0.3333333333333333, 0.25, 0.2, 0.16666666666666666, 0.14285714285714285, 0.125, 0.1111111111111111, 0.1]
print(sum([k for k in range(100)]))#4950
print(sum([3*(x ** 3) for x in range(20)]))#108300
L=[m.pow(r, 2) for r in [10*i for i in range(20)]]
print(L)#[0.0, 100.0, 400.0, 900.0, 1600.0, 2500.0, 3600.0, 4900.0, 6400.0, 8100.0,
#10000.0, 12100.0, 14400.0, 16900.0, 19600.0, 22500.0, 25600.0, 28900.0, 32400.0, 36100.0]


