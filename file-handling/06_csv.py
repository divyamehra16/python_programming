
# newline --> for reading or writing any extra lines in a csv file
import csv
with open("emp.csv","w",newline='') as f:
    w=csv.writer(f)
    w.writerow(['EMP No','EMP Name','EMP Salary','EMP Addr'])
    n=int(input("enter number of employees: "))
    for i in range(n):
        eno=input("enter a emp number: ")
        ename=input("enter emp name: ")
        esal=int(input("enter emp salary: "))
        eadd=input("enter emp address: ")
        w.writerow([eno,ename,esal,eadd])
print("content entered successfully!")


#reading a csv file 
import csv
with open("emp.csv","r",newline='') as f:
    r=csv.reader(f)
    for row in r:
        print("\t".join(row))
