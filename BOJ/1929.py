# 1929
# 소수 찾는건데 에라토스테네스의 체로 걸러버리면 된다.
# 에라토스테네스의 체를 잘 알아두자

def prime(n):
    s = [True]*(n+1)

    for i in range(2, n+1):
        if s[i]==True:
            for j in range(i+i, n+1, i):
                s[j]=False
    return s

m, n = list(map(int, input().split()))
ans = prime(n)

for i in range(m,n+1):
    if i==1:
        pass
    elif ans[i]==True:
        print(i)