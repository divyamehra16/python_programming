
# Tuple-comprehension  -->  same as list-comprehension just difference in parenthesis().

t=(x**2 for x in range(1,6))
print(type(t))
for x in t:
    print(x)

