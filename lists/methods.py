""" # 1. len()
l1=[1,2,3,4,5,6]
print(len(l1))


# 2. count() --> <list>.count(<element>)
n=[1,2,2,3,1,3,2,2,4,5]
print(n.count(2))


# 3. append()  --> <list>.append(<value>) --> append/add the value in the end of the list.
l=[]
l.append('python')
l.append('programming')
l.append('lamnguage')
print(l)
 """

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


# 6. remove() --> <list>.remove(<value>) --> 'error' if value doesn't exist *ValueError*
l1=[1,2,3,1]
l1.remove(1)
print(l1)
