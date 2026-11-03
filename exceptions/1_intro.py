# errors --> which is wrong.
# exceptions --> something which is not wrong but also not expected.

# types of errors:
    #1. Compile-time Error
    #2. Run-time Error --> "EXCEPTION"
            # End-User Input
            # Programming Logic
            # Memory Problems
    #3. Logical Error

# ABNORMAL Execution ko Normally execute krwana! --> EXCEPTION HANDLING

#Normal flow:
print("one")
print("two")
print("three")
print("four")
print("five")

#Abnormal Flow:
print("one")
print("two")
'''print(3/0)'''      #ZeroDivision Error
print("four")
print("five")

# Every exception is an "object" to it's "class".

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
