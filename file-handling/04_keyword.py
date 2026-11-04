 
# "with" keyword --> to automatically close the file

with open('abc.txt','r+') as fin:
    data=fin.read()         # file-pointer shifted to --> end
    print(data)     
    l1=['python\n','is\n','dynamically typed']
    fin.writelines(l1)


# "tell()" keyword --> return position{index} of file pointer
with open('wish.txt','r') as f:
    print(f.tell())
    print(f.read(2))
    print(f.tell())
    print(f.read(3))
    print(f.tell())


# "seek()" keyword --> move the file pointer

    #seek(<value>,fromWhere)
        # from :  0 --> from begning {default}
                # 1 --> from current
                # 2 --> from end

                
data="Python  language is excellent"
f=open("abc.txt", "w")
f.write(data)
f.close()
with open("abc.txt", "r+") as f:
    print(f.tell())
    text=f.read()
    print(text)
    print("The Current Cursor Position: ",f.tell())
    f.seek(24)
    print("The Current Cursor Position: ",f.tell())
    f.write("Britania Bisket")
    f.seek(0)
    text=f.read()
    print("Data After Modification:")
    print(text)
