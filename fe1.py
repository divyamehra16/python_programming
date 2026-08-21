'''
value=110
value='hii'
value=12.21
print(value)
print(type(value))'''
'''
a,b,c=10,20,30    #multiple values assign to multiple variables in single line
print(a,b,c)
'''
"""
a,b,c=10,20   #error
print(a,b,c)"""
"""
a=b=c=10   #single value to multiple variables simultaneously
print(a,b,c)"""
'''
a=20
print('first assigned value is;',a)    #re-initialize the variables
print(type(a))
a='hello!'
print('variable is re-initialised,now value is;',a)
print(type(a))
'''
#constant; full variable name in capital generally considered consant eg; FILE_LIMIT=2000
'''
emp_id=11        #datatype in python {int,str,float}
name='irfan'
salary=2000.40
print(type(emp_id))
print(type(name))
print(type(salary))
#data type can be found using type() function: in-built or pre-define function
'''
'''
a=2e2   #2 multiply e^2 {e==10}
b=2e4
print(a,b)
print(type(a),type(b))
'''
"""
a=3+5j   #complex data type
b=2-5.5j
c=3+10.5j
print(a,b,c,type(a))
print(a+b)
print(b+c)
print(a+c)
print(type(a+b+c))
"""
"""
a=True   #bool ; boolean datatype
b=False
print(a,type(a))
print(b,type(b))
print(a+a)
print(a+b)
print(b+b)    #empty string "" is false
"""
'''
a=None    #None datatype; that doesn't contain any value
print(a,type(a))
'''
"""
a="hello,python world!"     #string datatype; single and multi-line string
b='''hello,
python world!'''
c='''hello,
python
world!'''
print(a)
print(b)
print(c)
"""
"""
x=[10,200,30]  #bytes datatype; 
y=bytes(x)     
print(y)       
print(type(y))
print(y[0])
print(y[1])
print(y[2])
x=[10,20,300]  #range- [0 to 256) --> ValueError
y=bytes(x)
print(y)
x=[100,200]
y=bytes(x)
y[0]=110       #bytes are immutable --> TypeError
print(y)
x=[10,20,30,100]
y=bytes(x)
for i in y:
    print(i)
"""
"""
l1=range(5)      #0-4             #range datatype
l2=range(2,7)    #2-6
l3=range(2,10,2) #2,4,6,8
print(l1)
print(l2)
print(l3)
print(type(l3))
for i in l3:
    print(i)
a=range(10,2)   #will create nothing
print(a)
"""
"""
#type-conversion
a=5.9
n=int(a)            #int conversion
print(n,type(n))
b=5
m=float(b)          #float conversion
print(m,type(m))
c=6
l=str(c)            #string-conversion
print(l,type(l))
x=True
y=float(x)
print(y)
a='abc'
b=int(a)
print(b)
a='hello'            #boolean-conversion
a=bool(a)
print(a,type(a))
print(a*10)
b=""
b=bool(b)
print(b,type(b))
print(b*10)
"""


