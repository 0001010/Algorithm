# 10026
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(graph,a,b,k):
    qu = deque()
    qu.append((a,b))
    graph[a][b]=-1
    count = 1
    
    while qu:
        x, y = qu.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue

            if graph[nx][ny]==k:
                graph[nx][ny]=-2
                qu.append((nx, ny))
                count+=1
    
    return count

n = int(input())
graph = []
graph2 = []
for i in range(n):
    x = input()
    graph.append(list(x))
    graph2.append(list(x.replace('R','G')))
    
ans = 0
ans2 = 0

for k in ['R','G','B']:
    cnt = []
    cnt2 = []
    for i in range(n):
        for j in range(n):
            if graph[i][j]==k:
                cnt.append(bfs(graph,i,j,k))
            if graph2[i][j]==k:
                cnt2.append(bfs(graph2,i,j,k))
    ans+=len(cnt)
    ans2+=len(cnt2)
    
print(ans, ans2)