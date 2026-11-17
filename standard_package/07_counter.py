# collection -module
"""
counter(iterable)   --> count the occurences of each element in a sequence

defaultdict(type)   --> give the default value to a non-existing key of type you have passed. 

deque(iterable) --> a list --> double-ended queue
                    rear/last mei --> insertion
                    front --> deletion

namedtuple(typename,fields) --> tuple with named fields
"""

import collections
print(collections.Counter('banana'))
d=collections.defaultdict(int)
d['x']+=1
print(d['x'],d['y'])

dq=collections.deque([1,2,3,4])
dq.appendleft(0)
dq.append(5)
print(dq,type(dq))

student=collections.namedtuple("Student","roll name age")
# creating instances(positional,keyword)
s1=student(name='xyz',roll=101,age=18)
s2=student(202,'abc',19)
# accessing by name
print(s1.name,s1.age,s1.roll)
# accessing by index
print(s2[0],s2[1],s2[2])
# unpacking like normal tuple
roll,name,age=s1
name,age,roll=s2
print(s1)
print(s2)
