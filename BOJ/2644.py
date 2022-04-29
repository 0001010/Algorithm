# 2644
# 맞을까?
from collections import deque

num = int(input())
o, t = list(map(int, input().split()))
m = int(input())
dic = dict()

for i in range(num):
    dic[i+1] = set()
for j in range(m):
    one,two = list(map(int, input().split()))
    dic[one].add(two)
    dic[two].add(one)

# 여기가 핵심이다.
def bfs(graph, start):
    need_visited = deque([start])
    visited = [0]*(num+1) # visited를 num+1개 만큼 0으로 채운다.
    while need_visited:
        node = need_visited.popleft()
        for i in graph[node]: # graph[node]만큼 for문이 돌아가는데 원소가 visited에 들어갔을때 0이면 visited[i]에 visited[node]+1만큼 더하게 된다.
            if visited[i]==0:
                visited[i]+=(visited[node]+1)
                need_visited.append(i)
                print(i)
    return visited
    

g = bfs(dic, o)
if g[t]!=0:
    print(g[t])
else:
    print(-1)
