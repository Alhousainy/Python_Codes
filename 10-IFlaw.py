# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 21:46:24 2022

@author: ENG-Alhousainy
"""

print('='*60)
x=7
if x==5:
    print(x)#
    print(3*x)#
print(5*x)#35
name = 'Alhousainy'
if name == 'Ahmed':
    print('Name Is Error')
elif name == 'Alhousainy' :
    print('Name Is Correct')
else : print('Error!')
y=5
if y == 5:
    print(y)#5
    print(y*3)#15
print(y*5)#25
#else : print(5*y)#
z=15
if z > 10:print('Z Is Greater Than 10')#Z Is Greater Than 10
else :print('Z is Lower Than 10')
y =18
# if y< range(6):print('The Student Is Fail')
# elif y> range(6) and y<range(11):print('The Student Is Good')
# elif y> range(11) and y<range(15):print('The Student Is Very Good')
# else :print('The Student Is Excellent')
if y<5 :print('The Student Is Fail')
elif y > 7:print('The Student Is Good')
elif y> 10 :print('The Student Is Very Good')
else : print('The Student Is Excellent')
print('The New Operation')
y=22
if (y>0) and (y<5) :print('The Student Is Fail')
elif (y>5) and (y<10) :print('The Student Is Good')
elif (y>15) and (y<20) :print('The Student Is Very Good')
elif (y>20) and (y<=25):print('The Student Is Excellent')
else :print('Other Thing')
#The Student Is Excellent
if (y>0) & (y<5) :print('The Student Is Fail')
elif (y>5) & (y<10) :print('The Student Is Good')
elif (y>15) & (y<20) :print('The Student Is Very Good')
elif (y>20) & (y<=25):print('The Student Is Excellent')
else :print('Other Thing')
#The Student Is Excellent
x = 10 
if (x>0) & (y<5) :print('The Student Is Fail')
elif (x>5) & (y<10) :print('The Student Is Good')
elif (x>15) & (y<20) :print('The Student Is Very Good')
elif (x>20) & (y<=25):print('The Student Is Excellent')
else :print('Other Thing')
x = 10 
y=20
if (x>0) | (y<5) :print('The Student Is Fail')
elif (x>5) | (y<10) :print('The Student Is Good')
elif (x>15) | (y<20) :print('The Student Is Very Good')
elif (x>20) | (y<=25):print('The Student Is Excellent')
else :print('Other Thing')
maximum = x if(x>y) else y
print(maximum)#20
x,y = 15,8
m1 =x if (x>y) else y
print(m1)#15

