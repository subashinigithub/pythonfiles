'''
a="Welcome"
b="to"
c="all"
d=a+b+c
print(d)

a='hi'
b='everyone'
d=a+" "+b
print(d)
age=22
txt="My name is suba, and I am {}"
print(txt.format(age))
cookies=4
kitkat=2
icecream=5
myfav="I want{}, pieces of item{}, for my whish{}."
print(myfav)
print(myfav.format(cookies,kitkat,icecream))
cookies=4
kitkat=2
price=10
myfav="I want{2}, pieces of item{0}, for that price{1}"
print(myfav.format(cookies,kitkat,price))
a="agriculture"
print(a.split("u"))
a="livewire"
print(a.split("i"))'''
a="livewire"
x=a[:4].upper()
print(x)
y=a[-4:].upper()
print(y)
print(x+y)
b=x+y
print(b.split("I"))
