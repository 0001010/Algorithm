from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(graph, a,b):
    qu = deque()
    qu.append((a,b))
    graph[a][b]=0
    
    while qu:
        x, y = qu.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                qu.append((nx, ny))
    return

t = int(input())
for test in range(t):
    m, n, k = list(map(int, input().split()))
    graph = [[0]*n for i in range(m)]
    count = 0
    for i in range(k):
        x, y = list(map(int, input().split()))
        graph[x][y]=1
    for a in range(m):
        for b in range(n):
            if graph[a][b]==1:
                bfs(graph, a,b)
                count+=1
    print(count)