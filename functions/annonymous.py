# lambda
# map()
# filter()


# use map for multiple call of a function

def cube(x):
    return x**3
l=[1,2,3,4,5]
l1=list(map(cube,l))
l2=list(map(cube,[int(i) for i in l]))
print(l1,l2,sep='\n')


from functools import reduce
sum=reduce(lambda x,y:x+y,[1,2,3,4,5])
print(sum)

min=reduce(lambda x,y: x if x<y else y,[1,2,3,4,5])
max=reduce(lambda x,y: x if x>y else y,[1,2,3,4,5])
print(min,max)

