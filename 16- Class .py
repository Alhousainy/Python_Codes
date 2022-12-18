from struct import calcsize
print('='*30)
class summary:
    name ='Alhousainy'
    Age= 26
    Job ='Machine Learning Engineer'
    Company = 'ISFP'
print('My Name Is ==> ',summary.name)#My Name Is ==>  Alhousainy
print('My Age Is => ',summary.Age , 'Years Old ')#My Age Is =>  26 Years Old 
print('Iam a ', summary.Job)#Iam a  Machine Learning Engineer
print('Iam Work at  ',summary.Company)#Iam Work at   ISFP
print('='*30)
var=summary
print('My Name Is ==> ',var.name)#My Name Is ==>  Alhousainy
print('My Age Is => ',var.Age , 'Years Old ')#My Age Is =>  26 Years Old 
print('Iam a ', var.Job)#Iam a  Machine Learning Engineer
print('Iam Work at  ',var.Company)#Iam Work at   ISFP
print('='*30)
class introduce:
    name = 'Alhousainy'
    age=26
    Job='Dentist'
    hospital='6 Octobre'
    country='Egypt'
var1=introduce
var2=introduce
var1.name='Mostafa'
var2.name='Ahmed'
print('Your Name Is => ',introduce.name)#Your Name Is =>  Ahmed
print('Your Name Is => ',var1.name)#Your Name Is =>  Ahmed
print('Your Name Is => ',var2.name)#Your Name Is =>  Ahmed
print('='*30)
class car():
    def __init__(self,color):
        self.color=color
volvo=car('White')
nissan=car('Green')
print('The Color Of Volvo Car Is => ',volvo.color)#The Color Of Volvo Car Is =>  White
print('The Color Of Nissan Car Is => ',nissan.color)#The Color Of Nissan Car Is =>  Green
print('='*30)
class summary_one():
    def __init__(self,name,age,job,company,city,status):
        self.name=name
        self.age=age
        self.job=job
        self.company=company
        self.city=city
        self.status=status
var3=summary_one('Alhousainy',26,'Machine Learning Engineer','ISFP Company','Egypt','Single')
var4=summary_one('Ahmed',35,'Dentist','Apple','KSA','Married')
print('Your Name Is => ',var3.name)#Your Name Is =>  Alhousainy
print('Your Age Is => ',var3.age ,'Years Old')#Your Age Is =>  26 Years Old
print('Your Job Is => ',var3.job)#Your Job Is =>  Machine Learning Engineer
print('Your Company Is => ',var3.company)#Your Company Is =>  ISFP Company
print('Your Status Is => ',var3.status)#Your Status Is =>  Single
print('='*15)
print('Your Name Is => ',var4.name)#Your Name Is =>  Ahmed
print('Your Age Is => ',var4.age ,'Years Old')#Your Age Is =>  35 Years Old
print('Your Job Is => ',var4.job)#Your Job Is =>  Dentist
print('Your Company Is => ',var4.company)#Your Company Is =>  Apple
print('Your Status Is => ',var4.status)#Your Status Is =>  Married
print('='*30)
class defintion():
    def __init__(self,name='Alhousainy',age='26 Years Old',job ='ML ENG',company='ISFP'):
        self.n=name
        self.AGE=age
        self.J=job
        self.C=company
var5=defintion()
var6=defintion('Esso','15 Years Old','Developer','Apple')
print('Your Name Is => ',var5.n)#Your Name Is =>  Alhousainy
print('Your Age Is => ',var5.AGE)#Your Age Is =>  26 Years Old
print('Your Job Is => ', var5.J)#Your Job Is =>  ML ENG
print('Your Company Is => ' ,var5.C)#Your Company Is =>  ISFP
print('='*15)
print('Your Name Is => ' ,var6.n)#Your Name Is =>  Esso
print('Your Age Is => ' ,var6.AGE)#Your Age Is =>  15 Years Old
print('Your Job Is => ' ,var6.J)#Your Job Is =>  Developer
print('Your Company Is => ',var6.C)#Your Company Is =>  Apple
print('='*30)
class d:
    def __init__(self,nn,p2=10,p3=100):
        self.power2=p2**2
        self.power3=p3**3
        self.roots=nn
    def root(self):
        print('The Self Roots Is ==> ',self.roots**0.5)
