import math as m
from re import A
def star():
     for k in range(11):
        print('**')
print('='*60)
star()
#** ,**,**,**,**,**,**,**,**,**,**
print('='*30)
def odd_numbers():
    for k in range(1,11,2):
        print('The Odd Numbers Is ==> ',k)
odd_numbers()
'''The Odd Numbers Is ==>  1,The Odd Numbers Is ==>  3,The Odd Numbers Is ==>  5
The Odd Numbers Is ==>  7,The Odd Numbers Is ==>  9 '''
print('='*30)
#Odd Numbers
s=odd_numbers
s()
'''The Odd Numbers Is ==>  1 ,The Odd Numbers Is ==>  3,The Odd Numbers Is ==>  5,
The Odd Numbers Is ==>  7,The Odd Numbers Is ==>  9 '''
print('='*30)
def even_numbers():
    for j in range(0,11,2):
        print('The Even Number is ==> ',j)
even_numbers()
'''The Even Number is ==>  0,The Even Number is ==>  2,The Even Number is ==>  4
The Even Number is ==>  6,The Even Number is ==>  8,The Even Number is ==>  10 '''
print('='*30)
def find_avg(a,b):
    average = (a+b)/2
    print('The Average Is Equal ==> ',average)
find_avg(10,20)# ==> The Average Is Equal ==>  15.0
var1=int(input('Please Enter The Number ==> '))
var2=int(input('Please Enter The Number ==> '))
find_avg(var1,var2)
#Please Enter The Number==> 15,==>Please Enter The Number==>25,==>The Average Is Equal ==>  20.0
print('='*30)
def Check_Item(a):
    if a=='Alhousainy':print('The Name Is ==> ',a,'And Is a Machine Learning ENG')
    elif a=='Ahmed':print('The Name Is ==> ',a,' and is a doctor')
    else:print('The Name Is Error!')
text1=str(input('Please Enter The Name ==> '))
Check_Item(text1)#
print('='*30)
'''Please Enter The Name==>Alhousainy , ==>The Name Is==>Alhousainy And Is a Machine Learning ENG
Please Enter The Name ==> Ahmed ,==>The Name Is ==>  Ahmed  and is a doctor
Please Enter The Name ==> Ali ,==>The Name Is Error!'''
def find_avg1(*numbers):
    sum=0
    for i in numbers:
        sum+=i
    print('The Average Is ==> ',sum/(len(numbers)))
    print('The Numbers Is ==> ',numbers)
find_avg1(2,4)#The Average Is ==>  3.0 , ==>The Numbers Is ==>  (2, 4)
find_avg1(2,3,4)#The Average Is ==>  3.0 , ==>The Numbers Is ==>  (2, 3, 4)
find_avg1(1,2,3,4,5,6,7,8,9,10)
#The Average Is ==>  5.5,==>The Numbers Is ==>  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#find_avg1([i for i in range(1,20)]) ==> Error Call
#find_avg1([1,2,4,5,10,20,7,8,9,11,12])==>Error Call
print('='*30)
def avg_fo_two(a,b):
    print('The Average Is ==>',(a+b)/2)
var3=(10,20)
avg_fo_two(*var3)#The Average Is ==> 15.0
print('='*30)
def avg_of_three(a,b,c):
    print('The Average Is ==>',(a+b+c)/3)
var4=(10,20,40)
avg_of_three(*var4)#The Average Is ==> 23.333333333333332
print('='*30)
def test_var_args(f_arg,*argv):
    print('The First Normal Argument is ==> ',f_arg)
    for arg in argv:
        print('The Another Argument Is :  ',arg)
test_var_args('Alhousainy','Ahmed','Ali','Mostafa','Mona','Marwa','Lamiaa','Messi','Saleh','Mane')
'''
The First Normal Argument is ==>  Alhousainy
The Another Argument Is :   Ahmed
The Another Argument Is :   Ali
The Another Argument Is :   Mostafa
The Another Argument Is :   Mona
The Another Argument Is :   Marwa
The Another Argument Is :   Lamiaa
The Another Argument Is :   Messi
The Another Argument Is :   Saleh
The Another Argument Is :   Mane
'''
print('='*30)
def print_values(**values):
    print('The Values Is ==> ',values)
print_values(one='Ahmed',two='Esso',three='Mido',four=10.5,five=True,sex=0)
#The Values Is ==>  {'one': 'Ahmed', 'two': 'Esso', 'three': 'Mido', 'four': 10.5, 'five': True, 'sex': 0}
print('='*30)
def print_items(**values):
    for key,value in values.items():
        print(' The Item In Dict => {} = {} '.format(key,value))
