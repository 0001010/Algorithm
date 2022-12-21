# 2293
# dp문제인데 시간과 메모리가 둘다 적게 주어짐
# dp를 합 만큼 추가해줌 ex) 5이면 dp = [0,0,0,0,0]
# 이중for문으로 코인의 리스트만큼 돌아간다.


n, k = list(map(int, input().split()))
coin = []
for i in range(n):
    c = int(input())
    coin.append(c)
dp = [0]*(k+1)
dp[0] = 1

for i in coin: # 코인의 List만큼 돌아감 ex) coin = [1,2,5] 이면 i에 1,2,5가 차례로 들어감
    for j in range(i, k+1): # 각 코인마다 k까지의 합을 돌림(예 1~10)까지
        if j-i>=0: # 음수가 되면 추가 할 수 없으니 음수가 아닐때
            dp[j] += dp[j-i] # 해당 dp 합에다 j-i를 추가(업데이트)

print(dp[k])