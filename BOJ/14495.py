num = int(input())
dp = [0]*(num+1)
if num<=3:
    print(1)
else:
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1

    for i in range(4, num+1):
        dp[i] = dp[i-1] + dp[i-3]
    print(dp[num])