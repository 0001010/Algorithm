n = int(input())
dic = dict()
count = 0

for i in range(n):
    x = list(map(int, input().split()))
    if x[0] not in dic:
        dic[x[0]] = x[1]
        
    else:
        if dic[x[0]] == x[1]:
            pass
        else:
            count+=1
            dic[x[0]] = x[1]

print(count)