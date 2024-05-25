import modulesworkout
c=1
while(c==1):
    a=int(input('enter the no:'))
    b=int(input('enter the no:'))
    n=int(input('enter the no:'))
    if(n==1):
        print(modulesworkout.add(a,b))
    elif(n==2):
        print(modulesworkout.sub(a,b))
    elif(n==3):
         print(modulesworkout.mul(a,b))
    elif(n==4):
        print(modulesworkout.div(a,b))
    elif(n==5):
        print(modulesworkout.mod(a,b))
    elif(n==6):
        print(modulesworkout.exp(a,b))
    elif(n==7):
        print(modulesworkout.flordiv(a,b))
    else:
        print('The no is not valid')
    c=int(input('enter the no: '))
