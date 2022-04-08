# 1927
# heaoq를 사용해서 문제를 풀면된다.
# push할 때 (12345678, -12345678) 이런식으로 push하면 ()의 첫자리가 정렬됨
# 그래서 pop할 때 정렬된 순서대로 pop이 되는데 (1,-1)이런식으로 나오게 되므로 0번째를 슬라이싱해준다.

import heapq

num = int(input())
q = []

for i in range(num):
    inputs = int(input())
    if inputs==0:
        if len(q)==0:
            print(0)
        else:
            print(heapq.heappop(q)[0])
    else:
        heapq.heappush(q, (inputs, -inputs))