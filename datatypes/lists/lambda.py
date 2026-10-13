'''need to be a sequence'''

# lambda --> used for single line function.
# filter --> works on a sequence "used to select" --> kuch *condition* ke according extract elements. --> list
# map    --> "processing element" --> har element pe kuch kuch kaam. --> list
# reduce --> need to import it from functools --> single value


a=lambda x:x+2
print(a(2))

# extracting list of even numbers from a list;
l1=[1,2,3,4,5,6]
f=filter(lambda x:x%2==0,l1)    #-> filter(condition,sequence)
l=list(f)
print(l)

#extracting a two digit number;
l1=[1,2,33,42,11,4,55]
f=filter(lambda x:x>=10 and x<100,l1)
print(list(f))

#creating a list of square each element in a list; 
l1=[1,2,34]
m=map(lambda x:x**2,l1)
print(list(m))

#sum of all elements in a list;
from functools import reduce
l1=[1,2,344,5,6,54,77]
r=reduce(lambda x,y:x+y,l1)
print(r)
r=reduce(lambda x,y:x if x>y else y,l1)
print(r,"max")
r=reduce(lambda x,y:x if x<y else y,l1)
print(r,'min')


                # list comprehension --> multiline code in single line [<processing statement> for loop]


l1=[12,33,44,22]
l2=[]
for i in l1:
    l2.append(i*i)
print(l2)

l3=[i*i for i in l1]              # map()
print(l3)
l4=[i*i for i in l1 if i*i>1000]  # filter()
print(l4)


