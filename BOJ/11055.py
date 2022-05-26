# 11055

num = int(input())
lists = list(map(int, input().split()))

dp = [x for x in lists]

for i in range(num):
    for j in range(i):
        if lists[i]>lists[j]:
            dp[i] = max(dp[i], dp[j]+lists[i])

print(max(dp))