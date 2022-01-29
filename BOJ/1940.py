n = int(input())
m = int(input())
inputs = list(map(int, input().split()))
inputs.sort()
counts = 0
for i in inputs:
    if m-i in inputs:
        counts+=1

print(int(counts/2))