print_items(one='Ahmed',two='Esso',three='Mido',four=10.5,five=True,sex=0)
'''
The Item In Dict => one = Ahmed
 The Item In Dict => two = Esso
 The Item In Dict => three = Mido
 The Item In Dict => four = 10.5
 The Item In Dict => five = True 
 The Item In Dict => sex = 0
'''
print('='*30)
def greet_name(**kwargs):
    if kwargs is not None:
        for key,value in kwargs.items():
            print('The Item Is > %s == %s' %(key,value))
greet_name(name='Alhousainy' ,Age ='26 Years Old' ,Postion = 'Machine Learning ENG')
'''
The Item Is > name == Alhousainy
The Item Is > Age == 26 Years Old
The Item Is > Postion == Machine Learning ENG
'''
print('='*30)
def avg_fo_two_part2(a,b):
    print('The Average Is ==>',(a+b)/2)
def avg_of_three_part2(a,b,c):
    print('The Average Is ==>',(a+b+c)/3)

var5={'a':10,'b':20}
var6={'a':10,'b':20,'c':30}
avg_fo_two_part2(**var5)#The Average Is ==> 15.0
avg_of_three_part2(**var6)#The Average Is ==> 20.0
print('='*30)
def show_details(var1,var2,*args,**kwargs):
    print('The Variable one is ==> ',var1)
    print('The Power Of 5 For Variable 1 ==> ',m.pow(var1,5))
    print('The Varibale Two is ==> ',var2)
    print('The sqrt of Var2 Is ==> ',m.sqrt(var2))
    print('The Factorial Of Var2 ==> ',m.factorial(var2))
    print('The Average Of Var1 and Var 2 is ==> ', (var1+var2)/2)
    print('The List Is ==> ',args)
    print('The Dictionary Is ==> ',kwargs)
show_details(1,2,3,4,5,6,7,8,9)
'''
The Variable one is ==>  1
The Power Of 5 For Variable 1 ==>  1.0
The Varibale Two is ==>  2
The sqrt of Var2 Is ==>  1.4142135623730951
The Average Of Var1 and Var 2 is ==>  1.5
The List Is ==>  (3, 4, 5, 6, 7, 8, 9)
The Dictionary Is ==>  {}
'''
print('='*30)
show_details(10,20,40,50,'Alhousainy','ahmed','esso' , name ='Mostafa',Age=26,Pos='Doctor',Married=True)
'''
The Variable one is ==>  10
The Power Of 5 For Variable 1 ==>  100000.0
The Varibale Two is ==>  20
The sqrt of Var2 Is ==>  4.47213595499958
The Factorial Of Var2 ==>  2432902008176640000
The Average Of Var1 and Var 2 is ==>  15.0
The List Is ==>  (40, 50, 'Alhousainy', 'ahmed', 'esso')      
The Dictionary Is ==>  {'name': 'Mostafa', 'Age': 26, 'Pos': 'Doctor', 'Married': True}
'''
def powers(m,n=5):
    print('The Power Of M is ==> ',(m**(n)))
print('='*60)
powers(5,3)#The Power Of M is ==>  125
powers(5)#The Power Of M is ==>  3125
print('='*30)
def powers2(m,n):
    print('The Power Of M is ==> ',(m**(n)))
powers2(m=3,n=4)#The Power Of M is ==>  81
powers2(3,4)#The Power Of M is ==>  81
powers2(n=3,m=4)#The Power Of M is ==>  64
powers2(3,4)#The Power Of M is ==>  81
print('='*30)
def parrot(voltage,state='a stiff',action='voom',type = 'Norwegain Blue'):
    print('....This Parrot Wouldn’t is ==> ',action)
    print('If You Put Voltage Is ==> ',voltage,',Volts Through It')
    print('.....Lovely Plumage , The Type Is ==> ',type)
    print('.....The State Is ==> ',state, '!')
parrot(1000)
'''
....This Parrot Wouldn’t is ==>  voom
If You Put Voltage Is ==>  1000 ,Volts Through It
.....Lovely Plumage , The Type Is ==>  Norwegain Blue
.....The State Is ==>  a stiff !
'''
print('='*30)
parrot(voltage=1000)
'''
....This Parrot Wouldn’t is ==>  voom
If You Put Voltage Is ==>  1000 ,Volts Through It
.....Lovely Plumage , The Type Is ==>  Norwegain Blue
.....The State Is ==>  a stiff !
'''
print('='*30)
parrot(voltage=1000000,action='VooooooM')
'''
....This Parrot Wouldn’t is ==>  VooooooM
If You Put Voltage Is ==>  1000000 ,Volts Through It
.....Lovely Plumage , The Type Is ==>  Norwegain Blue
.....The State Is ==>  a stiff !
'''
print('='*30)
print('######################## Parrot One ########################')
def parrot_one(voltage,state='a stiff',action='voom',type = 'Norwegain Blue'):
    print('....This Parrot Wouldn’t is ==> ',action)
    print('If You Put Voltage Is ==> ',voltage,',Volts Through It')
    print('.....Lovely Plumage , The Type Is ==> ',type)
    print('.....The State Is ==> ',state, '!')
