# 2960
# 에라토스테네스의 체를 조금 변형하면 된다.
def prime(n):
    s = [True]*(n+1)
    t = []
    for i in range(2, n+1):
        if s[i]==True:
            for j in range(i, n+1, i):
                if j not in t:
                    t.append(j)
    return t

n, k = list(map(int, input().split()))
print(prime(n)[k-1])