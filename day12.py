'''def square(a):
    a=3
    n=a*a
    return n
def reverse(a):
    b=0
    while(a>0):
        r=a%10
        b=(b*10)+r
        a=a//10
    return b
def amstrong():
    a=153
    b=0
    while(a>0):
        r=a%10
        b=b+(r*r*r)
        a=a//10
    return b
def check(a,b):
    if(a==b):
        print('yes, correct')
    else:
        print('oops!!!!!! no')
def factorial():
    i=int(input('enter a no'))
    b=1
    for x in range(1,i+1):
        b*=x
    return b
def palindrome():
    a=input('enter a string: ')
    b=(a[::-1])
    print(b)
i=int(input('enter the no: '))
if(i==1):
    print('it is a adam no: ')
    a=int(input('enter a no:'))
    check(square(reverse()),reverse(square()))
elif(i==2):
    print('it is a palindrome function')
    n=int(input('enter a no:'))
    if(n==1):
       
        print('it is a string palindrome: ',palindrome())
    else:
        a=int(input("Enter the input : "))
        print('it is a int palindrome:',reverse(a))
elif(i==3):
    print('it is amstrong no: ',amstrong())
elif(i==4):
    print('it is factorial no: ',factorial())
else:
    print('it is not valid!!!!!')'''
text='Subashini'
print(text[-4:3:-1])
    
    
    
    
    
