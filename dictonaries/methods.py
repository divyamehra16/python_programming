# 1. len()   --> returns count number of key-value pairs

# 2. dict()
    # dict({key1:val1,key2:val2})
    # dict([(key,value),tup2])

d=dict()
print(d,type(d))

d=dict({1:'abc',2:'xyz'})
print(d,type(d))

d=dict([(1,'abc'),(2,'abc')])
print(d,type(d))


# 3. clear() 



# 4. get()   --> <dict>.get(<key>,defaultvalue) *defaultvalue= to handle the KeyError

d={1:"abc",2:'xyz'}
print(d.get(1))
print(d.get(10,'no key found'))


# 5. pop()   --> <dict>.pop()

print(d.pop(1))         # returns the value removed
print(d)


# 6. popitem()  --> <dict>.popitem()   -> any random item

d={1:11,2:22,3:33,4:44,5:55}
print(d.popitem())    #return the key-value pair in form of 'tuple'
print(d)


# 7. keys()

d={1:11,2:22,3:33,4:44,5:55}
l=d.keys()          # list of keys
print(l,type(l))

# 8. values()

d={1:11,2:22,3:33,4:44,5:55}
l=d.values()        # list of values
print(l,type(l))


# 9. items()

d={1:11,2:22,3:33,4:44,5:55}
l=d.items()         # list of tuples containing key-value pair
print(l,type(l))
for k,v in d.items():
    print(k,'---',v)


# 10. copy()
