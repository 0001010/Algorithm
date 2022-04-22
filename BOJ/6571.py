# 6571

dp = [0]*(1001)
dp[1] = 1
dp[2] = 2
for i in range(3, 1001):
    dp[i] = dp[i-1] + dp[i-2]

while True:
    a, b = list(map(int, input().split()))
    if a==0 and b==0:
        break
    count = 0
    for i in range(1, 1001):
        if a<=dp[i] and b>=dp[i]:
            count+=1
    print(count)