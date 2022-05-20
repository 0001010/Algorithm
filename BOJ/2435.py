# 2435

n, k = list(map(int, input().split()))

lists = list(map(int, input().split()))
max_val = []

for i in range(n-k+1):
    max_val.append(sum(lists[i:i+k]))

print(max(max_val))
