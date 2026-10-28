""" # SUM of Digits -- using recurssion
 
# using string;
def sod(n):
    sum=0
    if n=='':
        return 0
    else:
        sum+=int(n[0])+sod(n[1:])
        print(sum)
    return sum
print(sod(input("enter a number : ")))

#using an integer;
def sumofdigit(n):
    if n==0:
        return 0
    else:
        print(n)
        return n%10 + sumofdigit(n//10)
print(sumofdigit(int(input("enter a number: "))))


#reversing a string --> recurssion 
def reverse(x,y=''):
    if x=='':
        return ''
    else:
        y=x[-1]         #y+=x[-1]
        print(y,x)      #x=x[0:-1]
        return y+reverse(x[0:-1],y)     #return reverse(x,y)
    
print(reverse("python programming"))
"""

def sumofdigit(number,sum):
    if number==0:
        return sum
    else:
        sum+=number%10
        number=number//10
        return sumofdigit(number,sum)
print(sumofdigit(12345,0))
