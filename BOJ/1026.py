# 1026 보물

x = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))


sums = 0
for i in range(x):
    min_a = min(a)
    max_b = max(b)
    sums += min_a*max_b
    
    a.remove(min_a)
    b.remove(max_b)
print(sums)

# a에서 가장 높은 수가 b의 가장 낮은 수랑 곱하고 a의 가장 낮은수가 b의 가장 높은 수랑 곱하면 됨
# sort도 괜춘하네 