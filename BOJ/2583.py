# 2583

from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(graph,a,b):
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

n, m, k = list(map(int, input().split()))
graph = [[1]*(m) for i in range(n)]

for i in range(k):
    coor = list(map(int, input().split()))
    for j in range(coor[0], coor[2]):
        for z in range(coor[1], coor[3]):
            graph[z][j]=0
cnt = []
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            cnt.append(bfs(graph,i,j))
            
cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])