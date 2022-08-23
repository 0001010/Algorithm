# 10211
# dp문제이다. 문제를 이해하고 dp수식을 잘 세우면 풀리는문제


num = int(input())

for i in range(num):
    x = int(input())
    lists = list(map(int, input().split()))
    dp = [0]*x
    dp[0] = lists[0]
    for j in range(1, len(lists)):
        dp[j] = max(dp[j-1]+lists[j], lists[j])
    print(max(dp))