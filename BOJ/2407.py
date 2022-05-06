# 2407
# ! 공식만 알면 쉽게 풀리는 문제이다

n, m = list(map(int, input().split()))

num = 1
for i in range(1, m+1):
    num*=n-i+1
    
nums = 1
for j in range(1, m+1):
    nums*=j
    
print(int(num//nums))