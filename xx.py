'''a=[1,2,3]
b=[4,5]
a.extend(b)
print(a)
print(len(a))'''
l1=[1,2,3]
l2=[4,5,6]
res_lst=[]
for i in range(0, len(l1)):
    res_lst.append(l1[i]+l2[i])
print(res_lst)
