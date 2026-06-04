
#task 1
m=int(input("Enter the m value:"))
n=int(input("Enter the n value:"))
if m>n:
    print("Quoation:",m//n)
    print("Reminder:",m%n)
else:
    print("m is less than n")

#task 2
m1=int(input("Enter the Mark 1:"))
m2=int(input("Enter the Mark 2:"))
m3=int(input("Enter the Mark 3:"))
m4=int(input("Enter the Mark 4:"))
m5=int(input("Enter the Mark 5:"))

avg=(m1+m2+m3+m4+m5)/5
if avg>90:
    print("Grade O")
elif avg>80:
    print("Grade A+")
elif avg>70:
    print("Grade A")
elif avg>60:
    print("Grade B+")
else:
    print("Just pass")

#task 3
#positive or negative
a=int(input("Enter the Number:"))
if a>0:
    print("Positive")
else:
    print("Negative")
#odd or even
b=int(input("Enter the Number:"))
if b%2==0:
    print("Even")
else:
    print("Odd")
#pass or fail
c=int(input("Enter the Mark:"))
if c>50:
    print("Pass")
else:
    print("Fail")
#leap year or not
d=int(input("Enter the Year:"))
if d%4==0:
    print("Leap year")
else:
    print("Not an Leap Year")

#task 4
ch=input("Enter the Character:")
if ch=="a" or ch=="e" or ch=="i"or ch=="o" or ch=="u":
    print("Vowels")
else:
    print("Consonants")

#task 5
#maximum
n1=int(input("Enter the number:"))
n2=int(input("Enter the number:"))
n3=int(input("Enter the number:"))
if n1>n2 and n1>n3:
    print("Maximum:",n1)
elif n2>n3 and n2>n1:
    print("Maximum:",n2)
else:
    print("Minimum:",n3)
#minimum
n1=int(input("Enter the number:"))
n2=int(input("Enter the number:"))
n3=int(input("Enter the number:"))
if n1<n2 and n1<n3:
    print("Maximum:",n1)
elif n2<n3 and n2<n1:
    print("Maximum:",n2)
else:
    print("Minimum:",n3)

#task 6
a=input("Season:")
if a=="june" or a=="july" or a=="augest":
    print("Summer")
elif a=="december" or a=="january" or a=="febuary":
    print("Winter")
elif a=="march" or a=="april" or a=="may":
    print("Spring")
else:
    print("Autumn")

#task 8
a=int(input("Enter the number:"))
if a%5==0:
    print("Hello")
else:
    print("Bye")

#task 9
cel=int(input("Enter the Celsius:"))
if cel>100:
    print("Water is Boiling")
else:
    print("Water is not boiling")

#task 7
a=input("Enter the month:")
if a=="january" or a=="march" or a=="may" or a=="july" or a=="august" or a=="october" or a=="december":
    print("31 Days")
elif a=="april" or a=="june" or a=="september" or a=="november":
    print("30 days")
elif a==2:
    print("28 or 29 days")
else:
    print("invalid month")

#task 10
days = int(input("Enter number of days: "))

if days <= 5:
    charge = days * 2
elif days <= 10:
    charge = days * 3
elif days <= 15:
    charge = days * 4
else:
    charge = days * 5

print("Library Charge = Rs.", charge)

#task 11
age = int(input("Enter age: "))
height = float(input("Enter height in cm: "))

if age >= 18 and age <= 25 and height >= 165:
    print("Eligible")
else:
    print("Not Eligible")

#task 12
salary = float(input("Enter salary: "))
years = int(input("Years of service: "))

if years > 5:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05

print("Bonus =", bonus)
#task 13
units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = units * 2
else:
    bill = units * 3

print("Electricity Bill = Rs.", bill)
#task 14
password = input("Enter password: ")

if len(password) >= 8:
    print("Valid Password")
else:
    print("Invalid Password")






























