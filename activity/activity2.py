
# 1. WAP that takes string and two indices as input then extracts the substring reverse it and displays the result. *use only slicing*
""" 
str1=input('enter a string ; ')
s=int(input('enter start index ; '))
e=int(input('enter end index ; '))
sub=str1[s:e:]
print('ORIGINAL STRING:',str1)
print('Substring:',sub)
print('REVERSED Substring:',sub[::-1])
"""


# 2. PALINDROME string checker using slicing;

a=input('enter a string ; ')
print('Original:',a)
print('Reversed:',a[::-1])
if a==a[::-1]:
    print('The string is Palindrome')
else:
    print('The string is not Palindrone')
#print("palindrone") if a==a[::-1] else print('Not Palindrone')   {--> shorten-way}



# 3. WAP

str1=input('enter a string ; ')
print("First 3:",str1[0:3])
print("Last 3:",str1[-3::])
print("From 2 to 7:",str1[2:8])
print("Every 2nd character:",str1[::2])
print("Reversed string:",str1[::-1])



#domain-extractor using silincing and find() or index()

a=input('enter email *with @ as well ; ')
n=a.index('@')
print('Username:',a[:n])
print('Domain:',a[n+1:])
