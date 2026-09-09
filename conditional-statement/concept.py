#GRADING-System
 
s1=float(input('enter marks of student in ENGLISH out of 100 ; '))
s2=float(input('enter marks of student in HINDI out of 100 ; '))
s3=float(input('enter marks of student in MATHS out of 100 ; '))
s4=float(input('enter marks of student in SCIENCE out of 100 ; '))
s5=float(input('enter marks of student in GEOGRAPHY out of 100 ; '))
s6=float(input('enter marks of student in HISTORY out of 100 ; '))
st=((s1+s2+s3+s4+s5+s6)/600)*100
if st>=90 and st<=100:
    print('Grade :  A+')
    print('Student has PASSED')
elif st>=80 and st<=89:
    print('Grade :  A')
    print('Student has PASSED')
elif st>=70 and st<=79:
    print('Grade :  B+')
    print('Student has PASSED')
elif st>=60 and st<=69:
    print('Grade :  B')
    print('Student has PASSED')
elif st>=45 and st<=59:
    print('Grade :  C')
    print('Student has PASSED')
elif st>=33 and st<=44:
    print('Grade :  D')
    print('Student has PASSED')
else:
    print('Student has FAILED')

"""CONCEPT"""

# ("%.2f%value")== float upto 2 decimalswith a round-off

# SIMILARLY %d==decimal --> no round-off in any case

# and %s==string 

# and %c==character code --> take the integer {as a character-code} and convert it to corresponding character

val=8.764
val2=8.7815

print("%.2f"%val)
print("%.2f"%val2)

print("%.2d"%val)
print("%d"%val2)

str1="Python Programming"
print("%2s"%str1)
print("%.2s"%str1)

int1=65
print("%c"%int1)
