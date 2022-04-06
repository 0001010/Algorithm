# 1912
# dp문제이다
# lists에 입력을 받아두고 for문으로 num숫자까지 lists[i](더할 숫자) + dp[i-1](이전 dp)를 한다
# 그리고 lists[i] 리스트의 i번째와 비교해서 큰쪽을 dp[i]에 넣는다
# 연산이 다 되면 dp의 최대값을 출력한다

num = int(input())
lists = list(map(int, input().split()))
dp = [0]*num
dp[0] = lists[0]

for i in range(1, num):
    dp[i] = max(lists[i] + dp[i-1], lists[i])
    
print(max(dp))