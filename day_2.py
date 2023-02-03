
apple=100
banana=200
pineapple=300
print(apple,end=' ')
print(banana,end=' ')
print(pineapple,end=' ')

print(apple,banana,pineapple)


x,y,z=input("enter the three value:").split('0')
print("total number of students:",x)
print("number of boys:",y)
print("number of girls:",z)


a=int(input("enter the lemons:"))
b=21
if a<b:
    print()

a=5
b=True
if 1==b:
    print("yes")
else:
    print("no")
    


eml="teja26081@gmail.com"
ceml=input("enter the email")
psw=123456
otp=7789
cpsw=int(input("enter the password"))
cotp=int (input("enter the otp:"))
if eml==ceml and psw==cpsw:
    if otp==cotp:
     print("login successful")
    else=print("login failed")


a="raviteja"
print('y'not in a)
print('y' in a)
print(a[3])


for i in range (1,10):
    print(i)
for i in range (1,10):
    print(i,end="*")

for i in range (10,0,-1):
    print(i,end="*")



for i in range (97,123):
    print(chr(i),end=" ")


for i in range (122,96,-1):
    print(chr(i),end=" ")


for i in range (65,91):
    print(chr(i),end=" ")

for i in range (65,91):
    if(i==65 or i==69 or i==73 or i==79 or i==85):
     print(chr(i),end=" ")
for i in range (65,91):
    if(i!=65 and i!=69 and i!=73 and i!=79 and i!=85):
     print(chr(i),end=" ")
    
for i in range (91,65,-1):
    if(i!=65 and i!=69 and i!=73 and i!=79 and i!=85):
     print(chr(i),end=" ")


package=84
data=float(2.0)
calls=3000
msg=100
a=int(input("enter the day:"))
if a<=84:
    b=int(input("enter the calls:"))
    print(
    c=int(input("enter the messages:"))
    d=float(input("enter the data:"))
    print("your plan will expire in",84-a,"days")
else:
    print("your plan expired")

for i in range(1,151):
    if(i%10==0):
        print(i)
        
for i in range(1,30,2):
    print(i*5)
    
for i in range(1,151):
    if(i%10==0):
        print(i)

for i in range(1,30):
    if(i%2==1 and i<=5):
        print(i*5)
        
for i in range(1,30):
    if(i%2==1):
        print(i*5)
        
for i in range(-10,-1,2):
    print(i)
        

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")
   
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")

for i in range(1,11):
    print(i,"*10=",i*10)


i=1
while i<=5:
    j=1
    while j<=i:
        print((i*2-1),end=" ")
        j=j+1
    i=i+1
    print(' ')   
