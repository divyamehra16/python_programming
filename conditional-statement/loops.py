# for & while loops
'''
for --> with sequence
while --> condition
'''
# while-else & for-else
# --> 'else' chalega => when loop executed completely i.e. statement becomes false i.e. loop beech mei "break" nhi hua

x=[10,20,3,40,50]
for i in x:
    print(i)

y=2
for i in x:
    print(i+y)

c=5
while c:
    print('helloo')
    if c>0:
        c-=1
    if c<0:
        break
else:
    print('hii')

item=[10,20,30]
sum=0
for i in item:
    sum+=i
print(sum)


#wap to input a number and print the sum of digits

num1=input('enter a number ; ')
sum=0
for i in num1:
    sum+=int(i)
print(sum)