# 15965
def prime(n):
    s = [True]*(n+1)
    m = int(n**0.5)
    for i in range(2, m+1):
        if s[i]==True:
            for j in range(i+i, n+1, i):
                s[j]=False
    return [i for i in range(2, n+1) if s[i]==True]

k = int(input())
print(prime(7500000)[k-1])