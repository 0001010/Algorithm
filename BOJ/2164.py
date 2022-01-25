# 2164
"""
자료구조 문제를 풀때는 collections을 이용하면 쉽게 풀 수 있다.
deque를 부른다음 n개 만큼의 수를 deque에 넣는다.
그리고 pop 왼쪽을 한다음에 그 다음 왼쪽에 있는건 append한다
"""
from collections import deque

n = int(input())
deque = deque()

for i in range(n):
    deque.append(i+1)
    

while len(deque)>1:
    deque.popleft()
    deque.append(deque.popleft())
print(deque[0])