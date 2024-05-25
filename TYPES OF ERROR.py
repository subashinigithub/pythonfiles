'''x=10
if x==10
print(x)
#name error
print(x)
x="100"
y=5
z=y+x
x=['suba','karthi','subhani']
print(x[4])
x="nandhini"
x.reverse()
def fact(n):
    r=1
    for i in range(1,n):
        r=r*i
    return r
print(fact(5))'''
try:
    x=int(input('enter the no:'))
    y=10/x
    print('the result is:',y)
except ValueError:
    print('you must enter a valid integer')
except ZeroDivisionError:
    print('you cannot divide by zero')

