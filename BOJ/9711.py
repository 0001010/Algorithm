# 9711
# dp문제이고 피보나치 관련 문제이다.
# 피보나치의 수가 커지는데 시간은 1초밖에 없어서 피보나치를 여러번 돌리는거보다 가장 큰 수를 잡아서 피보나치를 만드는게 효율적이라고 판단


from collections import deque

qu = deque()

num = int(input())
max_p = 0

for i in range(num):
    p, q = list(map(int, input().split()))
    if max_p<=p:
        max_p = p
    qu.append([p,q])

dp = deque([0]*(max_p+1))
dp[1] = 1
dp[2] = 1
for i in range(3, max_p+1):
    dp[i] = dp[i-1] + dp[i-2]
case = 1
for j in qu:
    print("Case #"+str(case)+":",dp[j[0]] % j[1])
    case+=1
