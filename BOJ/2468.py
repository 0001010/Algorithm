# 2468
from collections import deque
import copy

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(graph,a,b,k):
    qu = deque()
    qu.append((a,b))
    graph[a][b]=0
    count=1
    
    while qu:
        x, y = qu.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if graph[nx][ny]>k:
                graph[nx][ny]=0
                qu.append((nx, ny))
                count+=1
    return count


n = int(input())
graph = []
max_k = 0
for i in range(n):
    lists = list(map(int, input().split()))
    max_k = max(max(lists), max_k)
    graph.append(lists)

ans = []
for k in range(1, max_k+1):
    graph_new = copy.deepcopy(graph)
    cnt = []
    for i in range(n):
        for j in range(n):
            if graph_new[i][j]>k:
                cnt.append(bfs(graph_new,i,j,k))
    ans.append(len(cnt))

if sum(ans)==0:
    print(1)
else:
    print(max(ans))