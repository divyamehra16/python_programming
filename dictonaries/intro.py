# NOT SEQUENCED datatype

# contain key-value pairs

# key-value separated using ':'

# duplicate keys "not allowed"

# duplicate values "allowed"

#insertion order is not preserved  --> "indexing not possible"

#dynamic data-type   --> create/add new values

d={1:'a',2:'b',3:'c'}
d[4]='d'
d['1']='str'            #create a new item
d[2]='hii'              #update the item
print(d)
d[1.0]='hello'          #integer(1) == float(1.0)
print(d)

'''print(d[10]) '''           # KeyError --> index out of range

# by-passing / Handling KeyError
if 10 in d:
    print(d[10])
else:
    print('key not found')
    

d={}
n=int(input('enter no. of elements '))
i=1
while i<=n:
    name=input('name')
    s=int(input('salary'))
    d[name]=s
    i+=1
print(d)
for x in d:
    print('The employee name',x,'has salary',d[x])


#removing a value from dict -->  del & del()
d={1:11,2:22,3:33,4:44}
print(d)
del d[1]
print(d)
del(d[2])
print(d)

# clear()  to remove everything  --> make dictionary empty.
d.clear()
print(d)
