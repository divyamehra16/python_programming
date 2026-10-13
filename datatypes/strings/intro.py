#Strings in Python

str1="Rajeev's Dairy"
str2='Rajeev said, "he has a dairy"'
print(str1)
print(str2)

str3=''             #Empty string == False
print(str3,bool(str3))
a=str3+2+3         #error - TypeError
b=bool(str3)+2+3  
print(b)
print(a)


#SLICING and INDEXING


#positive index == [0] to [len(<str>)-1]
#negative index == [-len(<str>)] to [-1]


a="python"
#positive index access;
print("positive index access")
for i in range(len(a)):
    print(a[i])

#negative index access;
print("negative index access")
for i in range(-len(a),0):
    print(a[i])


#str_name[star:stop:step]
str1="python programming"
print(str1[::])
print(str1[2:6:2])
print(str1[5::-1])
print(str1[-11::])
print(str1[-11:0:-1])
print(str1[0:-11])


#string is *IMMUTABLE*
a='python'
print(a,type(a))
a[0]='d'      #TypeError

#operation in string

#concatenation - {addition+}
#multiplication

a='python'
b='programming'
c=2
print("CONCATENATION",a+b,b+a)
print("MULTIPLICATION",a*c,c*a)
print(b*1.5)  #TypeError -  


#membership operator --> to check substring in a string 

a="python programming"
print('p' in a)
print('p' not in a)


#comparisons 

a='abcd'
b='efgh'
c='abcd'
if a==b:
    print('both Same')
else:
    print('different')
print('check a==c;',a==c)

#another way
output=print('same') if a==b else print('not same')
str1='same' if a==b else 'not same'
print(str1)

