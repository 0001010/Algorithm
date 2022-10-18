from itertools import product
n, m = list(map(int, input().split()))
if len(str(n))==len(str(m)):
    len_n = len(str(n))
    len_m = len(str(m))+2
else:
    len_n = len(str(n))
    len_m = len(str(m))+1
lists = []
for i in range(len_n,len_m):
    prod = product([4,7],repeat = i)
    for j in prod:
        num = int(''.join(map(str,j)))
        if n<= num and m>=num:
            lists.append(num)
        

print(len(set(lists)))  