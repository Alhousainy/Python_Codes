print('='*60)
import random as rn
Var=rn.random()
print('The Number Is ==> ',Var)#The Number Is ==>  0.9091261514443906
var2=rn.randint(1,20)
print('The Random Number Is equal ==> ',var2)#The Random Number Is equal ==>  20
#The Random Number Is equal ==>  18
#The Random Number Is equal ==>  4
#var3=rn.randint(20,8)
#print('The Random Number Is equal ==> ',var3)#Error Method
var4=rn.randint(-10,0)
print('The Random Number Is equal ==> ',var4)
#The Random Number Is equal ==>  0
#The Random Number Is equal ==>  -7
#The Random Number Is equal ==>  -8
var5=rn.uniform(1,20)
print('The Random Number Is Equal ==> ',var5)
#The Random Number Is Equal ==>  6.412245010448216
#The Random Number Is Equal ==>  6.474355450115203
#The Random Number Is Equal ==>  16.30688471458265
var6=rn.randrange(15)
var7=rn.randrange(10)
print('The Random Number Is Equal ==> ',var6)
#The Random Number Is Equal ==>  9
#The Random Number Is Equal ==>  10
#The Random Number Is Equal ==>  6
print('The Random Number Is Equal ==> ',var7)
print('='*20)
#The Random Number Is Equal ==>  6
#The Random Number Is Equal ==>  8
#The Random Number Is Equal ==>  7
var8=rn.randrange(0,50,3)
print(var8)#24 , #48 , #12 ,#21
print('='*20)
L=['Ahmed','Alhousainy','Ali','Mostafa','Zeyad','Zidan','Esso','Messi','Doku','Owen']
T=('Ahmed','Alhousainy','Ali','Mostafa','Zeyad','Zidan','Esso','Messi','Doku','Owen')
S={'Ahmed','Alhousainy','Ali','Mostafa','Zeyad','Zidan','Esso','Messi','Doku','Owen'}
print(rn.choice(L))#Zidan
#Alhousainy
#Ahmed
print(rn.choice(T))#Ali
#Zidan
#Esso
#Dict={'Ahmed':10,'Alhousainy':20,'Ali':30,'Mostafa':40,'Zeyad':60,'Zidan':70,'Esso':90}
#D=rn.choice(Dict.items())
#print('The Item is equal ==> ',D)#
print('='*20)
S='My Name Is Alhousainy'
y=rn.choice(S)
print("The Character Is ==> ",y)#The Character Is ==>  y
#The Character Is ==>  l
#The Character Is ==>  A
print('='*30)
w=rn.sample(range(20),10)
print('The Numbers Is ==> ',w)#The Numbers Is ==>  [13, 15, 18, 14, 9, 4, 10, 3, 0, 7]
#The Numbers Is ==>  [19, 4, 2, 8, 14, 18, 6, 1, 10, 13]
#The Numbers Is ==>  [4, 6, 15, 14, 2, 17, 11, 7, 9, 8]
#R=rn.sample(range(20),10)
'''for k in R:
     b[k]=R[k]+rn.random()
     print('The Random List ==> ',b)
'''
L=['Ahmed','Alhousainy','Ali','Mostafa','Zeyad','Zidan','Esso','Messi','Doku','Owen']
T=('Ahmed','Alhousainy','Ali','Mostafa','Zeyad','Zidan','Esso','Messi','Doku','Owen')
S={'Ahmed','Alhousainy','Ali','Mostafa','Zeyad','Zidan','Esso','Messi','Doku','Owen'}
rn.shuffle(L)
#rn.shuffle(T)
#rn.shuffle(S)
print('The Items Is ==> ',L)
#The Items Is ==>  ['Ali', 'Esso', 'Doku', 'Owen', 'Mostafa', 'Alhousainy', 'Zeyad', 'Messi', 'Ahmed', 'Zidan']
#print('The Items Is ==> ',T)#
#print('The Items Is ==> ',S)#
