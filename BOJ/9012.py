# 9012
from collections import deque

num = int(input())

for i in range(num):
    inputs = list(input())
    lists = deque()
    for j in inputs:
        lists.append(j)
        if j==')':
            if lists[0]==j:
                break
            if lists[-2]=='(':
                lists.pop()
                lists.pop()
    if len(lists)==0:
        print('YES')
    else:
        print('NO')