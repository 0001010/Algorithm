# 1660
n = int(input())
lists = [0]*300001
lists[1] = 1
i = 2
while True:
    lists[i] = (i**2)+lists[i-2]
    if lists[i]>n:
        break 
    else:
        i+=1
        
lists = lists[:i]
dp = [float('inf')] * (n + 1)
# dp부분을 inf로 놓으면 max값은 inf이다.

for i in range(1, n+1):
    for num in lists:
        if num==i:
            dp[i] = 1
            break
        dp[i] = min(dp[i], 1+dp[i-num])
        # dp[i]에 들어온게 없다면 inf가 되고 for에 num이 돌아갈때마다 만들 수 있는 수가 있음.
        # 예를들어 15면 1,4,10이고 14에서 1을 더해서 만들수있고 해서 for문으로 계속 최소값을 갱신함
print(dp[n])