    #15th September 2026

#revision --> string-methods
#split()
s1="python is a programming language, it is every easy"
s2="raju is my friend vimal is my friend tanu is my friend"
l1=s2.split("is my friend")
print(l1)
print(type(l1))
for word in l1:
    print(word)

#join()
l1=['xyz','abc','mno']
s1=";".join(l1)
print(s1)

# method dont perform changes on memory, it perform changes on the value.
# upper lower capitalize title swapcase
s1="python PROGramming"
print(s1,id(s1))
s1.upper()
print(s1,id(s1))
s2=s1.upper()
print(s2,id(s2))

s1="python 07"
print(s1.isalnum())
s1="python07"
print(s1.isalnum())
a='128'
print(a.isdigit())
print(a.isdecimal())


a=eval(input('enter'))
b=input('enter')
c=eval(b)
print(a)
val=b if b.isalpha() else eval(b)
print(val,type(val))

#string-interpultion
name='xyz'
place='noida'
age='18'

s1="{} lives in {} and his age is {}".format(name,place,age)
print(s1)
s1="{2} lives in {0} and his age is {1}".format(place,age,name)
print(s1)
s1="{n} lives in {p} and his age is {a}".format(p=place,a=age,n=name)
print(s1)

#now shortcut ;  f-string
s1=f"{name} lives in {place} and his age is {age}"
print(s1)

ms=f'''Dear {name},
come visit {place} on your {age}th birthday.'''
print(ms)
