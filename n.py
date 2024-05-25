'''a=[]
ar=int(input("enter the no of rows : "))
ac=int(input("enter the no of column : "))

for i in range(ar):
    for j in range(ac):
        a.append(int(input("enter the value : ")))
print(a)

b=[]
br=int(input("enter the no of rows: "))
bc=int(input("enter the no of column: "))

for x in range(br):
    for y in range(bc):
        b.append(int(input("enter the value: ")))
print(b)

c=[]

for i in range(4):
    c.append(a[i]+b[i])
print(c)'''
x=[[2,3],[4,5]]
y=[[1,2],[3,4]]
result=[[0,0],[0,0]]

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            a=x[i][k]
            b=y[k][j]
            result[i][j]+=a*b
for r in result:
    print(r)
    


