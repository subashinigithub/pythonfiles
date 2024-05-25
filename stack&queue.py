'''liststack=[3,2,1]
print(liststack)

liststack.append(5)
print(liststack)
liststack.append(6)
print(liststack)
liststack.pop()
print(liststack)

from collections import deque
queue=deque(['apple','orange','kiwi'])
print(queue)

queue.append('banana')
print(queue)

queue.popleft()
print(queue)

a=[1,2,3,4,5,6,7,8,9]
print(a)

del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)

del a
print(a)

t=1234,5432,'tuple'
print(t[1])
print(t)
t1=t,(1,2,3,4,5,'kg')
print(t1)
empty=()
singleton='hello'     
print(len(empty))
print(len(singleton))
print(singleton)
print(type(singleton))
t=123,353,'tuples'
x,y,z=t
print(t)
print(x)
print(y)
print(z)

basket={'apple','banana','orange','kiwi','apple'}
print(basket)
print('orange' in basket)
print('mango' not in basket)
a=set('balas')
b=set('balag')
print('unique letters in a',a)
print('letters in a but not in b',b-a,a-b)
print('both a or b',a|b)
print('letters in both a and b',a&b)
print('letters in a or b but not both',a^b)
a={x for x in 'ryacti' if x in 'abc'}
print(a)'''

dic={'name':'ram', 'age':26}
print(dic)
dic['guide']=987
print(dic)
del dic['age']
print(dic)
print(list(dic))
print(sorted(dic))
print('guido' in dic)
print('guide' in dic)
a=dict([('bala',3462),('rakesh',4353),('aravin',678)])
print(a)
dist={x:x**2 for x in(2,4,6)}
print(dist)
a=dict(a=98,b=98,h=956)
print(a)



