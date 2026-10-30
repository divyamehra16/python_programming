order=input("enter order of list 'space separated : ").split()

matrix=[]
for i in range(int(order[0])):
    l1=[]
    print("inserting elements in row-",i+1)
    for j in range(int(order[1])):
        x=int(input("enter a matrix element: "))
        l1.append(x)
    matrix.append(l1)
print(matrix)

#row-sum
row_sum=list(map(lambda x:sum(x),matrix))
print(row_sum)

#column-sum
column_sum=[]
for i in range(len(matrix[0])):
    s=0
    for j in range(len(matrix)):
        s+=matrix[j][i]
    column_sum.append(s)
print(column_sum)

#row with max sum
print(row_sum.index(max(row_sum))+1)

#sum of all elements
total_sum=sum(row_sum)
print(total_sum)

