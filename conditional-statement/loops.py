# for & while loops
'''
for --> with sequence
while --> condition
'''
# while-else & for-else
# --> 'else' chalega => when loop executed completely i.e. statement becomes false i.e. loop beech mei "break" nhi hua
#use to check the loop-COMPLETENESS


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


#break - to terminate the loop

a=int(input())
for i in range(1,a):
    if i%2==0:
        print('Not Prime')
        break


#pass - used to write the EMPTY-CODE

for i in range(10):
    if i==3 or i==5:
        pass
    else:
        print('hii')


#continue - to SKIP the next part of iteration

for i in range(10):
    if i%2==0:
        continue
    else:
        print('hello')





#wap to input a number and print the sum of digits

num1=input('enter a number ; ')
sum=0
for i in num1:
    sum+=int(i)
print(sum)