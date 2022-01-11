num = int(input())
result = 0

for i in range(1, num+1):
    decompose = list(map(int, str(i)))
    de_sum = sum(decompose)
    if i+de_sum == num:
        result = i
        break

print(result)