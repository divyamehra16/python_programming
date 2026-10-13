# 1. len()

# 2. count()

# 3. index()  ->  but not rindex()

# 4. sorted()   --> sorted(<seq>,reverse=True/False) False for "ascending" {by-default}, and True for "descending"

t=(20,10,30,40,24)
y=sorted(t,reverse=False)        # returns a "list data-type"
x=sorted(t,reverse=True)
print(t)
print(y)
print(x)


# 5. min() and max()

t=(1,2,45,25,66)
print(min(t))
print(max(t))

# tuple --> packing & unpacking

l1=[]
for i in range(3):
    r=int(input('enter roll no. '))
    n=input('enter name ')
    e=input('enter email ')
    p=input('enter phone no. ')
    t=r,n,e,p           # tuple-packing
    l1.append(t)

for r,n,e,p in l1:      # tuple-unpacking
    print("%5d %-15s %-20s %10s"%(r,n,e,p))
    # '-' left align then spaces {pehle naam/value phir space}, and '+' is right align{pehle space phir naam/value}
    