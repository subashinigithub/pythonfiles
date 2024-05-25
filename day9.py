'''for x in range(20):
    print('we re on time', x)
for x in range(20):
    if x==2:
        break
    print(x)
for x in range(3):
    print(x)
    if(x==1):
        break
    else:
        print('loop ended')
string='hello world'
for x in string:
    print(x)
collection=['hey', 5, 'd']
for x in collection:
    print(x)
a=int(input('enter a no'))
b=int(input('enter a no'))
n=int(input('enter a no'))
if(n==1):
    print(a+b)
elif(n==2):
    print(a-b)
elif(n==3):
    print(a*b)
elif(n==4):
    print(a/b)
elif(n==5):
    print(a%b)
else:
    print('not valid')
#calculator prgm

n=int(input('enter a no'))
if(n==1):
    print('amstrong no')
    a=int(input('enter a no'))
    b=0
    while(a>0):
        r=a%10
        b=b+(r*r*r)
        a=a//10
        print(b)
elif(n==2):
    print('adam no')
    a=int(input('enter a no'))
    b=0
    while(a>0):
        r=a%10
        b=(b*10)+r
        a=a//10
        print(b)
elif(n==3):
    print('factorial no')
    i=int(input('enter a no'))
    b=1
    while(i>0):
        b=b*i
        i-=1
        print(b)
elif(n==4):
    print('fibo no')
    i=int(input('enter a no'))
    x=1
    y=1
    while(i>0):
        z=x+y
        x=y
        y=z
        i-=1
        print(z)
else:
    print('not valid')
lists=[[1,2,3],[4,5,6],[7,8,9]]
for l in lists:
    print(l)
for x in l:
    print(x)
fruits=['apple','banana','cherry']
for x in fruits:
    if x=='banana':
        continue
    print(x)
for x in range(2,30, 5):
    print(x)'''
for x in range(7):
    pass
    
