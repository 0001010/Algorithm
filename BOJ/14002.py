# 14002
# dp LIS문제인데 LIS를 구하는건 어렵지 않았는데
# 출력이 문제였다.
# 역순으로 다시 거슬러 올라가면서 index를 부여해서 맞는것들만 다시 출력해주면 된다.

num = int(input())
lists = list(map(int, input().split()))

dp = [1]*(num)


for i in range(num):
    for j in range(i):
        if lists[i]>lists[j]:
            dp[i] = max(dp[i], dp[j]+1)
            
max_dp = max(dp)
print(max_dp)

sol = []

for i in range(num-1, -1, -1):
    if dp[i]==max_dp:
        sol.append(lists[i])
        max_dp-=1
sol.sort()
sol = map(str, sol)
print(' '.join(sol))