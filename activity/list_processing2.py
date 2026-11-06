numbers=[int(i) for i in input("enter numbers: ").split()]
index=[int(i) for i in input("enter 2-space separated indices: ").split()]
sub=numbers[index[0]:index[1]+1]
square=[i**2 for i in sub if i%2==0]
print("Sliced list:",sub)
print("Squared list:",square)