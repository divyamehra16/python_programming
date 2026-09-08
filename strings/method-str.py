#1. len() --> function

#2. lstrip() & rstrip()  & <string>.strip()--> removing extra spaces
""" 
a=" python  "
print(len(a))
print(len(a.rstrip()))
print(len(a.lstrip()))
print(len(a.rstrip().lstrip()))   #nexted / chaing of methods
print(len(a.strip()))
"""


#3. find() & rfind()  --> search a substring and return its "index"  {r == reverse} --><str>.find(<sub>,<index>)
""" 
s1="Python is a programming language. Python is easy to learn"
print(s1.find("Python"))
print(s1.find("Python",5))
print(s1.find("zython"))         #return (-1) if substr *not found*

print(s1.rfind("Python"))
print(s1.rfind("Python",35))     # searches from right to left
"""


#4. index() & rindex() --> search a substring and return its "index"  --><str>.index(<substr>)
"""
s1="Python is a programming language. Python is easy to learn"
print(s1.index("Python"))
print(s1.index("Python",5))
print(s1.index("zython"))     #return (ValueError) if substr *not found* 
"""


#5. count() --> number of "occurances" of substr in a string  --> <str>.count(<substr>)
""" 
s1="python is a programming language python is easy to learn python is object oriented"
s2=s1.count('python')
print(s2)
for i in s1:          
    print("count for",i,s1.count(i))

for i in s1:          
    print(i,s1.count(i) if s1.count(i)>10 else None) """


#6. split() --> {delimiter *object which we are using to split*}  -->  <str>.split(<delimiter>)
""" 
s1="Rajesh Suresh Rakesh Ramesh"       #by-default delimiter == space " "          
s2="Rajesh,Suresh,Rakesh"    
s3=s1.split()       
print(s1,type(s1))
print(s2.split(','))
print(s3,type(s3))

for i in s3:
    print(i,s1.count(i)) """
""" 
dob=input('enter dob (dd/mm/yyyy)')
year=dob.split('/')[2]
print(year)
year=dob[dob.rfind('/')+1:]
print(year)
"""


#7. join()  --> joining list elements in a string  --> <delimiter.join(<list>)
""" 
l1=['33','22','11']
s1='/'.join(l1)
print(s1)
s1=' '.join(l1)
print(s1,type(s1))
print(l1,type(l1)) """


#8. Other methods --> {For cases} --> <str>.upper(), <str>.lower(), <str>.swapcase(), <str>.title(), <str>.capitalize()
"""
a="pYtHON is A proGRammINg LanGUAGe"
print(a.upper())
print(a.lower())
print(a.swapcase())
print(a.title())
print(a.capitalize())
"""

# checking --> <str>.isupper(), <str>.islower(), <str>.isalpha(), <str>.isdigit(), <str>.isalnum(), <str>.isdecimal(), <str>.istitle() ;
""" 
a=input('enter ; ')
b=eval(a)
print(b,type(b))
print(b.isdigit())                 #only applicable for string
"""

#9. format() --> *PLACEHOLDERS   -->*String Interpulation*
# value , number, nickname
name="xyz"
age=12
place='noida'
str1="{} is {} years old and lives in {}".format(name,age,place)
print(str1)
str1="{} is {} years old and lives in {}".format(place,name,age)             #value assigned on the basis of sequence
print(str1)
str1="{1} is {2} years old and lives in {0}".format(place,name,age)          #indexing type-stuff
print(str1)
str1="{n} is {a} years old and lives in {p}".format(p=place,n=name,a=age)    #nickname
print(str1)

#f-strings
str1=f"{name} is {age} years old and lives in {place}"          #shortcut way
print(str1)
link="https://google.com"
print(f"Hi this is the {link}")
