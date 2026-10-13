# 1. len()
s={1,2,3,4}
print(len(s))


# 2. add()  --> adding a new element -> <set>.add(<single key>)

s={1,2,3}
s.add(4)
print(s)


#3. update() --> adding multiple sequenced -> <set>.update(<k1>,<k2>)

s={1,2,3,4}
s.update([5,6])
print(s)
s.update([2,3,7],range(10))  #--> will update the duplicate value
print(s)


# 4. copy() --> cloning / deep copy.
s.copy()


# 5. pop() --> will remove and return some random key 

s={1,2,3,4}
print(s.pop())
print(s) 


# 6. remove()  --> remove a key from a set --> <set>.remove(<key>)
        # if key not present --> "KeyError"

s={1,2,34,4,5}
s.remove(2)
print(s)
s.remove(3)     #Error
print(s)


# 7. discard()  --> same as remove but "no error"
s={1,2,34,4,5}
s.discard(2)
print(s)
s.discard(3)
print(s)


# 8. union()  --> all the keys present in both the sets
        # <set1>.union(<set2>)  or  <set1> | <set2>

x={1,2,3,4}
y={2,3,4,5,6,7}
print(x.union(y))
print(x|y)


# 9. intersection() --> common keys in both the sets
        # set1.instersection(set2)  or  set1 & set2

x={1,2,3,4}
y={2,3,4,5,6,7}
print(x.intersection(y))
print(x&y)


# 10. difference()  --> x-y (y vale elements x se hat jaenge) and vice-versa for y-x
        # x.difference(y) or x-y
        # y.difference(x) or y-x

x={1,2,3,4,10,20}
y={2,3,4,5,6,7}
print(x.difference(y))
print(x-y)
print(y-x)


# 11. symmetric_difference()  -->common portion from both the set is removed 
        # x.symmetric_difference(y)  or  x^y

x={1,2,3,4,10,20}
y={1,2,3,40,50}
print(x.symmetric_difference(y))
print(y^x)
