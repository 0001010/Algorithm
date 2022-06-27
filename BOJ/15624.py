# 15624

num = int(input())
dp = [0]*(num+4)
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, num+4):
    dp[i] = (dp[i-1] + dp[i-2])%1000000007
    
print(dp[num+1])