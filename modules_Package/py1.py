import package.module as module
print(module.x)
module.add(12,15)
module.sub(5,2)


#alias
import package.module as gla
print(gla.x)
gla.add(12,15)
gla.sub(5,2)



#directing calling a function from the module *directly*
from package.module import x,add,sub
# can use "*" for importing everthing 
print(x)
add(12,15)
sub(5,2)


#can change the function name --> nickname {aliasing function-name}
from package.module import x as y,add as sum,sub as substract
x=27
print(y)
sum(25,14)
substract(25,5)

# reload() --> in cooprate --> changes in module --> reload(<module-name>)

print(dir(module))  #--> only displays whatever is in the module
print(dir())

# reflexion --> dir() --> gives the list of everything present inside the module
x=10
y=20
def f1():
    print('hello!')
print(dir())