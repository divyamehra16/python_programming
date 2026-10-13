l1=[1,2,3,4,5,6]
d={i:i**2 for i in l1}          #dict comprehension

l2=[i**2 for i in l1]           #list comprehension
t=(i**2 for i in l1)            #tuple comprehension --> stores values in form of bytes
t1=tuple((i**2 for i in l1)) 

print(d)
print(l2)
print(t)
