# itertools -->
'''
product(*iterables) --> provides the "cartesian product"
permutations(iterables) --> possible arrangements
combinations(iterables) --> possible combinations
groupby(iterables,key) --> group consecutive elements by key
'''
""" import itertools
#product(*x)
print(list(itertools.product('abc',[1,2,3])))

#permutations(<seq>,key)
print(list(itertools.permutations('abc',2)))

#combinations(<seq>,<key>)
print(list(itertools.combinations('abc',2)))

#groupby(<seq>,<key>)
data=['apple','apricot','banana','blueberry','avacado']
data_sorted=sorted(data,key=lambda x:x[0])
for key,group in itertools.groupby(data_sorted,key=lambda x:x[-1]):
    print(key,list(group))

 """
import itertools
para="Python is a high-level, general-purpose programming language created by Guido van Rossum and first released in 1991. It uses clean, English-like syntax and indentation to structure code, making it widely used across AI, data science, web development, and automation"
lpara=para.split(" ")
psorted=sorted(lpara,key= lambda x:len(x))
for key,group in itertools.groupby(psorted,lambda x: len(x)):
    print(key,list(group))
