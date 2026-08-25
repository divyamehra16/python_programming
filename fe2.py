"""
a=-89                     #any number is true except 0 and None and ''
print(bool(a)+3)
a="amit"
print(bool(a)+3)
"""
'''
a=5
print('123'+a)            #TypeError- different datatypes for performing calc
print(a+'123')
print('123'+str(a)) 
print(a+int('123'))
'''
'''
a=10
b=20
c=(a if a>b else b)+20
print(c)
a=10
b=20
c=-5
d= (a if a<c else c) if a<b else(b if b<c else c) 
print(d)
'''
"""a=20
b=12
print(a//b)
print(a%b)
print(a/b)
print(a**2)
print(a+b)
print(a-b)
print(a*b)
"""
#relational operator (>,< & ==)

#logical operators (and or & not)
"""a=0 and 4
print(a)
b=5 and 7
print(b)
c=21 and 0
print(c)
d=12 or 0
print(d)
print(12 or 3)
print(0 or 4)
print(not 5)
print(not 0)"""
#assignment operator (+=, -=, /=, //=, *=, %=, **=, %=)
"""a=10
b=5
a+=b
print(a)
"""
#unary operator(-)
"""a=10
print(-a)
b=-5
print(-b)"""

#membership operator (in & not in)
"""text='welcome to python'
print("to" in text)
print('Welcome'in text)
print('is' not in text)"""

#identity operator (is & is not --> refering to same memory address or not)
"""a=12
b=12
#same memory with different name --> reference
c=13
print(id(a))
print(id(b))
print(id(c))
print(a is b)
print(a is not b)
print(a is c)"""

#input operator
name=input("enter a name;")
print(name)
#input - single value at a time
"""a=input("enter a number;")
b=input("enter another number;")
c=float(a)+float(b)
print(c)
d=int(a)+int(b)
print(d)"""
"""
a=float(input('enter num'))
b=float(input('enter num'))
c=a+b
print(c)
"""


