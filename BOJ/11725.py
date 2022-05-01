# 11725

import sys
sys.setrecursionlimit(10 ** 9)

num = int(input())
dic = dict()
for i in range(num):
    dic[i+1] = set()

for j in range(num-1):
    n, m = list(map(int, input().split()))
    dic[n].add(m)
    dic[m].add(n)
    
visited = [0]*(num+1)

def dfs(graph, start, visited):
    for node in graph[start]:
        if visited[node]==0:
            visited[node] = start
            dfs(graph, node, visited)
            
dfs(dic, 1, visited)

for i in range(2, num+1):
    print(visited[i])