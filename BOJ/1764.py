# 1764 듣보잡
n, m = list(map(int, input().split()))
list_1 = []
list_2 = []

for i in range(1, n+m+1):
    if i<=n:
        list_1.append(input())
    else:
        list_2.append(input())

intersection = list(set(list_1) & set(list_2))
intersection.sort()
print(len(intersection))
print('\n'.join(intersection))