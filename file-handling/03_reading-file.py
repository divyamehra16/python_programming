# read()--> returns a string of entire content 
# read(n) --> returns a string of n-characters of content  "1 character == 2 bytes"
# readline() --> single line in a list
# readlines() --> entire content in a list

f=open('abc.txt','r')
data=f.read()
print(data)
f.close()

f=open('abc.txt','r')
data=f.read(10)
print(data)
f.close()

f=open('abc.txt','r')
data=f.readline(10)
print(data)
f.close()

f=open('abc.txt','r')
data=f.readlines()          # list of entire content
print(data)
f.close()
