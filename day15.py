from new.adam import *



i=int(input('enter the no: '))
if(i%2==0):
    print('This is the even no')
else:
    b=i*2
    print(b)
    print(square(reverse(b)))
    print(reverse(square(b)))
    if(square(reverse(b))==reverse(square(b))):
        print('This is an adam no')
    else:
        print('This is not an adam no')
        
