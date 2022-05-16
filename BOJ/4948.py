# 4948
def prime(n):
    s = [True]*(n+1)
    for i in range(2, n+1):
        if s[i]==True:
            for j in range(i+i, n, i):
                s[j]=False
    return [i for i in range(2, n+1) if s[i]==True]

while True:
    inputs = int(input())
    a = set(prime(inputs))
    b = set(prime(2*inputs))
    if inputs==0:
        break
    if inputs==1:
        print(1)
    else:
        print(len(b-a)-1)