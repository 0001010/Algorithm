from sys import stdin
input = stdin.readline

num = int(input())
lists = []
ans = []
for i in range(num):
    x = list(map(int, input().split()))
    if x[0] != 0:
        y = sorted(x[1:])
        for j in y:
            lists.append(j)
    elif len(lists)==0:
        ans.append('-1')
    else:
        lists.sort()
        ans.append(str(lists.pop()))
        
print('\n'.join(ans))