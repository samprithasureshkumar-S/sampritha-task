
#task 1
l=[13,5,30,8]
print(sum(l))

#task 2
l=[99,107,34,76,88,120,33]
print(max(l))

#task 3
l=[99,107,34,76,88,120,33]
print(min(l))

#task 4
l=['python',34,78,'hello',56,'hello']
new=[]
for i in l:
    if i not in new:
        new.append(i)
print(new)

#task 5
l=[1,2,3,4,5]
copy=[]
for i in l:
    copy.append(i)
print(copy)

#task 6
l=[1,2,3,4,5]
l.reverse()
print(l)

#task 7
lst = [10, "Sam", 3.14, True]
print(lst)

#task 8
l=[1,2,3,4,'',6]
empty=[]
for i in l:
    if i !="":
        empty.append(i)
print(empty)

#task 9
l1=[1,2,3,4,5]
l2=[6,7,8,9]
l1.extend(l2)
print(l1)

#task 10
import random
l=[1,2,54,56]
print(random.choice(l))

#task 11
l=[33,54,67,89,10]
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even:",even)
print("Odd:",odd)

#task 12
l=[98,65,77,90]
l.sort()
print(l)

#task 13
l=[98,65,77,90]
l.sort(reverse=True)
print(l)

#task 14
l=[34,76,98,43,65,88]
count=0
for i in l:
    count+=1
print(count)

#task 15
l=[34,76,98,43,65,88]
avg=sum(l)/len(l)
print(avg)

#task 16
l=[23,4,56,74,9,74]
print(l.count(74))

#task 17
l=[23,4,56,74,9,74]
n=4
if n in l:
    print("True")
else:
    print("False")

#task 18
l=[23,4,56,74,9,74]
l.inser(4,3)
print(l)

#task 19
l=[23,4,56,74,9,74]
l.remove(56)
print(l)

#task 20
l=[23,4,56,74,9,74]
l.sort()
print(l[-2])

#task 21
l1=[1,2,3,4,5]
l2=[10,20,30]
l1.extend(l2)
print(l1)

#task 22
l1=[1,2,3,4,5]
l2=[10,2,30]
common=[]
for i in l1:
    if i in l2:
        common.append(i)
print(common)

#task 23
l = [-5, 10, -3, 8, 2]
for i in l:
    if i > 0:
        print(i, end=" ")

#task 24
l = [-5, 10, -3, 8, 2]
for i in range(len(l)):
    if l[i] < 0:
        l[i] = 0

print(lst)

#task 25
l = [-5, 10, -3, 8, 2]
print(l.index(10))

#task 26
l=['sam','priya','anvi','athu','anu']
for i in l:
    print(i)

#task 27
marks=[78,45,67,89,96,30,76,44,54,85]
print(max(marks))
print(min(marks))

#task 28
prices = [120, 350, 250, 400]
print("Total Bill =", sum(prices))

#task 29
salaries = [18000, 26000, 30000, 22000, 45000]
for i in salaries:
    if i > 25000:
        print(i)

#task 30
attendance = ["Present", "Absent", "Present", "Present", "Absent"]
count = attendance.count("Present")
print("Present Students =", count)






























