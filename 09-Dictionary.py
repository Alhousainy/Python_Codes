# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 02:14:56 2022

@author: ENG-Alhousainy
"""
print('='*60)
allkeys={'Egypt':'0020','USA':'001','KSA':'00966','UK':'0044','UAE':'00971'}
print(allkeys)#{'Egypt': '0020', 'USA': '001', 'KSA': '00966', 'UK': '0044', 'UAE': '00971'}
degress={'Alhousainy':49 ,'Mona':45 ,'Mostafa':40 ,'Ali':55 ,'Mia':38 ,'Ahmed':42 ,'Nada':30 ,'Shrook':25 ,'Liamiaa':20 }
print(degress)
#{'Alhousainy': 49, 'Mona': 45, 'Mostafa': 40, 'Ali': 55, 'Mia': 38, 'Ahmed': 42, 'Nada': 30, 'Shrook': 25, 'Liamiaa': 20}
weights ={ 33:'Bag1',26:'Bag2',30:'Bag3',29:'Bag4',28:'Bag5',20:'Bag6',40:'Bag7',40:'Bag7'}
print(weights)#{33: 'Bag1', 26: 'Bag2', 30: 'Bag3', 29: 'Bag4', 28: 'Bag5', 20: 'Bag6', 40: 'Bag7'}
points={n:n**2 for n in range(6)}
print(points)#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
degress['Mona']=48
degress['Limiaa']=47
print(degress)
#{'Alhousainy':49,'Mona': 48,'Mostafa': 40,'Ali':55,'Mia':38,'Ahmed':42,'Nada':30,'Shrook':25,'Liamiaa':20,'Limiaa':47}
print('Alhousainy' in degress)#True
print(33 in weights)#True
print(9 in points)#False
print('Khalad' in allkeys)#False
print(9 in points.values())#True
print('0020' in allkeys)#False
print('0020' in allkeys.values())#True
print(allkeys.get('Egypt'))#0020
print(allkeys.get('egypt'))#None
Dict={'A':10 ,'B':11 ,'C':12 ,'D':13 ,'E':14 ,'F':15 ,'A':20 ,'B':17 ,'M':5 ,'A':5 }
print(Dict)#{'A': 5, 'B': 17, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'M': 5}
print('A' in Dict)#True
print(Dict.get('A'))#5
print(11 in Dict.values())#True
print(25 in Dict.values())#False
print(Dict.get('France'))#None
print(Dict.get('D'))#13
print(Dict.get('M'))#5
print(Dict.get('M',20))#5
print(Dict.get('Egypt',20))#20
Dict1={'Alhousainy':'ML_ENG','Ali':'DR','Mostafa':'ENG','Mona':'Teacher','Alia':'D_S_Eng','Ahmed':'Lawyer'}
degrees={'Alhousainy':49 ,'Mona':45 ,'Mostafa':40 ,'Ali':55 ,'Mia':38 ,'Ahmed':42 ,'Nada':30 ,'Shrook':25 ,'Liamiaa':20 }
degrees['Alhousainy']=50
print(degrees)
#{'Alhousainy': 50, 'Mona': 45, 'Mostafa': 40, 'Ali': 55, 'Mia': 38, 'Ahmed': 42, 'Nada': 30, 'Shrook': 25, 'Liamiaa': 20}
degrees['Hoda']=37
print(degrees)
#{'Alhousainy':50,'Mona':45,'Mostafa':40,'Ali':55,'Mia':38,'Ahmed': 42, 'Nada': 30, 'Shrook': 25, 'Liamiaa': 20, 'Hoda': 37}
del(Dict['A'])
print(Dict)#{'B': 17, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'M': 5}
del(Dict['B'])
del(Dict['D'])
del(Dict['C'])
print(Dict)#{'E': 14, 'F': 15, 'M': 5}
Dict.clear()
print(Dict)#{}
Dict['Alhousainy']='Machine Learning Engineer'
Dict['Esso']='Web Webdevlopper'
Dict['Yasser']='Dentist'
print(Dict)#{'Alhousainy': 'Machine Learning Engineer', 'Esso': 'Web Webdevlopper', 'Yasser': 'Dentist'}
print(len(Dict))#3
del(Dict)
#print(Dict)#NameError==> name 'Dict' is not defined
print(Dict1)#{'Alhousainy': 'ML_ENG', 'Ali': 'DR', 'Mostafa': 'ENG', 'Mona': 'Teacher', 'Alia': 'D_S_Eng', 'Ahmed': 'Lawyer'}
D=Dict1.copy()
print(D)#{'Alhousainy': 'ML_ENG', 'Ali': 'DR', 'Mostafa': 'ENG', 'Mona': 'Teacher', 'Alia': 'D_S_Eng', 'Ahmed': 'Lawyer'}
D.clear()
print(Dict1)#{'Alhousainy': 'ML_ENG', 'Ali': 'DR', 'Mostafa': 'ENG', 'Mona': 'Teacher', 'Alia': 'D_S_Eng', 'Ahmed': 'Lawyer'}
print(D)#{}
D['Ahmed']=50
D['Mostafa']=49
D['Ali']=40
D['Mona']=35
print(Dict1)#{'Alhousainy': 'ML_ENG', 'Ali': 'DR', 'Mostafa': 'ENG', 'Mona': 'Teacher', 'Alia': 'D_S_Eng', 'Ahmed': 'Lawyer'}
print(D)#{'Ahmed': 50, 'Mostafa': 49, 'Ali': 40, 'Mona': 35}
D1=D.copy()
print(D)#{'Ahmed': 50, 'Mostafa': 49, 'Ali': 40, 'Mona': 35}
print(D1)#{'Ahmed': 50, 'Mostafa': 49, 'Ali': 40, 'Mona': 35}
D['Aymen']=42
D1=D.copy()
print(D)#{'Ahmed': 50, 'Mostafa': 49, 'Ali': 40, 'Mona': 35, 'Aymen': 42}
print(D1)#{'Ahmed': 50, 'Mostafa': 49, 'Ali': 40, 'Mona': 35, 'Aymen': 42}
D1=D.copy()
D['Khalad']=39
print(D)#{'Ahmed': 50, 'Mostafa': 49, 'Ali': 40, 'Mona': 35, 'Aymen': 42, 'Khalad': 39}
print(D1)#{'Ahmed': 50, 'Mostafa': 49, 'Ali': 40, 'Mona': 35, 'Aymen': 42}
L=['Alhousainy','Eslam','Mostafa','Ali','Ahmed']
#D2=dict(L)#Error
#print(D2)#
D2=dict.fromkeys(L)
print(D2)#{'Alhousainy': None, 'Eslam': None, 'Mostafa': None, 'Ali': None, 'Ahmed': None}
S={'A','B','C','D','E'}
# D3=dict(S)
# print(D3)#Error
D3=dict.fromkeys(sorted(S))
print(D3)#{'A': None, 'B': None, 'C': None, 'D': None, 'E': None}
D2['Alhousainy']=19
D2['Eslam']=18
D2['Mostafa']=20
D2['Ali']=15
D2['Ahmed']=17
print(D2)#{'Alhousainy': 19, 'Eslam': 18, 'Mostafa': 20, 'Ali': 15, 'Ahmed': 17}
D3['A']=10
D3['B']=11
D3['C']=12
D3['D']=13
D3['E']=14
print(D3)#{'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14}
grades={'A+':95,'A':90,'B+':85,'B':80,'C+':75,'C':70,'D':65,'E':55,'F':45}
print(grades)#{'A+': 95, 'A': 90, 'B+': 85, 'B': 80, 'C+': 75, 'C': 70, 'D': 65, 'E': 55, 'F': 45}
L_Key=list(grades.keys())
S_Key=set(grades.keys())
T_Key=tuple(grades.keys())
print(L_Key)#['A+', 'A', 'B+', 'B', 'C+', 'C', 'D', 'E', 'F']
print(sorted(S_Key))#['A', 'A+', 'B', 'B+', 'C', 'C+', 'D', 'E', 'F']
print(T_Key)#('A+', 'A', 'B+', 'B', 'C+', 'C', 'D', 'E', 'F')
L_Values=list(grades.values())
S_Values=set(grades.values())
T_Values=tuple(grades.values())
print(L_Values)#[95, 90, 85, 80, 75, 70, 65, 55, 45]
print(sorted(S_Values,reverse=True))#[95, 90, 85, 80, 75, 70, 65, 55, 45]
print(S_Values)#{65, 70, 75, 45, 80, 85, 55, 90, 95}
print(T_Values)#(95, 90, 85, 80, 75, 70, 65, 55, 45)
L_Items=list(grades.items())
S_Items=set(grades.items())
T_Items=tuple(grades.items())
print(L_Items)#[('A+', 95), ('A', 90), ('B+', 85), ('B', 80), ('C+', 75), ('C', 70), ('D', 65), ('E', 55), ('F', 45)]
print(S_Items)#{('B+', 85), ('F', 45), ('C+', 75), ('A', 90), ('B', 80), ('A+', 95), ('D', 65), ('E', 55), ('C', 70)}
print(T_Items)#(('A+', 95), ('A', 90), ('B+', 85), ('B', 80), ('C+', 75), ('C', 70), ('D', 65), ('E', 55), ('F', 45))
print(sorted(L_Items,key=lambda e:e[1]))
#[('A+', 95), ('A', 90), ('B+', 85), ('B', 80), ('C+', 75), ('C', 70), ('D', 65), ('E', 55), ('F', 45)]
print(sorted(S_Items,reverse=False,key=lambda e:e[1]))
#[('F', 45), ('E', 55), ('D', 65), ('C', 70), ('C+', 75), ('B', 80), ('B+', 85), ('A', 90), ('A+', 95)]
print(sorted(T_Items,reverse=True,key=lambda e:e[1]))
#[('A+', 95), ('A', 90), ('B+', 85), ('B', 80), ('C+', 75), ('C', 70), ('D', 65), ('E', 55), ('F', 45)]
print(sorted(S_Items,reverse=True,key=lambda e:e[1]))
#[('A+', 95), ('A', 90), ('B+', 85), ('B', 80), ('C+', 75), ('C', 70), ('D', 65), ('E', 55), ('F', 45)]
Students_Dict={'Alhousainy':(89,'26 Years Old','From Egypt'),'Ahmed':(70,'28 Years Old','From Libya'),
'Mona':(92,'22 Years Old','From Tunise'),'Marwa':(72,'18 Years Old','From KSA'),'Ali':(60,'30 Years Old','From Syria'),
'Esso':(95,'21 Years Old','From USA'),'George':(52,'35 Years Old','From France'),'Son':(75,'29 Years Old','From Korea'),
'Mostafa':(42,'26 Years Old','From Sudan'),'Zaki':(51,'40 Years Old','From Moroco')}
print(Students_Dict)#{'Alhousainy': (89, '26 Years Old', 'From Egypt'), 'Ahmed': (70, '28 Years Old', 'From Libya'),
# 'Mona': (92, '22 Years Old', 'From Tunise'), 'Marwa': (72, '18 Years Old', 'From KSA'),
# 'Ali': (60, '30 Years Old', 'From Syria'), 'Esso': (95, '21 Years Old', 'From USA'),
# 'George': (52, '35 Years Old', 'From France'), 'Son': (75, '29 Years Old', 'From Korea'),
# 'Mostafa': (42, '26 Years Old', 'From Sudan'), 'Zaki': (51, '40 Years Old', 'Moroco')}
print(Students_Dict.keys())
#dict_keys(['Alhousainy', 'Ahmed', 'Mona', 'Marwa', 'Ali', 'Esso', 'George', 'Son', 'Mostafa', 'Zaki'])
print(Students_Dict.values())#dict_values([(89, '26 Years Old', 'From Egypt'), (70, '28 Years Old', 'From Libya'),
# (92, '22 Years Old', 'From Tunise'), (72, '18 Years Old', 'From KSA'), (60, '30 Years Old', 'From Syria'), 
# (95, '21 Years Old', 'From USA'), (52, '35 Years Old', 'From France'), (75, '29 Years Old', 'From Korea'), 
# (42, '26 Years Old', 'From Sudan'), (51, '40 Years Old', 'Moroco')])
print(Students_Dict['Alhousainy'])#(89, '26 Years Old', 'From Egypt')
print(Students_Dict['Ahmed'])#(70, '28 Years Old', 'From Libya')
print(Students_Dict['George'])#(52, '35 Years Old', 'From France')
print(Students_Dict['Marwa'])#(72, '18 Years Old', 'From KSA')
print(Students_Dict['Alhousainy'][2])#From Egypt
print(Students_Dict['Ahmed'][2])#From Libya
print(Students_Dict['Esso'][2])#From USA
print(Students_Dict['Marwa'][2])#From KSA
print(Students_Dict['Zaki'][2])#From Moroco
del(Students_Dict['Ahmed'])
del(Students_Dict['Mona'])
del(Students_Dict['Marwa'])
del(Students_Dict['Mostafa'])
del(Students_Dict['Zaki'])
del(Students_Dict['George'])
print(Students_Dict)#{'Alhousainy': (89, '26 Years Old', 'From Egypt'), 'Ali': (60, '30 Years Old', 'From Syria'),
#'Esso': (95, '21 Years Old', 'From USA'), 'Son': (75, '29 Years Old', 'From Korea')}
D10={'A':7,5:'N','B':20.5}
print(D10)#{'A': 7, 5: 'N', 'B': 20.5}
