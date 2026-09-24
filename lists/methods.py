# 1. len()
l1=[1,2,3,4,5,6]
print(len(l1))


# 2. count() --> <list>.count(<element>)
n=[1,2,2,3,1,3,2,2,4,5]
print(n.count(2))


# 3. append()  --> <list>.append(<value>) --> append/add the value in the end of the list.
l=[]
l.append('python')
l.append('programming')
l.append('language')
print(l)

# 4. insert()  --> <list>.insert(<index>,<value>) --> insert the value at the given index in the list. -->and the element at that "particular position" shifted to the right side & other elements depend.
n=[20,30,40,50]
n.insert(0,10)
n.insert(6,60)
n.insert(-10,0)
print(n)


# 5. extend() --> <list>.extend(<sequence>)
l1=[1,2,3]
l2=['a','b','c']
l2.extend(l1)
print(l1, l2)


# 6. remove() --> <list>.remove(<value>) --> 'error' if value doesn't exist *ValueError*  --> doesn't return value
l1=[1,2,3,1]
l1.remove(1)
print(l1)


# 7. pop() --> <list>.pop(<index>) --> if index not found *IndexError* --> return the removed-value as well

l1=[1,2,3,4,5]
l1.pop()
l1.pop(2)
print(l1.pop(2))
print(l1)


# 8. reverse() --> <list>.reverse() --> inplace changes
l1=[1,2,3,4,'hello']
l1.reverse()
print(l1)


# 9. sort()  --> <list>.sort() --> list should contain "homogeneous" elements. else: TypeError
l1=[1,2,44,55,3,3]
l1.sort()    # by-default  --> ascending order
print(l1)


# 10. shallow copy   &   deep copy

    # shallow copy --> working in the same memory, we have just copied the reference.
x=[1,2,3,5]
y=x
y[3]=4
print(x,id(x))
print(y,id(y))

    # deep copy --> making the clone -> creating duplicate independent object.
x=[1,2,3,4]
y=x.copy()     # y=x[::]
y[0]=0
print(x,id(x))
print(y,id(y))


# 11. Operators 
    # i.  concatenation   -->  do list add 
    #ii.  mulptipliaction -->  replicate the list n-times -> n==integer else TypeError
    #iii. relational operators(>,<,==)  --> atleast one index true
    #iv.  membership operator

l1=[1,2,3]
l2=[4,5,6]
print(l1+l2)
print(l1,l2)
print(l1*2)
l3=[0,2,3]
print(l1<l3)
print([1,2,3]>[1,2,3,4])
# chronological ordering.
print(['AB','CD']>['ab','cd','ef'])


# nested list 
l1=[1,2,[3,[3.1,3.2,3.3]],4]
print(l1[2][1])

a=[80,90]
b=[30,20,10,a]
print(b[0])
print(b[1])
print(b[2])
print(b[3])
