#amstrong
'''a=153
a1=a
b=0
while(a>0):
    r=a%10
    print(r)
    b=b+(r*r*r)
    a=a//10
    print(a)
print(b)
if(a1==b):
    print('it is a amstrong no')
else:
    print('it is not a amstrong no')
#adam no
a=int(input('enter a no'))
a1=a
b=a*a
print(b)
c=0
while(b>0):
    r=b%10
    c=(c*10)+r
    b=b//10
print(c)
c1=0
while(a1>0):
    r=a1%10
    c1=(c1*10)+r
    a1=a1//10
print(c1)
d=c1*c1
print(d)
if(c==d):
    print('it is a adam no')
else:
    print('it is no adam no')
#fact
i=int(input('enter a no'))
b=1
while(i>0):
    b=b*i
    i-=1
print(b)'''
i=int(input('enter a no'))
x=1
y=1
while(i>0):
    z=x+y
    x=y
    y=z
    i-=1
    print(z)



