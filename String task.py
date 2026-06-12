
#task 1
n=input("Enter the string :")
temp=""
for i in n:
    temp=i+temp
if(n==temp):
    print("True")
else:
    print("False")

#task 2
vowel=input("Enter the string :")
count=0
for i in vowel:
    if i in "aeiouAEIOU":
        count+=1
print("Number of Vowels:",count)

#task 3
n=input("Enter the String :")
Reverse=""
for i in n:
    Reverse=i+Reverse
print("Reversed String :",Reverse)

#task 4
n=input("Enter the String :")
lcount=0
ucount=0
for i in n:
    if i>="A" and i<="Z":
        ucount+=1
    elif i>="a" and i<="z":
        lcount+=1
print("Uppercount :",ucount)
print("Lowercount :",lcount)

#task 5
string=input("Enter a string : ")
temp=""
for i in string:
    if i not in temp:
        temp=temp+i
print(temp)

#task 6
string=input("Enter a string : ")
temp=""
freq=""
for i in string:
    if i not in temp:
        temp+=i
    else:
        freq+=i
print(freq)

#task 7
string1=input("Enter String 1 :")
string2=input("Enter String 2 :")
if sorted(string1)==sorted(string2):
    print("True")
else:
    print("False")

#task 8
n=input("Enter the string :")
temp=""
for i in n: 
    if(i>="A" and i<="Z" or i>="a" and i<="z"):
        temp=temp+i
print(temp)

#task 9
n=input("Enter the string: ")
count=0
temp=""
for i in n:
    temp=i+temp
    count+=1
print(temp)
print(count)

#task 10
n=input()
sum=0
for i in n:
    if i in "123456789":
        sum=sum+int(i)
print(sum)

#task 11
String = input("Enter a string : ")
l = String.split(" ")
temp = "-".join(l)

print(temp)

#task 12
n=input()
print(n.title())

#task 13
n=input()
print(n[::2])

#task 14
String = input("Enter a string : ")
temp = ""

for i in String:
    if i in "0123456789":
        temp = temp + i

print(temp)
#task 15
String = input("Enter a string : ")

print(String.startswith("a"))
print(String.endswith("et"))


















