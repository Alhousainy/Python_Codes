# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 16:07:33 2022

@author: ENG-Alhousainy
"""

print('='*60)
T=('Satrday','Sunday','Monday','Tuesday','Wendesday','Thursday','Friday')
T1=(1,2,3,4,5,'Alhousainy',10.5,80+7j,True,False)
print(T1)#==>(1, 2, 3, 4, 5, 'Alhousainy', 10.5, (80+7j), True, False)
print(T[6])#==>Friday
L=['A','B','C','D',1,2,3,4,5,True,False]
T2=('A','B','C','D',1,2,3,4,5,True,False)
TUPLE =tuple(L)
LIST = list(T2)
print(LIST)#==>['A', 'B', 'C', 'D', 1, 2, 3, 4, 5, True, False]
print(TUPLE)#==>('A', 'B', 'C', 'D', 1, 2, 3, 4, 5, True, False)
x=1,2,3,4,5,6,'Alhousainy',True,False
print(x)#==>(1, 2, 3, 4, 5, 6, 'Alhousainy', True, False)
print(list(x))#==>[1, 2, 3, 4, 5, 6, 'Alhousainy', True, False]
Student = [('Ahmed','Egypt',25),('Zaki','Yeman',28),('Mona','Syria',18),('Samah','Libya',44),('Fatma','Jordan',10)]
new_student=sorted(Student,key=lambda s:s[2])
print(new_student)#==>[('Fatma','Jordan',10),('Mona','Syria',18),('Ahmed','Egypt',25),('Zaki','Yeman',28),('Samah','Libya',44)]




