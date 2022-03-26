# 1325
from sys import stdin
from collections import deque
import collections

input = stdin.readline

n, m = list(map(int, input().split()))
g = collections.defaultdict(list)
    
for j in range(m):
    one, two = list(map(int, input().split()))
    g[two].append(one)

def bfs(start):
    count = 1
    visited = [0 for i in range(n+1)]
    visited[start] = 1
    need_visited = deque([start])
    while need_visited:
        node = need_visited.popleft()
        for v in g[node]:
            if not visited[v]:
                need_visited.append(v)
                visited[v] = 1
                count +=1 
    return count

max_count = 0
lists = []
for i in range(1, n+1):
    cnt = bfs(i)
    if cnt>max_count:
        max_count = cnt
    lists.append([i, cnt])

for i, cnt in lists:
    if cnt==max_count:
        print(i, end = ' ')
