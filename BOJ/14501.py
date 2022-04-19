# 14501
num = int(input())
t = []
p = []
dp = [0]*(num+1)
for i in range(num):
    inputs = list(map(int, input().split()))
    t.append(inputs[0])
    p.append(inputs[1])

for j in range(num-1, -1, -1):
    if j + t[j] > num:
        dp[j] = dp[j+1]
    else:
        dp[j] = max(dp[j+1], p[j]+dp[j+t[j]]) 
# dp[j+1]부분은 이전것, p[j]+dp[j+t[j]] 부분은 현재+이전스탭인데 t에 해당하는 이전

print(dp[0])