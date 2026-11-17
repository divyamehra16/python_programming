# random module
""" 
randint(a,b) --> integer between a and b both inclusive
random()  --> float between [0.0,1.0)
choice(seq)  --> random element from a sequence
shuffle(list) --> shuffling the list elements --> make inplace changes
"""
from random import *
l1=["hello",101,"python",202]
print(choice(l1))
shuffle(l1)
print(l1)