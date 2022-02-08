# 2108번
from collections import Counter # 빈도수 카운트 할 때 아주좋은 함수임
import sys 

num = int(sys.stdin.readline())
lists = []

for i in range(num):
    lists.append(int(sys.stdin.readline()))
    
lists.sort()

most_count = Counter(lists).most_common(2)

if len(most_count)==1:
    most_count = most_count[0][0]
else:
    if most_count[0][1] == most_count[1][1]:
        most_count = most_count[1][0]
    else:
        most_count = most_count[0][0]

print(round(sum(lists)/len(lists)))
print(lists[len(lists)//2])
print(most_count)
print(max(lists) - min(lists))