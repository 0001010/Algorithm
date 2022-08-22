# 5567
# dfs로 깊이를 2로 제한
# 본인은 빼야하므로 -1

n = int(input())
m = int(input())

dic = dict()

for i in range(n):
    dic[i+1] = set()
for j in range(m):
    one, two = list(map(int, input().split()))
    dic[one].add(two)
    dic[two].add(one)


visited = [False]*(n+1) # 모두 false로 초기화


def dfs(graph, start, d, visited):
    visited[1] = True # 첫번째 노드는 True
    if d==2:
        return visited # 깊이가 2이면 return
    for node in graph[start]:
        if not visited[node]: # 만약 visited[node]가 True가 아니라면
            visited[node] = True # visited[node]를 True로 변경
        dfs(graph, node, d+1, visited) # 재귀 호출하면서 깊이를 1추가
        
dfs(dic, 1, 0, visited)
count = 0
for i in visited:
    if i==True:
        count+=1

print(count-1)

## dfs의 깊이를 2로 제한하면 될거같은 느낌인데
# 아니면 bfs로 갈아타던가...
# 위같으면 2,3,4가 친구의 친구까지니까 3개가 나와야