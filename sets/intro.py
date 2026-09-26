# mutable datatype

# silicing and indexing not possible

# insertion is not preserved

# duplicate value can not be stored

# {1,2,3} --> 1,2,3 are not elements they're "keys"

s={10,20,30,40}
print(s,type(s))
s=set()
print(type(s))

l=[1,2,1,2,1,3,4,2,4,5,6,7]
s=set(l)   #--> duplicate values/keys will be removed
print(s)