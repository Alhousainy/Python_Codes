print('='*30)
import numpy as np
poly=np.polynomial.Polynomial
m1=np.array([0,20,40,60,80,100,120,140,160,180])
m1_1=np.array([10,9,8,7,6,5,4,3,2,1])
points,stats=poly.fit(m1,m1_1,1,full=True)
print('The Points Is => ',points)#The Points Is =>  5.5 - 4.5 x**1
print('The Stats Is => ',stats)
#The Stats Is =>  [array([5.62063395e-30]), 2, array([1., 1.]), 2.220446049250313e-15]
points_1,stats_1=poly.fit(m1,m1_1,2,full=True)
print('The Points Is => ',points_1)
#The Points Is =>  5.5  -4.5 x**1  -2.069 x**2
points_2,stats_2=poly.fit(m1,m1_1,3,full=True)
print('The Points_2 Is =>  ',points_2)
#The Points_2 Is => 5.5   -4.5 x**1  -2.0693761958189623e-15x**2  -3.117247812237589e-16 x**3
m1_2=np.poly1d((-7))
m1_3=np.poly1d((-7,2))
m1_4=np.poly1d((-7,8,5))
m1_5=np.poly1d((-7,8,5,4))
print('The Poly Equation M1_2 Is => ',m1_2)
#The Poly Equation M1_2 Is => -7
print('The Poly Equation M1_3 Is => ',m1_3)
#The Poly Equation M1_3 Is => -7 x + 2
print('The Poly Equation M1_4 Is => ',m1_4)
#The Poly Equation M1_4 Is => 2  -7x + 8x +5
print('The Poly Equation M1_5 Is => ',m1_5)
#The Poly Equation M1_5 Is => 3 2  -7x + 8x +5x + 4
print('='*30)
m1_6=m1_5(5)
print('The Result After Is value of x is = 5 => ',m1_6)
#The Result After Is value of x is = 5 =>  -646
m1_7=m1_5(-3)
print('The Result of polynomial EQUATION after is x= -3 => ',m1_7)
#The Result of polynomial EQUATION after is x= -3 =>  250       
print('='*30)
print('The polynomial Value From Equation Is => ',np.polyval((1,2),2))
#The polynomial Value From Equation Is =>  4
print('The polynomial Value From Equation Is => ',np.polyval((1,2,3,4),7))
#The polynomial Value From Equation Is =>  466
print('The polynomial Value From Equation Is => ',np.polyval((1,2,3,5),-3))
#The polynomial Value From Equation Is =>  -13
print('The polynomial Value From Equation Is => ',np.polyval((1,2,3,5,-6),12.6))
#The polynomial Value From Equation Is =>  29738.769599999992   
print('='*30)
x1=np.polyder(np.poly1d((1,2,4)))
x2=np.polyder(np.poly1d((2,3,4)),2)
x3=np.polyder(np.poly1d((2,3,4)),3)
print('The Derviative one for equation x1 is => ',x1)
#The Derviative one for equation x1 is => 2 x + 2
print('The Derviative two for equation x2 is => ',x2)
#The Derviative two for equation x2 is => 4
print('The Derviative three for equation x3 is => ',x3)
#The Derviative three for equation x3 is => 0
x4=np.polyder(np.poly1d((2,3,5,12,7)))
x5=np.polyder(np.poly1d((2,3,5,12,7)),2)
x6=np.polyder(np.poly1d((2,3,5,12,7)),3)
print('The Dervative One For Equation X4 Is => ',x4)
#The Dervative One For Equation X4 Is =>   3   2 
#                                         8x +9x + 10 x + 12
print('The Dervative Two For Equation X5 Is => ',x5)
#The Dervative Two For Equation X5 Is =>      2  24 x + 18 x + 10
print('The Dervative Three For Equation X6 Is => ',x6)
#The Dervative Three For Equation X6 Is => 48 x + 18
print('='*30)
print('The Result Of Equation X1 After Is x =2 => ',x1(2))
#The Result Of Equation X1 After Is x =2 =>  6
print('The Result Of Equation X2 After Is x =2 => ',x2(2))
#The Result Of Equation X2 After Is x =2 =>  4
print('The Result Of Equation X3 After Is x =0 => ',x3(0))
#The Result Of Equation X3 After Is x =0 =>  0
print('The Result Of Equation X4 After Is x =3 => ',x4(3))
#The Result Of Equation X4 After Is x =3 =>  339
print('The Result Of Equation X5 After Is x =-1 => ',x5(-1))
#The Result Of Equation X5 After Is x =-1 =>  16
print('The Result Of Equation X6 After Is x =5 => ',x6(5))
#The Result Of Equation X6 After Is x =5 =>  258
print('='*30)
y1=np.polyint(np.poly1d((1,2,3,4)))
y2=np.polyint(np.poly1d((1,2,3,4)),2)
y3=np.polyint(np.poly1d((1,2,3,4,6)),3)
print('The Integration For Y1 Once => ',y1)
#The Integration For Y1 Once =>        4          3       2     
#                                 0.25 x + 0.6667 x + 1.5 x + 4 x
print('The Integration For Y2 Twice => ',y2)
#The Integration For Y2 Twice =>        5          4       3     2
#                                  0.05 x + 0.1667 x + 0.5 x + 2 x
print('The Integration For Y3 Third => ',y3)
#The Integration For Y3 Third =>            7           6        5          4     3
#                                  0.004762 x + 0.01667 x + 0.05 x + 0.1667 x + 1 x
print('='*30)
print('The Result Of Equation AFter y=2 is => ',y1(2))
#The Result Of Equation AFter y=2 is =>  23.333333333333332     
print('The Result Of Equation AFter y=3 is => ',y2(3))
#The Result Of Equation AFter y=3 is =>  57.14999999999999      
print('The Result Of Equation AFter y=5 is => ',y3(5))
#The Result Of Equation AFter y=5 is =>  1017.8571428571428     
print('='*30)
y4=np.roots(np.poly1d((1,2)))
y5=np.roots(np.poly1d((1,2,3)))
y6=np.roots(np.poly1d((1,2,4,5)))
print('the roots for first degree =>',y4)
#the roots for first degree => [-2.]
print('the roots for second degree =>',y5)
#the roots for second degree => [-1.+1.41421356j -1.-1.41421356j]
print('the roots for third degree =>',y6)
#the roots for third degree => [-1.52595748+0.j -0.23702126+1.79456184j -0.23702126-1.79456184j]
print('='*30)
m2=np.array([3,6,2,5,4])
m3=np.array([2,3,-9,6,2.5])
m4=np.polyfit(m2,m3,2)
m5=np.polyfit(m2,m3,3)
print('The Polyfit Square Is => ',m4)
#The Polyfit Square Is =>  [ -1.78571429  17.08571429 -35.3       ]
print('The Polyfit Cube Is => ',m5)
#The Polyfit Cube Is =>  [  0.33333333  -5.78571429  31.95238095 -52.1       ]
print('='*30)
