#task 1
def series1():
    for i in range(2,17,2):
        print(i,end=" ")
series1()

#task 2
def series2():
    for i in range(50,-10,-10):
        print(i,end=" ")
series2()

#task 3
def square(a):
    print(a*a)
square(6)

#task 4
def cube(a):
    print(a**3)
cube(8)

#task 5
def SplitNumber(a):
    while a>0:
        print(a%10,end=" ")
        a//=10
SplitNumber(2345)

#task 6
def AmstrongNumber(n):
    digits=str(n)
    power=len(digits)
    total=0
    for i in digits:
        total+=int(i)**power
    if total==n:
        print("Amstrong Number")
    else:
        print("Not an Amstrong number")
AmstrongNumber(153)

#task 7
def SpyNumber(n):
    digits=str(n)
    p=1
    s=0
    for i in digits:
        i=int(i)
        s+=1
        p*=1
    if s==p:
        print("Spy Number")
    else:
        print("Not an Spy Number")
SpyNumber(234)

#task 8
def SquareNumber(n):
    for i in str(n):
        print(int(i)**2,end=" ")
SquareNumber(4268)

#task 9
def countdigits(n):
    print(len(str(n)))
countdigits(2689578)

#task 10
def sum_of_divisors(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
    print(total)

sum_of_divisors(10)

#task 11
def input_price(n):
    price = int(input("Enter the price : "))
    calculate_charge(price)
def calculate_charge(price):
    if price >= 50000:
        price = price - (price * (10/100))
        print(price)
    elif price >= 30000 and price <= 49999:
        price = price - (price * (5/100))
        print(price)
    else:
        price = price - (price * (2/100))
        print(price)

input_price(56000)

#task 12
def addvalues(a,b):
    sum=a+b
    print(a+b)
a = int(input("Enter a number: "))
b = float(input("Enter a number: "))
addvalues(a,b)

#task 13
def is_capital(ch):
    if 'A' <= ch <= 'Z':
        print("Capital letter")
    else:
        print("Not capital")

is_capital('G')

#task 14
def is_vowel(ch):
    if ch.lower() in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")

is_vowel('e')

#task 15
def to_small_letter(ch):
    print(ch.lower())

to_small_letter('D')
        

































