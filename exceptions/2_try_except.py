
# Handling exceptions --> "try-except" statements.
print("one")
print("two")
print("three")
try:
    print(5/0)
except ZeroDivisionError as e:
    print("Exception information:",e)
print("four")
print("five")


# multiple exceptions are there but program has only one {*marne ke bahut tareeke hai lekin marenge ek he tareeke se*}
# one "try" - multiple "except"
try:
    num1=int(input("enter a number: "))
    num2=int(input("enter a number: "))
    print(num1/num2)
except (ValueError,ZeroDivisionError) as e:         # handling multiple-exceptions in Single Line.
    print("Unexpected value: the problem is",e)

"""except ZeroDivisionError:            # Multiple Except-blocks
    print("Division with 0 Not-Possible")
except ValueError:
    print("Unexpected value: enter number only")
"""


# default expect block should be at the last only
try:
    num1=int(input("enter a number: "))
    num2=int(input("enter a number: "))
    print(num1/num2)
except ZeroDivisionError as e:
    print("Unexpected value: the problem is",e)
except:
    print("exception raised! enter valid input")

# try --> All statements will not be executed: agr kisi statement pe "exception raise hua" toh "rest statements will not" get executed.
# except --> only executed when Exception is raised in try-block.