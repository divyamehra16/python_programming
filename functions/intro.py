# FUNCTIONS - group of statements or block of codes. 
    # maintain the code in the easy way.
    # code re-usability.

# TYPES -->  (i) Pre-define or built-in.      (ii) user define.

#defining a function
def display():
    print('Welcome to function!')
#calling a function
display()


def sum(a,b):
    print('Sum of two values :',a+b)
sum(5,2)

# if function is not returning anything still we're printing it, then it'll return "None".

# returning function
def multiply(a,b):
    c=a*b
    return c
x=multiply(3,2)
print("Multiplication of a number :",x)

# non-returning function
def multiply(a,b):
    c=a*b
    print(c)
x=multiply(3,2)
print("function returning",x)

# multiple return values
def m1(a,b):
    c=a+b
    d=a-b
    return c,d      #tuple packing
x,y=m1(5,2)         #tuple unpacking
print("sum :",x)
print("difference :",y)


# Function can call another function
def m1():
    print("First function")
def m2():
    print("Second function")
    m1()
m2()


# Important points:
    # all functions in python are "first-class" functions.
    # first-class functions --> can be passed around and manipulated {in a same way like strings integers etc}.
'''in python, following things are possible : '''
    # 1. assign a function to vaiables.
    # 2. pass function as a parameters to another functions.
    # 3. define one function inside another.
    # 4. function can return another function.

# 1. assign a function to vaiables --> "function-ALIASING"
def add():
    print("Hello!")
sum=add     # assigning funct to a variable
sum()
add()


# 2. pass function as a parameters to another functions.
def display(x):
    print("This is display function!")
def message():
    print("Python World!")
display(message())          #function ka parameter -> dusra function
