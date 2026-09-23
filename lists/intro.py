#array --> homogeneous and fixed length
#list --> heterogeneous and dynamic length

l1=[]       #--> empty list
print(l1)
print(type(l1))

# 1. list()
r=range(0,10)
l1=list(r)
print(l1,type(l1))

# 2. MUTABLE
l1=[1,2,3,4,5]
print(l1)
l1[0]=0
print(l1)

# IndexError --> list index out of range error
l1=[1,2,3,4,5,6]
print(l1[0],l1[10])


# Slicing of list
n=[1,2,3,4,5,6]
print(n)
print(n[2:5:2])
print(n[4::2])
print(n[3:5])
