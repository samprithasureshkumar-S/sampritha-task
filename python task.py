
#task 1
String="Sampritha"
count=0
for i in String:
    count+=1
print("String Length :",count)

#task 2
n=input("Enter the String :")
print(n.isalpha())

#task 3
n=input("Enter the String :")
print(n.isdigit())

#task 4
n=input("Enter the String :")
count=0
for i in n:
    if i.isalpha() and i not in "aeiouAEIOU":
        count+=1
print("Count:",count)

#task 5
n=input("Enter the String :")
for i in n:
    if n.count(i) == 1:
        print(i)
        break

#task 6
n=input("Enter the String :")
print(n.swapcase())

#task 7
n=input("Enter the String :")
remove=" "
for i in n:
    if i!=" ":
        remove+=i
print(remove)

#task 8
n=input("Enter the String :")
for i in n:
    if n[0].lower() in "aeiou":
        print("Starts with vowel")
    else:
        print("Does not Starts with vowel")

#task 9
n=input("Enter the String :")
ch=input("Enter the Character :")
count=1
for i in ch:
    if i==ch:
        count+=1
print(count)

#task 10
n=input("Enter the String :")
result=" "
for i in n:
    if i in "aeiouAEIOU":
        result+="*"
    else:
        result+=i
print(result)

#task 11
n = input("Enter string: ")
for i in range(0, len(n), 2):
    print(n[i], end=" ")

#task 12
n=input("Enter the string:")
for i in range(1, len(n), 2):
    print(n[i], end=" ")

#task 13
n=input("Enter the string:")
l=[]
for i in n:
    l.append(i)
print(l)

#task 14
s = input("Enter string: ")
count = 0
for i in s:
    if not i.isalnum() and i != " ":
        count +=1
    print(count)

#task 15
n=input("Enter the string")
if n.isalnum():
    print("its true")
else:
    print("false")
    
#task 16
n="   hello   "
n1=""
start=0
end=len(s)-1
while start<=end and n[start].isspace():
    start+=1
while end>=start and n[end].isspace():
    end-=1
for i in range(start,end+1):
    n1+=n[i]
print(s1)

#task 17
n=input("Enter the string")
for i in n:
    print(i,ord(i))

#task 18
n = input("Enter sentence: ")
word = ""
for i in n:
    if i != " ":
        word += i
    else:
        print(word)
        word = ""
print(word)

#task 19
n = input("Enter sentence: ")
words = n.split()
longest = words[0]

for i in words:
    if len(i) > len(longest):
        longest = i

print(longest)

#task 20
n=input("Enter the string")
n1=n.isidentifier()
print(n1)




























































