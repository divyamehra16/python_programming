# types of arguments --> i. Formal arguments --> def sum(a,b) here a,b-formal arguments
                    #   ii. Actual arguments --> sum(23,1)  here  23,1-actual arguments

#type of FORMAL Arguments:
"""
1. Positional Argument
2. Keyword Arguments
3. Default Arguments
4. Variable Length Arguments
5. Keyword Variable Length Arguments
"""
# POSITIONAL Arguments
def details(name,age):
    print(f"Hi! myself {name} and my age is {age}")
details("Naina",17)
details(19,"Mansi")

# KEYWORD Arguments
details(name="Mansi",age=19)        # BETTER way--> Always use it
details(age=19,name="Naina")

# DEFAULT Arguments
def SI(p,r=2,t=10):
    return (p*r*t)/100
print(SI(1000))
print(SI(1000,3))
print(SI(1000,3,5))

# VARIABLE-Length Arguments
def add(x,*y):      # *y== create a tuple
    print(type(y),y)
    return x+sum(y)
print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))
print(add(10,20,25))
print(add(20))      #*y== empty-tuple
print(add(10,))
#print(add())        # ERROR


def add(*y):      # *y== create a tuple
    print(type(y),y)
    return sum(y)
print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))
print(add(10,20,25))
print(add(20))      #*y== empty-tuple
print(add(10,))
print(add())        # NO-Error


# KEYWORD-variable length Arguments
def printdata(**d):     # **d--> create a dictionary
    print(type(d),d)
    for key,value in d.items():
        print(key,"=>",value)
printdata(name="xyz",age=25)
printdata(id="GLA2026",name="abc",course="Btech")


# *<variable> === creates a list
# **<variable> === creates a dictionary