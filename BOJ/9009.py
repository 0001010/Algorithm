num = int(input())

dp = [0]*46
dp[1] = 1
dp[2] = 2
for i in range(3, 46):
    dp[i] = dp[i-1] + dp[i-2]

for i in range(num):
    sol = []
    x = int(input())
    while (x):
        for j in range(46):
            if dp[j]<=x:
                s = dp[j]
        x-=s
        sol.append(s)
        sol.sort()
    print(' '.join(map(str,sol)))