import os
if os.path.isfile("system.log"):
    with open("system.log") as fout:
        data=fout.readlines()
        lcount,ecount=0,0
        str1=""
        for i in data:
            lcount+=1
            if i.startswith("ERROR"):
                ecount+=1
                str1+=i
    print(f"Total lines: {lcount}",f"Error lines: {ecount}",str1,sep='\n')

else:
    with open("system.log","w") as f1:
        n=int(input("enter a number: "))
        for i in range(n):
            line1=input("enter your content: ")
            f1.write(line1+'\n')
