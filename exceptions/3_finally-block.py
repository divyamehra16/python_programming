# try --> All statements will not be executed: agr kisi statement pe "exception raise hua" toh "rest statements will not" get executed.
# except --> only executed when Exception is raised in try-block.
# finally --> exception aaye na aaye, exception eith handled or not --> finally-block will execute. "chalega he"!

try:
    num1=int(input("enter a number: "))
    num2=int(input("enter a number: "))
    print(num1/num2)
except (ValueError,ZeroDivisionError) as e:
    print("Unexpected value: the problem is",e)
finally: 
    print(num1+num2)


try:
    print(10/0)
except NameError:
    print("ERROR!")
finally:
    print("Execution Done") 

# Nested try-except-finally blocks:
try:
    print("Outer try")
    try:
        print("Inner Try")
    except:
        print("Inner exception")
    finally:
        print("Inner finally")
except:
    print("Outer exception")
finally:
    print("Outer finally")

try:
    print("Outer try")
    print(10/0)
    try:
        print("Inner Try")
    except:
        print("Inner exception")
    finally:
        print("Inner finally")
except:
    print("Outer exception")
finally:
    print("Outer finally")


try:
    print("Outer try")
    try:
        print("Inner Try")
        print(10/0)
    except:
        print("Inner exception")
    finally:
        print("Inner finally")
except:
    print("Outer exception")
finally:
    print("Outer finally")


try:
    print("Outer try")
    try:
        print("Inner Try")
        print(10/0)
    except NameError:
        print("Inner exception")
    finally:
        print("Inner finally")
except:
    print("Outer exception")
finally:
    print("Outer finally")
