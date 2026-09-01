#1. len() --> function

#2. lstrip() & rstrip()  & <string>.strip()--> removing extra spaces
a=" python  "
print(len(a))
print(len(a.rstrip()))
print(len(a.lstrip()))
print(len(a.rstrip().lstrip()))   #nexted / chaing of methods
print(len(a.strip()))
