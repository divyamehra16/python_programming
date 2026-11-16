# to exit a from a program --> sys.exit(0)

# os--> module name; 
#path --> submodule of os;

import os,sys
fname=input("enter file name: ")
if os.path.isfile(fname):
    print("File exist:",fname)
    f=open(fname,"r")
else:
    print("File doest not exist:",fname)
    sys.exit(0)         # 0--> normal termination,   1--> abnormal termination
print("the conent of the file is:")
print(f.read())


# {for i in fobject} automatic --> f.readline()

#without use of sys module
import os
fname=input("enter file name: ")
if os.path.isfile(fname):
    print("File exist")
    f=open(fname,"r")
    lcount=wcount=ccount=0
    for line in f:
        lcount+=1
        ccount+=len(line)
        wcount+=len(line.split())
    print("Number of lines in a file :",lcount)
    print("Number of words in a file :",wcount)
    print("Number of characters in a file :",ccount)
else:
    print("File does not exist")


# standard module --> bina kuch download krke use krr rahe ho --> eg: sys functools
# external module --> panda, numpy
