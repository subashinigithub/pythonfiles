'''items=['icecream','teddy','cake','kitkat','cake']
new=['ring','rose','chain']

print(items)
print(type(items))

items.append('watch')
print(items)

items.extend(new)
print(items)

items.insert(3,'bracelet')
print(items)

items.remove('cake')
print(items)

items.pop()
print(items)

print(items.index('teddy',0))
print(items.count('cake'))

items.sort()
print('sorted:',items)

new.reverse()
print('reverselist:',new)

new=items.copy()
print('copied list',new)

new.clear()
print(new)'''
vegetables=[]
a= int(input('enter the no of items:'))
for x in range(a):
    vegetables.append(input('enter the veg name'))
    print(vegetables)
    
