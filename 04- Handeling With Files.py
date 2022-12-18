# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 16:00:02 2022

@author: ENG-Alhousainy
"""

print('='*60)
f= open('D:\\Programming\\Machine learning Python\\Files\\1.txt','w')
f.write('My Name Is Alhousainy and My Age Is 26 Years Old and I am a machine Learning Engineer')
f.close()
'''
f1=open('D:\\Programming\\Machine Learning Python\\Files\\2.text','w')
f1.write('First Line ==> Hello Python Team and Iam very for Working with Them\n')
f1.write('Second line ==>Iam New Member for a Machine Learning Team\n')
f1.write('Third Line ==> My Age is 26 Years Old\n')
f1.close()'''
f1=open('D:\\Programming\\Machine Learning Python\\Files\\3.text','w')
f1.write('Line 1 ==>Hello Python Team and Iam very for Working with Them\n')
f1.write('line 2 ==>Iam New Member for a Machine Learning Team\n')
f1.write('Line 3 ==>My Age is 26 Years Old\n')
f1.close()
f2=open('D:\\Programming\\Machine Learning Python\\Files\\3.text','a')
f2.write('Line 4 ==>Iam Working at Integrated Solution For Ports\n')
f2.write('Line 5 ==>Iam Very Happy For Working With Them')
f2.close()
f3=open('D:\\Programming\\Machine Learning Python\\Files\\3.text','r')
for i in f3:
    print(i)
f3.close()
print('='*60)
#print==>Line 1 ==>Hello Python Team and Iam very for Working with Them
#print==>line 2 ==>Iam New Member for a Machine Learning Team
#print==>Line 3 ==>My Age is 26 Years Old
#print==>Line 4 ==>Iam Working at Integrated Solution For Ports
#print==>Line 5 ==>Iam Very Happy For Working With Them
f4 =open('D:\\Programming\\Machine Learning Python\\Files\\python_CSV.csv','w')
f4.write('Line 1 ==>Hello Python Team and Iam very for Working with Them\n')
f4.write('line 2 ==>Iam New Member for a Machine Learning Team\n')
f4.write('Line 3 ==>My Age is 26 Years Old\n')
f4.write('Line 4 ==>Iam Working at Integrated Solution For Ports\n')
f4.write('Line 5 ==>Iam Very Happy For Working With Them\n')
f4.close()
f5 =open('D:\\Programming\\Machine Learning Python\\Files\\python_Excel.xls','w')
f5.write('Line 1 ==>Hello Python Team and Iam very for Working with Them\n')
f5.write('line 2 ==>Iam New Member for a Machine Learning Team\n')
f5.write('Line 3 ==>My Age is 26 Years Old\n')
f5.write('Line 4 ==>Iam Working at Integrated Solution For Ports\n')
f5.write('Line 5 ==>Iam Very Happy For Working With Them\n')
f5.close()
f6 = open('D:\\Programming\\Machine Learning Python\\Files\\python_CSV.csv','a')
f6.write('Line 7==> Welcome TensrFlow Group\n')
f6.write('Line 8==> Welcome ISFP Members\n')
f6.close()
f7 =open('D:\\Programming\\Machine Learning Python\\Files\\python_Excel.xls','a')
f7.write('Line 7==> Welcome TensrFlow Group\n')
f7.write('Line 8==> Welcome ISFP Members\n')
f7.close()
f8 = open('D:\\Programming\\Machine Learning Python\\Files\\python_CSV.csv','r')
for i in f8:
   print(i)
f8.close()
print('='*60)
f9 = open('D:\\Programming\\Machine Learning Python\\Files\\python_CSV.csv','r')
for i in f9:
    print(i)
f9.close()
print('='*60)
import os
var = os.getcwd()
print(var)#print ==>D:\Programming\Machine learning Python
os.makedirs('D:\\Programming\\Machine Learning Python\\Files\\pyhon',exist_ok=True)
#os.makedirs('D:\\Programming\\Machine Learning Python\\Files\\pyhon',exist_ok=False)
var1=os.path.exists('D:\\Programming\\Machine Learning Python\\Files\\pyhon')
var2=os.path.exists('D:\\Programming\\Machine Learning Python\\Files\\python_CSV.csv')
print(var1)#print==>True
print(var2)#print==>True
var3=os.path.exists('D:\\Programming\\Machine Learning Python\\pyhon')
var4=os.path.exists('D:\\Programming\\Machine Learning Python\\python_CSV.csv')
print(var3)#print==>False
print(var4)#print==>False
import shutil as sh
# sh.copyfile('D:\\Programming\\Machine Learning Python\\Files\\python_CSV.csv',
# 'D:\\Programming\\Machine Learning Python\\Files\\pyhon\\python.csv' )
# sh.copyfile('D:\\Programming\\Machine Learning Python\\Files\\python_Excel.xls'
# ,'D:\\Programming\\Machine Learning Python\\Files\\pyhon\\python.xls' )
# sh.copytree('D:\\Programming\\Machine Learning Python\\Files\\pyhon',
# 'D:\\Programming\\Machine Learning Python\\Files\\Alhousainy')
sh.move('D:\\Programming\\Machine Learning Python\\Files\\python_CSV.csv',
'D:\\Programming\\Machine Learning Python\\ISFP.csv')
sh.move('D:\\Programming\\Machine Learning Python\\Files\\pyhon',
'D:\\Programming\\Machine Learning Python\\ISFP_File')