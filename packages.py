def amstrong(b):
    c=0
    while(b>0):
        r=b%10
        c=c+(r*r*r)
        b=b//10
        return c
def factorial(b):
    c=1
    for x in range(1,b+1):
        c*=x
        return c
