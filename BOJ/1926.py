# 1926

from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(graph, a,b):
    qu = deque()
    qu.append((a,b))
    graph[a][b]=0
    count = 1
    
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
                count+=1
    
    return count

n, m = list(map(int, input().split()))
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    
cnt = []
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            cnt.append(bfs(graph,i,j))
        
print(len(cnt))

if len(cnt)==0:
    print(0)
else:
    print(max(cnt))