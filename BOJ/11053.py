# 11053
# dp로 풀수도 있고 bs로 풀수도 있다고한다.
# dp로 풀 경우
# dp값을 전부 1로 초기화한다음 for문으로 num만큼 돌리는데 lists[i]가 lists[j]보다 크면 dp[i] = max(dp[i], dp[j]+1)

num = int(input())
lists = list(map(int, input().split()))
dp = [1]*(num)
for i in range(num):
    for j in range(i):
        if lists[i]>lists[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
    