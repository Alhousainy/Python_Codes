# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 15:13:14 2022

@author: ENG-Alhousainy
"""
print('='*60)
L =['Alhousainy','Abdelrahman', True , False , 10, 15.18, 10+20j,'Alhousainy', True , 10]#List
T=('Alhousainy','abdelrahman',True , False , 10 , 15.18 , 10+20j,'Alhousainy', 10 , False)#Tuple
print(L)#print ==>['Alhousainy', 'Abdelrahman', True, False, 10, 15.18, (10+20j), 'Alhousainy', True, 10]
print(T)#print ==>('Alhousainy', 'abdelrahman', True, False, 10, 15.18, (10+20j), 'Alhousainy', 10, False)
S ={'Alhousainy','abdelrahman',True , False , 10 , 15.18 , 10+20j}
print(S)#Print ==>{False, True, 'Alhousainy', (10+20j), 10, 15.18, 'abdelrahman'} 
D ={'A':10,'B':20,'C':30}#Dictinary
print(D)#Print==>{'A': 10, 'B': 20, 'C': 30}
l1 = ['Alhousainy','Abdelrahman', 10 , 2 ,['ISFP',10+20j],'D',['Mostafa', True]]
print(l1)#print==>['Alhousainy', 'Abdelrahman', 10, 2, ['ISFP', (10+20j)], 'D', ['Mostafa', True]]
#Example About 5 Students
l2=[[10,20,30],[10,15,25],[8,20,30],[10,20,30],[7,11,10]]
print(l2)#print==>[[10, 20, 30], [10, 15, 25], [8, 20, 30], [10, 20, 30], [7, 11, 10]]
l3=list('I Love Python')
print(l3)#print==>['I', ' ', 'L', 'o', 'v', 'e', ' ', 'P', 'y', 't', 'h', 'o', 'n']
a=list('python')
b,c,d,e,f,g=a
print(a)#print==>['p', 'y', 't', 'h', 'o', 'n']
print(b)#print==>p
print(c)#print==>y
print(d)#print==>t
print(e)#print==>h
print(f)#print==>o
print(g)#print==>n
l4=['Alhousainy', 'Abdelrahman', 26 , 5+10j]
print(len(l4))#print ==>4
print(l4[2])#print==>26
l5=list('My Name Is Alhousainy')
print(len(l5))#print==>21
print(l5)
#print==>['M', 'y', ' ', 'N', 'a', 'm', 'e', ' ', 'I', 's', ' ', 'A', 'l', 'h', 'o', 'u', 's', 'a', 'i', 'n', 'y']
print(l5[11:21])#print==>['A', 'l', 'h', 'o', 'u', 's', 'a', 'i', 'n', 'y']
l6=l5[11:21]
print(l6)#print==>['A', 'l', 'h', 'o', 'u', 's', 'a', 'i', 'n', 'y']
l7=l5[:7]
print(l7)#print==['M', 'y', ' ', 'N', 'a', 'm', 'e']
l8=l5[:-3]
print(l8)#print==>['M', 'y', ' ', 'N', 'a', 'm', 'e', ' ', 'I', 's', ' ', 'A', 'l', 'h', 'o', 'u', 's', 'a']
l9=l5[11:]
print(l9)#print ==>['A', 'l', 'h', 'o', 'u', 's', 'a', 'i', 'n', 'y']
l10=l5[40:]
print(l10)#print ==>[]
l11=l5[:]
print(l11)
#print==>['M', 'y', ' ', 'N', 'a', 'm', 'e', ' ', 'I', 's', ' ', 'A', 'l', 'h', 'o', 'u', 's', 'a', 'i', 'n', 'y']
l5[10]='#'
l5[2] ='#'
l5[7] ='#'
print(l5)
#print==>['M', 'y', '#', 'N', 'a', 'm', 'e', '#', 'I', 's', '#', 'A', 'l', 'h', 'o', 'u', 's', 'a', 'i', 'n', 'y']
l5[2:6]=[]
print(l5)#print==>['M', 'y', 'e', '#', 'I', 's', '#', 'A', 'l', 'h', 'o', 'u', 's', 'a', 'i', 'n', 'y']
l5[2]=['N','a','m','e']
print(l5)
#print==>['M', 'y', ['N', 'a', 'm', 'e'], '#', 'I', 's', '#', 'A', 'l', 'h', 'o', 'u', 's', 'a', 'i', 'n', 'y']
l5[:]=[]
print(l5)#print==>[]
a1=['A','L','h','o','u','s','a','i','n','y']
b=[1,2,3,4,5]
c=[True, False , 9.4, 5+10j,'y']
x=[a1,b,c]
print(x)
#priny==>[['A', 'L', 'h', 'o', 'u', 's', 'a', 'i', 'n', 'y'], [1, 2, 3, 4, 5], [True, False, 9.4, (5+10j), 'y']]
print(x[0])#print==>['A', 'L', 'h', 'o', 'u', 's', 'a', 'i', 'n', 'y']
print(x[1])#print==>[1, 2, 3, 4, 5]
print(x[2])#print==>[True, False, 9.4, (5+10j), 'y']
print(x[0][1])#print==>L
print(x[1][2])#print==>3
print(x[2][0])#print==>True
print(x[0][0:4])#print==>['A', 'L', 'h', 'o']
L1 =['A', 'L', 'h', 'o', 1 , 2 , 3 , 4 , 5 , 6,True , False]
print(len(L1))#print==>12 Elements
del L1[5]
print(L1)#print==>['A', 'L', 'h', 'o', 1, 3, 4, 5, 6, True, False]
del L1[-1]
print(L1)#Print ==>['A', 'L', 'h', 'o', 1, 3, 4, 5, 6, True]
del L1[-2]
print(L1)#Print ==>['A', 'L', 'h', 'o', 1, 3, 4, 5, True]
del L1[0:5]
print(L1)#print ==>[3, 4, 5, True]
del L1
#print(L1)#print ==>[]
L2 = ['a','b','c','a','d',1 ,2 , 1, 1,1,8,'a','a','a']
L2.remove(1)
print(L2)#print ==>['a', 'b', 'c', 'a', 'd', 2, 1, 1, 1, 8, 'a', 'a', 'a']
L2.remove('a')
print(L2)#print==>['b', 'c', 'a', 'd', 2, 1, 1, 1, 8, 'a', 'a', 'a']
x =['a','b','c']
y =[1,2,3,4,5,6,7,8,9]
z=[True ,False]
m=x+y+z
print(m)#print==>['a', 'b', 'c', 1, 2, 3, 4, 5, 6, 7, 8, 9, True, False]
x1='Alhousainy  '
y1='esso  '
z1='Arwa  '
x2='yasser  '
L_T=x1+y1+z1+x2
print(L_T)#print==>Alhousainy  esso  Arwa  yasser  
L_T=[x1,y1,z1,x2]
print(L_T)#print==>['Alhousainy', 'esso', 'Arwa', 'yasser']
print(x*5)#print==>['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
print(x1*5)#print==>Alhousainy  Alhousainy  Alhousainy  Alhousainy  Alhousainy  
print([x1*5])#print==>['Alhousainy  Alhousainy  Alhousainy  Alhousainy  Alhousainy  ']
print([x1]*5)#print==>['Alhousainy  ', 'Alhousainy  ', 'Alhousainy  ', 'Alhousainy  ', 'Alhousainy  ']
print([x1])#print==>['Alhousainy  ']
no = [10]
print(no)#print==>[10]
print(no*100)#print==>[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
# 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
# 10,10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
# 10,10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
no1=[0]*8
print(no1)#print==>[0, 0, 0, 0, 0, 0, 0, 0] ==> One Row * 8 columns
no2=[[0]*8]*10
print(no2) # 10 Rows * 8 Columns
#print==>[[0, 0, 0, 0, 0, 0, 0, 0],
#print==>[0, 0, 0, 0, 0, 0, 0, 0],
#print==>[0, 0, 0, 0, 0, 0, 0, 0],
#print==>[0, 0, 0, 0, 0, 0, 0, 0],
#print==>[0, 0, 0, 0, 0, 0, 0, 0],
#print==>[0, 0, 0, 0, 0, 0, 0, 0],
#print==>[0, 0, 0, 0, 0, 0, 0, 0],
#print==>[0, 0, 0, 0, 0, 0, 0, 0],
#print==>[0, 0, 0, 0, 0, 0, 0, 0],
#print==>[0, 0, 0, 0, 0, 0, 0, 0]]
print(len(no2))#print==>10
print(no*10)#[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
print(sum(no*10))#print==>100
no3=[10,50,60,7,8,90,100,350]
print(sum(no3))#print==>675
a= sum(no3)
b= len(no3)
print(a/b)#print==>84.375
List=[80,90,70,40,10,20,30,100,350]
print(max(List))#print ==>352
print(min(List))#print ==>10
List_1=['A','l','h','o','u','s','a','i','n','y']
print(max(List_1))#print==>y
print(min(List_1))#print ==>A
print(sorted(List))#print==>[10, 20, 30, 40, 70, 80, 90, 100, 350]
print((List))#print==>[80, 90, 70, 40, 10, 20, 30, 100, 350]
print(sorted(List_1))#print==>['A', 'a', 'h', 'i', 'l', 'n', 'o', 's', 'u', 'y']
print((List_1))#print ==>['A', 'l', 'h', 'o', 'u', 's', 'a', 'i', 'n', 'y']
List.sort()
print(List)#print==>[10, 20, 30, 40, 70, 80, 90, 100, 350]
List_1.sort()
print(List_1)#print==>['A', 'a', 'h', 'i', 'l', 'n', 'o', 's', 'u', 'y']
print('='*60)
###################################################################################################
EX1=[10,20,5,7,8,22,33,9,15]
print(sorted(EX1))#print==>[5, 7, 8, 9, 10, 15, 20, 22, 33]
print(sorted(EX1,reverse =True))#print==>[33, 22, 20, 15, 10, 9, 8, 7, 5]
print(sorted(EX1,reverse=False))#print==>[5, 7, 8, 9, 10, 15, 20, 22, 33]
EX2=['A','l','h','o','u','s','a','i','n','y']
print(sorted(EX2))#print==>['A', 'a', 'h', 'i', 'l', 'n', 'o', 's', 'u', 'y']
print(sorted(EX2,reverse=True))#print==>['y', 'u', 's', 'o', 'n', 'l', 'i', 'h', 'a', 'A']
print(sorted(EX2,reverse=False))#print==>['A', 'a', 'h', 'i', 'l', 'n', 'o', 's', 'u', 'y']
EX3=[('Eslam',10),('Khalad',15),('Ahmed',50),('Mostafa',40),('Mona',17)]
b=sorted(EX3,key=lambda b:b[0])
print(b)#print==>[('Ahmed', 50), ('Eslam', 10), ('Khalad', 15), ('Mona', 17), ('Mostafa', 40)]
c=sorted(EX3,key=lambda e:e[1])
print(c)#print==>[('Eslam', 10), ('Khalad', 15), ('Mona', 17), ('Mostafa', 40), ('Ahmed', 50)]
EX4=[('Ahmed','egypt',28 ,15),('zaki','yeman',32 ,12),
('Mona','Moroco',25 ,30),('Ali','Libya',11 ,19),('George','lebnon',21 ,8)]
y=sorted(EX4 , key = lambda c: c[0])
print(EX4)#print==>[('Ahmed', 'egypt', 28, 15), ('zaki', 'yeman', 32, 12), 
# ('Mona', 'Moroco', 25, 30), ('Ali', 'Libya', 11, 19), ('George', 'lebnon', 21, 8)]
A=sorted(EX4, key = lambda e: e[1])
print(A)#[('Ali', 'Libya', 11, 19), ('Mona', 'Moroco', 25, 30),
#('Ahmed', 'egypt', 28, 15), ('George', 'lebnon', 21, 8), ('zaki', 'yeman', 32, 12)]
n=sorted(EX4, key = lambda e: e[2])
print(n)#[('Ali', 'Libya', 11, 19), ('George', 'lebnon', 21, 8), ('Mona', 'Moroco', 25, 30),
#('Ahmed', 'egypt', 28, 15), ('zaki', 'yeman', 32, 12)]
D=sorted(EX4, key = lambda e: e[3])
print(D)#[('George', 'lebnon', 21, 8), ('zaki', 'yeman', 32, 12), ('Ahmed', 'egypt', 28, 15),
#('Ali', 'Libya', 11, 19), ('Mona', 'Moroco', 25, 30)]
d=sorted(EX4,reverse =True, key = lambda e: e[3])
print(d)#[('Mona', 'Moroco', 25, 30), ('Ali', 'Libya', 11, 19), ('Ahmed', 'egypt', 28, 15),
#('zaki', 'yeman', 32, 12), ('George', 'lebnon', 21, 8)]
ST1='I Love Python Becuase It Is An Easy Programming Language'
S= ST1.split()
print(S)#print==>['I', 'Love', 'Python', 'Becuase', 'It', 'Is', 'An', 'Easy', 'Programming', 'Language']
#Seperator Example
ST2='My=Name=Is=Alhousainy'
S1=ST2.split('=')#Seperator
print(S1)#['My', 'Name', 'Is', 'Alhousainy']
ST3='18,45,7,98,100,50,200'
S2=ST3.split(',')
print(S2)#print==>['18', '45', '7', '98', '100', '50', '200']
ST4='My,Name,Is,Alhousainy,And,My,Age,Is,26,Years,Old,And,Iam,An,Machine,Learning,Eng'
S3=ST4.split(',',maxsplit=4)
print(S3)
#print==>['My', 'Name', 'Is', 'Alhousainy', 'And,My,Age,Is,26,Years,Old,And,Iam,An,Machine,Learning,Eng']
LIST2=[10,20,30,15,17,18,19]
S5 =10 in LIST2
print(S5)#print==>True
#print(10 in LIST2)#print==>True
#print(100 in LIST2)#print==>False
S6 = 100 in LIST2
#===================================================================================
print(S6)#print==>True
LIST3=['Ahmed','Mona','Zaky','Farouk']
#print('Ahmed' in LIST3)#print==>True
#print('Ali' in LIST3)#print ==>False
S7 ='Ahmed' in LIST3
S8 ='Ali' in LIST3
print(S7)#print ==>True
print(S8)#print ==>False
#=====================================================================================
print('='*60)
LIST4=['My', 'Name', 'Is', 'Alhousainy']
LIST5=['And', 'My', 'Age', 'Is' , 26,'Years','Old']
LIST5.extend(LIST4)
print(LIST5)#print==>['And', 'My', 'Age', 'Is', 26, 'Years', 'Old', 'My', 'Name', 'Is', 'Alhousainy']
#===========================================================================================
print('='*60)
LIST6 = [1,2,3,4,5,'Ahmed','mostafa','Mohammed']
LIST6.append(20)
LIST6.append(50)
LIST6.append('Alhousainy')
LIST6.append(True)
LIST6.append((50,40,20))
LIST6.append([8,4])
print(LIST6)
#print==>[1, 2, 3, 4, 5, 'Ahmed', 'mostafa', 'Mohammed', 20, 50, 'Alhousainy', True, (50, 40, 20), [8, 4]]
#=========================================================================================================
print('='*60)
LIST7=[1,10,8,9,'Mohammed','Esso',True]
LIST7.insert(3, 'Yasser')
print(LIST7)#print==>[1, 10, 8, 'Yasser', 9, 'Mohammed', 'Esso', True]
LIST7.insert(2, 'Arwa')
print(LIST7)#print==>[1, 10, 'Arwa', 8, 'Yasser', 9, 'Mohammed', 'Esso', True]
LIST7.insert(4, 'Ahmed')
print(LIST7)#print==>[1, 10, 'Arwa', 8, 'Ahmed', 'Yasser', 9, 'Mohammed', 'Esso', True]
LIST7.insert(1, 'MUM')
print(LIST7)#print==>[1, 'MUM', 10, 'Arwa', 8, 'Ahmed', 'Yasser', 9, 'Mohammed', 'Esso', True]
LIST7.insert(0, 'DAD')
print(LIST7)#print==>['DAD', 1, 'MUM', 10, 'Arwa', 8, 'Ahmed', 'Yasser', 9, 'Mohammed', 'Esso', True]
#============================================================================================================
print('='*60)
LIST8=[1,1,2,3,4,5,6,7,8,9,2,2,2,5,5,5,5,4,4,4,4,10,10,10,10,10,10]
print(LIST8.count(1))#print ==>2
print(LIST8.count(2))#print ==>4
print(LIST8.count(4))#print ==>5
print(LIST8.count(5))#print ==>5
print(LIST8.count(10))#print ==>6
#============================================================================================================
print('='*60)
LIST9=['A','B','C','D','AC','DA','MH','BR']
print(LIST9.index('AC'))#print==> 4
print(LIST9)#print ==>['A', 'B', 'C', 'D', 'AC', 'DA', 'MH', 'BR']
LIST9.reverse()
print(LIST9)#print ==>['BR', 'MH', 'DA', 'AC', 'D', 'C', 'B', 'A']
LIST9.reverse()
print(LIST9)#print ==>['A', 'B', 'C', 'D', 'AC', 'DA', 'MH', 'BR']
LIST9.pop()
print(LIST9)#print ==>['A', 'B', 'C', 'D', 'AC', 'DA', 'MH']
LIST9.pop(3)
print(LIST9)#print==>['A', 'B', 'C', 'AC', 'DA', 'MH']
#============================================================================================================
print('='*60)
L10 = range(20)
print(L10)#print==>range(0,20)
L11=list(L10)
print(L11)#print==>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
L12=list(range(10))
print(L12)#print==>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
L13 =list(range(3,11))
print(L13)#print==>[3, 4, 5, 6, 7, 8, 9, 10]
L14=list(range(1,50,3))
print(L14)#print==>[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49]
