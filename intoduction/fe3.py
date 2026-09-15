#calculate SI
p=float(input('enter principle value; '))
r=float(input('enter rate; '))
t=float(input('enter time value; '))
si=(p*r*t)/100
print('simple interest is',si)


#eval --> accepet value in string and evalaute it and return the result.

a=eval('10+10')
b=eval('10>=10')
c=eval('10 or 20')
d=eval('10 and 30')
e=eval('10/5')
f=eval('10//5')
g=eval('10%5')
h=eval('10**2')
print(a,b,c,d,e,f,g,h)

#eval with input
val=eval(input('enter a value'))
print(val,type(val))


#use of eval
a=eval(input('num1 '))
b=eval(input('num2 '))
c=a+b
print(c,type(c))




