# 1747
# 에라토스테네스의 체로 풀면 풀리는데 최대의 값을 저렇게 정해줘도 괜찮을지 의문이네

def prime(n, num):
    s = [True]*(n+1)
    for i in range(2, n+1):
        if s[i]==True:
            for j in range(i+i, n+1, i):
                s[j]=False
    return[i for i in range(num, n+1) if s[i]==True]

num = int(input())
if num==1:
    print(2)
else:
    prime_n = prime(2000000, num)
    for i in prime_n:
        a = str(i)
        if a==a[::-1]:
            print(a)
            break