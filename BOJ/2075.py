# 2075
# 메모리가 아주 작은 범위로 제한되어있어서 계속 원소를 추가할 수 없다고 판단했다.
# deque를 이용해서 pop을 하는 방법을 사용
# num만큼 반복되는데 inputs을 받아서 ans에 추가후 정렬 -> 
# 메모리제한으로 num만큼 pop해주면 최종적으로 deque안에는 num개 만큼의 원소가 남아있게됨
# num개의 원소중 num번째를 출력하라는것이니까 0번째 인덱스를 출력하면 된다.

from collections import deque

num = int(input())
ans = deque()
for i in range(num):
    inputs = deque(map(int, input().split()))
    ans = ans + inputs
    ans = deque(sorted(list(ans)))
    if i>0:
        for j in range(num):
            ans.popleft()
print(ans[0])
