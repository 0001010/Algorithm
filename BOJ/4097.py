# 4097 수익
# DP문제인거같다. 
from sys import stdin

while True:
    x = int(stdin.readline())
    if x==0:
        break
    lists = []
    
    for i in range(x):
        inputs = int(stdin.readline())
        lists.append(inputs)

    for j in range(1, x):
        lists[j] = max(lists[j], lists[j] + lists[j-1])
        # for문의 해당 원소에 대해서 그 전 원소값과 더해 max연산을 하고 그 리스트 자리에 넣음 
    print(max(lists))
        
