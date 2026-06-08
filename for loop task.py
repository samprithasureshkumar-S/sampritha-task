
#task 1
x=[10,20,30,40,50]
print(20 in x)

#task 2
x=[10,20,30,40,50]
print(100 in x)

#task 3
name="python"
print("p" in name)

#task 4
name="python"
print("z" not in name)

#task 5
fruits=["apple","orange","grapes"]
print("apple" in fruits)

#task 6
for i in range (1,11):
    print(i)

#task 7
for i in range (5,16):
    print(i)

#task 8
for i in range (2,20,2):
    print(i)

#task 9
for i in range (1,20,2):
    print(i)

#task 10
for i in range (10,100,10):
    print(i)

#task 11
for i in range(1,11):
    print(i,"*5=",i*5)
    
#task 12
mul=int(input("Enter the table:"))
for i in range(1,11):
    print(i,"x",mul,"=",i*mul)
    
#task 13
sum=0
for i in range (1,11):
    sum+=i
print(sum)
    
#task 14
sum=0
for i in range (1,21,2):
    sum+=i
print(sum)
    
#task 15
for i in range(1,11):
    print(i*i)
    
#task 16
for i in range(10,0,-1):
    print(i)
    
#task 17
for i in range(20,0,-1):
    print(i)
    
#task 18
for i in range (20,1,-2):
    print(i)

#task 19
for i in range(19,0,-2):
    print(i)
    
#task 20
for i in range(10,0,-1):
    print(i)
    
#task 21
for i in range (50,-1,-5):
    print(i)
    
#task 22
n=int(input("Enter the number:"))
for i in range (n,0,-1):
    print(i)

#task 23
for i in range(10,0,-1):
    print(i,"x5=",i*5)

#task 24
ch="python"
for i in ch:
    print(i)
    
#task 25
n=input("Enter the name:")
for ch in n:
    print(ch)

#task 26
count=0
x=input()
for i in x:
    count=count+1
print(count)

#task 27
x=input()
count=0
for ch in x:
    if ch  in "aeiouAEIOU":
        count+=1
print(count)

#task 28
for i in range(1,6):
    for j in range(6):
        print("*",end="")
    print()

#task 29
for i in range(5):
    for j in range(i):
        print(j,end=" ")
    print(i)

#task 30
for i in range(5):
    for j in range(i,5):
        print(j,end="")
    print()
