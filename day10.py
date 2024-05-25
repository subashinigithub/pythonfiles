'''i=int(input('enter a no'))
b=1
for x in range(1,i):
    b*=x
    print(b)

a=153
b=0
for x in str(a):
    r=a%10
    b=b+(r*r*r)
    a=a//10
    print(b)
    
a=12
b=a*a
#basic function
def my_function():
    print("hello world")
    print("hi everyone")
    print("welcome to all")
my_function()
my_function()
#two parameter
def harry(fname,lname):
    print(fname+""+lname)
a=input('enter a no')
b=input('enter a no')
harry(a,b)
def my_function(child3,child2,child1):
    print('the youngest child is'+child3)
my_function(child1='email',child2='java',child3='python')
my_function('c#','html','css')
def my_function(**kid):
    print('his last name is',kid['fname'],kid['lname'])
my_function(fname='tobias',lname='refsnes')
def my_function(*kids):
    print('the youngest child is:'+kids[2])
my_function('email','tobias','linux')'''

a=int(input('enter a no'))
a1=a
b=a*a
print(b)
c=0
for x in str(b):
    r=b%10
    c=(c*10)+r
    b=b//10
    print(c)
c1=0
for x in str(a1):
    r=a1%10
    c1=(c1*10)+r
    a1=a1//10
    print(c1)
    d=c1*c1
    print(d)