parrot_one(action='VOOOOOM', voltage=1000000) # 2 keyword arguments
'''
....This Parrot Wouldn’t is ==>  VOOOOOM
If You Put Voltage Is ==>  1000000 ,Volts Through It
.....Lovely Plumage , The Type Is ==>  Norwegain Blue
.....The State Is ==>  a stiff !
'''
print('='*30)
parrot_one('a million', 'bereft of life', 'jump') # 3 positional arguments
'''
....This Parrot Wouldn’t is ==>  jump
If You Put Voltage Is ==>  a million ,Volts Through It        
.....Lovely Plumage , The Type Is ==>  Norwegain Blue
.....The State Is ==>  bereft of life !
'''
print('='*30)
parrot_one('a thousand', state='pushing up the daisies') # 1 positional, 1 keyword
'''
....This Parrot Wouldn’t is ==>  voom
If You Put Voltage Is ==>  a thousand ,Volts Through It       
.....Lovely Plumage , The Type Is ==>  Norwegain Blue
.....The State Is ==>  pushing up the daisies !
'''
print('='*30)
print('######################## Parrot Two ########################')
def parrot_two(voltage,state='a stiff',action='voom'):
    print('....This Parrot Wouldn’t is ==> ',action)
    print('If You Put Voltage Is ==> ',voltage,',Volts Through It')
    print('.....The State Is ==> ',state, '!')
Dict={'voltage':'Four Million ','state':'bleedin demised','action':'VooooM'}
parrot_two(**Dict)
'''
....This Parrot Wouldn’t is ==>  VooooM
If You Put Voltage Is ==>  Four Million  ,Volts Through It    
.....The State Is ==>  bleedin demised !
'''
print('='*30)
def Introduce(name , job , company , age=30, status='Married'):
    print('1-Your Name Is ==> ',name)
    print('2-Your Age Is ==> ',age , 'Years Old')
    print('3-Your Job Is ==> ',job)
    print('4-Your Status Is ==> ',status)
    print('5-And Your Company Is ==> ',company)
name=str(input('Please Enter Your Name ==> '))
job=str(input('Please Enter Your Job ==> '))
company=str(input('Please Enter Your Company It is Work ==> '))
Introduce(name,job,company)
'''
Please Enter Your Name ==> Alhousainy
Please Enter Your Job ==> Machine Learning Engineer
Please Enter Your Company It is Work ==> ISFP
1-Your Name Is ==>  Alhousainy
2-Your Age Is ==>  30 Years Old
3-Your Job Is ==>  Machine Learning Engineer
4-Your Status Is ==>  Married
5-And Your Company Is ==>  ISFP
'''
print('='*30)
Dict1={'name':name,'job':job,'company':company,'age':'25','status':'Single'}
Introduce(**Dict1)
'''
Please Enter Your Name ==> Alhousainy
Please Enter Your Job ==> Machine Learning Engineer
Please Enter Your Company It is Work ==> ISFP
1-Your Name Is ==>  Alhousainy
2-Your Age Is ==>  25 Years Old
3-Your Job Is ==>  Machine Learning Engineer
4-Your Status Is ==>  Single
5-And Your Company Is ==>  ISFP
'''
print('='*30)
def power_2(y,c):
    x=m.pow(y,c)
    return x
num1=int(input('Please Enter Number One ==> '))
num2=int(input('Please Enter Number Two ==> '))
print('The End Number Is Equal ==> ',power_2(num1,num2))
#Please Enter Number One ==> 4, Please Enter Number Two ==> 5 , The End Number Is Equal ==>  1024.0
print('='*30)
def power_3(x,y):
    var=m.pow(x,y)
    print('The X is =  ',x ,'Is Power Of y = ',y ,'Is ==> ',var)
    var1=m.factorial(x)
    print('The Factorial number ',x,' Is ==> ',var1)
    var2=m.factorial(y)
    print('The Factorial number ',y,' Is ==> ',var2)
    #var3=sum(var+var1+var2)
    #print('The Sum of ',var,'+',var1,'+',var2,'is = ',var3)
    return var
def Times4(w):
    var4=w*4
    return var4
def add7(zz):
    var5=zz+7
    return var5
