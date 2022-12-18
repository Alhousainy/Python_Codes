# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 15:33:33 2022

@author: ENG-Alhousainy
"""

print("="*60)
import math 
a= math.factorial(6)
print(a)#print ==> 720
#=========================================================
print("="*60)
import math as m
a= m.factorial(6)
print(a)#print ==> 720
#=========================================================
print("="*60)
from math import factorial
a= factorial(6)
print(a)#print ==> 720
#=========================================================
print("="*60)
from math import *
a=factorial(6) 
d= sin(10)
f=tan(15)
e= pow(2,3)
print(a)#print ==> 720
print(d)#print ==> -0.5440211108893698
print(f)#print ==> -0.8559934009085188
print(e)#print ==> 8.0
#=========================================================
print("="*60)
from math import factorial
a= factorial(6)
print(a)#print ==> 720
#############################################################
print("="*60)
import math as m
a= m.factorial(6)
print(a)#print ==> 720
print(m.exp(7))#print ==> 1096.6331584284585
print(m.log(10))#print ==> 2.302585092994046
print(m.log(7,49))#print ==> 0.5
print(m.log10(10000))#print ==> 4.0
print(m.sqrt(81))#print ==> 9.0
print(m.radians(30))#print ==> 0.5235987755982988
print(m.degrees(0.3490658))#print ==>19.99999711235769 == 20 تقريباً
print(m.sin(30))#print ==> -0.9880316240928618 ==> وده ناتج غلط لان الناتج بتاعها المفروض  يساوي نص 
print(m.sin(m.radians(30)))#print ==> 0.49999999999999994 ==> اللي هو تقريباً يساوي .5
print(m.copysign(7, 3))#Print ==> 7.0
print(m.copysign(7,- 3))#Print ==> -7.0
print(m.copysign(-7,3))#Print ==> 7.0
print(m.copysign(-7,- 3))#Print ==> -7.0
print(m.ceil(5.1))#Print ==> 6
print(m.ceil(5.777))#Print ==> 6
print(m.ceil(5.015))#Print ==> 6
print(m.floor(5.1))#Print ==> 5
print(m.floor(5.777))#Print ==> 5
print(m.floor(5.015))#Print ==> 5
print(m.asin(m.radians(0.5)))#print ==> 

























