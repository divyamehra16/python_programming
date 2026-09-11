#optimization -->memory efficient and time & space efficient.
#flowchart algorithm 

'''1. Write a python code to remove characters having odd index in strings.'''
 
str1=input('enter a string ; ')
str2=""
for i in str1.split(' '):
    str2+=i[::2]+' '
print(str2.strip())



'''2. WAP to count occurances of a substring in a string.'''

a=input('enter a string ; ')
b=input('enter a sub-string ; ')
print(a.count(b))



'''3. WAP to count each character in a string having more than 1 occurance'''
#1. enter the string 
#2. create a substring
#3. loop through every character
    #a. check- character count > 1 and should not be in the substring
    #b. concat it in the substring
    #c.; print substring

str1=input('enter a string ; ')
sub=''
for i in str1:
    if str1.count(i)>1:
        if i not in sub:
            sub+=f"{i}{str1.count(i)}"
print(sub.strip())



'''4. problem statement - given a string consisting of * and # count the occurances of both and based on their count print integer and a proper statement'''

s=input('enter string consisting of * and # only ; ')
s1=s.count('#')
s2=s.count('*')
if s1>s2:
    print('-1 number of # is greater than *')
if s2>s1:
    print('1 : number of * greater than #')
if s1==s2:
    print('0 number of * and # are equal')


    
'''WAP that takes a string as input and extract all charcters at even position(0,2,4...) and odd position (1,3,5...) separately using a slicing. and display'''

str1=input('enter a string ; ')
print('even index characters : ',str1[::2])
print('odd index charaters : ',str1[1::2])
