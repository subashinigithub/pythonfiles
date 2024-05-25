'''def my_function(country='norwary'):
    print('I am from:' + country)
my_function('sweden')
my_function('india')
my_function()
my_function('brazil')

def my_function(food):
    for x in food:
        print(x)
fruits=['apple','banana','cherry']
hat=['a','b','c','d']
my_function(fruits)
my_function(hat)
my_function('javaliteusing')


def square(a):
    n=a*a
    return n

def reverse(a):
    b=0
    while(a>0):
        r=a%10
        b=(b*10)+r
        a=a//10
    return b
def check(a,b):
    if(a==b):
        print("yes, correct")
    else:
        print("oops!!!!!!! no")

a=int(input("Enter the value : "))
squ=square(a)
first=reverse(squ)

rev=reverse(a)
second=square(rev)
print(first,second)
if(first==second):
    pass
else:
    pass

a=int(input('Enter the value:'))
if(square(reverse(a))==reverse(square(a))):
          print('it is a adam no')
a=int(input('enter the value:'))      
check(square(reverse(a)),reverse(square(a)))'''

data=[10,20,30,40,50]
print(data[1::2])
    

    
    


