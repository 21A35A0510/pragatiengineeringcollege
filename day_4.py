'''
#0,0,7,6,14,12,21,18,28.....
term=int(input("enter the term:"))
if term%2==0:
    term=term//2
    print(6*(term-1))
else:
    term=term//2+1
    print(7*(term-1))

val=int(input("enter the term:"))
x=0
y=0
for i in range(1,val+1):
    if(i%2!=0):
        x=x+7
    else:
        y=y+6
if(val%2!=0):
    print('{} term in the program is {}'.format(val,x-7))
else:
    print('{} term in the program is {}'.format(val,y-6))
'''
'''


##strings##

#concatination of string
str1="india"
str2=" bharat"
print(str1+str2)


str1="india"
str2=input("enter the name:")
str1 +=str2
print(str1)


#repetetion
str1="india "
print(str1*10)


#index value
text= 'india'
index= 0
for i in text:
    print("text[",index,"]=",i)
    index +=1


#title
text='india is  great'
print(text.title())

#upper=lower
text='India Is  Great'
print(text.swapcase())

#split
text='India Is Great'
print(text.split())

#join
print('-'.join(['India','Is','Great']))

#index
str1='donkey monkey'
print(list(enumerate(str1)))

#uppercase
str="ravi teja"
print(str.upper())

#lowercase
str="RAVI TEJA"
print(str.lower())

str1='66'
print(str1.zfill(4))


#slicing program
str1='indian'
print(str1[1:5])
'''

'''
import string
print(type(string.ascii_letters))

import string
print(type(string.digits))

import string
print(string.digits)
'''

'''import string
print('g' in string.lowercase)
print(string.find(string.lowercase,'g')!=-1)

import string
ch='g'
print('a' <=ch <='z')'''

#directories in string
'''print(dir(str))'''
'''
#match
import re
str1="she sells sea shells at sea shore"
p1="sells"
if re.match(p1,str1):
    print("match found")
else:
    print(p1,"not present in string")

#search
import re
str1="she sells sea shells at sea shore"
p1="sells"
if re.search(p1,str1):
    print("match found")
else:
    print(p1,"not present in string")
 
#replace
import re
str1="she sells sea shells at sea shore"
p1="sea"
rep='ocean'
ns=re.sub(p1,rep,str1,1)
print(ns)
'''

'''
import re
p=r"[aeiou]"
if re.search(p," clue"):
    print("matchy vowel")
else:
    print("there is no vowel")
'''
#write a program to check whether the given input is satisfying the condtion of analgram
#test case 1
#input s1-listen s2-silent
#output true
    
#test case 2
#input s1-race s2-acer
#output true
'''
from collections import Counter
def check(str1,str2):
    if(Counter(str1)==Counter(str2)):
        print("true")
    else:
        print("not")
str1='silent'
str2='listen'
check(str1,str2)

#0,0,2,1,4,2,6,3,8,4
n= int(input('enter the number:'))
a=b=0
for i in range(1,n+1):
    if(i%2!=0):
        a=a+2
    else:
        b=b+1
if(n%2!=0):
    print('{}'.format(a-2))
else:
    print('{}'.format(b-1))
'''

size=int(input("enter the size of bin"))
max=count=flag=0
x=input()
arr=list(x)
for i in range(0,size):
    if arr[i]=='1':
        count=count+1
        flag=1
    elif(arr[i]=='0' and flag==1):
        count=0
        flag=0
        if count>max:
            max=count
print(max)

