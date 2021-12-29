from collections import Counter

n, c = list(map(int, input().split()))

lists = list(map(int, input().split()))
counts = sorted(Counter(lists).items(), key = lambda item : item[1], reverse = True)

lists2 = []

for i in counts:
    for j in range(i[1]):
        lists2.append(str(i[0]))
        
print(' '.join(lists2))