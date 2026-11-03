# else-block --> when an "exception" is raised only then else-block will be "executed".
try:
    print("Outer try")
    try:
        print("Inner Try")
    except NameError:
        print("Inner exception")
    finally:
        print("Inner finally")
except:
    print("Outer exception")
else:
    print("else block")
finally:
    print("Outer finally")

# try {with exceptions} -> except -> finally
# try {with no-exceptions} -> else -> finally
