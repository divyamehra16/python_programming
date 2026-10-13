# collection / sequence of objects
# immutable datatype

x=(1,2,3,4)
y=1,2,3,4           # packing --> creating a tuple
a,b,c,d=y           # unpacking 
a,b,c,d=d,c,a,b     # internal unpacking
print(a,b,c,d)
print(x,type(x))
print(y,type(y))

t=(40)
print(t,type(t))
t=(40,)             # single-value tuple
print(t,type(t))

l1=[12,3,44,5]     # sequence to tuple using ---> tuple()
t=tuple(l1)
print(t)
t=tuple(range(4))
print(t[2:100])


# operators :  +  &  *

t1=(1,2,3,4)
t2=(5,6,7)
print(t1+t2)
print(t1*2)