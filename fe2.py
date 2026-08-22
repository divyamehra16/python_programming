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
a=20
b=12
print(a//b)
print(a%b)
print(a/b)
print(a**2)
print(a+b)
print(a-b)
print(a*b)
