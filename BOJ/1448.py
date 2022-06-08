from collections import deque

num = int(input())
lists = []

for i in range(num):
    x = int(input())
    lists.append(x) 
s = 0
lists.sort(reverse = True)
for i in range(len(lists)-2):
    if lists[i] < lists[i+1] + lists[i+2]:
        print(lists[i] + lists[i+1] + lists[i+2])
        s+=1
        break
if s==0:
    print(-1)