a=d(2500)
a.root()
#The Self Roots Is ==>  50.0
print('='*30)
class gg:
    def __init__(self,NAME,T='Car',model='BMW',production='2020'):
        self.Type=T
        self.M=model
        self.P=production
        self.roots=NAME
    def kk(self):
        print('Your Name Is ==> ',self.roots)#Your Name Is ==>  Alhousainy
        print('Your Type Is ==> ',self.Type)#Your Type Is ==>  Car
        print('Your Model Is => ',self.M)#Your Model Is =>  BMW
        print('Your Prodution Is => ',self.P)#Your Prodution Is =>  2020
S=str(input('Please Enter Your Name => '))#Please Enter Your Name => Alhousainy
var7=gg(S)
var7.kk()
print('='*30)
class Suumary_Two():
    def __init__(self,name,age,job,Company='Microsoft',Country='Egypt'):
        self.N1=Company
        self.N2=Country
        self.N3=name
        self.N4=age
        self.N5=job
    def Details(self):
        print('Your Name Is => ',self.N3)
        print('Your Age Is => ',self.N4)
        print('Your Job Is => ',self.N5)
        print('Your Company Is => ',self.N1)
        print('Your Country Is => ',self.N2)
        print('='*30)
S1=str(input('Please Enter Your Name : '))
S2=str(input('Please Enter Your Age : '))
S3=str(input('Please Enter Your Job : '))
S4=str(input('Please Enter Your Company : '))
S5=str(input('Please Enter Your Country : '))
print('='*15)
'''
Please Enter Your Name : Alhosuainy 
Please Enter Your Age : 26 Years Old
Please Enter Your Job : Machine Learning Engineer
Please Enter Your Company : ISFP
Please Enter Your Country : Egypt
'''
var8=Suumary_Two(S1,S2,S3,S4,S5)
var8.Details()
'''
Your Name Is =>  Alhosuainy
Your Age Is =>  26 Years Old
Your Job Is =>  Machine Learning Engineer
Your Company Is =>  ISFP
Your Country Is =>  Egypt
'''
var9=Suumary_Two(S1,S2,S3)
var9.Details()
'''
Your Name Is =>  Alhosuainy
Your Age Is =>  26 Years Old
Your Job Is =>  Machine Learning Engineer
Your Company Is =>  Microsoft
Your Country Is =>  Egypt
'''
class Calc:
    def Square(num):
        print('The Square Number ',num,' Is => ',num**2)
    def summ(a,b,c,d,e,f):
        return((a+b-c+e)*(d+f))
a=Calc
num1=int(input('Please Enter The Number : '))
a.Square(num1)#The Square Number  5  Is =>  25
print(a.summ(1,2,3,4,5,7))#55
print('='*30)
class Account:
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
            self.balance -= amount
    def show(self):
        s = '%s, %s, balance: %s' % (self.name, self.no, self.balance)
        print (s)
a1 = Account('John Olsson', '19371554951', 20000)
a2 = Account('Liz Olsson', '19371564761', 50000)
print("a1 balance : " , a1.balance )
print("a2 no : " , a2.no)
a1.deposit(1000)
a1.withdraw(4000)
a2.withdraw(10500)
a1.withdraw(3500)
print ("a1's balance:", a1.balance)
print ("a2's balance:", a2.balance)
a1.show()
a2.show()
print('='*30)
'''
a1 balance :  20000
a2 no :  19371564761
a1's balance: 13500
a2's balance: 39500
John Olsson, 19371554951, balance: 13500
Liz Olsson, 19371564761, balance: 39500
'''
class Person:
    def __init__(self, name,mobile_phone=None,office_phone=None,private_phone=None, email=None):
        self.name = name
        self.mobile = mobile_phone
        self.office = office_phone
        self.private = private_phone
        self.email = email
    def add_mobile_phone(self, number):
        self.mobile = number
    def add_office_phone(self, number):
       self.office = number
    def add_private_phone(self, number):
       self.private = number
    def add_email(self, address):
       self.email = address
    def dump(self):
        s = self.name + '\n'
        if self.mobile is not None:
            s += 'mobile phone: %s\n' % self.mobile
        if self.office is not None:
            s += 'office phone: %s\n' % self.office
        if self.private is not None:
            s += 'private phone: %s\n' % self.private
        if self.email is not None:
            s += 'email address: %s\n' % self.email
            print (s)
p1 = Person('Hans Hanson',office_phone='767828283', email='h@hanshanson.com')
p2 = Person('Ole Olsen', office_phone='767828292')
p2.add_email('olsen@somemail.net')
phone_book = [p1, p2]
for person in phone_book:
    person.dump()
print('='*30)
'''
Hans Hanson
office phone: 767828283
email address: h@hanshanson.com

Ole Olsen
office phone: 767828292
email address: olsen@somemail.net
'''