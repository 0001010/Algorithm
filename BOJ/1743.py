# 1743

from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(graph, a,b):
    qu = deque()
    qu.append((a,b))
    graph[a][b]=0
    cnt = 1
    
    while qu:
        x, y = qu.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                qu.append((nx, ny))
                cnt+=1
    return cnt

n, m, k = list(map(int, input().split()))
graph = [[0]*(m) for i in range(n)]
for i in range(k):
    x, y = list(map(int, input().split()))
    graph[x-1][y-1] = 1
count=[]
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            count.append(bfs(graph,i,j))
            
print(max(count))