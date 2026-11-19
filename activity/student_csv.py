
import csv

with open("Student.csv","w",newline='') as fin:
    writer=csv.writer(fin,delimiter=',')
    n=int(input("enter a number: "))
    for i in range(n):
        name=input("enter name of student: ")
        marks=input("enter marks of student: ")
        writer.writerow([name,marks])

with open("Student.csv",'r',newline='') as fout:
    reader=csv.reader(fout)
    marks=0
    c=0
    for i in reader:
        try:
            if 0<=int(i[1])<=100:
                marks+=int(i[1])
                c+=1
            else:
                raise TypeError
        except (TypeError,ValueError):
            print(f"Invalid record for {i[0]}")
    if marks:
        print("Average marks:","%.2f"%(marks/c))
    else:
        print("No valid records")
