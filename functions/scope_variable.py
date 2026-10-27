# Lifetime --> duration between the variable memory allocation(creation) and variable memory de-allocation(destruction) performed by PVM.
# Scope --> duration where the variable is accessible.
            # LEGB --> Local, Enclosing, Global, Built-in.

# in python both scope and lifetime is same -> agr variable allocated hai memory mei toh vo accessible bhi hai.
# if variable is OUT of SCOPE --> "NameError"
 
def m():
    a=11
    print(a)
def n():
    print(a)    # NameError
m()
n()


a=11
b=12
def m():
    print("a from function m()",a)
    print("b from function m()",b)
def n():
    print("a from function n()",a)
    print("b from function n()",b)
m()
n()

# global KEYWORD;
a=11
def m():
    a=20
    print("a from function m(): ",a)
def n():
    print("a from function n(): ",a)
m()
n()

a=11
def m():
    global a
    a=30
    print("a from function m(): ",a)
def n():
    print("a from function n(): ",a)
m()
n()

# globals() --> built-in function
# returns a dictionary of all the global variables.
a=10
def m():
    a=2
    print(a)
    print(globals()["a"])
m() 


# Recurssive Function --> if-else statement 

# if- talks about stopping condition , else- contain recursive function.

def print_data(x):
    if x==11:       # define the stopping condition first.
        print("done")
    else:
        print(x)
        print_data(x+1)
print_data(1)
# Recursive function -- LIFO structure --> STACK is created for memory.
# calling ke pehle print --> forward tracking
# calling ke baad print --> backward tracking

def print_data(x):
    if x==11:
        print("completed")
    else:
        print_data(x+1)
        print(x)

print_data(1)

#factorial using recurssive function:
def factorial(n):

    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))


def power(x,y):
    if y==0:
        return 1
    else:
        return x*power(x,y-1)
print(power(2,3))
