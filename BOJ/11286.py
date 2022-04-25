# 11286
# heapq를 이용해서 풀 수 있는 문제인데 input의 절대값을 input값과 같이 넣어서 풀면된다.
import heapq

num = int(input())
hq = []

for i in range(num):
    inputs = int(input())
    if inputs != 0:
        heapq.heappush(hq, (abs(inputs), inputs)) # 여기를 잘 사용하자
        # 첫원소를 절대값으로 넣어주고 두번째를 input값으로 넣어줘서 절대값으로 정렬 될 수 있다.
    else:
        if len(hq)>0:
            print(heapq.heappop(hq)[1])
        else:
            print(0)
