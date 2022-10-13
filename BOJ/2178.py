# 2178

from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(graph, a,b):
    qu = deque()
    qu.append((a,b))
    graph[a][b]=1
    
    while qu:
        x, y = qu.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m: # 벽을 넘어가면 무시
                continue
            if graph[nx][ny]==0: # 벽이면 무시
                continue
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y]+1 # 이전 graph에 있는 count에서 1을 추가
                qu.append((nx, ny))

    return graph[n-1][m-1] # 우리가 찾을건 n-1, m-1 임

n, m = list(map(int, input().split()))
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(bfs(graph, 0,0))# 시작이 0,0부터 시작임