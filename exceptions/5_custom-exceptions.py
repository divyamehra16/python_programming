
# custom exceptions --> "user-raised" exceptions
try:
    num=int(input("enter positive number: "))
    if num<0:
        raise ValueError       
except ValueError as e:
    print(f"You provided {e}. please provide valid positive number")

# raise --> keyword to forcefully raise an exception according to your program