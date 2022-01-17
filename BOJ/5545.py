# 5545
num = int(input())
a, b = list(map(int, input().split()))
c = int(input())
lists = []

for i in range(num):
    lists.append(int(input()))
    
lists.sort(reverse = True)

curr = c/a

for j in range(1, len(lists)+1):
     new = (c + sum(lists[:j])) / (a+b*j)
     if curr <= new:
         curr = new
     else:
         break

print(int(curr))