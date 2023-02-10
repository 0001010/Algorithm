# 3896
# 에라토스테네스의 체를 사용해서 소수를 걸러내고 거기에서 이분탐색으로 소수이면 0
# 소수가 아니라면 앞뒤의 범위를 살펴서 그 차이를 출력하면 된다.


def prime(n):
    s = [True]*(n+1)
    m = int((n+1)**0.5)
    for i in range(2, m+1):
        if s[i]==True:
            for j in range(i+i, n+1, i):
                s[j]=False
    return [i for i in range(2, n+1) if s[i]==True]

def bs(lists, num):
    start = 0
    end = len(lists)-1
    while start<=end:
        mid = (start + end)//2
        if lists[mid]==num:
            return -1 
        elif lists[mid]<num:
            start = mid+1
        else:
            end = mid-1
    return mid # index 반환

primes = prime(1300000)

num = int(input())
for i in range(num):
    x = int(input())
    a = bs(primes, x)
    if a>-1:
        if primes[a]<x:
            print(primes[a+1]-primes[a])
        else:
            print(primes[a]-primes[a-1])
    else:
        print(0)