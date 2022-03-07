# 11727
# 단순 dp문제인데 dp부분의 점화식을 잘 활용해보자
num = int(input())

dp = [0]*(num+1)
dp[0] = 1
dp[1] = 3
for i in range(2, num+1):
    dp[i] = dp[i-1] + dp[i-2]*2



print(dp[num-1]%10007)