num_one=int(input('Please Input The Number ==> '))
num_Two=int(input('Please Input The Number ==> '))
print('The Final Result Is ==> ' ,add7(Times4(power_3(num_one,num_Two))))
'''
Please Input The Number ==> 2
Please Input The Number ==> 5
The X is =   2 Is Power Of y =  5 Is ==>  32.0
The Factorial number  2  Is ==>  2
The Factorial number  5  Is ==>  120
The Final Result Is ==>  135.0
'''
print('='*30)
xx=5
def gg():
    xx=14
gg()
print(xx)#5
print('='*30)
yy=5
def zz():
    global yy
    yy=14
zz()
print(yy)#14
print('='*30)
var_Three=lambda num_one,num_Two:m.pow(num_one,num_Two)
print('The Var_Three Is ==> ',var_Three(num_one,num_Two)) #The Var_Three Is ==>  32.0
print('='*30)
L=[lambda x:1,lambda x:x,lambda x:m.pow(x,2),lambda x:m.pow(x,3),lambda x:m.factorial(x)]
print('The Number Is ==> ',L[0](5))#The Number Is ==>  1
print('The Number Is ==> ',L[1](5))#The Number Is ==>  5
print('The Number Is ==> ',L[2](5))#The Number Is ==>  25.0
print('The Number Is ==> ',L[3](5))#The Number Is ==>  125.0
print('='*30)
MyList=[i for i in range(21)]
even_numbers=list(filter(lambda x:x%2==0,MyList))
odd_numbers=list(filter(lambda y:y%2==1,MyList))
print('The Even Numbers is ==>',even_numbers)#The Even Numbers is==>[0,2,4,6,8,10,12,14,16,18,20]
print('The Odd Numbers Is ==>',odd_numbers)#The Odd Numbers Is==>[1,3,5, 7, 9, 11, 13, 15, 17, 19]   
print('='*30)
print('Square List Using Map+Lambda'.strip('#'))
print('Square List ==> ',list(map(lambda x:m.pow(x,2) ,MyList)))
#############Square List Using Map+Lambda#################
#Square List==>[0.0,1.0,4.0,9.0,16.0,25.0,36.0,49.0,64.0,81.0,100.0
#,121.0,144.0,169.0,196.0,225.0,256.0,289.0,324.0,361.0,400.0]
print('='*30)
L1=(1,2,3,4,5,6)
def cpower(x):
    return m.pow(x,3)
print(list(map(lambda x:cpower(x),L1)))#[1.0, 8.0, 27.0, 64.0, 125.0, 216.0]
print(list(filter(lambda x:cpower(x),L1)))#[1, 2, 3, 4, 5, 6]
print('='*30)
def yie():
    for i in range(11):
        yield i
for g in yie():
    print('The Number Is ==> ',g)
'''
The Number Is ==>  0
The Number Is ==>  1
The Number Is ==>  2
The Number Is ==>  3
The Number Is ==>  4
The Number Is ==>  5
The Number Is ==>  6
The Number Is ==>  7
The Number Is ==>  8
The Number Is ==>  9
The Number Is ==>  10
'''
print('='*30)
'''f= yie()
print(next('The Number Is ==> ',f))#The Number Is ==>  0
print(next('The Number Is ==> ',f))#The Number Is ==>  1
print(next('The Number Is ==> ',f))#The Number Is ==>  2
print(next('The Number Is ==> ',f))#The Number Is ==>  3
print('='*30)'''
def fibon(n):
    a=b=1
    result=[]
    for i in range(n):
        result.append(a)
        a,b=b,a+b
    return result

num10=int(input('Please Enter The Fibon Number : '))#Please Enter The Fibon Number : 15
print('The List Is ==>',fibon(num10))
#The List Is ==> [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
print('='*30)
def fibon_one(n):
    a=b=1
    for i in range(n):
        yield a
        a,b=b,a+b
for x in fibon_one(num10):
    print('The Number Is ==> ',x)
'''
The Number Is ==>  1
The Number Is ==>  1
The Number Is ==>  2
The Number Is ==>  3
The Number Is ==>  5
The Number Is ==>  8
The Number Is ==>  13
The Number Is ==>  21
The Number Is ==>  34
The Number Is ==>  55
The Number Is ==>  89
The Number Is ==>  144
The Number Is ==>  233
The Number Is ==>  377
The Number Is ==>  610
'''
print('='*30)
def fac(n):
    if n ==1:
        return 1
    else:
        return n *fac(n-1)

num11=int(input('Please Enter The Factorial Number ==> '))#Please Enter The Factorial Number ==> 10
print('The Factorial Number ',num11,' Is ==> ',fac(num11))#The Factorial Number  10  Is ==>  3628800