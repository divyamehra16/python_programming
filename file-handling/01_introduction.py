# Text files --> contain text
# Binary files --> donot contain text eg: video img

# modes --> w,r,a,w+,r+,a+,x
# x --> exclusive mode --> no-overwriting
#FileNotFoundError --> OS error


# opening a file --> "<fileObject> = open(<fileName>,<mode>)"
# closing a file --> "<fileObjct>.close()"

# <fileObject>.name() --> "name of file opened"
# <fileObject>.mode --> "return the mode in which file is opened"

# <fileObject>.closed --> "return T/F whethr file is closed"
# <fileObject>.readable() --> "T/F"
# <fileObject>.writable() --> "T/F"

""" f=open("abc.txt", 'w')
print("File Name: ", f.name)
print("File Mode: ", f.mode)
print("Is File Readable: ", f.readable())
print("Is File Writable: ", f.writable())
print("Is File Closed : ", f.closed)
f.close()
print("Is File Closed : ", f.closed)
 """
# file saved --> EOF character at the end is must! 
# if not than EOFError

""" f=open('wish.txt','w')
f.write("Welcome\n")
f.write("to\n")
f.write("Python World!\n")
print("Data is written successfully!")
f.close()
 """

f=open('wish.txt','a')
f.write("Welcome\n")
f.write("to\n")
f.write("Python World!\n")
print("Data is written successfully!")
f.close()
