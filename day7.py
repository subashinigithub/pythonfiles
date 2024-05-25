a=int(input('enter a no'))
a1=a
b=0
while(a>0):
    r=a%10
    b=(b*10)+r
    a=a//10
print(a1,b)
if(a1==b):
    print('it is a palindrome')
else:
    print('it is not a palindrome')
