#checking number is positive or negative

x=int(input("enter a number ; "))
if x<0:
    print('The number is negative')
else:
    print('The number is positive')


#validating the name entered with the username we have;

user_name='rahul'
x=input('enter username ; ')
if x.upper()==user_name.upper():
    print('user name is valid')
else:
    print('invalid user name')


#finding the biggest number among two numbers;

num1=int(input('enter a number1 ; '))
num2=int(input('enter a number2 ; '))
if num1>num2:
    print('bigger number is ;', num1)
else:
    print('bigger number is ;', num2)


#finding the biggest number among three numbers;

