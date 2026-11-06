
numbers=[int(x) for x in input("enter space separated numbers: ").split()]
cubes=[ i**3 for i in numbers if i%2!=0]
l2=list(filter(lambda x: x>=30,numbers))
print("Cubes of odd numbers:",cubes)
print("greater than 30:",l2)
