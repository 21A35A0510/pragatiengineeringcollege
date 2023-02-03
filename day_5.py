'''
def total(a,b):
    result=a+b
    print('the sum is',result)
def diff(a,b):
    result2=a-b
    print('the difference is',result2)
def prod(a,b):
    result3=a*b
    print('the product is',result3)
def div(a,b):
    result4=a/b
    print('the division is',result4)
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
total(a,b)
diff(a,b)
prod(a,b)
div(a,b)
'''

'''def rj(money):
    print("give ravi the sum of ", money)
money=50
rj(money)

def rj(money):
    print("give ravi the sum of ", money)
rj(5*10)'''

'''var ='ravi'
def show():
    global var1
    var1='good boy'
    print("in function var cis", var)
show()
print("outside fun", var1)
print("var is ", var)'''

'''def outf():
    var=10
    def innf():
        var=20
        print("inner var",var)
    innf()
    print("outer var",var)
outf()'''

#write a program with the user defined function which returns an integer value to the colon

'''def cube(x):
    return(x*x*x)
num=10
result=cube(num)
print("output of the evaluation is", result)'''


#write a program to add 6 user defined numbers and return the value to the main program
#test case1 8,6,4,2,10,0

'''def display(str1):
    print(str1)
str1='Ravi'
display(str1)

def display(name,age):
    print("name", name)
    print("age", age)
n="vj"
y=77
display(name=n, age=y)'''

'''#write a program to print the fibonacci series using recursion by functions till 7
def fib(n):
    if n<2:
        return 1
    return(fib(n-1)+fib(n-2))
n=int(input())
for i in range(n):
    print("fibanocci (",i,")",fib(1))'''
    
'''from time import*
t1=perf_counter()
i=sum=0
while i<1000000:
    sum+=i
    i+=1
sleep(0)
t2=perf_counter()
print('execution time=%f seconds'%(t2-t1))'''

from datetime import*
d=date.today()
print(d)
d=date(2023,2,3)
for x in range(1,10):
    nextdate=d+timedelta(days=x)
    print(nextdate)

'''def hanoi(n,a,b,c):
    if n>0:
        hanoi(n-1,a,b,c)
        if a:
            c.append(a.pop())
        hanoi(n-1,b,z,c)
a=[1,2,3,4]
b=[]
c=[]
print("before puzzle")
print(a,b,c)
hanoi(n,a,b,c)
print("after puzzle")
print(a,b,c)'''