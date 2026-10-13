
# same comprehensions as for other data-types just use {}

s={i*i for i in range(5)}       #just keys
print(s,type(s))

#dict
d={i:i*i for i in range(5)}     #key-value pair
print(d,type(d))




#Frequency Dictionary 
d={}
l1=[1,2,3,2,3,1,3,1,3,5,2,5,2,2,4]
print(list(set(l1)))
for i in l1:
    d[i]=l1.count(i)
print(d)
d1={x:y for x,y in d.items() if y>1}
print(d1)



# FROZEN SET --> "fSet" --> forzenset(<iteration>)
# converting mutable seq/iteration to immutable --> no operation can be done

v={1,2,3,4}
fset=frozenset(v)
print(v,type(v))
print(fset,type(fset))
v.add(5)
print(v)
print(fset)

v=[1,2,3,4]
fset=frozenset(v)
print(v,type(v))
print(fset,type(fset))
v.append(5)
print(v)
print(fset)
