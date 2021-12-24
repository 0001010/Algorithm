n, k = list(map(int, input().split()))
lists = []

for i in range(n):
    inputs = int(input())
    lists.append(inputs)
    
lists.sort(reverse = True)

rem = 0
for j in lists:
    if k>=j:
        a = k//j
        rem+=a
        k-=a*j
        
print(rem)