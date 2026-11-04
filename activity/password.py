n=int(input("enter a number: "))
upper,lower,digit,special,nosp,length=(0,0,0,0,1,0)
for i in range(n):
    password=input("enter your password: ")
    for j in password:
        if len(password)>=8:
            length=1
        if j.isalpha():
            if j.isupper():
                upper+=1
            else:
                lower+=1
        elif j.isdigit():
            digit+=1
        elif j in ["!","@","#","$","%","^","&","*"]:
            special+=1
        elif j.isspace():
            nosp=0
    l1=list(map(lambda x: 1 if x>0 else 0,[upper,lower,digit,special,nosp,length]))
    print(l1)
    print(f"{password} - {sum(l1)}/6")
