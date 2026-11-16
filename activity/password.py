
n=int(input("enter a number: "))

for i in range(n):
    upper,lower,digit,special,nosp,length=0,0,0,0,1,0
    password=input("enter your password: ")
    if len(password)>=8:
        length=1

    for j in password:
        if j.isalpha():
            if j.isupper():
                upper=1
            else:
                lower=1
        elif j.isdigit():
            digit=1
        elif j in ["!","@","#","$","%","^","&","*"]:
            special=1
        elif j.isspace():
            nosp=0

    l1=[upper,lower,digit,special,nosp,length]
    if sum(l1)==6:
        print(f"{password}: Strong {sum(l1)}/6")
    else:
        print(f"{password}: Weak {sum(l1)}/6")
