# 2606


"""
dfs로 풀었는데 
for문으로 dic을 만들어서 입력 받는것들을 set에 넣음
dic에 들어가있는것들을 for문으로 돌리면서 시작점의 원소가 lists에 없으면 dic에 있는 것들을 lists에 넣고 재귀로 호출함

"""


dic = {}
lists = []

for i in range(int(input())):
    dic[i+1] = set()

for j in range(int(input())):
    n, m = list(map(int, input().split()))
    dic[n].add(m)
    dic[m].add(n)  

def DFS(start, dic):
    for z in dic[start]:
        if z not in lists:
            lists.append(z)
            DFS(z, dic)

            

def bfs(start, dic):
    queue = [start]
    while queue:
        for i in dic[queue.pop()]:
            if i not in lists:
                lists.append(i)
                queue.append(i)


bfs(1, dic)
print(len(lists)-1)
