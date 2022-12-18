# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 18:40:18 2022

@author: ENG-Alhousainy
"""

print("="*60)
name = "Alhousainy Abdelrahman Ali-Elden Abdelrahman"
name2= 'Eslam Abdelrahman Ali-Elden Abdelrahman'
#print(name,'\n',name2)
print(name)
print(name2)
ind1 = name[8]
ind2 = name2[10]
print(ind1 ," , and , " , ind2)
a = "how are you"
print(a[0:2])#print ==> ho 
#if you print how 
print(a[0:3])#print ==> how
print(a[4:7])#print ==> are
print(a[:11])#print ==>  how are you
print(a[4:])#print ==> are you
print(a[:])#print ==> how are you
print(a[4:11:2])#print ==> aeyu
print(a[0:11:3])#print ==> h eo
print(a[:7:3])#print ==> h e
print(a[8::4])#print ==> y
print(a[::2])#print ==> hwaeyu
print(a[-1:4:-1])#print ==> uoy er
print(a[::-1])#print ==> uoy era woh
print(list(a))#print ==> ['h', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u']
print(sorted(list(a)))#print ==> [' ', ' ', 'a', 'e', 'h', 'o', 'o', 'r', 'u', 'w', 'y']
print(set(a))#print ==> {'a', 'r', 'w', 'y', 'u', 'e', 'o', ' ', 'h'} 
b= "Hello World and Machine Learning Group and "
print(b.split())#print ==> ['Hello', 'World', 'and', 'Machine', 'Learning', 'Group', 'and']
summ = "I Alhousainy & I am work at ISFP company & Studying Machine Learning "
print(summ.split("&"))
print(a.splitlines())#print ==> ['how are you']
#==========================================================================================
print("="*60)
stat = "Hello My Team & My Name is Alhousainy & I am Very happy to work with them & I 26 years Old & I Machine Learning Eng"
print(set(stat))#print ==> {'o', 'e', 'm', 'A', '2', 'O', 't', ',', 'L', 'y', 'N', 'H', 'V', 'p', 'g', 'E', 'c', 'r', 'M', 'h', 'a', 'l', 's', '#', '&', 'k', 'w', '6', 'd', 'u', 'T', 'i', 'n', 'I', ' '}
print(stat.split())
#print ==>['Hello', 'My', 'Team', '&', 'My', 'Name', 'is', 'Alhousainy', '&', 'I', 'am', 'Very', 'happy', 'to', 'work', 'with', 'them', ',', 'I', '26', 'years', 'Old', '#', 'I', 'Machine', 'Learning', 'Eng']
print(stat.split("&"))
#print ==> ['Hello My Team ', ' My Name is Alhousainy ', ' I am Very happy to work with them , I 26 years Old # I Machine Learning Eng']
print(stat.split("&"))
#print ==>['Hello My Team ', ' My Name is Alhousainy ', ' I am Very happy to work with them ', ' I 26 years Old ', ' I Machine Learning Eng']
print(stat.splitlines(3)) 
#print ==> ['Hello My Team & My Name is Alhousainy & I am Very happy to work with them & I 26 years Old & I Machine Learning Eng']
#==========================================================================================================================
print("="*60)
a='23549499898912232659484812121551251549994'
print(a.split('1'))#print ==> ['235494998989', '22326594848', '2', '2', '55', '25', '549994']
print(a.partition('1'))#print ==> ('235494998989', '1', '2232659484812121551251549994')
mails ='Ahmed@gmail.com, mahmoud@yahoo.com, mona@hotmail.com, fady@mail.org'
b= mails.split(",")
print(b)#print ==> ['Ahmed@gmail.com', ' mahmoud@yahoo.com', ' mona@hotmail.com', ' fady@mail.org']
mail1= 'Alhousainy.Abdelrahman@gmail.com'
c=mail1.partition('@')
print(c)#print ==> ('Alhousainy.Abdelrahman', '@', 'gmail.com')
d=mails.rpartition("@")
print(d)#print ==> ('Ahmed@gmail.com, mahmoud@yahoo.com, mona@hotmail.com, fady', '@', 'mail.org')
introduce = 'he is mohamed and he is an engineer'
print(introduce.find('he'))#print ==>0
print(introduce.rfind('he'))#print ==> 18
print(introduce.find('z'))#print ==> -1
#print(introduce.index('z'))#print ==> error ==> Substring not found
re= mails.replace("c", "w")
print(re)#print ==>Ahmed@gmail.wom, mahmoud@yahoo.wom, mona@hotmail.wom, fady@mail.org
print(mails)#print ===> Ahmed@gmail.com, mahmoud@yahoo.com, mona@hotmail.com, fady@mail.org
ex1= 'he is mostafa and he is student and he is excellent boy'
re1= ex1.replace("he", "Iam")
print(re1)#print ==> Iam is mostafa and Iam is student and Iam is excellent boy
print(ex1)#print ==> he is mostafa and he is student and he is excellent boy
print(ex1.count('h'))#print ==> 3
print(mails.count('com'))#print ==> 3
print(mails.count('@'))#print ==> 4
s= 'hoW ArE You mAN'
print(s.capitalize())#print ==> How are you man
print(s.title())#print ==> How Are You Man
print(s.upper())#print ==> HOW ARE YOU MAN
print(s.lower())#print ==> how are you man 
t1= 'hOW arE You mAN'
print(t1.swapcase())#print ==> How ARe yOU Man
t2= 'how are you man'
print(t2.center(30))#print ==>        how are you man        
print(t2.center(30,'#'))#print ==> #######how are you man########
#====================================================================================================
print("="*60)
t3 ='How Are You Man'
print(t3.ljust(30,'*'))#print ==>How Are You Man***************
print(t3.rjust(30,'*'))#print ==>***************How Are You Man
print(t3.ljust(30))#print ==> How Are You Man               
print(t3.rjust(30))#print ==>                How Are You Man
mails_1 ='Ahmed@gmail.com, mahmoud@yahoo.com, mona@hotmail.com, fady@mail.org'
t4='Hello world and Welcome to Python Group'
t5='Hello world & Welcome to Python Group + Company # 98.5% '
print(mails_1.isalpha())#print ==> False
print(t4.isalpha())#Print ==> False
print(t5.isalpha())#Print ==> False
t6 ='Hello,world,Welcome,to,Python,Group'
print(t6.isalpha())#Print ==> False
t7='HelloworldandWelcometoPythonGroup'
print(t7.isalpha())#Print ==> True
t8='   How Are You    '
print(t8.strip())#print ==>How Are You
print(t8.rstrip())#print ==>   How Are You
print(t8.lstrip())#print ==>How Are You    
t9 = '***abc***'
print(t9.strip('*'))#print ==> abc
print(t9.rstrip('*'))#print ==>***abc
print(t9.lstrip('*'))#print ==>abc***
#=====================================================================================================
ex= 'Dear Sir\nI Would Like To Tell You Something'
print(ex)#print ==> Dear Sir
#I Would Like To Tell You Something
#ex1= 'C:\windows\new folder'
#print(ex1)
ex2 = r'C:\Windows\new folder'
print(ex2)#print ==> C:\Windows\new folder
ex3= """Sweet Home 
alabama"""
print(ex3)#print ==> Sweet Home 
#alabama
a= 'Hello world'
b ="Python"
print(a,b)#print ==> Hello world Python
#print(t1,end=' ')#print ==> 
print(a, end = ' ' )
t10 = 'My Name Is Hesham'
print(t10)#print ==> My Name Is Hesham
t11 = 'Alhousainy'
t10 = 'My Name Is %s' %t11
print(t10)#print ==>My Name Is Alhousainy
t10 = 'My Name Is %s' %t11.rjust(40,'=').upper()
print(t10)#print ==> My Name Is ==============================ALHOUSAINY
#t15 = 'My Age Is %d' %'26'
#print(t15)#print ==> error
t15 = 26
t16 = 'my age is %d' %t15
print(t16)#print ==> my age is 26
name = 'Alhousainy'
country = 'Egypt'
stat = 'My Name Is %s and I am From %s and My Age Is %d' %(name,country,t15)
print(stat)#print ==> My Name Is Alhousainy and I am From Egypt and My Age Is 26
nat = ' I am Egyptian'
print(nat)#print ==> I am Egyptian
nat1 = 'I\' am Egyptian'
print(nat1)#print ==> I' am Egyptian
nat2 = "I' am Egyptian"
print (nat2)#print ==> I' am Egyptian
nat3 = 'Yes," He Said !'
print(nat3)#print ==> Yes," He Said !
nat4='My Name Is "Alhousainy"'
print(nat4)#print ==> My Name Is "Alhousainy"
nat5 = "\"Yes,\" he said !"
print(nat5)#print ==> "Yes," he said !
nat6='"Isn\'t,"She Said'
print(nat6)#print ==> "Isn't,"She Said
#==============================================================================
print("="*60)
n1= '123456'
n2 = 'abc897546'
print(n1.isdigit())#print ==> True
print(n2.isdigit())#print ==> False
st1 = "MOHAMMED"
st2= "AHMEd"
print(st1.isupper())#print ==> True
print(st2.isupper())#print ==> False
st3='alhousainy'
st4='Alhousainy'
print(st3.islower())#print ==> True
print(st4.islower())#print ==> False
st5 = "My Name Is Alhousainy"
st6 = "My Name is Alhousainy"
print(st5.istitle())#print ==> True
print(st6.istitle())#print ==> False
st7="My Name Is Alhousainy"
print(st7.endswith('Alhousainy'))#print ==> True
print(st7.endswith('y'))#print ==> True
print(st7.endswith('Is'))#print ==> False
print(st7.endswith('M'))#print ==> False
st8 = '-'.join(('Ahmed', 'Mostafa', 'Mohamed', 'Khalad'))
print(st8)#print==> Ahmed-Mostafa-Mohamed-Khalad
st9 = '\n'.join(('My Name Is Alhousainy', 'Iam an Machine Learning Engineer', 'I Working at ISFP Company'))
print(st9)
#print==>My Name Is Alhousainy
#print==>Iam an Machine Learning Engineer
#print==>I Working at ISFP Company
st10 = ' '.join('Welcome World')
print(st10)#print ==> W e l c o m e   W o r l d
st11='  '.join(('Ahmed', 'Mostafa', 'Mohamed', 'Khalad'))
print(st11)#print ==> Ahmed  Mostafa  Mohamed  Khalad
import numpy as np
st12 =' '.join([str(i) for i in np.random.randint(10, size = 15)])
print(st12)
#print==> 2 7 8 7 6 2 1 3 4 3 6 1 9 0 6
st13 =' '.join([str(i) for i in np.random.randint(10, size = 100)])
print(st13)
#print ==>3 2 2 0 0 8 4 4 0 0 5 7 1 5 9 3 6 2 0 0 4 2 5 3 2 0 5 5 2 5 1
#print ==>1 3 8 3 1 6 7 1 5 8 9 2 6 4 5 6 8 2 1 1 6 2 1 7 9 5 9 7 1 5 4 0
#print ==>8 5 2 4 4 0 0 4 3 6 2 1 6 8 7 0 5 7 2 3 3 2 7 7 9 4 2 6 4 8 2 7
#print ==>0 7 2 7 4 4 1 8 5 0 4 4 3 3 9 4 2 1 8 4
st14 ='=='.join([str(i) for i in np.random.randint(10, size = 15)])
print(st14)#print ==> 4==6==4==8==5==0==8==3==0==8==9==4==3==4==2
#===============================================================================================
print('='*60)
import numpy as np
import math as m
st1 = 'The Value Of Pi is = {}'.format(np.pi)
st2 = 'The Value Of Pi Is = {}'.format(m.pi)
print(st1)#print ==>The Value Of Pi is = 3.141592653589793
print(st2)#print ==> The Value Of Pi Is = 3.141592653589793
st3 = '{0} and {1}'.format('My Name Is Alhousainy','My Age Is 26 Years old')
print(st3)#print ==> My Name Is Alhousainy and My Age Is 26 Years old
st4 ='{1} and {0}'.format('My Name Is Alhousainy','My Age Is 26 Years old')
print(st4)#print ==> My Age Is 26 Years old and My Name Is Alhousainy
st5 = 'First : {first}. Last: {last}.'.format(last ='Z', first = 'A')
print(st5)#print ==> First : A. Last: Z.
st6 = 'Name Is {name} , My Age is {age} and My Position is {pos}'.format(age = '26',pos ='Machine Learning Eng' , name ='Alhousainy')
print(st6)#print ==> Name Is Alhousainy , My Age is 26 and My Position is Machine Learning Eng
st7 ='The Value Of Pi Is = {0:.3f}'.format(np.pi)
print(st7)#print ==> The Value Of Pi Is = 3.142
st8 ='My Name Is {:s} and My Age is {:d} and My Status is {:s} and My Job is {:s} '.format('Alhousainy',26,'single','Ml_Eng')
print(st8)#print ==> My Name Is Alhousainy and My Age is 26 and My Status is single and My Job is Ml_Eng 
st9 = '|'+'{:^51}'.format('Hello')+'|'
print(st9)#print ==> |                       Hello                       |
st10 = '{0:10} ==> {1:10d}'.format('Alhousainy',1996)
print(st10)#print ==> Alhousainy ==>       1996
import re

email = re.compile('\w+@\w+\.[a-z]{3}')
text = "To email Guido , try guido@python.org or guido@google.com"
st11 = email.findall(text)
print(st11)#print ==> ['guido@python.org', 'guido@google.com']
email_2 = re.compile('\w+@\w+\.[a-z]{2}')
text_2 = "To email Guido , try guido@python.org or guido@google.com"
st12 = email.findall(text)
print(st12)#print ==> ['guido@python.or', 'guido@google.co']
email_3 = re.compile(r'([\w.]+)@(\w+)\.([a-z]{3})')
text_3 = "To email Guido , try guido@python.org or guido@google.com"
st14 = email_3.findall(text)
print(st14)#print ==> [('guido', 'python', 'org'), ('guido', 'google', 'com')]
'''
#email_3 = re.compile('\w\.\+@\w+\.[a-z]{15}')
#text3 ='To Email Alousainy.Abdelrahman@gmail.org or Eabdelrahman@isfp.net or Eabelrahman.Ml@yahoo.org '
#st13 = email_3.findall(text3)
#print(st13)#print ==> 
#email_3 = re.compile(r'([\w\.]+)([\w\.]+)@(\w+)\.([a-z]{15})')
#text3 ='To Email Alousainy.Abdelrahman@gmail.org or Eabdelrahman@isfp.net or Eabelrahman.Ml@yahoo.org '
#st13 = email_3.findall(text3)
#print(st13)#print ==>
#email_3 = re.compile(r'([\w.]+)@(\w+)\.([a-z]{3})')
#text_3 = "To email Guido , try guido@python.org or guido@google.com"
#st14 = email_3.findall(text)
#print(st14)#print ==> ['guido@python.or', 'guido@google.co']

email= re.compile(r'([\w.]+)@(\w+)\.([a-z]{3})')
text = "To email Alhousainy , try Alhousainy@gmail.com or Alhousainy.Abdelrahman@yahoo.org or Eabdelrahman@isfp.net"
st15 = email.findall(text)
print(st15)
#print ==> [('Alhousainy', 'gmail', 'com'), ('Alhousainy.Abdelrahman', 'yahoo', 'org'), ('Eabdelrahman', 'isfp', 'net')]

email = re.compile('\w+@\w+\.[a-z]{3}')
text = "To email Alhousainy , try Alhousainy@gmail.com or Alhousainy.Abdelrahman@yahoo.org or Eabdelrahman@isfp.net"
st16 = email.findall(text)
print(st16)
#print ==> ['Alhousainy@gmail.com', 'Abdelrahman@yahoo.org', 'Eabdelrahman@isfp.net']
'''
'''
text ="To email Alhousainy , try alhousainy@python.org or Alhousainy@isfp.net or Eabdelrahman@yahoo.com"
email4 = re.compile(r'(?p<user>[\w.]+)@(?p<domain>\w+).(?p<suffix>[a-z]{3})')
match= email4.match('alhousainy@python.org','Alhousainy@isfp.net')
print(match.groupdict())
#print ==> 
'''