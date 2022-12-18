# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 21:34:27 2022

@author: ENG-Alhousainy
"""

print('='*60)
L=[1,2,3,6,7,9,2,2,3,4,1,5,8,9,9,8,7,6,1,1]
S1={1,2,3,6,7,9,2,2,3,4,1,5,8,9,9,8,7,6,1,1}
print(S1)#==>{1, 2, 3, 4, 5, 6, 7, 8, 9}
S2={'a','b','x','v','c','g','d','n','y','e','f','h','m','o','w','a','a','b','d','f','f','c','c','x','x','r','g','v','e'}
print(S2)#==>{'x', 'o', 'b', 'a', 'v', 'd', 'h', 'm', 'c', 'y', 'e', 'n', 'f', 'r', 'g', 'w'}
S3={n**2 for n in range(12)}
print(S3)#==>{0, 1, 64, 121, 4, 36, 100, 9, 16, 49, 81, 25}
S4={m for m in range(15)}
print(S4)#==>{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
import math as m
S5={m.pow(x,4) for x in range(11) }
print(S5)#==>{0.0, 1.0, 256.0, 2401.0, 4096.0, 6561.0, 16.0, 81.0, 625.0, 1296.0, 10000.0}
S6={m.factorial(x) for x in range(6)}
print(S6)#==>{1, 2, 6, 24, 120}
S7 = {x*m.pi for x in range (6)}
print(S7)#==>{0.0, 3.141592653589793, 6.283185307179586, 9.42477796076938, 12.566370614359172, 15.707963267948966}
S8={0,1,2,3,4,5}
S9 ={0,1,2,3,4,5,6,7,8,9,10}
print(S8 or S9)#==>{0, 1, 2, 3, 4, 5}
print(S8 and S9)#==>{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
c1={'Egypt','KSA','USA','Argentina','Russia'}
c2={'France','KSA','Brazil','Panama','Japan','Jordan','Sudan','South Korea','Chile','Egypt','Lebanon'}
#Types Uninion ==> 1-    c1|c2    ,    2-   c1.unoin(c2)  , 3-    c2.union(c1)
print(c1.union(c2))#{'Chile', 'Sudan', 'Lebanon', 'Panama', 'Russia', 'KSA', 'USA',
#'Brazil', 'Argentina', 'South Korea', 'Japan', 'Egypt', 'France', 'Jordan'}
#print(c1 | c2)
#print(c2.union(c1))
print(c1.intersection(c2))#{'KSA', 'Egypt'}
print(c2.intersection(c1))#{'KSA', 'Egypt'}
print(c1&c2)#{'KSA', 'Egypt'}
#Symmetric deifference
print(c1.symmetric_difference(c2))
print(c2.symmetric_difference(c1))
print(c1^c2)
#{'Chile', 'South Korea', 'Lebanon', 'Sudan', 'Argentina', 'Panama', 'Russia', 'Japan', 'USA', 'France', 'Brazil', 'Jordan'}
print(c1-c2)#==>{'USA', 'Russia', 'Argentina'}
print(c1.difference(c2))#==>{'USA', 'Russia', 'Argentina'}

