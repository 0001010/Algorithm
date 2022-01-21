n = int(input())
lists = [0]*1000001
lists[0] = 1
lists[1] = 2

for i in range(2, n+1):
    lists[i] = (lists[i-1] + lists[i-2])%15746

print(lists[n-1])