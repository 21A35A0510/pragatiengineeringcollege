'''
#swapping
a=10
b=20
print("before swap")
print("a=",a)
print("b=",b)
a=a+b
b=a-b
a=a-b
print("after swap")
print("a=",a)
print("b=",b)


a=10
b=20
a=a*b
b=a/b
a=a/b
print(a,b)

#circumflex
a=10
b=20
a=a^b
b=a^b
a=a^b
print(a,b)

#lists
num=[1,2,3,4,5,6,7,8,9,10]
print(num)
print("first element in list",num[0])
print(num[2:5])#slice
print(num[::2])
print(num[1::3])
del num[2:4]
print(num)


num=[1,'a',"abc",[2,3,4],5.6]
print(num[3][0])


num=[100,100.1,99,99.1]
print(max(num))
print(min(num))


num=[1,2,3,4,5,6,7,8,9,10]
print(sum(num))


n=int(input("enter n value:"))
i=1
s=0
while i<=n:
    s=s+i
    i+=1
print(s)


num=[6,3,7,0,1,2,4,9]
num.remove(0)
print(num)


num=[6,3,7,0,1,2,4,9]
print(num.reverse())



sum=0
n=int(input())
while(n!=0):
    r=n%10
sum+=(r*r*r)/(pow(r,3))
n=n//10
if(sum==num):
    print('armstrong number')
else:
    print('not an armstrong number')
 

#write a python program to make a list of queues till the value 10
    #test case 1
    #n=10
    #input[0,1,8,27,.......,1000]
#method1
cubes=[]
for i in range(11):
    cubes.append(i**3)
print(cubes)

#method2
cubes=[i**3 for i in range(11)]
print(cubes)

#method3
print([i**3for i in range(11)])

#write a python program to find the absolute value of the difference between even and odd
#test case 1
#1=1223
#2=4567
#3=123456789

num=[int(d) for d in str(input("enter the number:"))]
even,odd=0,0
for i in range(0,len(num)):
    if i%2==0:
        even=even + num[i]
    else:
        odd=odd+num[i]
print(abs(odd-even))
'''

term=int(input("enter the term:"))
if term%2==0:
    term=term//2
    print(3**(term-1))
else:
    term=term//2+1
    print(2**(term-1))