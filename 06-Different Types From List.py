# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 10:04:21 2022

@author: ENG-Alhousainy
"""
print('='*60) 
y=[x**3 for x in range(12)]
print(y)#print ==>[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331]
x=[i**2 for i in range(12)]
print(x)#print ==>[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
import numpy as np
Y=[np.sqrt(x) for x in range(12)]
print(Y)#print ==>[0.0, 1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979,
# 2.449489742783178, 2.6457513110645907, 2.8284271247461903, 3.0, 3.1622776601683795, 3.3166247903554]
X=[3*n for n in range(100,500,5)]
print(X)#print ==>[300, 315, 330, 345, 360, 375, 390, 405, 420, 435, 450, 465, 480, 495, 510, 525, 540, 555, 570,
#585, 600, 615, 630, 645, 660, 675, 690, 705, 720, 735, 750, 765, 780, 795, 810, 825, 840,855,870,885,900,915,
#930, 945, 960, 975, 990, 1005, 1020, 1035, 1050, 1065, 1080, 1095, 1110, 1125, 1140, 1155,1170,1185,1200,1215,
#1230, 1245, 1260, 1275, 1290, 1305, 1320, 1335, 1350, 1365, 1380, 1395, 1410, 1425, 1440, 1455, 1470, 1485]
#========================================================================================================
print('='*60)
#Method Two
import math as m
L =list(map(lambda x:x**3 , range(12)))
print(L)#print ==>[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331]
L1=list(map(lambda x : np.power(x,5),range(12)))
print(L1)#print ==>[0, 1, 32, 243, 1024, 3125, 7776, 16807, 32768, 59049, 100000, 161051]
L2=list(map(lambda x :m.factorial(x), range(12)))
print(L2)#print==>[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800]
L3=[-5+m.sqrt(i) for i in range(20)]
print(L3)#print ==>[-5.0,-4.0,-3.585786437626905,-3.267949192431123,-3.0,-2.76393202250021,-2.550510257216822,
# -2.3542486889354093, -2.1715728752538097, -2.0, -1.8377223398316205, -1.6833752096446002, -1.5358983848622456,
# -1.3944487245360109, -1.2583426132260587, -1.127016653792583, -1.0, -0.8768943743823394, -0.7573593128807152,
# -0.641101056459326]
L4=[-5+i*0.5 for i in range(40)]
print(L4)#print==>[-5.0, -4.5, -4.0, -3.5, -3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0,
#2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0,
#12.5, 13.0, 13.5, 14.0, 14.5]
#================================================================================================
print('='*60)
L1 =[(names , jobs) for names in ['A','B','C'] for jobs in ['DR','ENG','Lawyer']]
print(L1)#[('A', 'DR'), ('A', 'ENG'), ('A', 'Lawyer'), ('B', 'DR'), ('B', 'ENG'), ('B', 'Lawyer'),
#('C', 'DR'), ('C', 'ENG'), ('C', 'Lawyer')]
Users = ['Ahmed','Mostafa','Mona','Alaa','Mina']
Job =['Engineer','Doctor','Lawyer','Judge','Officer']
L2=[(names ,jobs) for names in Users for jobs in Job]
print(L2)#[('Ahmed', 'Engineer'),('Ahmed', 'Doctor'),('Ahmed', 'Lawyer'),('Ahmed', 'Judge'),('Ahmed', 'Officer'),
#('Mostafa', 'Engineer'),('Mostafa', 'Doctor'),('Mostafa', 'Lawyer'),('Mostafa', 'Judge'),('Mostafa', 'Officer'),
#('Mona', 'Engineer'), ('Mona', 'Doctor'), ('Mona', 'Lawyer'), ('Mona', 'Judge'), ('Mona', 'Officer'),
#('Alaa', 'Engineer'), ('Alaa', 'Doctor'), ('Alaa', 'Lawyer'), ('Alaa', 'Judge'), ('Alaa', 'Officer'),
#('Mina', 'Engineer'), ('Mina', 'Doctor'), ('Mina', 'Lawyer'), ('Mina', 'Judge'), ('Mina', 'Officer')]
L3=[(x,y) for x in [1,2,3,4,5] for y in [10,20,30,40]]
print(L3)#print[(1, 10), (1, 20), (1, 30), (1, 40), (2, 10), (2, 20), (2, 30), (2, 40), (3, 10),
#(3, 20), (3, 30), (3, 40), (4, 10), (4, 20), (4, 30), (4, 40), (5, 10), (5, 20), (5, 30), (5, 40)]
#==================================================================================================
'''
#مثال على التباديل والتوافيق
print('='*60)
print('التباديل والتوافيق ')
combination =[(x,y,z) for x in range(5) for y in range(7) for z in range (10)]
print(combination)#print ==>[(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 3), (0, 0, 4), (0, 0, 5), (0, 0, 6),
#(0, 0, 7), (0, 0, 8), (0, 0, 9), (0, 1, 0), (0, 1, 1), (0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 1, 5), (0, 1, 6),
#(0, 1, 7), (0, 1, 8), (0, 1, 9), (0, 2, 0), (0, 2, 1), (0, 2, 2), (0, 2, 3), (0, 2, 4), (0, 2, 5), (0, 2, 6),
#(0, 2, 7), (0, 2, 8), (0, 2, 9), (0, 3, 0), (0, 3, 1), (0, 3, 2), (0, 3, 3), (0, 3, 4), (0, 3, 5), (0, 3, 6),
#(0, 3, 7), (0, 3, 8), (0, 3, 9), (0, 4, 0), (0, 4, 1), (0, 4, 2), (0, 4, 3), (0, 4, 4), (0, 4, 5), (0, 4, 6),
#(0, 4, 7), (0, 4, 8), (0, 4, 9), (0, 5, 0), (0, 5, 1), (0, 5, 2), (0, 5, 3), (0, 5, 4), (0, 5, 5), (0, 5, 6),
#(0, 5, 7), (0, 5, 8), (0, 5, 9), (0, 6, 0), (0, 6, 1), (0, 6, 2), (0, 6, 3), (0, 6, 4), (0, 6, 5), (0, 6, 6),
#(0, 6, 7), (0, 6, 8), (0, 6, 9), (1, 0, 0), (1, 0, 1), (1, 0, 2), (1, 0, 3), (1, 0, 4), (1, 0, 5), (1, 0, 6),
#(1, 0, 7), (1, 0, 8), (1, 0, 9), (1, 1, 0), (1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 1, 4), (1, 1, 5), (1, 1, 6),
#(1, 1, 7), (1, 1, 8), (1, 1, 9), (1, 2, 0), (1, 2, 1), (1, 2, 2), (1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 2, 6),
#(1, 2, 7), (1, 2, 8), (1, 2, 9), (1, 3, 0), (1, 3, 1), (1, 3, 2), (1, 3, 3), (1, 3, 4), (1, 3, 5), (1, 3, 6),
#(1, 3, 7), (1, 3, 8), (1, 3, 9), (1, 4, 0), (1, 4, 1), (1, 4, 2), (1, 4, 3), (1, 4, 4), (1, 4, 5), (1, 4, 6),
#(1, 4, 7), (1, 4, 8), (1, 4, 9), (1, 5, 0), (1, 5, 1), (1, 5, 2), (1, 5, 3), (1, 5, 4), (1, 5, 5), (1, 5, 6),
#(1, 5, 7), (1, 5, 8), (1, 5, 9), (1, 6, 0), (1, 6, 1), (1, 6, 2), (1, 6, 3), (1, 6, 4), (1, 6, 5), (1, 6, 6),
#(1, 6, 7), (1, 6, 8), (1, 6, 9), (2, 0, 0), (2, 0, 1), (2, 0, 2), (2, 0, 3), (2, 0, 4), (2, 0, 5), (2, 0, 6),
#(2, 0, 7), (2, 0, 8), (2, 0, 9), (2, 1, 0), (2, 1, 1), (2, 1, 2), (2, 1, 3), (2, 1, 4), (2, 1, 5), (2, 1, 6),
#(2, 1, 7), (2, 1, 8), (2, 1, 9), (2, 2, 0), (2, 2, 1), (2, 2, 2), (2, 2, 3), (2, 2, 4), (2, 2, 5), (2, 2, 6),
#(2, 2, 7), (2, 2, 8), (2, 2, 9), (2, 3, 0), (2, 3, 1), (2, 3, 2), (2, 3, 3), (2, 3, 4), (2, 3, 5), (2, 3, 6),
#(2, 3, 7), (2, 3, 8), (2, 3, 9), (2, 4, 0), (2, 4, 1), (2, 4, 2), (2, 4, 3), (2, 4, 4), (2, 4, 5), (2, 4, 6),
#(2, 4, 7), (2, 4, 8), (2, 4, 9), (2, 5, 0), (2, 5, 1), (2, 5, 2), (2, 5, 3), (2, 5, 4), (2, 5, 5), (2, 5, 6),
#(2, 5, 7), (2, 5, 8), (2, 5, 9), (2, 6, 0), (2, 6, 1), (2, 6, 2), (2, 6, 3), (2, 6, 4), (2, 6, 5), (2, 6, 6),
#(2, 6, 7), (2, 6, 8), (2, 6, 9), (3, 0, 0), (3, 0, 1), (3, 0, 2), (3, 0, 3), (3, 0, 4), (3, 0, 5), (3, 0, 6),
#(3, 0, 7), (3, 0, 8), (3, 0, 9), (3, 1, 0), (3, 1, 1), (3, 1, 2), (3, 1, 3), (3, 1, 4), (3, 1, 5), (3, 1, 6),
#(3, 1, 7), (3, 1, 8), (3, 1, 9), (3, 2, 0), (3, 2, 1), (3, 2, 2), (3, 2, 3), (3, 2, 4), (3, 2, 5), (3, 2, 6),
#(3, 2, 7), (3, 2, 8), (3, 2, 9), (3, 3, 0), (3, 3, 1), (3, 3, 2), (3, 3, 3), (3, 3, 4), (3, 3, 5), (3, 3, 6),
#(3, 3, 7), (3, 3, 8), (3, 3, 9), (3, 4, 0), (3, 4, 1), (3, 4, 2), (3, 4, 3), (3, 4, 4), (3, 4, 5), (3, 4, 6),
#(3, 4, 7), (3, 4, 8), (3, 4, 9), (3, 5, 0), (3, 5, 1), (3, 5, 2), (3, 5, 3), (3, 5, 4), (3, 5, 5), (3, 5, 6),
#(3, 5, 7), (3, 5, 8), (3, 5, 9), (3, 6, 0), (3, 6, 1), (3, 6, 2), (3, 6, 3), (3, 6, 4), (3, 6, 5), (3, 6, 6),
#(3, 6, 7), (3, 6, 8), (3, 6, 9), (4, 0, 0), (4, 0, 1), (4, 0, 2), (4, 0, 3), (4, 0, 4), (4, 0, 5), (4, 0, 6),
#(4, 0, 7), (4, 0, 8), (4, 0, 9), (4, 1, 0), (4, 1, 1), (4, 1, 2), (4, 1, 3), (4, 1, 4), (4, 1, 5), (4, 1, 6),
#(4, 1, 7), (4, 1, 8), (4, 1, 9), (4, 2, 0), (4, 2, 1), (4, 2, 2), (4, 2, 3), (4, 2, 4), (4, 2, 5), (4, 2, 6),
#(4, 2, 7), (4, 2, 8), (4, 2, 9), (4, 3, 0), (4, 3, 1), (4, 3, 2), (4, 3, 3), (4, 3, 4), (4, 3, 5), (4, 3, 6),
#(4, 3, 7), (4, 3, 8), (4, 3, 9), (4, 4, 0), (4, 4, 1), (4, 4, 2), (4, 4, 3), (4, 4, 4), (4, 4, 5), (4, 4, 6),
#(4, 4, 7), (4, 4, 8), (4, 4, 9), (4, 5, 0), (4, 5, 1), (4, 5, 2), (4, 5, 3), (4, 5, 4), (4, 5, 5), (4, 5, 6),
#(4, 5, 7), (4, 5, 8), (4, 5, 9), (4, 6, 0), (4, 6, 1), (4, 6, 2), (4, 6, 3), (4, 6, 4), (4, 6, 5), (4, 6, 6),
#(4, 6, 7), (4, 6, 8), (4, 6, 9)]
'''
#==================================================================================================
print('='*60)

print('المصفوفات = 7 صفوف * 5 أعمدة')
matrix =[[0 for i in range(5)] for j in range (7)]
print(matrix)#المصفوفات = 7 صفوف * 5 أعمدة
#[[0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0]]
matrix1 =[[i for i in range(5)] for j in range (7)]
print(matrix1)
#[[0, 1, 2, 3, 4],
#[0, 1, 2, 3, 4],
#[0, 1, 2, 3, 4], 
#[0, 1, 2, 3, 4], 
#[0, 1, 2, 3, 4], 
#[0, 1, 2, 3, 4], 
#[0, 1, 2, 3, 4]]
#=======================================================================================================
print('='*60)
L1 = iter([10,20,30,40,1,2,3,4,5,6,7,8,9,11])
print(next(L1))#print==>10
print(next(L1))#print==>20
print(next(L1))#print==>30
print(next(L1))#print==>40
print(next(L1))#print==>1
print(next(L1))#print==>2
print(next(L1))#print==>3
L2=iter(['Ahmed','Mostafa','Ali', '3laa','Arwa','Esso','Yasser','Dad','Mum'])
# print(next(L2))#print ==>Ahmed
# print(next(L2))#print ==>Mostafa
# print(next(L2))#print ==>Ali
# print(next(L2))#print ==>3laa
# print(next(L2))#print ==>Arwa
#Length
# print(len(next(L2)))#print ==>5
# print(len(next(L2)))#print ==>7
# print(len(next(L2)))#print ==>3
# print(len(next(L2)))#print ==>4
# print(len(next(L2)))#print ==>4
a= next(L2)
print(a[0])#print ==>A
a= next(L2)
print(a[0])#print ==>M
a= next(L2)
print(a[0])#print ==>A
a= next(L2)
print(a[0])#print ==>3
a= next(L2)
print(a[0])#print ==>A
a= next(L2)
print(a[0])#print ==>E
a= next(L2)
print(a[0])#print ==>Y
#Using Range With Iter
B = iter(range(12))
print(next(B))#print ==>0
print(next(B))#print ==>1
print(next(B))#print ==>2
print(next(B))#print ==>3
print(next(B))#print ==>4
#====================================================================
print('='*60)
List1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,0,5,6,8,1,2,3,4]
print(List1[7])#print==>8
List2=List1
print(List2[7])#print==>8
L3 =['A','B','C']
List2.extend(L3)
print(List2)#print==>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 5, 6, 8, 1, 2, 3, 4, 'A', 'B', 'C']
print(List1)#print==>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 5, 6, 8, 1, 2, 3, 4, 'A', 'B', 'C']
List1.append('F')
print(List1)#print==>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 5, 6, 8, 1, 2, 3, 4, 'A', 'B', 'C', 'F']
print(List2)#print==>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 5, 6, 8, 1, 2, 3, 4, 'A', 'B', 'C', 'F']
#===============================================================================================================
x=[1,2,3,4,5,6,7,8,9]
y=x.copy()
print(x)#print==>[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(y)#print==>[1, 2, 3, 4, 5, 6, 7, 8, 9]
z=['A','B']
y.append('D')
x.extend(z)
print(x)#print==>[1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B']
print(y)#print==>[1, 2, 3, 4, 5, 6, 7, 8, 9, 'D']
#================================================================================================
print('='*60)
names =['Ahmed', 'Mona','Ali','Mostafa' ,'Omar','Eslam']
for c , value in enumerate(names , 1):
    print(c,value)
#print ==>1 Ahmed
#print ==>2 Mona
#print ==>3 Ali
#print ==>4 Mostafa
#print ==>5 Omar
#print ==>6 Eslam
print('='*20)
List_Names =['Ahmed', 'Mona','Ali','Mostafa' ,'Omar','Eslam']
for i , value in enumerate(List_Names):
    print(i,value)
print('='*20)
for x , value in enumerate(range(11),300):
    print(x,value)
print('='*20)
#====================================================================================================
alist =['a1','a2','a3','a4']
blist=['b1','b2','b3','b4']
for a,b in zip(alist,blist):
    print(a,b)
print('='*20)
L1 = ['Alhousainy','Arwa' ,'Esso','Yasser']
L2 =['is Engineer' ,'Is Secondary Student' ,'Is Unviersity Student' ,'Is Dentist']
for a ,b in zip(L1,L2):
    print(a,b)
print('#'*30)    
L3=['Ahmed','Mostafa' ,'Mona','Dina','Ali','George']
L4=['IS From Egypt','Is From Libya','IS From Jordan','IS From Emirates','IS From Yeman','IS From Germany']
L6=['He is an Engineer' ,'He is a Doctor', 'She is a Lawyer','She is a judge','he is an Officer','he is a Lecturer']
L7=['and is 26 Years Old' ,'and is 20 Years Old','and is 33 Years Old','and is 40 Years Old','and is 30 Years Old','and is 28 Years Old']
for a,b,c,d in zip(L3,L4,L6,L7):
    print(a,b,c,d)    
# Ahmed IS From Egypt He is an Engineer and is 26 Years Old
# Mostafa Is From Libya He is a Doctor and is 20 Years Old
# Mona IS From Jordan She is a Lawyer and is 33 Years Old
# Dina IS From Emirates She is a judge and is 40 Years Old
# Ali IS From Yeman he is an Officer and is 30 Years Old
# George IS From Germany he is a Lecturer and is 28 Years Old  
############################################################################################
print('='*50)
# import operator as op
from operator import itemgetter
Students =[('Ahmed','Egypt',15),('Mostafa','Libya',18),('Mona','Moroco',25),('George','Syria',27),('Kamel','Kawit',12)]
Arrange =sorted(Students , key = itemgetter(2))
print(Arrange)
#print ==> قام بالترتيب بناءً على العمر 
# [('Kamel', 'Kawit', 12), ('Ahmed', 'Egypt', 15), ('Mostafa', 'Libya', 18),
# ('Mona', 'Moroco', 25), ('George', 'Syria', 27)]   
Arrange2 = sorted(Students,key = itemgetter(0)) 
print(Arrange2)
#print ==> قام بالترتيب بناءً على العنصر الاول وهو الاسم
# [('Ahmed', 'Egypt', 15), ('George', 'Syria', 27), ('Kamel', 'Kawit', 12),
# ('Mona', 'Moroco', 25), ('Mostafa', 'Libya', 18)]
Arrange3 = sorted(Students,key = itemgetter(1)) 
print(Arrange3)
#print ==> قام بالترتيب بناءاً على الدولة
#[('Ahmed', 'Egypt', 15), ('Kamel', 'Kawit', 12), ('Mostafa', 'Libya', 18),
#('Mona', 'Moroco', 25), ('George', 'Syria', 27)]
S=[('Ahmed','Egypt',25),('Mostafa','Libya',18),('Mona','Moroco',25),('George','Syria',27),
('Kamel','Kawit',12),('Kamal' ,'Egypt',15)]
print(sorted(S,key=itemgetter(1)))
#[('Ahmed', 'Egypt', 15), ('Kamal', 'Egypt', 25), ('Kamel', 'Kawit', 12), 
#('Mostafa', 'Libya', 18), ('Mona', 'Moroco', 25), ('George', 'Syria', 27)]
print(sorted(S,key=itemgetter(1,2)))
# [('Kamal', 'Egypt', 15), ('Ahmed', 'Egypt', 25), ('Kamel', 'Kawit', 12), 
# ('Mostafa', 'Libya', 18), ('Mona', 'Moroco', 25), ('George', 'Syria', 27)]
S1=[('Ahmed','Egypt',25),('Mostafa','Libya',18),('Mona','Moroco',25),('George','Syria',27),
('Kamel','Kawit',12),('Kamal' ,'Egypt',15),('Mohammed' ,'Syria',15),('Tamer' ,'Moroco',13),
('Mina' ,'Egypt',12),('Hala' ,'Libya',10)]
print(sorted(S1,key=itemgetter(1)))
# [('Ahmed', 'Egypt', 25), ('Kamal', 'Egypt', 15), ('Mina', 'Egypt', 12), ('Kamel', 'Kawit', 12), 
# ('Mostafa', 'Libya', 18), ('Hala', 'Libya', 10), ('Mona', 'Moroco', 25), 
# ('Tamer', 'Moroco', 13), ('George', 'Syria', 27), ('Mohammed', 'Syria', 15)]
print(sorted(S1,key=itemgetter(1,2)))
# [('Mina', 'Egypt', 12), ('Kamal', 'Egypt', 15), ('Ahmed', 'Egypt', 25), ('Kamel', 'Kawit', 12),
# ('Hala', 'Libya', 10), ('Mostafa', 'Libya', 18), ('Tamer', 'Moroco', 13), ('Mona', 'Moroco', 25), 
# ('Mohammed', 'Syria', 15), ('George', 'Syria', 27)]
from operator import methodcaller
S2=['ahmed','ali','Mostafa','Mona' ,'alhousainy','abdelrahman','lamiaa','alia']
y=sorted(S2,key=methodcaller('count','a'))
print(y)
#['ahmed', 'ali', 'Mona', 'Mostafa', 'alhousainy', 'alia', 'abdelrahman', 'lamiaa']
