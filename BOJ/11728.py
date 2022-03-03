# 11728
a, b = list(map(int, input().split()))
n = list(map(int, input().split()))
m = list(map(int, input().split()))

ans = n + m
ans.sort()
ans = list(map(str, ans))
print(' '.join(ans))