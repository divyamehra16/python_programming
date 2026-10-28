# Generator type function

# "yield" ---> keyword

def apnamap(func,l):
    for i in l:
        yield func(i)
l=[1,2,3,4,5]
l=list(apnamap(str,l))
print(l)

s=list(apnamap(int,input("enter number space separated: ").split()))
print(s)

def apnarange(x,y,s=1):
    while x<=y:
        yield x
        x+=s
l1=list(apnarange(5,10))
print(l1)
