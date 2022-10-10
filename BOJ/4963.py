# 4963

from collections import deque

dx = [0,0,1,-1,-1,1,1,-1]
dy = [1,-1,0,0,1,1,-1,-1]

def bfs(graph, a,b):
    qu = deque()
    qu.append((a,b))
    graph[a][b]=0
    
    while qu:
        x, y = qu.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=h or ny<0 or ny>=w:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                qu.append((nx, ny))
    return 

while True:
    w, h = list(map(int, input().split()))
    if w==0 and h==0:
        break
    
    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1:
                bfs(graph, i,j)
                cnt+=1
    print(cnt)