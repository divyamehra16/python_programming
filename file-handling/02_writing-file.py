# <fileObject>.write() --> write a single line
 
f=open('wish.txt','w')
f.write("Welcome\n")
f.write("to\n")
f.write("Python World!\n")
print("Data is written successfully!")
f.close()


# <fileObject>.writelines() --> write multiple lines

f=open('wish.txt','w+')
f.writelines(['Welcome\n','to\n','Python World!\n'])
f.writelines(['hello\n','dear\n','Python World!\n'])
print("written successfully!")
f.close()