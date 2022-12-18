print('='*60)
n=int(input('Please Enter The Number : '))
while n<=10:
    print('The Number Is = ' , n)
    n+=1
print('The Operation Is Done')
#The Number Is =  3
#The Number Is =  4
#The Number Is =  5
#The Number Is =  6
#The Number Is =  7
#The Number Is =  8
#The Number Is =  9
#The Number Is =  10
#The Operation Is Done
print('='*30)
while True:
    a= int(input('Please Enter The Number ==> '))
    if a>=15:
        print('Yes The Coorect and The Number Is Greater Than From 15 is =' ,a)
        break
    else:print('No The Number Is Lower Than From 15 and The Number Is = ',a)
print('End')
print('='*30)
'''Please Enter The Number ==> 10
No The Number Is Lower Than From 15 and The Number Is =  10
Please Enter The Number ==> 14
No The Number Is Lower Than From 15 and The Number Is =  14
Please Enter The Number ==> 18
Yes The Coorect and The Number Is Greater Than From 15 is = 18
End'''
while True:
    S=str(input('Please Enter The Name : '))
    if S == 'Alhousainy':
        print('The Cirrect Name and The Name Is =' ,S)
        break
    else:
        print('No The Name Is Wrong ! and the name is => ',S)
        print('Please Try Again!')
print('The End')
print('='*30)
'''''
Please Enter The Name : Ahmed
No The Name Is Wrong ! and the name is =>  Ahmed
Please Try Again!
Please Enter The Name : Mostafa
No The Name Is Wrong ! and the name is =>  Mostafa
Please Try Again!
Please Enter The Name : Alhousainy
The Cirrect Name and The Name Is = Alhousainy
The End'''
name =str(input('Please Enter The Name :'))
while name =='Ahmed':
    print('The Name Is Right and The Name Is =>',name)
    name=str(input('Please Enter The Name Again : '))
print('Done')
'''''
Please Enter The Name :Ahmed
The Name Is Right and The Name Is => Ahmed
Please Enter The Name Again : Ahmed
The Name Is Right and The Name Is => Ahmed
Please Enter The Name Again : Mostafa
Done'''
print('='*30)
r=int(input('Please Enter The Number : '))
while r:
    print('The Number Is Greater Than 0 and The Number Is = ',r)
    r-=1
print('The Operation Is End')
'''''
Please Enter The Number : 8
The Number Is Greater Than 0 and The Number Is =  8
The Number Is Greater Than 0 and The Number Is =  7
The Number Is Greater Than 0 and The Number Is =  6
The Number Is Greater Than 0 and The Number Is =  5
The Number Is Greater Than 0 and The Number Is =  4
The Number Is Greater Than 0 and The Number Is =  3
The Number Is Greater Than 0 and The Number Is =  2
The Number Is Greater Than 0 and The Number Is =  1
The Operation Is End'''
print('='*30)
x=0
while x<=5:
    x+=1
    name = str(input('Please Enter The Name =>'))
    print('The Number Is Less Than From 5 and The Number Is ==> ',x, 'and The Name Is =>',name)
else:print('The Number Is Greater Than From 5 and The Number Is = ',x)
'''''
Please Enter The Name =>Alhousainy
The Number Is Less Than From 5 and The Number Is ==>  1 and The Name Is => Alhousainy
Please Enter The Name =>Mostafa
The Number Is Less Than From 5 and The Number Is ==>  2 and The Name Is => Mostafa
Please Enter The Name =>Ahmed
The Number Is Less Than From 5 and The Number Is ==>  3 and The Name Is => Ahmed
Please Enter The Name =>Ali
The Number Is Less Than From 5 and The Number Is ==>  4 and The Name Is => Ali
Please Enter The Name =>Mia
The Number Is Less Than From 5 and The Number Is ==>  5 and The Name Is => Mia
Please Enter The Name =>Khalad
The Number Is Less Than From 5 and The Number Is ==>  6 and The Name Is => Khalad
The Number Is Greater Than From 5 and The Number Is =  6   '''