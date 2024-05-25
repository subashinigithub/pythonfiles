a=130
b=80
c=160
'''
if(a>b):
    print("a is greater than b")
elif(a>c):
    print("a is greater than c")
else:
    print("a is less than both")
if(a>b):
    if(a>c):
        print("a is greater than both")
    else:
        print("a is greater than b")
else:
    print("a is less than b")
if(a<b):
    print("b is greatest no")
    if(b>c):
        print("b is greatest than c")
    else:
        print("c is smallest no")
else:
    print("smallest no all")
if(a>b and a>c):
    print("a is smaller than both")
elif(b>a and b>c):
    print("b is greater than both")
else:
    print("c is larger than all")
a=input("enter a string")


if(a.strip()==a[::-1].strip()):
    print("it is a palindrome")
else:
    print("it is not a palindrome")

a=input('enter a student name:')
b=int(input('enter a student age:'))
m1=int(input('enter a mark1:'))
m2=int(input('enter a mark2:'))
m3=int(input('enter a mark3:'))
m4=int(input('enter a mark4:'))
m5=int(input('enter a mark5:'))
total=m1+m2+m3+m4+m5
avg=total/5
print('Name:',a)
print('Age:',b)
print('Avg',avg)
if(avg>90):
    print("a student is eligible to bio maths")
elif(avg>80):
    print("a student is eligible to cs")
elif(avg>70):
    print("a student is eligible to pure-science")
elif(avg>60):
    print("a student is eligible to commerce-acc")
elif(avg>50):
    print("a student is eligible to accounts-ca")
elif(avg>45):
    print("a student is eligible to literature")
else:
    print("a student is not eligible")'''
a=input('enter a emp name:')
b=int(input('enter a emp age:'))
c=(input('enter a destination:'))
d=int(input('enter a emp id:'))
e=int(input('enter a emp experience:'))
if(c=="python" and e==1):
    print("the employee salary became 10000")
elif(c=="python" and e==2):
    print("the employee salary became 20000")
elif(c=="python" and e==3):
    print("the employee salary became 30000")
elif(c=="java" and e==4):
    print("the employee salary became 50000")
elif(c=="java" and e==5):
    print("the employee salary became 70000")
else:
    print("the did not get hike")
    
      

